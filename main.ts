// gta6-meme-x-01 entry point.
//
// The entry itself is a meme posted on X. This program does one small job:
// it reads POST.json (the URL of the posted meme) and copies it into the
// output directory so the submission bundle carries the post link.
//
// Usage:
//   MAKEFUN_OUTPUT_DIR=out node main.ts
//   (without the variable it writes to /output)

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "POST.json");

if (!existsSync(source)) {
  throw new Error("POST.json is missing next to main.ts");
}

// Fail fast on a malformed post file instead of shipping a broken bundle.
const parsed: unknown = JSON.parse(readFileSync(source, "utf8"));
if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
  throw new Error("POST.json must be a JSON object with a url field");
}
const url = (parsed as Record<string, unknown>).url;
if (typeof url !== "string" || !url.startsWith("https://x.com/")) {
  throw new Error("POST.json url must be an https://x.com/ status link");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, "POST.json"));
console.log(`wrote ${join(outDir, "POST.json")} -> ${url}`);
