# Agent Memory System

## Overview

This directory stores accumulated knowledge that agents build over time. Memory allows agents to learn from past content performance, audience behavior, creative decisions, and strategic insights — making every week's output better than the last.

## How It Works

1. **Before starting work**: Each agent reads `shared.md` + their own memory file
2. **After completing work**: Agents append new learnings to their memory file
3. **Analytics Optimizer**: Writes to multiple agents' memory files after weekly/monthly reviews
4. **Orchestrator**: References memory when routing work to provide relevant context

## Memory Files

| File | Owner | Contents |
|------|-------|----------|
| `shared.md` | All agents | Cross-agent knowledge: audience insights, brand learnings, business changes |
| `analytics.md` | Analytics Optimizer | Performance patterns, KPI trends, what works/flops |
| `shortform-content.md` | Short-Form Content | Hook patterns, format insights, content gaps discovered |
| `scriptwriter.md` | Scriptwriter | Script patterns, tone calibrations, filming learnings |
| `copywriter.md` | Copywriter | CTA variations tested, caption styles, WA response patterns |
| `creative-director.md` | Creative Director | Visual styles, shot types, editing techniques that work |
| `strategy.md` | Strategy Planner | Campaign results, seasonal learnings, funnel insights |
| `market-research.md` | Market Research | Competitor intel, audience behavior shifts, trend history |
| `reviewer.md` | Reviewer | Common errors caught, quality patterns, recurring issues |

## Entry Format

Every memory entry follows this format:

```
### [YYYY-MM-DD] Short title

**Context**: What happened / what was observed
**Insight**: What we learned
**Action**: How this should change future work
**Evidence**: Data or example supporting this (optional but preferred)
```

## Rules

1. **Be specific** — "Question hooks get 2.3x more views than statement hooks" not "question hooks work better"
2. **Include evidence** — link to the content piece, metric, or review that produced the insight
3. **Date everything** — insights decay; what worked 6 months ago may not work now
4. **Prune quarterly** — during quarterly reviews, archive insights older than 6 months that haven't been re-confirmed
5. **No duplicates** — check if a similar insight already exists before adding; update the existing entry instead
6. **Contradictions are OK** — if new data contradicts an old insight, add the new entry and mark the old one as `[SUPERSEDED by YYYY-MM-DD entry]`
