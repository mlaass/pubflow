---
name: pub.next
description: Promote a content file to the next pipeline stage
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
disable-model-invocation: true
---

# /pub.next — Promote to Next Stage

Run the following command with the user's content ID:

```bash
cd scripts && uv run pubflow-promote "$ARGUMENTS"
```

After running, confirm the move by showing the old and new locations.
