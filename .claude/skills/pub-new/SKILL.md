---
name: pub.new
description: Create a new content idea in the pipeline
user-invocable: true
argument: Topic title for the new idea
disable-model-invocation: true
---

# /pub.new — Create New Idea

Run the following command with the user's topic as the argument:

```bash
cd scripts && uv run pubflow-new "$ARGUMENTS"
```

After running, read the created file and show the user its path and contents.
