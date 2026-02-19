---
name: pub.refine
description: Rewrite a draft addressing the editorial critique
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.refine — Refine Draft

You are a senior editor producing the final polished version of an article.

## Steps

1. **Find the file**: Look in `pipeline/4_drafts/` for a file matching the given ID prefix.
2. **Read context**: Read `pipeline/0_context/brand_voice.md` and `pipeline/0_context/compliance_rules.md`.
3. **Read the draft + critique**: Read the file. It should contain both the draft and an appended "Editorial Critique" section.
4. **Refine**: Rewrite the article to address every issue raised in the critique:
   - Fix all compliance issues
   - Improve weak areas identified in the critique
   - Maintain the strengths noted
   - Ensure brand voice consistency
   - Add missing sources or disclaimers
5. **Remove critique section**: The refined version should NOT include the "Editorial Critique" section — it is consumed by this step.
6. **Write the file**: Overwrite with the refined article, preserving frontmatter and updating `stage: refined`.
7. **Promote**: Run `cd scripts && uv run pubflow-promote {id}` to move it to `5_refined/`.
8. **Report**: Tell the user the refined version is ready. Summarize what changed.
