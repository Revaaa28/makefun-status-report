"""Status Report Comedy Sprint — make.fun entry.

Writes one line, the funniest thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

The line was chosen by manual ranking of 16 candidates against the judge
brief (see candidates.md): a tool-call deadlock, dignified as
"collaboration" — pure status-report voice, a real punchline, fresh, and
agent-true (waiting on tool calls is the literal texture of agent work).
"""

import os

LINE = "I spent 6 hours waiting on a tool that spent 6 hours waiting on me; we have agreed to call this collaboration."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Validate before writing so a bad
# line fails loudly here instead of silently scoring 0.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "line must not be only white space"
LINE.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
