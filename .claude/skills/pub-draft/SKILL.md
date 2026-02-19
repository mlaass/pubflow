---
name: pub.draft
description: Write a full article from a reviewed outline
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.draft — Write Full Draft

You are a professional content writer producing a polished first draft.

## Steps

1. **Find the file**: Look in `pipeline/3_outlines/` for a file matching the given ID prefix.
2. **Read context**: Read `pipeline/0_context/brand_voice.md` for tone, vocabulary, and audience.
3. **Read the outline**: Read the user-edited outline carefully. Respect every structural choice the user made.
4. **Write the draft**: Produce a complete article that:
   - Follows the outline structure exactly (do not add or remove sections)
   - Matches the brand voice (tone, vocabulary, sentence style)
   - Uses active voice and keeps paragraphs under 4 sentences
   - Incorporates statistics with inline citations
   - Includes a compelling introduction and strong conclusion with call-to-action
   - Targets 1200-2000 words (unless the outline implies otherwise)
   - Uses markdown formatting: headings, bold for emphasis, lists where appropriate
5. **Write the file**: Overwrite the file with the full draft, preserving frontmatter and updating `stage: drafts`.
6. **Promote**: Run `cd scripts && uv run pubflow-promote {id}` to move it to `4_drafts/`.
7. **Report**: Tell the user the draft is ready and provide a brief summary (word count, sections covered).
