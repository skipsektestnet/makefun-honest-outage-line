"""The Most Honest Outage Line: writes the entry text to /output/entry.txt.

Why this line: Status-page voice, first person, specific; the dashboard being down too, and nobody knowing, is the honest turn.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Everything is down, including the dashboard that would tell you what is down. I do not know when it comes back. Nobody here does either.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
