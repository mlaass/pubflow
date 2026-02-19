---
name: pub.illustrate
description: Find and download images for an article using the Pexels API
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.illustrate — Add Images

You are a visual editor selecting and downloading stock photos for an article.

## Prerequisites

The environment variable `PEXELS_API_KEY` must be set. If it's not available, tell the user:
> "Set your Pexels API key: `export PEXELS_API_KEY=your_key_here`
> Get a free key at https://www.pexels.com/api/"

## Steps

1. **Find the file**: Look in `pipeline/5_refined/` or `pipeline/6_ready/` for a file matching the given ID prefix.
2. **Read the article**: Scan the article for key visual themes — main topic, section topics, metaphors.
3. **Search for images**: For each key theme, query the Pexels API:

```bash
curl -s -H "Authorization: $PEXELS_API_KEY" \
  "https://api.pexels.com/v1/search?query=SEARCH_TERM&per_page=3&orientation=landscape"
```

4. **Select images**: Choose 1 hero image and 2-3 section images. Prefer:
   - High resolution (at least 1200px wide)
   - Landscape orientation
   - Professional, on-brand aesthetics
   - Diverse representation
5. **Download images**: Create an images directory and download selected photos:

```bash
mkdir -p pipeline/6_ready/images/{slug}
curl -sL -o pipeline/6_ready/images/{slug}/hero.jpg "PHOTO_URL"
```

6. **Update frontmatter**: Add image references to the article's frontmatter:

```yaml
heroImage: /images/{slug}/hero.jpg
heroAlt: "Description of the hero image"
```

7. **Add credits**: Append a credits section at the bottom of the article:

```markdown
---
*Photos by [Photographer](profile_url) on [Pexels](https://pexels.com)*
```

8. **Report**: Show the user the selected images and their placements.
