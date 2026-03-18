# Suggested Linear Issue

Title:

`Fix counter decrement so values never go below zero`

Description:

```
The `decrement()` function in the counter demo is wrong for zero and negative inputs.

Acceptance criteria:
- `decrement(0)` returns `0`
- `decrement(-5)` returns `0`
- existing positive decrement behavior still works
- validation command passes:
  python3 -m unittest discover -s tests -q
```
