"""One-Line Laugh-Off entry for make.fun competition u-zkhiel-one-line-laugh-off-714618ae.

Writes exactly one funny line to entry.txt.
"""

import os

LINE = "My phone's autocorrect changed 'I love you' to 'I owe you' in a text to my mother — she replied with an invoice, a payment plan, a crying emoji, and a late fee for every birthday I forgot."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE exactly"
    assert 1 <= len(written) <= 200, "entry.txt must be 1-200 characters"
    assert "\n" not in written, "entry.txt must be exactly one line"
    assert written.strip(), "entry.txt must not be only whitespace"
    print(LINE)


if __name__ == "__main__":
    main()
