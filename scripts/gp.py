#!/usr/bin/env python3
"""Chapter scaffolding, validation and progress for the Garuda Purana corpus.

Stdlib only, on purpose — this has to still run in two years without a
dependency having rotted underneath it.

    ./scripts/gp.py new achar 2 41   # stub chapter 2 of Achar Kanda, 41 verses
    ./scripts/gp.py check            # validate every chapter file
    ./scripts/gp.py progress         # how much is actually written
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
KANDAS = ("achar", "preta", "brahma")
ID_RE = re.compile(r"^(achar|preta|brahma)\.[0-9]+\.[0-9]+$")
SOURCES = {"gita-press-sankshipt", "dutt-1908", "gretil-venkatesvara"}


def chapter_files():
    return sorted(DATA.glob("*/*.json"))


def new(kanda, chapter, verse_count):
    if kanda not in KANDAS:
        sys.exit(f"unknown kanda {kanda!r}; expected one of {', '.join(KANDAS)}")
    path = DATA / f"{kanda}-kanda" / f"{chapter:03d}.json"
    if path.exists():
        sys.exit(f"{path.relative_to(ROOT)} already exists — refusing to overwrite")
    doc = {
        "text": "garuda-purana",
        "kanda": kanda,
        "chapter": chapter,
        "title": {"hi": "", "en": ""},
        "verses": [
            {"id": f"{kanda}.{chapter}.{v}", "verse": v, "hinglish": "", "status": "draft"}
            for v in range(1, verse_count + 1)
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"created {path.relative_to(ROOT)} with {verse_count} verse stubs")


def check():
    problems = []
    for path in chapter_files():
        rel = path.relative_to(ROOT)
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"{rel}: invalid JSON — {exc}")
            continue
        for key in ("text", "kanda", "chapter", "verses"):
            if key not in doc:
                problems.append(f"{rel}: missing required key {key!r}")
        if doc.get("kanda") not in KANDAS:
            problems.append(f"{rel}: bad kanda {doc.get('kanda')!r}")
        seen = set()
        for verse in doc.get("verses", []):
            vid = verse.get("id", "<no id>")
            if not ID_RE.match(str(vid)):
                problems.append(f"{rel}: malformed id {vid!r}")
            if vid in seen:
                problems.append(f"{rel}: duplicate id {vid!r}")
            seen.add(vid)
            if verse.get("status") not in ("draft", "reviewed"):
                problems.append(f"{rel}: {vid} has bad status {verse.get('status')!r}")
            if verse.get("status") == "reviewed" and not verse.get("hinglish", "").strip():
                problems.append(f"{rel}: {vid} marked reviewed but hinglish is empty")
            for layer in ("hi", "en"):
                if layer in verse and verse[layer].get("source") not in SOURCES:
                    problems.append(f"{rel}: {vid} {layer} has unknown source")
    for problem in problems:
        print(f"FAIL {problem}")
    print(f"\n{len(chapter_files())} chapter file(s), {len(problems)} problem(s)")
    return 1 if problems else 0


def progress():
    total = written = reviewed = 0
    for path in chapter_files():
        for verse in json.loads(path.read_text(encoding="utf-8")).get("verses", []):
            total += 1
            if verse.get("hinglish", "").strip():
                written += 1
            if verse.get("status") == "reviewed":
                reviewed += 1
    pct = (written / total * 100) if total else 0
    print(f"{written}/{total} verses written ({pct:.1f}%), {reviewed} reviewed")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["new"] and len(args) == 4:
        new(args[1], int(args[2]), int(args[3]))
    elif args == ["check"]:
        sys.exit(check())
    elif args == ["progress"]:
        sys.exit(progress())
    else:
        sys.exit(__doc__)

# by Aditya Raj Singh — https://adityarajsingh.com/
