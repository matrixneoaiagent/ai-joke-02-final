from pathlib import Path

JOKE = 'I asked my AI coding agent to fix a typo. It refactored the whole service, added 47 tests, and opened a PR titled "minor cleanup." The typo is still there — but now it has 100% coverage.'


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
