---
tracker:
  kind: linear
  project_slug: "testing-f21a45b44bd4"
  api_key: $LINEAR_API_KEY
  active_states:
    - Todo
    - In Progress
  terminal_states:
    - Done
    - Cancelled
    - Duplicate
polling:
  interval_ms: 5000
workspace:
  root: /tmp/symphony-linear-counter-workspaces
hooks:
  timeout_ms: 10000
  after_create: |
    python3 /Users/raj1.bajre/Documents/Symphony/demo-counter-app/scripts/bootstrap_workspace.py /Users/raj1.bajre/Documents/Symphony/linear-counter-demo-repo .
agent:
  max_concurrent_agents: 1
  max_turns: 4
codex:
  command: codex app-server
  approval_policy: never
  thread_sandbox: workspace-write
  turn_sandbox_policy:
    type: workspaceWrite
---

You are working on Linear issue `{{ issue.identifier }}`.

Title: {{ issue.title }}

Description:
{% if issue.description %}
{{ issue.description }}
{% else %}
No description provided.
{% endif %}

You are in an unattended Symphony run for a small Python repository.

Required workflow:

1. Read the issue carefully.
2. If the issue is in `Todo`, move it to `In Progress`.
3. Reproduce the problem locally with tests before changing code.
4. Fix only the scoped bug in this repository copy.
5. Run targeted validation after the fix.
6. If the bug is fixed and tests pass, move the Linear issue to `Done`.
7. If blocked, add a concise Linear comment describing the blocker and stop.

Use the `linear_graphql` tool for tracker updates when needed.

The expected validation command for this repository is:

```bash
python3 -m unittest discover -s tests -q
```
