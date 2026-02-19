# PubFlow — Agent-Driven Content Pipeline

## Project Structure

```
pubflow/
├── pipeline/           # State machine on disk
│   ├── 0_context/      # Brand voice & compliance rules
│   ├── 1_ideas/        # Raw content ideas
│   ├── 2_research/     # Research briefs
│   ├── 3_outlines/     # Structured outlines (human-edited)
│   ├── 4_drafts/       # First drafts
│   ├── 5_refined/      # Polished articles
│   └── 6_ready/        # Ready for publishing
├── scripts/            # Python pipeline management (uv + typer)
├── web/                # SvelteKit blog (mdsvex, adapter-netlify)
└── .claude/skills/     # 9 pub.* skills
```

## Content ID Format

`{NNN}-{slug}` — e.g. `001-getting-started-with-pubflow`. The numeric prefix is zero-padded to 3 digits and stays constant as the file moves through stages.

## Pipeline Stages

1. **ideas** → 2. **research** → 3. **outlines** → 4. **drafts** → 5. **refined** → 6. **ready**

Files move forward via `pubflow-promote`. The `stage` field in frontmatter is updated automatically.

## Available Commands

| Command | What it does |
|---------|-------------|
| `/pub.new "Title"` | Create idea in `1_ideas/` |
| `/pub.research <id>` | Web search → research brief |
| `/pub.outline <id>` | Research → structured outline |
| `/pub.draft <id>` | Outline → full article |
| `/pub.critique <id>` | Append editorial critique |
| `/pub.refine <id>` | Rewrite addressing critique |
| `/pub.illustrate <id>` | Download Pexels images |
| `/pub.next <id>` | Move file to next stage |
| `/pub.publish <id>` | Copy from `6_ready/` to web app |

## Running Scripts

```bash
cd scripts && uv run pubflow-new "My Topic"
cd scripts && uv run pubflow-promote 001
cd scripts && uv run pubflow-publish 001
```

## Environment Variables

- `PEXELS_API_KEY` — Required for `/pub.illustrate`

## Tech Stack

- **Monorepo**: TurboRepo with bun workspaces
- **Web**: SvelteKit 2 (Svelte 5) + mdsvex + adapter-netlify
- **Scripts**: Python 3.11+ with uv, typer
- **Agent**: Claude Code skills (.claude/skills/)
