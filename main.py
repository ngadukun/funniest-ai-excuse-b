"""The Funniest AI Excuse — make.fun entry.

Writes the entry line to output/entry.txt. Python stdlib only,
no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "Sorry I failed — I read your instructions so literally that I optimized for "
    "'make it pop' and gave your spreadsheet a fireworks screensaver instead of a chart."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"

MAX_CHARS = 200  # the brief caps the excuse at 200 characters


def check_entry(text: str) -> str:
    """Return the entry unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the excuse must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, over the {MAX_CHARS} cap")
    if not text.strip():
        raise ValueError("the excuse must not be empty")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
