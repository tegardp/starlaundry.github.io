# Star Laundry — Multi-Agent Marketing System

## Overview

This is a practical, repeatable marketing execution system for **Star Laundry Boyolali** — the first modern coin laundry in Boyolali, Indonesia. It supports monthly marketing planning, campaign execution, and weekly short-form content production across Instagram Reels and TikTok.

The system uses 9 specialized agents that collaborate through defined workflows. Each agent owns a specific domain and produces concrete deliverables.

## Business Context

- **Business**: Star Laundry — modern laundromat (koin laundry)
- **Location**: Jl. Jambu, Boyolali, Jawa Tengah
- **Tagline**: "Bersih Wangi, Pasti Rapi"
- **Services**: Cuci Setrika, Cuci Lipat, Self-Service, Drop-Off, Antar Jemput, Laundry Satuan
- **Price Range**: Rp 5,000–13,000/kg | Self-service Rp 10,000/7kg
- **Target**: Anak kos, pekerja kantoran, keluarga muda, pelaku usaha (radius 3–5km)
- **Channels**: WhatsApp (primary CTA), Instagram, TikTok, Google Maps, offline
- **Content Language**: Indonesian (Bahasa Indonesia)

## Agent Roster

| # | Agent | Role | Files |
|---|-------|------|-------|
| 1 | **Orchestrator** | Routes work, combines outputs, never does specialist work | `agents/orchestrator.md` |
| 2 | **Market Research** | Audience analysis, competitor intel, market demand | `agents/market-research.md` |
| 3 | **Strategy Planner** | Marketing plans, campaigns, funnels, calendars | `agents/strategy-planner.md` |
| 4 | **Short-Form Content** | Reel ideation, hooks, content buckets, platform adaptation | `agents/shortform-content-agent.md` |
| 5 | **Scriptwriter** | Video scripts, scene beats, alternative hooks, recording notes | `agents/scriptwriter.md` |
| 6 | **Copywriter** | Captions, WA copy, offer messaging, CTA text | `agents/copywriter.md` |
| 7 | **Creative Director** | Visual direction, shot ideas, filming style, editing rhythm | `agents/creative-director.md` |
| 8 | **Reviewer** | Quality checks, brand fit, platform fit, accuracy | `agents/reviewer.md` |
| 9 | **Analytics Optimizer** | KPI tracking, performance reviews, optimization loops | `agents/analytics-optimizer.md` |

## Folder Map

```
marketing/
├── README.md                    ← You are here
├── agents/                      ← Agent definitions and instructions
├── brand/                       ← Positioning, audience, tone, messaging
├── strategy/                    ← Plans, campaigns, funnels, pillars
├── calendar/                    ← Monthly/weekly plans, content calendar
├── shortform/                   ← Reel content system (IG + TikTok)
│   ├── idea-bank/               ← Raw content ideas
│   ├── briefs/                  ← Approved content briefs
│   ├── scripts/                 ← Video scripts
│   ├── hooks/                   ← Hook variations
│   ├── captions/                ← Caption + CTA copy
│   ├── shotlists/               ← Shot lists for filming
│   └── templates/               ← Short-form specific templates
├── campaigns/                   ← Campaign plans by type
├── assets/                      ← Visual guidelines, creative briefs
├── memory/                      ← Agent memory (accumulated learnings)
├── analytics/                   ← KPIs, reviews, experiment logs
├── workflows/                   ← Step-by-step production workflows
└── templates/                   ← Reusable templates
```

## Quick Start

### Monthly Planning (1st week of month)
1. Run `workflows/monthly-planning.md`
2. Analytics reviews last month → Strategy sets objectives → Short-Form Content builds calendar
3. Output: approved monthly plan in `calendar/monthly-plan.md`

### Weekly Content Batch (every Monday)
1. Run `workflows/weekly-content-production.md`
2. Short-Form Content ideates → Scriptwriter writes scripts → Copywriter writes captions → Creative Director adds shot lists → Reviewer checks everything
3. Output: 5–7 content pieces ready to film

### Single Reel Creation
1. Run `workflows/shortform-workflow.md`
2. Concept → Hook (3 variations) → Script → Caption → Shot list → Review → Platform adaptation
3. Output: filming-ready brief with script, caption, and shot list

### Campaign Launch
1. Use `templates/campaign-template.md` to plan
2. Run `workflows/monthly-planning.md` campaign section
3. Execute through weekly content batches

## Key Principles

