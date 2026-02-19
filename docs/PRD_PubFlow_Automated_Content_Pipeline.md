# **Product Requirements Document: PubFlow**

**Date:** February 19, 2026

**Status:** Draft

**Owner:** CTO / Engineering Team

**Target System:** SvelteKit 2 (Svelte 5\) on Netlify (SSR)

## **1\. Executive Summary**

The goal is to build **PubFlow**, a **Human-in-the-loop Content Engine** housed within a single monorepo alongside the corporate website.

Instead of a "black box" script, PubFlow implements a **State Machine on Disk** where content progresses through stages (Idea \-\> Research \-\> Draft) via specific folders. Each piece of content is tracked by a **Human-Readable ID** (e.g., 001-strategic-vision) to ensure lineage and version control.

The workflow is entirely **Agent-Driven**: The user interacts exclusively via Claude Code Skills (e.g., /pub.new, /pub.draft), which either execute AI tasks or trigger underlying helper scripts.

## **2\. Problem Statement**

* **Need:** High-quality, regulatory-compliant content published 1-2x weekly.  
* **Control:** Need to "steer" the AI at the outline and draft stages.  
* **Tracking:** Need to strictly track the history of an article from idea to publication.  
* **Interface:** Unified interface (Chat CLI) for both generation and file management.

## **3\. System Architecture: The Monorepo**

We will use a simplified monorepo structure to keep content, scripts, and the website code together.

### **3.1 Directory Structure**

/my-company-monorepo  
  ├── .claude/  
  │    └── skills/            \# PubFlow Skills  
  │         ├── pub.new.md    \# Wraps \`new\_idea.py\`  
  │         ├── pub.next.md   \# Wraps \`promote.py\`  
  │         └── pub.draft.md  \# AI generation prompts  
  ├── scripts/                \# PubFlow Core Logic (Python/Node)  
  │    ├── new\_idea.py        \# Logic: Generates ID & file  
  │    └── promote.py         \# Logic: Moves files between stages  
  ├── pipeline/               \# The PubFlow State Machine  
  │    ├── 0\_context/         \# Brand Voice, Regulatory Guidelines  
  │    ├── 1\_ideas/           \# 001-topic-slug.md (Rough notes)  
  │    ├── 2\_research/        \# 001-topic-slug.md (AI Research)  
  │    ├── 3\_outlines/        \# 001-topic-slug.md (Human Reviewed)  
  │    ├── 4\_drafts/          \# 001-topic-slug.md (First Draft)  
  │    ├── 5\_refined/         \# 001-topic-slug.md (Polished)  
  │    └── 6\_ready/           \# Final MDX & Assets  
  └── web/                    \# SvelteKit App  
       ├── src/  
       │    ├── lib/content/  \# Symlinked or copied from '6\_ready'  
       │    └── routes/blog/  \# Dynamic generic route \[slug\]  
       └── netlify.toml

### **3.2 The ID System**

Every piece of content receives a permanent **Human-Readable ID** upon creation.

* **Format:** {SEQUENCE}-{SLUG} (e.g., 012-market-analysis)  
* **Traceability:** The ID remains constant as the file moves through folders 1\_ideas \-\> 6\_ready.

## **4\. Functional Requirements: The pub Namespace**

All interactions happen via the Agent using the pub namespace.

### **4.1 Stage Management Skills (Wrappers)**

These skills execute deterministic scripts to manage the file system state.

* **Skill:** /pub.new "Topic Name"  
  * **Mechanism:** Calls python scripts/new\_idea.py "Topic Name".  
  * **Action:** Finds next ID, creates pipeline/1\_ideas/013-topic.md.  
* **Skill:** /pub.next \<id\> (or /pub.promote)  
  * **Mechanism:** Calls python scripts/promote.py \<id\>.  
  * **Action:** Moves file from current folder (e.g., 1\_ideas) to next folder (e.g., 2\_research).  
* **Skill:** /pub.publish \<id\>  
  * **Mechanism:** Calls python scripts/publish.py \<id\>.  
  * **Action:** Moves final Markdown to web/src/lib/content/ and assets to web/static/images/.

