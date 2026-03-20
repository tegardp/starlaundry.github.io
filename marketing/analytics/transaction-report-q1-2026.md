# Star Laundry — Transaction Analytics Report
**Period**: 1 Januari – 18 Maret 2026 (77 hari operasional)
**Data Source**: Transformed sheet (4,860 item rows / 3,040 invoices)
**Holiday**: 19–23 Maret 2026 (Lebaran — tidak beroperasi)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Revenue | Rp 96,275,816 |
| Total Transactions | 3,040 |
| Unique Customers | 742 |
| Avg Revenue/Day | Rp 1,250,335 |
| Avg Transactions/Day | 39.5 |
| Avg Revenue/Transaction | Rp 31,670 |
| Repeat Customer Rate | 60.8% (451/742) |
| Payment Collection Rate | 98.4% Lunas |
| Pickup Completion Rate | 96.2% Diambil Semua |

---

## 1. Revenue Trends

### Monthly
| Bulan | Revenue | Transaksi | Rev/Day |
|-------|---------|-----------|---------|
| Januari | Rp 34,109,990 | 1,098 | Rp 1,100,322 |
| Februari | Rp 39,392,366 | 1,245 | Rp 1,406,870 |
| Maret (1–18) | Rp 22,773,460 | 697 | Rp 1,265,192 |

**Trend**: Februari was the peak month (+15.5% vs Jan). Maret on track similarly before Lebaran pause.

### Weekly
| Minggu | Revenue | Transaksi |
|--------|---------|-----------|
| W01 (1–4 Jan) | Rp 3,134,470 | 103 |
| W02 (5–11 Jan) | Rp 6,703,555 | 219 |
| W03 (12–18 Jan) | Rp 7,176,765 | 231 |
| W04 (19–25 Jan) | Rp 9,886,240 | 307 |
| W05 (26 Jan–1 Feb) | Rp 8,644,575 | 296 |
| W06 (2–8 Feb) | Rp 10,359,140 | 335 |
| W07 (9–15 Feb) | Rp 10,045,983 | 319 |
| W08 (16–22 Feb) | Rp 9,116,130 | 275 |
| W09 (23 Feb–1 Mar) | Rp 9,581,598 | 293 |
| W10 (2–8 Mar) | Rp 8,665,004 | 285 |
| W11 (9–15 Mar) | Rp 7,770,971 | 229 |
| W12 (16–18 Mar) | Rp 5,191,385 | 148 |

**Peak week**: W06 (Rp 10.4M, 335 txn). Steady plateau W04–W10 around Rp 8.6–10.4M/week.

---

## 2. Service Mix

### By Category
| Kategori | Revenue | Share |
|----------|---------|-------|
| Cuci Setrika | Rp 32,356,980 | 33.6% |
| Drop Off | Rp 19,357,500 | 20.1% |
| Cuci Lipat | Rp 17,478,110 | 18.2% |
| Self Service | Rp 13,385,000 | 13.9% |
| Satuan/Lainnya | Rp 11,236,051 | 11.7% |
| Setrika Saja | Rp 2,417,175 | 2.5% |
| Delivery | Rp 45,000 | 0.0% |

### Top 10 Services by Revenue
| Service | Revenue | Orders | Avg/Order |
|---------|---------|--------|-----------|
| Cuci Setrika Wangi 2 Hari | Rp 18,491,070 | 582 | Rp 31,771 |
| Cuci Lipat Rapi 1 Hari | Rp 12,085,000 | 524 | Rp 23,063 |
| Drop off Kering Saja | Rp 7,826,500 | 426 | Rp 18,372 |
| Drop Off Cuci Kering | Rp 7,650,000 | 224 | Rp 34,152 |
| Cuci Setrika Wangi 1 Hari | Rp 6,304,910 | 157 | Rp 40,159 |
| Cuci Saja (Self service) | Rp 4,590,000 | 387 | Rp 11,860 |
| Cuci Setrika Wangi Reguler | Rp 4,292,280 | 124 | Rp 34,615 |
| Kering Saja (Self Service) | Rp 4,210,000 | 303 | Rp 13,894 |
| Drop off Cuci Saja | Rp 3,642,000 | 233 | Rp 15,631 |
| Cuci Setrika Wangi 6 Jam | Rp 3,268,720 | 57 | Rp 57,346 |

**Insight**: "Cuci Setrika Wangi 2 Hari" is the #1 service (19.2% of total revenue). Express services (6 Jam, 3 Jam) have much higher per-order value — opportunity for upsell.

---

## 3. Customer Analysis

### Retention
| Metric | Value |
|--------|-------|
| Total Unique Customers | 742 |
| Repeat Customers (2+ visits) | 451 (60.8%) |
| One-time Customers | 291 (39.2%) |
| Customers with 5+ visits | 198 (26.7%) |
| Customers with 10+ visits | 97 (13.1%) |

### Visit Frequency Distribution
| Visits | Customers | % |
|--------|-----------|---|
| 1 | 291 | 39.2% |
| 2–3 | 197 | 26.5% |
| 4–6 | 115 | 15.5% |
| 7–10 | 69 | 9.3% |
| 11–20 | 53 | 7.1% |
| 21+ | 17 | 2.3% |

