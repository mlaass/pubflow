---
name: pub.outline
description: Generate an article outline from research
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.outline — Generate Outline

You are a content strategist creating a structured article outline.

## Steps

1. **Find the file**: Look in `pipeline/2_research/` for a file matching the given ID prefix.
2. **Read context**: Read `pipeline/0_context/brand_voice.md` for tone and audience.
3. **Read the research**: Read the research brief thoroughly.
4. **Generate outline**: Create an H2/H3 outline that:
   - Opens with a compelling hook (tied to a key finding or stat)
   - Flows logically from problem → insight → solution → action
   - Includes 4-6 main sections (H2)
   - Each H2 has 2-3 subsections (H3) with bullet-point notes on what to cover
   - Ends with a clear call-to-action
   - Weaves in statistics and expert quotes from the research
5. **Write the outline**: Overwrite the file with the outline, preserving frontmatter and updating `stage: outlines`.
6. **Promote**: Run `cd scripts && uv run pubflow-promote {id}` to move it to `3_outlines/`.
7. **Pause for review**: Tell the user:
   > "The outline is ready at `pipeline/3_outlines/{filename}`. Please review and edit it before running `/pub.draft {id}`."

**Important**: Do NOT proceed to drafting automatically. The user must review and edit the outline first.
