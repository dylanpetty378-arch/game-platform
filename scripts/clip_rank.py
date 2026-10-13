"""Image pre-ranking with CLIP (free, CPU) — scores a listing's first photo for "looks like something collectors pay for".

Used by cloud_cycle.py on the top title-scored candidates before choosing the Lens queue.
  from clip_rank import ClipRanker; cr = ClipRanker(); scores = cr.score_listings(rows)  # rows need 'imgs'
  python3 scripts/clip_rank.py <listings.json> [N]        # quick test: prints best and worst

Score = (mean of top-3 similarities to POSITIVE prompts) − (mean of top-3 similarities to NEGATIVE prompts), ×100.
Typical range −5…+5. Embeddings are also returned so a learned model can be trained later (docs/improvements.md).
Model: open_clip ViT-B-32 / laion2b_s34b_b79k (~350 MB, cached by the workflow).
"""
import io, sys, json, time, concurrent.futures as cf, urllib.request
POSITIVE = [
    'a photo of an antique', 'a photo of a vintage collectible', 'a photo of fine art pottery', 'a photo of an oil painting',
    'a photo of a framed artwork', 'a photo of sterling silver jewelry', 'a photo of gold jewelry', 'a photo of a vintage watch',
    'a photo of a vintage film camera', 'a photo of a camera lens', 'a photo of a vintage guitar', 'a photo of a musical instrument',
    'a photo of a bronze sculpture', 'a photo of art glass', 'a photo of a Native American turquoise piece', 'a photo of Asian antiques',
    'a photo of a vintage toy', 'a photo of a vintage fishing reel', 'a photo of mid-century modern design object',
    'a photo of an antique clock', 'a photo of vintage militaria', 'a photo of a vintage sign', 'a photo of old books',
    'a photo of a carved wooden figure', 'a photo of studio pottery with a maker mark', 'a photo of vintage tools',
]
NEGATIVE = [
    'a photo of a sofa', 'a photo of a mattress', 'a photo of a dresser', 'a photo of a dining table', 'a photo of an office chair',
    'a photo of car parts', 'a photo of tires', 'a photo of a modern television', 'a photo of a laptop', 'a photo of a cell phone',
    'a photo of plastic storage bins', 'a photo of clothes on a hanger', 'a photo of shoes', 'a photo of kitchen appliances',
    'a photo of a baby stroller', 'a photo of exercise equipment', 'a photo of a modern bicycle', 'a photo of building materials',
    'a photo of a cheap plastic toy', 'a photo of a stock product image on white background', 'a photo of a pile of household junk',
    'a screenshot with text', 'a photo of a pet', 'a photo of a car',
    # size rule: nothing bigger than a passenger seat
    'a photo of a large wooden cabinet', 'a photo of an armoire', 'a photo of a wooden trunk', 'a photo of a rocking chair',
    'a photo of a large wall mirror', 'a photo of a desk', 'a photo of a piano', 'a photo of a large folding screen',
    'a photo of a large area rug on the floor', 'a photo of a bookcase', 'a photo of a full-size floor lamp',
]

def _fetch(url, timeout=20):
    for t in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=timeout) as r:
                return r.read()
        except Exception:
            time.sleep(1)
    return None

class ClipRanker:
    def __init__(self, model='ViT-B-32', pretrained='laion2b_s34b_b79k'):
        import torch, open_clip
        self.torch = torch
        self.model, _, self.prep = open_clip.create_model_and_transforms(model, pretrained=pretrained)
        self.model.eval(); tok = open_clip.get_tokenizer(model)
        with torch.no_grad():
            t = self.model.encode_text(tok(POSITIVE + NEGATIVE)); t = t / t.norm(dim=-1, keepdim=True)
        self.tp, self.tn = t[:len(POSITIVE)], t[len(POSITIVE):]

    def score_listings(self, rows, batch=64, threads=32):
        """rows: dicts with 'imgs'. Returns list of (score or None, embedding list or None) in the same order."""
        from PIL import Image
        torch = self.torch
        urls = [f"https://images.craigslist.org/{r['imgs'][0]}_300x300.jpg" if r.get('imgs') else None for r in rows]
        out = [(None, None)] * len(rows)
        with cf.ThreadPoolExecutor(threads) as ex:
            for start in range(0, len(rows), batch):
                idx = list(range(start, min(start + batch, len(rows))))
                raws = list(ex.map(lambda i: _fetch(urls[i]) if urls[i] else None, idx))
                ims, keep = [], []
                for i, b in zip(idx, raws):
                    if not b: continue
                    try: ims.append(self.prep(Image.open(io.BytesIO(b)).convert('RGB'))); keep.append(i)
                    except Exception: pass
                if not ims: continue
                with torch.no_grad():
                    e = self.model.encode_image(torch.stack(ims)); e = e / e.norm(dim=-1, keepdim=True)
                sp = (e @ self.tp.T).topk(3, dim=1).values.mean(1); sn = (e @ self.tn.T).topk(3, dim=1).values.mean(1)
                for k, i in enumerate(keep):
                    out[i] = (round(float((sp[k] - sn[k]) * 100), 2), [round(float(v), 4) for v in e[k].tolist()])
        return out

if __name__ == '__main__':
    rows = json.load(open(sys.argv[1])); n = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    import random; random.seed(1); rows = random.sample(rows, min(n, len(rows)))
    t = time.time(); cr = ClipRanker(); t1 = time.time()
    res = cr.score_listings(rows); t2 = time.time()
    sc = sorted([(s, r['title'][:50], r['price'], r['cat']) for (s, _), r in zip(res, rows) if s is not None], reverse=True)
    print(f'model load {t1-t:.0f}s, {len(rows)} images in {t2-t1:.0f}s ({len(rows)/(t2-t1):.1f}/s)')
    print('TOP:'); [print(' ', x) for x in sc[:15]]
    print('BOTTOM:'); [print(' ', x) for x in sc[-10:]]