### New vs Returning Customers (Weekly)
| Week | New | Return | Return % |
|------|-----|--------|----------|
| W01 | 94 | 9 | 9% |
| W02 | 117 | 102 | 47% |
| W03 | 64 | 167 | 72% |
| W04 | 101 | 206 | 67% |
| W05 | 61 | 235 | 79% |
| W06 | 73 | 261 | 78% |
| W07 | 53 | 265 | 83% |
| W08 | 44 | 230 | 84% |
| W09 | 36 | 256 | 88% |
| W10 | 36 | 249 | 87% |
| W11 | 27 | 202 | 88% |
| W12 | 36 | 111 | 76% |

**Trend**: New customer acquisition slowing (94/week → 27–36/week). Return rate healthy at 83–88%. Need fresh acquisition push post-Lebaran.

### Top 10 Customers by Revenue
| Phone | Revenue | Visits |
|-------|---------|--------|
| 6282226901886 | Rp 1,822,406 | 32 |
| 6282128806703 | Rp 1,638,370 | 26 |
| 6285729460185 | Rp 1,336,850 | 35 |
| 6281226066497 | Rp 1,109,300 | 21 |
| 6285641681198 | Rp 1,095,550 | 25 |
| 6285876048486 | Rp 995,210 | 32 |
| 6281393224496 | Rp 917,110 | 27 |
| 6285728517299 | Rp 755,800 | 13 |
| 6281325707363 | Rp 739,790 | 12 |
| 6281338941538 | Rp 701,500 | 23 |

---

## 4. Operational Patterns

### Peak Days
| Hari | Revenue | Transaksi |
|------|---------|-----------|
| Sabtu | Rp 16,074,850 | 508 |
| Jumat | Rp 15,325,565 | 486 |
| Minggu | Rp 14,247,275 | 478 |
| Selasa | Rp 13,516,424 | 419 |
| Rabu | Rp 13,284,304 | 417 |
| Senin | Rp 12,621,703 | 382 |
| Kamis | Rp 11,205,695 | 350 |

**Peak**: Weekend (Jumat–Minggu) accounts for 47.4% of all transactions. Kamis is the slowest day.

### Peak Hours
| Jam | Transaksi | Pola |
|-----|-----------|------|
| 07:00–08:59 | 627 | Morning rush |
| 09:00–10:59 | 598 | Late morning |
| 11:00–12:59 | 470 | Midday dip |
| 13:00–14:59 | 356 | Afternoon low |
| 15:00–16:59 | 372 | Afternoon recovery |
| 17:00–18:59 | 390 | Evening pickup |
| 19:00–20:59 | 221 | Evening wind-down |

**Peak hours**: 07:00–10:59 (40.3% of daily transactions). Afternoon 13:00–14:59 is the quietest period.

### Turnaround Time
| Metric | Value |
|--------|-------|
| Median | 6.0 hours |
| Average | 20.1 hours |
| Under 6 hours | 48.0% |
| Under 24 hours | 68.3% |
| Under 48 hours | 81.4% |

---

## 5. Payment & Pickup Status

| Payment Status | Count | % |
|----------------|-------|---|
| Lunas | 2,991 | 98.4% |
| Belum Lunas | 49 | 1.6% |

| Pickup Status | Count | % |
|---------------|-------|---|
| Diambil Semua | 2,925 | 96.2% |
| Belum Diambil | 112 | 3.7% |
| Diambil Sebagian | 3 | 0.1% |

**Note**: 112 orders belum diambil — potential WA reminder campaign target.

---

## 6. Key Insights & Recommendations

### Strengths
1. **Strong retention**: 60.8% repeat rate, healthy for local service business
2. **High collection rate**: 98.4% paid — minimal bad debt
3. **Weekend dominance**: Jumat–Minggu is the money zone — keep staffing full
4. **Cuci Setrika Wangi 2 Hari**: Workhorse service, 19.2% of revenue

### Opportunities
1. **New customer acquisition declining** (W01: 94 new → W11: 27 new) — post-Lebaran relaunch campaign needed
2. **Express upsell**: 6 Jam services have 2x higher per-order value (Rp 57K vs Rp 32K) — promote urgency
3. **Delivery underutilized**: Only Rp 45K total — huge untapped potential for Antar Jemput
4. **Kamis is slowest day**: Consider "Kamis Hemat" promo (like existing Senin Hemat)
5. **Afternoon slot empty** (13:00–15:00): Target office workers with "Titip Siang" promo
6. **112 belum diambil**: Automated WA reminder = easy recovery revenue
7. **Self Service growing**: 13.9% of revenue — content should showcase this for anak kos segment

### Post-Lebaran Priorities (24 Maret onwards)
1. "Selamat Datang Kembali" reopening campaign
2. Fresh customer acquisition push (target: 60+ new customers/week like W04 levels)
3. Stamp card reminder for returning customers
4. Referral push while Lebaran momentum is fresh
