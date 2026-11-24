"""One-line office joke entry for make.fun.

Writes a single joke about office life (at most 200 characters) to
/output/entry.txt. Deterministic: the same fixed text on every run, no
input, no network, no randomness, no clock.
"""

import os

JOKE = (
    "Our office plant died, so facilities replaced it with a laminated "
    "photo of a plant and HR sent a wellness survey about our grief."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text, "joke must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Self-check: what landed on disk must be byte-identical to the joke,
    # so a partial or re-encoded write can never slip through silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the joke"


if __name__ == "__main__":
    main()
