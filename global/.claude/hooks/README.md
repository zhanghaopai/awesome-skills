# Hook behavior

`post_edit_check.py` runs automatically after successful `Write` and `Edit` calls.
It is read-only, adds lightweight feedback for source files above 300 lines, and never fails an edit.
It is a responsibility-review signal, **not** a SOLID parser. It intentionally does not scan the entire repository, run expensive tests or call a model on each edit.

Optional AI-assisted Stop review is in `settings.agent-review.example.json`. Merge its `Stop` entry into `settings.json` only if you want an agent review on **every** stop (additional token usage; experimental hook type). The default installation does not enable this.

Requires Python 3.9+ accessible as `python` on PATH. Change `command` to a full Python executable path if needed. No third-party packages.

Diagnostics: run `/hooks` and `claude --debug`; use `/architecture-review` for manual full design review.
