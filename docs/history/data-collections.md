# Data Collections — What We Grow

Six datasets. Each one makes the next decision faster or more accurate. The
brand reference is the moat; the pass log is the one nobody keeps and the one
that tells us what we're missing.

All files live in the project as CSV so they open in Excel, import to Sheets,
and feed a tracker app later without conversion.

---

## 1. `items.csv` — the spine

One row per item **acquired**. Every acquisition, no exceptions, including the
ones that go badly. This is ground truth and everything else is measured against
it.

| Field | Type | Notes |
|---|---|---|
| `item_id` | text | Sequential: `2026-001` |
| `acquired_date` | date | |
| `source` | text | Facebook / eBay / thrift / estate sale / auction |
| `source_detail` | text | Store name or seller |
| `original_listing_title` | text | **Verbatim.** What the seller called it — this is the raw material of the whole business |
| `asking_price` | currency | |
| `amount_paid` | currency | |
| `category` | text | furniture / clothing / toys / housewares / collectible / electronics |
| `brand` | text | What it actually is |
| `line_or_pattern` | text | Brasilia, Acclaim, Butterprint, SX-780 |
| `era` | text | |
| `id_confidence` | HIGH/MED/LOW | At time of purchase |
| `id_evidence` | text | "Label inside top drawer" / "form match only" |
| `condition_grade` | A–F | |
| `est_resale_at_purchase` | currency | What we projected — **keeps us honest** |
| `clean_time_min` | number | |
| `stage_shoot_time_min` | number | |
| `dylan_time_min` | number | Sourcing + listing + shipping |
| `supplies_cost` | currency | |
| `listed_date` | date | |
| `list_platform` | text | |
| `list_title` | text | The title we wrote |
| `list_price` | currency | |
| `sold_date` | date | |
| `sold_price` | currency | |
| `platform_fees` | currency | |
| `shipping_cost` | currency | |
| `net_profit` | currency | Computed |
| `days_to_sell` | number | Computed |
| `profit_per_hour` | currency | Computed — **the metric that matters most** |
| `notes` | text | What surprised us |

**Why `est_resale_at_purchase` matters:** comparing it against `sold_price` across
fifty items is the only way to find out whether our valuations run optimistic, and
by how much. If we're systematically 20% high, every max bid should come down 20%.

---

## 2. `passes.csv` — the calibration set

One row per item **evaluated and declined**. Most resellers never build this, and
it's why most resellers never find out what they're missing. A pass log turns
declined items into training data.

| Field | Type | Notes |
|---|---|---|
| `pass_id` | text | |
| `date` | date | |
| `source` | text | |
| `listing_title` | text | Verbatim |
| `asking_price` | currency | |
| `suspected_brand` | text | Best guess at the time |
| `id_confidence` | HIGH/MED/LOW | |
| `est_resale` | currency | |
| `reason_passed` | text | price / confidence / condition / space / time / scope |
| `followup_sold_price` | currency | **Check back later** — what did it actually go for? |
| `followup_date` | date | |
| `verdict` | text | `correct pass` / `missed win` / `unknown` |
| `notes` | text | |

**The follow-up is the whole point.** Once a month, spot-check ten passes. If a
pattern of "missed win" shows up in a category, our confidence tiers or our
percentages are too conservative there and should move.

---

## 3. `comps.csv` — dated price evidence

Every comp pulled, recorded with its date. Comps decay; a dated archive shows how
fast and lets us reuse research instead of repeating it.

| Field | Type |
|---|---|
| `date_recorded` | date |
| `brand` | text |
| `line_or_pattern` | text |
| `category` | text |
| `condition_grade` | A–F |
| `platform` | text |
| `sold_price` | currency |
| `sale_date` | date |
| `included_shipping` | yes/no |
| `listing_url` | text |
| `notes` | text |

After a few months this becomes our own private price guide for the categories we
actually work in — more relevant than any published guide, because it's built from
the exact items we see.

---

## 4. `brands.csv` — the moat

The compounding asset. Every identification we make once gets written down so the
next one is instant recall instead of fresh research. After a hundred items,
triage stops being research.

| Field | Type | Notes |
|---|---|---|
| `brand` | text | |
| `category` | text | |
| `era_active` | text | |
| `tier` | A/B/C | A = always stop; B = stop if cheap; C = generally pass |
| `identifying_marks` | text | What the mark looks like |
| `mark_location` | text | **Where to find it** — the single most useful field |
| `lines_of_note` | text | The specific lines that carry the premium |
| `typical_sold_range` | text | |
| `best_platform` | text | |
| `fake_risk` | text | Roseville, designer goods, etc. |
| `demand_notes` | text | Seasonality, trend direction |
| `last_updated` | date | |

Seeded with the names in `identification-routing.md`; grows with every item.

---

## 5. `signals.csv` — what sourcing cues actually pay

Turns hunting intuition into measured hit rates.

| Field | Type | Notes |
|---|---|---|
| `signal_type` | text | title phrase / photo cue / seller behavior / misspelling / category |
| `signal_text` | text | "not sure what it is", "pendelton", "one dark photo" |
| `times_seen` | number | |
| `times_hit` | number | Led to a profitable buy |
| `hit_rate` | % | Computed |
| `avg_profit_when_hit` | currency | |
| `last_updated` | date | |

Signals with a measured hit rate get promoted into `standing-searches.md`.
Signals that don't produce get dropped. This is how the hunting gets sharper
rather than just busier.

---

## 6. `fees.csv` — keeps the math honest

Small, but stale numbers here corrupt every max bid we compute.

| Field | Type |
|---|---|
| `platform` | text |
| `category` | text |
| `fee_pct` | % |
| `fixed_fee` | currency |
| `payment_processing` | text |
| `listing_fee` | currency |
| `shipping_model` | text |
| `verified_date` | date |
| `source_url` | text |

**Re-verify quarterly.** Put it on the calendar.

---

## Review cadence

| When | What | Time |
|---|---|---|
| **Per item sold** | Complete the `items.csv` row. Add any new brand knowledge to `brands.csv`. | 5 min |
| **Weekly** | Update signal hit rates. Review aging inventory against the markdown schedule. | 20 min |
| **Monthly** | Follow up on ten `passes.csv` rows. Compare `est_resale_at_purchase` to actuals. Adjust confidence tiers if there's a pattern. | 45 min |
| **Quarterly** | Re-verify `fees.csv`. Review profit-per-hour by category and **kill the categories that don't pay.** | 1 hr |

That last one is the most valuable hour in the schedule. This business will
naturally drift toward whatever is most interesting rather than whatever is most
profitable, and the quarterly review is the correction.

---

## The metrics

Computed from `items.csv`:

1. **Profit per hands-on hour** — overall and by category. The constraint.
2. **Go-decision hit rate** — % of purchases that met or beat projected profit.
3. **Median days to sell** — the cash cycle.
4. **Capital turns per quarter** — how hard each dollar works.
5. **Valuation bias** — mean of (`sold_price` − `est_resale_at_purchase`). Should trend toward zero. If it's persistently negative, every max bid is too high.
6. **Pass calibration** — % of followed-up passes marked `missed win`.
