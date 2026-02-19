---
name: pub.publish
description: Publish a finished article from 6_ready to the web app
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
disable-model-invocation: true
---

# /pub.publish — Publish to Web

Run the following command with the user's content ID:

```bash
cd scripts && uv run pubflow-publish "$ARGUMENTS"
```

After running, confirm the file was copied to `web/src/lib/content/` and list any images copied.
