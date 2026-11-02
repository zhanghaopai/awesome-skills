"""Claude Code PostToolUse: cheap, non-mutating source-file heuristics.
Reads hook JSON from stdin; outputs additionalContext only for actionable warnings.
Requires Python 3.9+; no third-party packages.
"""
import json
import pathlib
import sys

EXTS = {'.py', '.java', '.cpp', '.cc', '.cxx', '.c', '.h', '.hpp', '.hxx', '.js', '.jsx', '.ts', '.tsx', '.go', '.rs', '.cs'}
SKIP = {'node_modules', '.git', 'dist', 'build', 'target', 'vendor', '.venv', 'venv', 'generated', '__pycache__'}
FILE_REVIEW_LINES = 300
FILE_ALERT_LINES = 600
MAX_BYTES = 2_000_000

def main():
    try:
        event = json.load(sys.stdin)
        if event.get('tool_name') not in ('Write', 'Edit', 'MultiEdit'):
            return 0
        raw = (event.get('tool_input') or {}).get('file_path')
        if not raw:
            return 0
        file = pathlib.Path(raw).resolve()
        if file.suffix.lower() not in EXTS or any(part.lower() in SKIP for part in file.parts):
            return 0
        if not file.is_file() or file.stat().st_size > MAX_BYTES:
            return 0
        lines = file.read_text(encoding='utf-8', errors='replace').splitlines()
        if len(lines) <= FILE_REVIEW_LINES:
            return 0
        severity = 'high' if len(lines) > FILE_ALERT_LINES else 'review'
        msg = (f'Architecture {severity}: {file.name} has {len(lines)} lines. '
               'Check SRP and separation of domain, validation, IO and UI. '
               'Refactor only if there are genuinely independent responsibilities; '
               'do not split cohesive logic merely to reach a threshold.')
        print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': msg}}, ensure_ascii=False))
        return 0
    except (ValueError, OSError, TypeError) as exc:
        print(f'[architecture hook] skipped: {exc}', file=sys.stderr)
        return 0  # never break coding on a missing/unreadable file

if __name__ == '__main__':
    sys.exit(main())
