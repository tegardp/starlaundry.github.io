# Workflow: Content Optimization & Feedback Loop

## Trigger
- **Weekly**: Every Friday (performance review)
- **Monthly**: Last Friday of each month (deep analysis)
- **Ad hoc**: When a content piece significantly over/underperforms

## Required Inputs
- Content performance data from platform analytics (IG Insights, TikTok Analytics)
- Content log with posting dates, pillars, platforms, hooks used
- Business metrics (transactions, new customers, WA contacts)
- Previous optimization recommendations (to track if they were applied)

## Steps — Weekly Review

| # | Step | Owner Agent | Detail |
|---|------|-------------|--------|
| 1 | Collect performance data | **Analytics Optimizer** | Pull views, engagement, completion rate, saves, shares, WA clicks for all content posted this week |
| 2 | Rank content | **Analytics Optimizer** | Rank by views, then by engagement rate. Identify top 2 and bottom 2 |
| 3 | Analyze top performers | **Analytics Optimizer** | What hook type, pillar, format, posting time, platform? What made it work? |
| 4 | Analyze underperformers | **Analytics Optimizer** | What went wrong — weak hook, wrong time, saturated topic, poor execution? |
| 5 | Check experiment results | **Analytics Optimizer** | Any A/B tests running? Update results. |
| 6 | Generate recommendations | **Analytics Optimizer** | 3 specific, evidence-based recommendations for next week |
| 7 | Feed back to agents | **Analytics Optimizer** → **Orchestrator** | Route recommendations to relevant agents |
| 8 | Update memory | **Analytics Optimizer** | Write top insights to `memory/analytics.md` + relevant agent memory files | Persistent learnings for future weeks |

## Steps — Monthly Deep Analysis

| # | Step | Owner Agent | Detail |
|---|------|-------------|--------|
| 1 | Aggregate monthly KPIs | **Analytics Optimizer** | All KPIs vs targets, trend analysis |
| 2 | Content pillar analysis | **Analytics Optimizer** | Which pillar performs best? Is the mix right? |
| 3 | Hook type analysis | **Analytics Optimizer** | Question vs statement vs POV vs comparison — which gets best retention? |
| 4 | Platform comparison | **Analytics Optimizer** | IG vs TikTok — where should we invest more? |
| 5 | Business correlation | **Analytics Optimizer** + **Market Research** | Does social performance connect to transactions/revenue? |
| 6 | Competitive check | **Market Research** | Are competitors doing anything different that works? |
| 7 | Strategic recommendations | **Analytics Optimizer** → **Strategy Planner** | Data-driven input for next month's strategy |
| 8 | Update content approach | **Strategy Planner** + **Short-Form Content** | Adjust pillar mix, hook strategy, format priorities |
| 9 | Update memory (deep) | **Analytics Optimizer** | Write monthly insights to all relevant memory files + `memory/shared.md` | Accumulated monthly learnings |

## Feedback Loop Map

```
PUBLISH → MEASURE → ANALYZE → RECOMMEND → ADJUST → PUBLISH (improved)
   ↑                                                    |
   └────────────────────────────────────────────────────┘
```

### Who receives what feedback:

| Recommendation Type | Goes To |
|--------------------|---------|
| Pillar mix changes | Strategy Planner |
| Hook type performance | Short-Form Content + Scriptwriter |
| Posting time optimization | Orchestrator (calendar adjustment) |
| Visual/editing quality | Creative Director |
| Caption/CTA performance | Copywriter |
| Format changes (length, structure) | Scriptwriter |
| Audience insights | Market Research |

## Underperformer Iteration Process

When content performs below 0.5x average views OR <2% engagement:

| # | Step | Owner |
|---|------|-------|
| 1 | Flag underperformer | Analytics Optimizer |
| 2 | Diagnose root cause | Analytics Optimizer |
| 3 | Propose iteration (new hook, new angle, different format) | Analytics Optimizer → Short-Form Content |
| 4 | Create revised concept | Short-Form Content |
| 5 | Write new script | Scriptwriter |
| 6 | Review revised version | Reviewer |
| 7 | Publish and track | Analytics Optimizer |
| 8 | Compare performance: original vs iteration | Analytics Optimizer |
| 9 | Log learning | Analytics Optimizer (experiment log) |

## Experiment Framework

### How to run A/B tests:

1. **Hypothesis**: "Changing X will improve Y because Z"
2. **Variable**: One change only (hook type, posting time, format, etc.)
3. **Control**: Current approach
4. **Variant**: New approach
5. **Platform**: Test on higher-volume platform first (usually TikTok)
6. **Duration**: Minimum 2 weeks (4 data points)
7. **Success metric**: Define before testing
8. **Decision rule**: Variant must beat control by >20% to switch permanently

### Always-running experiments:
- Alternate hook types (question vs statement vs POV) on same pillar
- Test 2 posting times per week and track which performs better
- Test video length (30s vs 45s) on same content type

## Required Outputs

### Weekly Report
```
WEEKLY PERFORMANCE — Week [#], [Month Year]

TOP PERFORMERS:
1. [Title] — [views], [engagement %] — Why: [analysis]
2. [Title] — [views], [engagement %] — Why: [analysis]

UNDERPERFORMERS:
1. [Title] — [views], [engagement %] — Why: [analysis] — Fix: [recommendation]
2. [Title] — [views], [engagement %] — Why: [analysis] — Fix: [recommendation]

EXPERIMENTS IN PROGRESS:
- [Experiment]: [status/preliminary results]

RECOMMENDATIONS FOR NEXT WEEK:
1. [Specific, evidence-based recommendation]
2. [Specific, evidence-based recommendation]
3. [Specific, evidence-based recommendation]
```

### Monthly Report
```
MONTHLY PERFORMANCE — [Month Year]

KPI DASHBOARD:
| KPI | Target | Actual | Trend |
|-----|--------|--------|-------|

BEST PERFORMING:
- Pillar: [X] — [evidence]
- Hook type: [X] — [evidence]
- Platform: [X] — [evidence]
- Posting time: [X] — [evidence]

STRATEGIC RECOMMENDATIONS:
1. [Recommendation with evidence]
2. [Recommendation with evidence]

EXPERIMENT RESULTS:
- [Completed experiments + learnings]

NEXT MONTH PRIORITIES:
1. [Priority based on data]
```

## Completion Criteria

- Weekly report delivered by Friday evening
- Monthly report delivered last Friday of the month
- All recommendations are specific and evidence-based
- Experiment log updated (`analytics/experiment-log.md`)
- Feedback routed to correct agents via Orchestrator