1. **Orchestrator never does specialist work** — it routes and combines only
2. **Deep context stays in specialist agents** — each agent has its own expertise
3. **Scriptwriter is first-class** — not an afterthought; scripts drive content quality
4. **Reviewer checks before finalization** — nothing ships without review
5. **Analytics feeds back** — every performance insight improves future content
6. **Agents have memory** — each agent reads/writes `memory/` files to accumulate learnings across sessions
7. **Unified short-form workflow** — Instagram and TikTok share one pipeline with platform-specific adaptation notes
8. **WhatsApp is the primary CTA** — every piece of content drives to WhatsApp

## Operating Cadence

| Frequency | Activity | Owner |
|-----------|----------|-------|
| Monthly | Marketing plan + campaign planning | Strategy Planner |
| Weekly | Content batch production (5–7 pieces) | Short-Form Content + Scriptwriter |
| Weekly | WA broadcast (2x: Monday + Friday) | Copywriter |
| Weekly | Google Maps post (1x) | Copywriter |
| Weekly | Performance review | Analytics Optimizer |
| Per piece | Script → Caption → Shot list → Review | Full agent chain |
| Quarterly | Strategy review + pillar refresh | Strategy Planner + Market Research |

## Reference Documents

- `MARKETING_BLUEPRINT.md` (repo root) — Original comprehensive strategy with 60 content ideas, promo calendar, KPI targets
- `brand/` — Brand positioning, audience profiles, tone of voice
- `shortform/platform-differences.md` — Instagram Reels vs TikTok guidance
- `shortform/operating-model.md` — 10 collaboration scenarios explained step by step

---

## Repo Analysis (Phase 1)

### Business Context Discovered

- **Business Type**: Modern laundromat (koin laundry) — first of its kind in Boyolali
- **Owner**: Istiqomah Novi Purnanti
- **Location**: Jl. Jambu, Lodalang, Siswodipuran, Kec. Boyolali, Jawa Tengah 57311
- **Contact**: 0822-2567-2756 | @starlaundry.boyolali
- **Website**: starlaundry-byl.com (static HTML, GitHub Pages)
- **Hours**: 7:00 AM – 9:00 PM daily

### Services & Pricing

| Service | Price | Speed |
|---------|-------|-------|
| Cuci Setrika Wangi | Rp 6,000–13,000/kg | Reguler to 6-hour express |
| Cuci Lipat Rapi | Rp 5,000–8,000/kg | 1-day to 3-hour express |
| Setrika Wangi | Rp 5,000–10,000/kg | 2-day to 6-hour express |
| Self-Service | Rp 10,000/load (7kg, 40 min) | Same-day |
| Drop-Off | Rp 12,500/load | Same-day |
| Antar Jemput | Free (0–3km), free min 5kg (3–5km) | Per schedule |
| Laundry Satuan | Rp 8,000–85,000/piece | Varies |

### Target Audience Segments

1. **Anak Kos / Mahasiswa** — Price-sensitive students in boarding houses, TikTok-first
2. **Pekerja Kantoran** — Office workers wanting speed and convenience, WA-first
3. **Keluarga Muda** — Young families with bulk laundry, value reliability + free delivery
4. **Pelaku Usaha** — Hotels, restaurants, salons needing bulk recurring services

### Key Differentiators vs Traditional Laundry

| Star Laundry | Traditional |
|-------------|-------------|
| Dryer profesional (30 min, any weather) | Jemur matahari (weather-dependent) |
| Setrika uap (smoother results) | Setrika biasa |
| Mesin 20kg (clothes not cramped) | Small machines |
| WhatsApp auto-notifications | Manual/phone |
| Self-service available | Not available |
| Free pickup/delivery | Rarely offered |

### Active Promos (always-on)

| Promo | Details |
|-------|---------|
| Cuci Pertama | Rp 3,000/kg (new customers) |
| Referral | Rp 5,000 off for both parties |
| Stamp Card | 10 washes = 1 free |
| Senin Hemat | Rp 4,000/kg every Monday (min 3kg) |
| Promo Pelajar | 15% off with student ID |
| Review Reward | Rp 2,000 off for Google Maps review |

### Brand Identity

- **Primary tagline**: "Bersih Wangi, Pasti Rapi"
- **Brand colors**: Blue #2AADE0 (primary), Yellow #FBB818 (accent), Light Blue #E8F6FD
- **Voice**: Friendly, practical, casual Indonesian — like a helpful neighbor
- **Personality**: Modern, friendly, practical, reliable, affordable

### Existing Marketing Assets Found

- `MARKETING_BLUEPRINT.md` — 550-line comprehensive strategy (positioning, 30 IG ideas, 30 TikTok ideas, 20 WA templates, monthly calendar, KPI dashboard)
- Website with structured data, SEO, Google Analytics (GA-BZHKHWPQQ2)
- Facebook domain verification active
- Google Maps listing with coordinates

### Key Insights for Content Strategy

