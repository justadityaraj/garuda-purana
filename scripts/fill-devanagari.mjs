#!/usr/bin/env node
/**
 * Fill `sanskrit` (Devanagari) from `iast` wherever it is missing.
 *
 * GRETIL publishes IAST; the reading page shows Devanagari. Rather than
 * hand-transliterating thousands of verses, convert mechanically with the
 * standard indic-transliteration mapping and store the result in the data.
 *
 *   node scripts/fill-devanagari.mjs --check   # verify against known verses
 *   node scripts/fill-devanagari.mjs           # write missing fields
 */
import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import Sanscript from "@indic-transliteration/sanscript";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const DATA = join(ROOT, "data");

const toDeva = (iast) =>
  iast
    .split(" / ")
    .map((line) => Sanscript.t(line.trim(), "iast", "devanagari"))
    .join(" ।\n") + " ॥";

const files = readdirSync(DATA, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .flatMap((d) =>
    readdirSync(join(DATA, d.name))
      .filter((f) => f.endsWith(".json"))
      .map((f) => join(DATA, d.name, f)),
  );

if (process.argv.includes("--check")) {
  // Verses that already carry hand-verified Devanagari are the test set: if
  // the converter disagrees with them, the mapping is wrong and nothing
  // should be written.
  let checked = 0,
    failed = 0;
  for (const f of files) {
    for (const v of JSON.parse(readFileSync(f, "utf8")).verses) {
      if (!v.sanskrit || !v.iast) continue;
      checked++;
      const norm = (s) => s.replace(/[\s।॥\n]/g, "");
      if (norm(toDeva(v.iast)) !== norm(v.sanskrit)) {
        failed++;
        console.log(`MISMATCH ${v.id}`);
        console.log(`  stored:    ${v.sanskrit.replace(/\n/g, " ")}`);
        console.log(`  generated: ${toDeva(v.iast).replace(/\n/g, " ")}`);
      }
    }
  }
  console.log(`\nchecked ${checked} verse(s) with known Devanagari, ${failed} mismatch(es)`);
  process.exit(failed ? 1 : 0);
}

let filled = 0;
for (const f of files) {
  const doc = JSON.parse(readFileSync(f, "utf8"));
  let touched = false;
  for (const v of doc.verses) {
    if (!v.sanskrit && v.iast) {
      v.sanskrit = toDeva(v.iast);
      filled++;
      touched = true;
    }
  }
  if (touched) writeFileSync(f, JSON.stringify(doc, null, 2) + "\n", "utf8");
}
console.log(`filled ${filled} verse(s)`);
