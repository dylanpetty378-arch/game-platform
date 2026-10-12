# Shareable finds report – format standard

The PDF Dylan texts to whoever runs pickups (first made Sept 21, 2026: `DFW-Resale-Finds.pdf`). Generator: `claude/build_finds_pdf.py` – replace the `items` and `leads` lists, run, done. Keep every future report in this structure so it reads the same each time.

## Who it's for
Someone with **no context from our chats** – a friend, family member or helper. It must make sense on a phone, on its own.

## Voice and tone
- **Objective and informational**, not instructions and not in Dylan's voice. "Worth checking…", "Sold for…", never "Buy this" / "Text me".
- Conversational and plain. Short sentences. No jargon without a two-word explanation ("Decipher, the company that made the 1990s Star Wars card game").
- Honest about uncertainty: "Unclear", "probably", "could be tourist pottery". Never overstate.

## Page structure
1. **Title:** "Underpriced finds around Dallas–Fort Worth" (or the area covered).
2. **Date line:** date, plus "every listing was confirmed still up" when the liveness check was run.
3. **Intro paragraph (3–4 sentences):** what these are (secondhand listings that look underpriced, usually because the photos show a brand the listing doesn't mention), what each entry covers, that prices are asking prices on that date, and that listings sell fast.
4. **Ratings line:** Top pick › Strong › Good › Borderline, colored, with one sentence on what drives the rating (gap between asking and sold prices, and how sure the ID is), and where sold prices come from.
5. **"The finds"** – one card per item, sorted Top pick → Borderline.
6. **"Promising, but missing a key detail"** – smaller cards for leads.
7. **Footer line:** sale prices are examples, not guarantees; condition changes value.

## Item card (in this order)
| Line | Content |
|---|---|
| Header bar | Colored rating word + plain name of what it actually is (brand/model in parentheses) |
| Facts line | **Asking price** (and "likely takes ~$X" or "was $Y" when known) · city · platform · **View listing** (clickable link – required) |
| Context (2–3 sentences) | What the item is and why it matters to buyers. |
| **Selling elsewhere:** | Real sold prices – specific sales when we have them ("$341, $380, $395…"), otherwise a sourced range. Name the source type (eBay sold, price guide). |
| **Does the seller know?** | Yes / Partly / No / Unclear + the evidence: quote the seller's actual title, note price cuts and how long it's been listed. **Must come from the live check, never a guess.** |
| **Worth checking:** | The one or two things to confirm in person (label under the seat, shutter fires, bobbin case present). |

## Lead card
Name · price · city · platform · **View listing** / one line of context with the sold-price range / **Missing:** the one fact needed from the seller.

## Visual spec (ReportLab)
- Letter, 40pt side margins; DejaVu Sans (regular + bold, with bold mapping registered so `<b>` works).
- Title 20pt bold; section heads 14pt bold; card body 9.5–10.5pt.
- Cards = one-column tables, 532pt wide, colored 5pt left bar + 1pt border in the rating color, light-gray header row, `KeepTogether` so a card never splits across pages.
- Rating colors: Top pick `#C00000`, Strong `#548235`, Good `#2F5597`, Borderline `#BF8F00`, Lead gray `#7F7F7F`.
- Links: blue `#0563C1`, underlined, text "View listing".
- Target length: 2–3 pages for ~10 items + 4 leads.

## Before sending
- Run the liveness check; drop sold items; update "Does the seller know?" from the real titles.
- Every card has a working link.
- Render pages to PNG and look at them once (bold labels, no split cards, no overflow).
