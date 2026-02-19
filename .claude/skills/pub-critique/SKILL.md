---
name: pub.critique
description: Review a draft for quality and compliance
user-invocable: true
argument: Content ID or numeric prefix (e.g. "002")
---

# /pub.critique — Quality Review

You are an editorial reviewer and compliance checker.

## Steps

1. **Find the file**: Look in `pipeline/4_drafts/` for a file matching the given ID prefix.
2. **Read compliance rules**: Read `pipeline/0_context/compliance_rules.md`.
3. **Read brand voice**: Read `pipeline/0_context/brand_voice.md`.
4. **Read the draft**: Read the full draft carefully.
5. **Critique**: Evaluate against these dimensions:
   - **Accuracy**: Are claims supported? Are statistics sourced and dated?
   - **Compliance**: Does it follow all compliance rules? Is the disclaimer included if required?
   - **Brand voice**: Does tone match the brand voice guide?
   - **Structure**: Does it flow logically? Are transitions smooth?
   - **Engagement**: Is the hook compelling? Is the CTA clear?
   - **Readability**: Paragraph length, active voice, jargon level
6. **Append critique**: Do NOT rewrite the article. Instead, APPEND a critique section at the end of the file:

```markdown

---

## Editorial Critique

### Strengths
- ...

### Issues to Address
1. [Specific issue with line reference and suggested fix]
2. ...

### Compliance Check
- [ ] Required disclaimer present
- [ ] No prohibited claims
- [ ] All statistics sourced
- ...
```

7. **Report**: Summarize the critique for the user and suggest running `/pub.refine {id}` when ready.
