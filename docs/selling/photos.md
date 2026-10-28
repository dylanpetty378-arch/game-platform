# Photos — capture, staging and editing for selling used goods (Oct 28 2026)

Dylan (Oct 28 2026): "everything that can be done to not only get good photos of select, specific things, but also
editing techniques and things Claude can do to quickly take photos and make them perfect for selling/staging while
still being realistic about the thing being sold." Setup: phone camera, a driveway, a garage, Keller TX. Furniture
sells locally on Facebook Marketplace; small collectibles ship on eBay. Claude edits in Python (Pillow, numpy) via
`scripts/stage.py` — no Photoshop, no AI generation. Companion docs: `playbook.md` §2 (first-photo rule, set-listing
duplicate rejection), `household-families.md` (per-family shot lists), `research/selling/by-item-family-2026-10-27.md` §15.

**The honesty rule (hard).** An edit may correct exposure, white balance, perspective, crop, and clutter *outside* the
item. It may never hide, soften or remove a flaw on the item, change its colour, or add anything that isn't there.
Facebook's Commerce Policies forbid misleading listings and its image matching removes stock and heavily edited photos
("Misleading Product"), with reach cuts and strikes (https://closo.co/blogs/platform-specific-guides/the-real-risk-do-stock-photos-get-taken-down-on-facebook-marketplace);
eBay bars stock photos as the primary image for pre-owned items (https://export.ebay.com/en/first-steps/manage-listings/photo-tips/).
A "perfect" photo of a flawed item is a return, a no-show, or a one-star rating.

## 1. Capture — the rules that matter

| Rule | Do | Why / source |
|---|---|---|
| **Light** | Daylight only: open garage door with the piece just inside the shade line, or driveway in the hour after sunrise / before sunset; overcast is ideal. No flash, overheads off, no direct sun, no dappled shade. | Overheads add a yellow cast; flash flattens and glares; direct sun makes hard shadows that hide finish and fabric (https://whataroom.com/pages/how-to-photograph-a-sofa · https://qisforquandie.com/2019/04/26/outdoor-photo-shoots). Oct 27 shoot: 8–9 am driveway worked. |
| **Lens** | 1× only. Step back instead of switching to 0.5×. 2× for jewelry and small detail. No digital zoom past 2×. | Ultra-wide bends the sofa's edges and stretches the near end; 2× avoids wide-angle distortion on small pieces (https://whataroom.com/pages/how-to-photograph-a-sofa · https://blog.picupmedia.com/how-to-photograph-jewelry-on-a-black-background). |
| **Camera height** | Sofa/loveseat/bed: seat height, 3–4 ft, phone level. Tables/case goods: top-of-piece height, slightly above. Small items: 45° and straight-down. | Eye level tilted down makes a sofa look squat and the seat look huge (https://whataroom.com/pages/how-to-photograph-a-sofa). |
| **Distance** | Fill 80–90% of the frame; ~10% margin all round. Hero straight-on; second shot 45°. | eBay's framing guidance (https://export.ebay.com/en/first-steps/manage-listings/photo-tips/); margin leaves room for straightening and the square thumbnail crop. |
| **Background** | Garage door down behind the piece (flat, neutral), plain wall, or swept concrete. Small items: white poster board curved up the wall; jewelry/silver/watches: black velvet (matte, creases smoothed). Out of frame: lawn, cars, trash cans, hoses, the other pieces, people. | Plain backdrop keeps the item front and centre; matte black for shiny metal (https://www.ebay.com/sellercenter/listings/photo-tips · https://blog.picupmedia.com/how-to-photograph-jewelry-on-a-black-background). |
| **Phone settings** | Grid on; tap the item, hold for AE/AF lock, slide exposure down a touch if the piece is pale; 4:3 not 16:9; Portrait mode off; HDR/"Smart HDR" off for glass, chrome, screens; Live Photo off; highest-quality JPEG or HEIC. | 4:3 uses the full sensor, 16:9 is a crop (https://www.howtogeek.com/831731/how-to-take-photos-in-169-on-iphone/); marketplaces crop thumbnails to square/4:5, so 16:9 loses the ends. Portrait mode blurs edges of legs and arms; HDR haloes reflective edges. |
| **Steadiness** | Both hands, elbows in, or lean on the car/ladder; tripod or shutter timer for details. Burst 3, keep the sharpest. | eBay and whataroom both call for a tripod or braced phone (https://www.ebay.com/sellercenter/listings/photo-tips · https://whataroom.com/pages/how-to-photograph-a-sofa). |
| **Lens** (the glass) | Wipe it on a shirt before every shoot. | A smeared lens is the #1 cause of the "glowy" look that reads as a filter. |
| **Scale** | A coin, tape measure or hand in detail shots; a chair or a person's shoes beside a rug. | eBay: "place a coin or ruler beside the item" (https://export.ebay.com/en/first-steps/manage-listings/photo-tips/). |

## 2. Staging by family

Remove: everything that isn't sold with it (personal items, the dog, the other listings). Add only what buyers expect
in the room: a throw pillow on a sofa, one bowl on a shelf, a lamp lit. Never stage so the piece reads as a different
size (no tiny side table pushed against a sofa to make the sofa look big; no wide lens). eBay: props "can obscure the
item or confuse buyers about what's included" — if it's in the hero and not included, say so in the body.

| Family | Remove / add | Hero | Shot list (4–8) | Flaw shots |
|---|---|---|---|---|
| **Sofa / loveseat** | Cushions fluffed, throws off, one pillow allowed; lint-rolled | Straight-on at seat height, whole piece | 45°; side; cushions lifted (deck); back; legs; law tag | every stain, pilling, sagging cushion from above, pet scratches, frame wobble (video) |
| **Tables / case goods** | Empty top; drawers closed; dust it; hardware straight | Straight-on, top edge just visible | 45°; top in raking light (angled, so scratches show honestly); each drawer open; back/maker stamp; underside; hardware | gouges, water rings, veneer lift, missing hardware, wobble |
| **Beds** | **Set up** with a plain fitted sheet or bare slats, no bedding pile. If it can't be assembled: lay every part in assembly order on the driveway, hardware bag opened on a white sheet | Assembled, 45° from the foot | headboard straight-on; side rail joint; slats; hardware bag; the disassembled stack; manual/label | cracked slats, stripped bolts, scuffed rail ends |
| **Rugs** | Vacuumed; flat, every wave smoothed; nothing on it | Whole rug straight-down from a ladder (or from the garage attic hatch); never rolled | second end (colour varies by pile direction); pile macro; corner folded to show the back and binding; fringe; label | traffic lanes, stains, fraying, pet damage — in the same light as the hero (https://rencollection.com/blogs/news/rug-photography-tips-2026-guide-to-viral-texture-shots) |
| **Lamps** | Bulb in, **on**, shade straight; shoot in the garage with the door half down for the lit shot | Lit, straight-on, whole lamp | off in daylight for true colour; base; switch/cord; shade interior; label | shade dents/yellowing, cord wear, chips |
| **Electronics / TVs** | **On**, screen showing a bright clean image (a photo, not a menu); remote and cables in one shot | Powered on, straight-on | ports; model/serial label; remote + cables; stand; white-screen shot for dead pixels | scratches on screen (angled light), bent pins, missing feet |
| **Kitchen / appliances** | Cleaned inside and out; door **open** for interior; plugged in if it lights | Front, closed, clean | interior; control panel lit; model plate; back/coils; accessories (racks, trays, bowls) | rust, chips, stained seals, missing parts |
| **Clothing** | Steamed; **flat lay** on white board or a plain bedsheet, or on a hanger against the garage door; never on the floor | Flat lay, straight-down, whole garment | back; brand tag; size/care tag; fabric macro; measurements laid flat with a tape | pilling, stains, loose threads, hem wear |
| **Jewelry / watches** | Cleaned (gloves, microfiber); black velvet; 2× lens; museum putty to stand rings | Macro, 45°, one highlight | straight-down; hallmark/karat stamp macro; clasp; on a scale reading grams; beside a coin | scratches on case/crystal, missing stones, worn plating |
| **Glass / ceramics** | Washed; white board behind, window or open garage door behind the board for backlight (shows chips and cracks honestly) | Against white, slightly above eye level | base/maker's mark straight-down; rim from above; backlit; set together if a set | chips (fingernail on them), crazing, hairlines backlit |
| **Framed art** | Dust the glass; hang on a bare wall or lean on the closed garage door; shoot from 20–30° off axis or with the glass out; wear dark clothes | Whole piece, square in frame, no glare | signature/edition macro; frame corner; back (labels, hanging wire); with a chair for scale | frame chips, foxing, fading, glass scratches (https://shotkit.com/take-picture-without-glare/) |
| **Books** | Dust jackets straightened | Spine stack (titles readable) or single cover | open to title page; copyright page; top edge; dust jacket back | foxing, water damage, torn jacket, writing inside |
| **Toys / LEGO / lots** | Washed; **grid layout** on white board, everything visible, nothing stacked | Full grid straight-down | built set; box + instructions; minifigs together; batteries compartment | missing pieces counted and shown, cracks, chew marks |

(Per-family shot lists in `household-families.md` are the fuller versions; these are the staging rules on top of them.)

## 3. The honest-flaw rule

Every flaw gets **its own photo**, in the **same light as the hero** (not a dim close-up that reads as a cover-up),
with a coin, tape or hand for scale, and the body refers to it by number ("gouge on top, photo 4"). Put the flaw
shots after the angle and detail shots, before the label shot. It raises trust rather than lowering it: eBay tells
sellers to "call these out clearly in your listing description and photos" because photos "let the buyer see the actual
condition" and that is what prevents not-as-described returns
(https://pages.ebay.com/returns/tips.html · https://www.ebay.com/sellercenter/listings/photo-tips); Marketplace guides
say the same — photograph the defects so buyers see them before they commit, since misrepresentation is the common
source of buyer frustration and ghosting (https://www.cheapism.com/facebook-marketplace-mistakes ·
https://elementor.com/blog/how-to-sell-on-facebook-marketplace/). On our own listings: seen-but-no-messages is a trust
problem (playbook §1), and a buyer who already knows about the gouge doesn't walk at pickup.

## 4. Editing — what Claude does in Python, in order

`scripts/stage.py` applies these in this order to a folder of phone photos. Every step is reversible, global (whole
frame), and visible-honest; nothing is painted onto the item.

| # | Step | Setting | Pillow / numpy approach | Honesty check |
|---|---|---|---|---|
| 1 | **HEIC → JPEG** | keep full res, read EXIF orientation | `pillow_heif.register_heif_opener()`; `ImageOps.exif_transpose(img)` | — |
| 2 | **Auto-levels** (histogram stretch) | clip 0.5% each end, per channel or luminance only | `np.percentile(arr, [0.5, 99.5])` → rescale, `np.clip` | fixes grey driveway haze; luminance-only when colour must not shift |
| 3 | **White balance** | gray-world, or pick a known neutral (concrete, white board, garage door) | gray-world: scale each channel by `mean(gray)/mean(channel)`; neutral: scale so the sampled patch's R=G=B | correct the cast, never tint. Skip if the item is the only large colour in frame (gray-world would desaturate it) — pick a neutral instead |
| 4 | **Exposure** | +5–15% for garage/driveway shade; skip in open overcast | `ImageEnhance.Brightness(img).enhance(1.10)` or gamma `arr ** (1/1.1)` | highlights must not clip on the item; check `arr.max()` on the item's crop |
| 5 | **Contrast** | +3–8% | `ImageEnhance.Contrast(img).enhance(1.06)` | small; big contrast hides scratches in shadow |
| 6 | **Straighten** | ±3°; level the garage door seam, table edge or floor line | `img.rotate(angle, resample=BICUBIC, expand=False)` then crop the wedge corners | — |
| 7 | **Perspective (keystone)** | furniture shot off-axis or tilted down: pull verticals vertical, **partial** correction, then back off | `img.transform(size, Image.PERSPECTIVE, coeffs)` with coeffs solved from four corner points (numpy `lstsq`) | don't use on a 45° hero (it's meant to converge), on anything shot with 0.5×, or when the fix would stretch the piece — a stretched sofa misstates size (https://www.talkphotography.co.uk/threads/keystone-correction-when-to-use-it.703602/) |
| 8 | **Crop** | item + 5–10% margin; hero 4:3 or 1:1; details free | `img.crop(box)`; for 1:1 pad with the background's median colour, never stretch | the item stays whole; never crop a flaw out of the hero |
| 9 | **Clutter** | first by cropping; else clone **background only** (garage wall, concrete) over a hose or a trash can that is not touching the item | copy a clean patch of the same texture, `img.paste(patch, box)`, feather the edge with a `GaussianBlur` mask | never within ~5% of the item's outline; never on the item; a shadow the item casts stays |
| 10 | **Sharpen** | unsharp mask r=1, 60–80%, threshold 2 | `img.filter(ImageFilter.UnsharpMask(radius=1, percent=70, threshold=2))` | after resize; no halos on edges |
| 11 | **Resize + save** | 1600 px long edge; JPEG q=85–90, `optimize=True`; **strip EXIF** (GPS = our house) | `ImageOps.contain(img, (1600, 1600))`; `img.save(p, quality=88, exif=b"")` | Facebook strips GPS from public copies but keeps the original; strip it ourselves (https://www.fast.io/resources/social-media-photo-metadata-platforms-strip.md) |
| 12 | **Consistent set** | same WB and brightness target across all photos of one piece | compute each image's mean luminance, nudge to the hero's (±5%) | the flaw shot must not be darker than the hero |
| 13 | **Order + rename** | `<piece>-hero.jpg`, `-2`…: hero → angles → details → flaws → label | filename prefix; the listing body numbers follow this order | — |
| 14 | **Contact sheet** | all candidates for a piece in a grid, pick the hero | `Image.new` canvas, thumbnails pasted in rows, filename captioned with `ImageDraw` | Claude proposes, Dylan picks |

Oct 27 recipe actually used (`plans/2026-10-27-garage-clearout.md`): HEIC → JPG, crop, brightness +10%, contrast +6%,
hero chosen, resized to 1600 px tall. That is steps 1, 4, 5, 8, 11, 13 — `stage.py` adds 2, 3, 6, 10, 12, 14 by default
and 7, 9 only when asked.

**Never:** HDR/clarity glow; saturation or vibrance on fabric, wood or rugs (colour returns are the rug sellers' own
warning: https://rencollection.com/blogs/news/rug-photography-tips-2026-guide-to-viral-texture-shots); blur, heal or
clone on a scratch, stain or chip; AI background replacement or "virtual staging" of the item; stock, catalogue or
screenshot images (eBay allows catalogue images only as non-primary for pre-owned, Facebook removes them); sky swaps;
borders, text, logos, price stickers or watermarks (eBay policy; they also keep images out of Google Shopping:
https://www.ebay.com/sellercenter/listings/photo-tips); local dodge/burn on the item; filters of any kind.

## 5. Platform specs

| Platform | Photos | Size | Thumbnail / aspect | Rules |
|---|---|---|---|---|
| **Facebook Marketplace** | up to 10 per listing (app and web composer; verify on the day — some guides say the web composer caps lower on older accounts) | min 500×500, 1200–1600 px long edge; JPEG/PNG ≤10 MB | first photo = thumbnail, shown **square** in search grid and ~4:5 in feed — keep the item centred with margin | no stock, no copied images, no text overlays (price/contact), no screenshots; identical photos across two listings = duplicate rejection (playbook §2) (https://bgremove-2y1.pages.dev/guides/facebook-marketplace-image-requirements · https://elementor.com/blog/how-to-sell-on-facebook-marketplace/) |
| **eBay** | **24** free per listing + 1 video (form says "up to 40" since Apr 2026 but slots stop at 24) | min 500 px long side; 1600 recommended; ≤7 MB | first photo square-cropped in search; gallery shows full | no borders (unless part of the scene), no text/logos/watermarks; white or neutral background "always safe"; stock/catalogue not as primary for pre-owned (books/media excepted); show all sides and blemishes (https://www.ebay.com/sellercenter/listings/photo-tips · https://export.ebay.com/en/first-steps/manage-listings/photo-tips/ · https://www.valueaddedresource.net/ebay-expands-listings-photo-limit-40/) |
| **OfferUp** | 12 (business help centre figure; consumer app matches) | <5 MB, JPEG/PNG | square thumbnail | first photo must be the actual item (https://help.business.offerup.com/hc/en-us/articles/27947563430292) |
| **Craigslist** | 24 per post | upload ≤12 MB; displayed ~600 px on the long side, so detail must survive downscale; use .jpg | first image = thumbnail in gallery view | no official size doc; the help page only says use .jpg and resize if upload fails (https://www.craigslist.org/about/help/posting/features/images · https://softhandtech.com/?p=58919) |
| **Nextdoor For Sale & Free** | 10 | standard | square card | verified neighbours; same honesty rules (playbook §2) |

So: shoot everything to the eBay standard (1600 px, 24 slots) and the Facebook set is the first 10 of that order.

## 6. The 10-minute driveway shoot (multi-piece clear-out)

Before: lens wiped, grid on, 4:3, HDR off, Portrait off, garage door **up** for shade light, a swept 10×10 ft patch of
concrete, white poster board + black velvet + a coin + a tape measure in a bin, a step ladder.

| Min | Do |
|---|---|
| 0–1 | Pull each piece to the shade line one at a time; everything else back out of frame. Phone level, 1×. |
| 1–6 | Per piece (~45 s): hero straight-on at the right height → 45° → one side/back → one detail (finish, fabric, mechanism, label) → **every flaw** with the coin/tape → label/stamp. Burst the hero 3×. Beds assembled or parts in order; rug flat from the ladder; lamp lit; electronics on; coffee table open. |
| 6–8 | **Group shot for each set listing** (sofa + loveseat + ottoman; table + chairs; Porter set): all pieces together, one new photo that appears in no single listing — Facebook rejects a set listing whose photos are reused from the singles (playbook §2). Shoot two groupings so there is a spare. |
| 8–9 | Small items: poster board on the workbench, straight-down and 45°, then the base/mark; jewelry on velvet at 2×. |
| 9–10 | Scroll back once: anything blurry, cut off, or with a car in the corner — reshoot now, not tomorrow. AirDrop/upload the folder. |

Then Claude: `stage.py <folder>` → contact sheet → Dylan picks heroes → ordered, renamed set per piece → listing bodies
reference flaw photo numbers.

## Sources
- eBay Seller Center, photo tips — https://www.ebay.com/sellercenter/listings/photo-tips
- eBay export site, photo requirements — https://export.ebay.com/en/first-steps/manage-listings/photo-tips/
- eBay, returns tips (show flaws) — https://pages.ebay.com/returns/tips.html
- Value Added Resource, eBay 24 vs 40 photo limit (Apr 2026) — https://www.valueaddedresource.net/ebay-expands-listings-photo-limit-40/
- Facebook Marketplace image requirements (IsoPeel guide, unofficial) — https://bgremove-2y1.pages.dev/guides/facebook-marketplace-image-requirements
- Elementor, how to sell on Facebook Marketplace (10 photos, flaws) — https://elementor.com/blog/how-to-sell-on-facebook-marketplace/
- Closo, stock/edited photos on Marketplace — https://closo.co/blogs/platform-specific-guides/the-real-risk-do-stock-photos-get-taken-down-on-facebook-marketplace
- Cheapism, Marketplace mistakes — https://www.cheapism.com/facebook-marketplace-mistakes
- OfferUp business help, listing photos (12) — https://help.business.offerup.com/hc/en-us/articles/27947563430292
- Craigslist help, images — https://www.craigslist.org/about/help/posting/features/images · https://softhandtech.com/?p=58919
- WhatARoom, how to photograph a sofa — https://whataroom.com/pages/how-to-photograph-a-sofa
- Q is for Quandie, outdoor furniture shoots — https://qisforquandie.com/2019/04/26/outdoor-photo-shoots
- Picup Media, jewelry on black — https://blog.picupmedia.com/how-to-photograph-jewelry-on-a-black-background
- Ren Collection, rug photography — https://rencollection.com/blogs/news/rug-photography-tips-2026-guide-to-viral-texture-shots
- Shotkit, photos without glare — https://shotkit.com/take-picture-without-glare/
- TalkPhotography, keystone correction — https://www.talkphotography.co.uk/threads/keystone-correction-when-to-use-it.703602/
- How-To Geek, 4:3 vs 16:9 on iPhone — https://www.howtogeek.com/831731/how-to-take-photos-in-169-on-iphone/
- Fast.io, which platforms strip metadata — https://www.fast.io/resources/social-media-photo-metadata-platforms-strip.md
