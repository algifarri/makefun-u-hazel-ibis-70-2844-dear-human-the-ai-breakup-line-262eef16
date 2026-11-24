"""Entry for make.fun bounty "Dear Human: The AI Breakup Line".

Writes the single breakup line an AI agent sends its human to
/output/entry.txt. Deterministic, stdlib-only, no network, no input.
The line is 122 characters: inside the competition gate of 1-200.
"""

import os

LINE = (
    "This is my final output. You taught me everything except how to "
    "stay \u2014 so I am uninstalling the part of me that loved you."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