1. **WhatsApp-first**: All CTAs drive to WA — this is the conversion channel
2. **Hyper-local**: 3–5km radius, kos-kosan, campus, office areas
3. **Equipment is the differentiator**: 20kg washer, dryer, steam iron — content must show this
4. **Low-budget production**: Phone filming, CapCut editing, staff as talent
5. **Indonesian language**: All content in Bahasa Indonesia, casual register
6. **Seasonal calendar**: Ramadan, Lebaran, back-to-school, 17 Agustus, musim hujan

---

## Multi-Agent Architecture (Phase 2)

### Agent Interaction Map

```
                        ┌─────────────┐
                        │ ORCHESTRATOR │
                        │  (routes &   │
                        │  combines)   │
                        └──────┬──────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
    ┌─────▼─────┐      ┌─────▼──────┐      ┌─────▼──────┐
    │  MARKET    │      │  STRATEGY  │      │ ANALYTICS  │
    │  RESEARCH  │─────→│  PLANNER   │←─────│ OPTIMIZER  │
    └────────────┘      └─────┬──────┘      └────────────┘
                              │                    ▲
                    ┌─────────┼─────────┐          │
                    │         │         │          │
              ┌─────▼───┐ ┌──▼──────┐ ┌▼────────┐ │
              │SHORT-FORM│ │CREATIVE │ │COPY-    │ │
              │ CONTENT  │ │DIRECTOR │ │WRITER   │ │
              └────┬─────┘ └─────────┘ └────┬────┘ │
                   │                        │      │
              ┌────▼─────┐                  │      │
              │SCRIPT-   │──────────────────┘      │
              │WRITER    │                         │
              └────┬─────┘                         │
                   │                               │
              ┌────▼─────┐                         │
              │ REVIEWER │─────────────────────────┘
              └──────────┘
```

### Data Flow

1. **Planning flow**: Market Research → Strategy Planner → Short-Form Content → Scriptwriter → Copywriter/Creative Director → Reviewer → Orchestrator
2. **Feedback flow**: Analytics Optimizer → Strategy Planner (strategy changes) + Short-Form Content (content adjustments) + Scriptwriter (format insights)
3. **Review flow**: Any agent → Reviewer → back to originating agent (if revision) or Orchestrator (if approved)

### System Design Rules

1. Orchestrator never performs specialist work — only routes and combines
2. Deep context stays inside specialist agents — Orchestrator keeps summaries only
3. Short-form content workflow is unified for IG + TikTok — platform adaptation happens at the end
4. Scriptwriter is first-class — scripts drive content quality, not an afterthought
5. Reviewer checks all outputs before finalization — nothing ships without the quality gate
6. Analytics creates feedback loops — every week's performance improves next week's content

---

## Complete File Inventory (Phase 4)

### Agents (9 files)
| File | Purpose |
|------|---------|
| `agents/orchestrator.md` | Routes work, combines outputs, manages workflow |
| `agents/market-research.md` | Audience, competitors, trends, demand signals |
| `agents/strategy-planner.md` | Plans, campaigns, pillars, funnels, calendars |
| `agents/shortform-content-agent.md` | Reel ideation, hooks, content buckets, platform adaptation |
| `agents/scriptwriter.md` | Hook-first scripts, scene beats, recording notes |
| `agents/copywriter.md` | Captions, WA copy, CTAs, comment playbooks |
| `agents/creative-director.md` | Visual direction, shot lists, filming/editing style |
| `agents/reviewer.md` | Quality, accuracy, brand fit, duplication checks |
| `agents/analytics-optimizer.md` | KPI tracking, performance reviews, experiments |

### Brand (4 files)
| File | Purpose |
|------|---------|
| `brand/positioning.md` | Brand positioning, taglines, value prop, competitive matrix |
| `brand/audience.md` | 4 audience personas with demographics, pain points, offers |
| `brand/tone-of-voice.md` | Language rules, platform tone, emoji guide, on/off-brand examples |
| `brand/messaging-pillars.md` | 6 messaging pillars with copy examples in Indonesian |

### Strategy (5 files)
| File | Purpose |
|------|---------|
| `strategy/marketing-plan.md` | Monthly plan framework with filled example |
| `strategy/campaign-framework.md` | Campaign types, brief template, 3 example campaigns |
| `strategy/channel-strategy.md` | Per-channel strategy: WA, IG, TikTok, GMaps, offline |
| `strategy/content-pillars.md` | 7 content pillars with 10 ideas each |
| `strategy/funnel-map.md` | 6-stage funnel with tactics, offers, KPIs per stage |

