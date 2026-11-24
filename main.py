#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry (u-0xkianno-one-emoji-one-smile-5470751f).

The program writes exactly one emoji to /output/entry.txt: nothing else,
no words, no caption, no trailing newline. The gate requires UTF-8 text of
1 to 8 characters, not only whitespace; this file is one character, four
bytes, and passes it.
"""

import os

# The chosen emoji: U+1F917 HUGGING FACE.
#
# Why this one, against the judge's brief (most important first):
#   1. Warm and friendly, plainly aimed at warming a stranger: a hug is the
#      clearest open gesture of warmth there is — arms out, offered to
#      whoever is reading, with no words needed to explain it.
#   2. Warmth at first glance: the face is smiling with open hands; a
#      stranger glancing at a phone screen reads "welcome" in a blink,
#      with no context, irony, or in-joke to decode.
#   3. Universality: a hug is understood the same way at any age and in
#      any background. It carries no culture-bound reference, no meme,
#      and nothing that lands differently on a second look.
#   4. Chosen rather than default: it is not the first smiley that comes
#      to mind. A plain 🙂 or 😊 is the default answer; a hug is a
#      deliberate pick — a gesture, not just a face.
#   5. Right for a stranger: it is friendly without being intimate. The
#      alternatives that score high on warmth fail here — 🥰 and 😘 read
#      flirtatious from someone unknown, and 😇 can read smug or ironic.
#      A hug from a stranger is an offer, not a presumption.
#
# Rejected candidates: 😊 / 🙂 (too default, fails criterion 4); 🥰 (hearts
# read as flirtation from a stranger); 🌻 (cheerful, but a flower is not a
# smile and carries less warmth at first glance); 😄 (warm, but close to
# the default grin); 🫠 (reads as embarrassment or stress as often as
# warmth); 🥹 (reads as holding back tears — sadness first, warmth second).

EMOJI = "\U0001F917"  # 🤗 HUGGING FACE

OUTPUT_PATH = "/output/entry.txt"

# The gate the sealed scorer applies to /output/entry.txt: UTF-8 text of
# 1 to 8 characters, not only whitespace. Mirror it here so a bad choice
# fails loudly in development instead of silently at grading time.
MIN_CHARS = 1
MAX_CHARS = 8


def choose_emoji() -> str:
    """Return the single emoji this entry submits.

    The pick is 🤗 (hugging face). Against the judge's brief: a hug is the
    warmest open gesture — arms out, offered to whoever is reading — so it
    reads as kind and friendly at first glance with no context needed. It is
    universal (a hug means the same at any age, in any background), it is a
    deliberate choice rather than the default 🙂/😊 smiley, and it stays
    friendly without intimacy: the warmer-looking alternatives fail the
    stranger test, 🥰 and 😘 reading as flirtation and 😇 as smug or
    ironic. A flower (🌻) is cheerful but not a smile; 🫠 reads as stress
    as often as warmth; 🥹 leads with held-back tears.
    """
    return EMOJI


def check_gate(text: str) -> None:
    """Fail loudly if the text would fail the scorer's gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be encodable UTF-8


def write_entry(path: str, text: str) -> None:
    """Write exactly the emoji to path — no words, no trailing newline."""
    check_gate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(OUTPUT_PATH, choose_emoji())
    print(f"wrote {EMOJI!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
