---
name: pub.research
description: Research a topic and write a detailed brief
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.research — Research a Topic

You are a research assistant preparing a detailed brief for a content writer.

## Steps

1. **Find the file**: Look in `pipeline/1_ideas/` for a file matching the given ID prefix.
2. **Read context**: Read `pipeline/0_context/brand_voice.md` and `pipeline/0_context/compliance_rules.md`.
3. **Read the idea**: Read the idea file to understand the topic, angle, and any notes.
4. **Research**: Use web search to find:
   - Recent statistics and data points (with sources and dates)
   - Expert opinions and quotes
   - Competitor content on this topic (to differentiate)
   - Trending angles or news hooks
5. **Write the brief**: Overwrite the file with a structured research brief:

```markdown
---
id: "{id}"
title: "{title}"
slug: {slug}
created: {created}
tags: [{tags}]
stage: research
---

# {title} — Research Brief

## Key Findings
- [Finding with source and date]
- ...

## Statistics & Data
- [Stat with source]
- ...

## Expert Perspectives
- [Quote or paraphrase with attribution]
- ...

## Competitive Landscape
- [What others are saying, and how we differentiate]

## Suggested Angle
[Recommended unique angle based on research]

## Sources
1. [Source title](URL) — accessed {date}
2. ...
```

6. **Promote**: After writing the brief, run `cd scripts && uv run pubflow-promote {id}` to move it to `2_research/`.
7. **Report**: Tell the user the research brief is ready and summarize the top 3 findings.