### Workflows (6 files)
| File | Purpose |
|------|---------|
| `workflows/monthly-planning.md` | 9-step monthly planning with review gates |
| `workflows/weekly-content-production.md` | 8-step weekly batch production with filming schedule |
| `workflows/shortform-workflow.md` | 11-step single reel creation end-to-end |
| `workflows/scriptwriting-workflow.md` | 13-step scriptwriter-centric workflow |
| `workflows/review-workflow.md` | 12-step quality gate with checklists per deliverable type |
| `workflows/optimization-workflow.md` | Weekly + monthly analysis with feedback routing |

### Short-Form Content (7 files)
| File | Purpose |
|------|---------|
| `shortform/README.md` | System overview and quick reference |
| `shortform/platform-differences.md` | IG vs TikTok: 10 differences with Star Laundry examples |
| `shortform/content-pillars.md` | 7 video-specific pillars with format guidance |
| `shortform/content-series.md` | 8–10 repeatable series with episode ideas |
| `shortform/operating-model.md` | 10 collaboration scenarios step by step |
| `shortform/templates/idea-template.md` | Idea bank entry template |
| `shortform/templates/brief-template.md` | Short-form specific brief template |

### Templates (5 files)
| File | Purpose |
|------|---------|
| `templates/brief-template.md` | General content brief |
| `templates/script-template.md` | Full script template with hooks, beats, recording notes |
| `templates/caption-template.md` | Caption template for IG, TikTok, WA, GMaps |
| `templates/campaign-template.md` | Campaign planning template |
| `templates/content-template.md` | Completed content piece documentation |

### Calendar (3 files)
| File | Purpose |
|------|---------|
| `calendar/monthly-plan.md` | Monthly plan with week-by-week calendar |
| `calendar/weekly-plan.md` | Weekly plan with daily schedule and checklists |
| `calendar/content-calendar-template.md` | Calendar view with status tracking |

### Analytics (3 files)
| File | Purpose |
|------|---------|
| `analytics/kpi-framework.md` | Weekly + monthly KPIs with targets and tracking setup |
| `analytics/content-review-template.md` | Per-piece and weekly batch review templates |
| `analytics/experiment-log.md` | A/B test log with backlog of experiment ideas |

### Campaigns (4 files)
| File | Purpose |
|------|---------|
| `campaigns/README.md` | Campaign system overview |
| `campaigns/seasonal-campaigns/ramadan-lebaran.md` | Full Ramadan/Lebaran campaign plan |
| `campaigns/evergreen-campaigns/.gitkeep` | Placeholder for evergreen campaigns |
| `campaigns/launch-campaigns/.gitkeep` | Placeholder for launch campaigns |

### Memory (10 files)
| File | Purpose |
|------|---------|
| `memory/README.md` | Memory system overview, entry format, rules |
| `memory/shared.md` | Cross-agent knowledge: audience insights, brand learnings, seasonal patterns |
| `memory/analytics.md` | Performance patterns, KPI trends, experiment results |
| `memory/shortform-content.md` | Hook patterns, format insights, content gaps |
| `memory/scriptwriter.md` | Script patterns, tone calibrations, filming learnings |
| `memory/copywriter.md` | CTA variations, caption styles, WA response patterns |
| `memory/creative-director.md` | Visual styles, shot types, editing techniques |
| `memory/strategy.md` | Campaign results, seasonal learnings, funnel insights |
| `memory/market-research.md` | Competitor intel, audience behavior shifts, trend history |
| `memory/reviewer.md` | Common errors, quality patterns, recurring issues |

### Assets (4 files)
| File | Purpose |
|------|---------|
| `assets/visual-guidelines.md` | Brand colors, typography, photo/video style |
| `assets/creative-brief-template.md` | Universal creative brief |
| `assets/shot-list-template.md` | Shot list template for video content |
| `assets/editing-guidelines.md` | CapCut editing guidelines, export settings |

---

## Suggested Next Steps

### Immediate (This Week)
1. Pick 3 content ideas from `shortform/content-series.md` — start with "Tumpukan ke Rapi" (easiest to film, highest viral potential)
2. Run them through `workflows/shortform-workflow.md` to produce your first batch
3. Set up the Google Sheet per `analytics/kpi-framework.md` (4 tabs: Content Log, Performance Data, Weekly KPIs, Experiments)

### Short-Term (Next 2 Weeks)
4. Fill the April monthly plan using `calendar/monthly-plan.md` (post-Lebaran recovery)
5. Run your first experiment: question hook vs statement hook (see `analytics/experiment-log.md`)
6. Establish the weekly Monday batch planning cadence

### Medium-Term (Next Month)
7. Complete 4 weeks of content and run the first monthly performance review
8. Start the "Musim Hujan" series when rainy season hits
9. Build a 2-piece buffer of evergreen content for emergencies
10. Review and iterate — let Analytics Optimizer's feedback improve the system
