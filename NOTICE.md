# NOTICE — third-party sources and rights

This repository combines material from several sources under different terms.
Read this before redistributing, forking, or reusing anything here.

## Sanskrit text

Sourced from [GRETIL](https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/3_purana/garup1_u.htm)
(Göttingen Register of Electronic Texts in Indian Languages), based on the Bombay
Venkatesvara Steam Press edition, input by members of the SANSKNET project.

The underlying text is ancient and in the public domain. GRETIL's contribution is
the digitisation and encoding; their files state "copyright and terms of usage as
for source file" and are provided for reference and academic use. Attribution to
GRETIL is retained on every verse carrying their text via the `source` field.

## Hindi translation

From *Sankshipt Garud Puran*, published by Gita Press, Gorakhpur.

**Used with the express permission of Gita Press**, granted to Aditya Raj Singh
for this project.

> _The written confirmation of this permission is to be reproduced here verbatim.
> Until it appears below, treat the Hindi layer as permissioned to this project
> specifically and **not** sub-licensed to downstream forks._

Gita Press has distributed its texts freely for a century and its stated purpose
is the widest possible circulation of these works. That generosity is the basis
on which the Hindi appears here, and it should not be strained — if you are
forking this repository for anything commercial, seek your own permission.

## English translation

Manmatha Nath Dutt, c. 1908. Public domain by age — published before 1923, and
the translator died in 1912, placing it well outside the 60-year post-mortem term
under Indian copyright law.

## Hinglish retelling

Original work by Aditya Raj Singh, licensed CC BY-SA 4.0.

It is a **retelling**, not a translation, and carries no scholarly authority. It
is written from the Hindi with the aim of being readable, and it is always
published alongside its source so a reader can check it.

## Artwork

Both images are public domain, sourced via Wikimedia Commons:

- *Vishnu Carried by Garuda Through a Stormy Sky*, Kotah, 1775. Metropolitan
  Museum of Art, Bequest of Mrs. Horace W. Frost.
  [Commons file](https://commons.wikimedia.org/wiki/File:8b_Vishnu_Carried_by_Garuda_Through_a_Stormy_Sky_1775_Kotah_Bequest_of_Mrs._Horace_W._Frost.jpg)
- *Garuda Vahan Vishnu*, Ravi Varma studio lithograph, c. 1910.
  [Commons file](https://commons.wikimedia.org/wiki/File:%22Garuda_Vahan_Vishnu,%22_from_the_Ravi_Varma_studio,_c.1910%27s_Source-_ebay,_Oct._2009.jpg)

Both predate 1923 and are out of copyright by age. They are reproductions of
two-dimensional public-domain artworks, which acquire no new copyright.

## Transliteration

Devanagari is generated from GRETIL's IAST with
[@indic-transliteration/sanscript](https://github.com/indic-transliteration/sanscript.js)
via `scripts/fill-devanagari.mjs`. The converter is checked against verses whose
Devanagari was verified by hand — run `node scripts/fill-devanagari.mjs --check`.
It is a mechanical mapping, not an editorial judgement; where a verse carries
hand-entered Devanagari, that is left untouched.

## Code

Everything under `site/`, `schema/`, and any scripts: MIT. See [LICENSE](LICENSE).

<!-- by [Aditya Raj Singh](https://adityarajsingh.com/) -->