### **4.2 Content Generation Skills (AI Tasks)**

These skills contain the Prompt Engineering logic to generate content.

**Step 1: Research**

* **Skill:** /pub.research \<id\>  
* **Context:** Reads pipeline/1\_ideas/\<id\>.md AND pipeline/0\_context/\*.  
* **Action:** Performs Web Search (Grounding). Overwrites file with detailed research brief and citations.

**Step 2: Structuring**

* **Skill:** /pub.outline \<id\>  
* **Context:** Reads pipeline/2\_research/\<id\>.md.  
* **Action:** Generates structured H2/H3 outline.  
* **Stop:** *User manually edits the outline in 3\_outlines/ before proceeding.*

**Step 3: Drafting**

* **Skill:** /pub.draft \<id\>  
* **Context:** Reads pipeline/3\_outlines/\<id\>.md (User Edits).  
* **Action:** Writes full content.

**Step 4: Quality Control**

* **Skill:** /pub.critique \<id\>  
* **Context:** Reads pipeline/4\_drafts/\<id\>.md \+ 0\_context/compliance\_rules.md.  
* **Action:** Appends a "Critique" section to the file (does not rewrite).  
* **Skill:** /pub.refine \<id\>  
* **Action:** Rewrites sections based on the critique.

**Step 5: Assets**

* **Skill:** /pub.illustrate \<id\>  
* **Action:** Scans text \-\> Queries Pexels API \-\> Downloads images \-\> Updates Frontmatter.

## **5\. Technical Stack**

| Component | Choice | Why? |
| :---- | :---- | :---- |
| **Monorepo** | **TurboRepo** | Simple management of scripts \+ web app. |
| **Frontend** | **Svelte 5 \+ SvelteKit** | SSR on Netlify for SEO. |
| **Agent Interface** | **Claude Code (.claude/skills)** | Unified CLI for workflow. |
| **Script Logic** | **Python (Typer)** | Handles file operations for /pub.new, /pub.next. |
| **Search** | **Google Grounding** | For up-to-date industry news. |
| **Images** | **Pexels API** | For /pub.illustrate. |

## **6\. Implementation Roadmap**

### **Phase 1: The Monorepo Skeleton**

* ![][image1]Initialize git repo & SvelteKit app.  
* ![][image1]Create pipeline/ folder structure.  
* ![][image1]Write scripts/manager.py to handle the logic for .new and .next.

### **Phase 2: The Skill Definitions**

* ![][image1]Create .claude/skills/pub.new.md (Prompt: "Run the new\_idea script...").  
* ![][image1]Create .claude/skills/pub.research.md (Prompt: "Read context, search web, write brief...").  
* ![][image1]Create .claude/skills/pub.draft.md (Prompt: "Write article based on outline...").  
* ![][image1]Create .claude/skills/pub.illustrate.md (Prompt: "Call the image fetcher script...").

### **Phase 3: The Svelte Integration**

* ![][image1]Install mdsvex.  
* ![][image1]Create dynamic route src/routes/blog/\[slug\]/+page.svelte.

## **7\. User Story: End-to-End Session**

1. **Start:** User types /pub.new "Sustainable Energy Trends".  
   * *Result:* 015-sustainable-energy.md created in 1\_ideas.  
2. **Context:** User pastes a PDF link into the file.  
3. **Research:** User types /pub.research 015\.  
   * *Result:* File updated with facts.  
4. **Move:** User types /pub.next 015\.  
   * *Result:* File moved to 2\_outlines.  
5. **Steer:** User manually edits the outline file.  
6. **Draft:** User types /pub.draft 015\.  
   * *Result:* Full text generated.  
7. **Publish:** User types /pub.publish 015\.  
   * *Result:* Site rebuilds with new post.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAbCAYAAADBLdN1AAAAWElEQVR4Xu3BAQ0AAADCoPdPbQ43oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAwMFugAB7qYxEgAAAABJRU5ErkJggg==>