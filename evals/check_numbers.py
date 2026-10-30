#!/usr/bin/env python3
"""Check that the rule block and the version string agree across the repository.

Run it before you push. CI runs it on every push and pull request.

    python3 evals/check_numbers.py            # exit 1 on the first mismatch

Checks:
- The rule block: prompts/system-prompt.md and output-styles/simple-korean.md
  carry the same text, and SKILL.md carries the same reply rules.
- The version string in SKILL.md, the three manifests, and the README badge.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
problems = []


def rule_block(text):
    """The text between the first two --- lines, or the body after the frontmatter."""
    parts = re.split(r"^---[ \t]*$", text, flags=re.M)
    return parts[1].strip() if len(parts) >= 3 else text.strip()


def sync():
    prompt = rule_block((ROOT / "prompts" / "system-prompt.md").read_text(encoding="utf-8"))
    style = (ROOT / "output-styles" / "simple-korean.md").read_text(encoding="utf-8")
    style = re.sub(r"^---\n.*?\n---\n", "", style, count=1, flags=re.S).strip()
    if prompt != style:
        problems.append("rule block differs between prompts/system-prompt.md and output-styles/simple-korean.md")
    skill = (ROOT / "skills" / "simple-korean" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in ("Answer in prose", "No em-dashes", "No contractions", "first sentence gives the answer",
                   "Condition before command", "make sure that", "Never touch"):
        for name, text in (("SKILL.md", skill), ("prompts/system-prompt.md", prompt)):
            if phrase.lower() not in text.lower():
                problems.append(f"{name} lacks the rule phrase {phrase!r}")


def versions():
    v = {}
    v["SKILL.md"] = re.search(r'version: "([^"]+)"', (ROOT / "skills/simple-korean/SKILL.md").read_text()).group(1)
    for f in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json"):
        v[f] = re.search(r'"version":\s*"([^"]+)"', (ROOT / f).read_text()).group(1)
    v["README badge"] = re.search(r"badge/version-([0-9.]+)-", README).group(1)
    if len(set(v.values())) != 1:
        problems.append(f"version strings differ: {v}")


def main():
    sync()
    versions()
    if problems:
        print("MISMATCH")
        for p in problems:
            print(" -", p)
        return 1
    print("check_numbers OK: the rule block and the version string agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
