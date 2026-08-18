# Garuda Purana

An open, machine-readable corpus of the Garuda Purana — with a Hinglish retelling
so people can actually read it.

## The myth, first

There is a widespread belief that the Garuda Purana is only read after a death in
the family, or that reading it invites misfortune. **It is not true.**

The text is roughly 90% Achar Kanda — cosmology, ethics, ayurveda, and a famous
section on gemstones. The material about death and the afterlife sits in the
Preta Kanda, near the end. Most people have only ever encountered that portion,
often through the *Saroddhara* — a 16-chapter digest by Naunidhirama that gets
sold as though it were the whole Purana. That confusion is where the myth comes
from.

You can read this. Anyone can read this. That is the point of publishing it.

## Why this exists

The Garuda Purana is available, technically. It exists as scanned PDFs, in
Victorian-era English translations, and in formal Hindi. All three are hard to
read, which means "available" and "readable" are not the same thing.

So this repo carries four layers per verse:

| Layer | What it is |
|---|---|
| Sanskrit | The verse, Devanagari |
| IAST | Roman transliteration |
| Hindi | Gita Press translation |
| **Hinglish** | A plain-language retelling |

The Hinglish layer is the reason this repo exists. Nobody has done a Hinglish
rendering of a scripture at this scale, and it is the version most people under
forty will actually finish.

**It is a retelling, not a translation.** It is always shown beside the Hindi it
was written from, never in place of it.

## Status

Early. Being written one reading session at a time — the corpus grows as the
text gets read, rather than being dumped in one go. Every verse carries a
`status` field so you can tell finished work from drafts.

## Data

One JSON file per chapter under `data/<kanda>/<chapter>.json`. The files
themselves are the API — fetch them raw from GitHub. There is no service to call,
nothing to sign up for, and no rate limit.

```json
{
  "id": "achar.1.1",
  "kanda": "achar",
  "chapter": 1,
  "verse": 1,
  "iast": "oṃ nārāyaṇaṃ namaskṛtya naraṃ caiva narottamam …",
  "hinglish": "…",
  "status": "draft"
}
```

`sanskrit`, `hi`, `en` and `hinglish` are all optional — a verse is valid with
any subset. See `schema/verse.schema.json`.

## Contributing

Corrections to the Hinglish are welcome, especially where a retelling has drifted
from the Hindi. Translations into other Indian languages are welcome too.

Please do not submit AI-generated retellings. The point of the Hinglish layer is
that a person read the verse and understood it.

## Licence and sources

Code is MIT. Original content is CC BY-SA 4.0. Third-party sources and the
permissions they rest on are documented in [NOTICE.md](NOTICE.md) — read that
before redistributing anything here.

<!-- by [Aditya Raj Singh](https://adityarajsingh.com/) -->
