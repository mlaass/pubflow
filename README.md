# PubFlow

A GitHub template for an agent-driven content pipeline. Content progresses through a state machine on disk — from idea to published blog post — driven by Claude Code skills.

## Prerequisites

- [Bun](https://bun.sh/) (v1.0+)
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- (Optional) [Pexels API key](https://www.pexels.com/api/) for image sourcing

## Quick Start

```bash
# 1. Clone / use this template
gh repo create my-company-blog --template pubflow
cd my-company-blog

# 2. Install dependencies
bun install           # JS dependencies (root + web)
cd scripts && uv sync # Python dependencies

# 3. Customize your brand
# Edit pipeline/0_context/brand_voice.md
# Edit pipeline/0_context/compliance_rules.md

# 4. Start creating content (in Claude Code)
/pub.new "My First Article"
/pub.research 002
/pub.outline 002
# Edit the outline in pipeline/3_outlines/
/pub.draft 002
/pub.critique 002
/pub.refine 002
/pub.illustrate 002
/pub.next 002          # move to 6_ready
/pub.publish 002       # copy to web app

# 5. Run the dev server
bun dev
```

## Pipeline Walkthrough

Content moves through 6 stages as files in the `pipeline/` directory:

| Stage | Folder | Description |
|-------|--------|-------------|
| 1 | `1_ideas/` | Raw topic ideas with angle and notes |
| 2 | `2_research/` | AI-researched brief with sources |
| 3 | `3_outlines/` | Structured H2/H3 outline — **you edit this** |
| 4 | `4_drafts/` | Full first draft |
| 5 | `5_refined/` | Polished version after critique cycle |
| 6 | `6_ready/` | Final article ready to publish |

Each file has a permanent ID like `001-getting-started-with-pubflow` that stays constant across stages.

## Available Skills

| Skill | Description |
|-------|-------------|
| `/pub.new "Title"` | Create a new idea |
| `/pub.research <id>` | Research a topic with web search |
| `/pub.outline <id>` | Generate an article outline |
| `/pub.draft <id>` | Write a full draft from the outline |
| `/pub.critique <id>` | Review for quality and compliance |
| `/pub.refine <id>` | Rewrite addressing the critique |
| `/pub.illustrate <id>` | Source images from Pexels |
| `/pub.next <id>` | Promote to next stage |
| `/pub.publish <id>` | Publish to the web app |

## Customization

### Brand Voice

Edit `pipeline/0_context/brand_voice.md` to define your tone, audience, vocabulary, and example sentences. All AI skills read this file to match your style.

### Compliance Rules

Edit `pipeline/0_context/compliance_rules.md` to set disclaimers, prohibited claims, and editorial rules. The `/pub.critique` skill checks drafts against these rules.

### Web App

The SvelteKit app in `web/` renders published content using mdsvex. Customize:
- `web/src/routes/+page.svelte` — Landing page
- `web/src/routes/blog/+page.svelte` — Blog index
- `web/src/routes/blog/[slug]/+page.svelte` — Post layout

### Deployment

Configured for Netlify out of the box. See `web/netlify.toml`.

## Project Structure

```
pubflow/
├── .claude/skills/     # 9 pub.* Claude Code skills
├── docs/               # PRD and project documentation
├── pipeline/           # Content state machine
│   ├── 0_context/      # Brand voice & compliance rules
│   └── 1-6_*/          # Pipeline stages
├── scripts/            # Python CLI tools (uv + typer)
│   └── src/pubflow_scripts/
├── web/                # SvelteKit blog
│   └── src/
│       ├── lib/content/ # Published articles land here
│       └── routes/blog/ # Blog routes
├── CLAUDE.md           # Agent project context
├── turbo.json          # TurboRepo config
└── package.json        # Root workspace config
```

## License

MIT
