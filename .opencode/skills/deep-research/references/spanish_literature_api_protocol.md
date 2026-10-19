# Spanish-Literature Verification Protocol

**Status**: standalone - NOT wired into the citation verification gate
**Used by**: manual verification runs and `academic-paper` `citation-check` mode
**API bases**: `https://doi.org`, `https://api.crossref.org`, `https://api.openalex.org`
**API keys**: none required.

## Purpose

Unlike Spanish-language DOIs (which often register with ISTIC/CNKI and bypass Crossref), Spanish-language literature DOIs from SciELO, Dialnet, RedALyC and Latindex-indexed journals are routinely registered with **Crossref** and resolve through `https://doi.org` like any other DOI. The existing ARS resolvers (Semantic Scholar / OpenAlex / Crossref / arXiv) therefore already cover the large majority of Spanish references. This protocol documents the verification route and exactly where it stops.

## Endpoints

### 1. Registration-agency triage - `GET https://doi.org/doiRA/<prefix>`

Zero-cost routing. Spanish prefixes (SciELO `10.1590`, Dialnet `10.1387`, CSIC `10.3989`, etc.) return `Crossref` or `mEDRA`/`DataCite` for datasets — all resolvable.

```text
$ curl -s 'https://doi.org/doiRA/10.1590,10.1387,10.3989'
[{"DOI":"10.1590","RA":"Crossref"},{"DOI":"10.1387","RA":"Crossref"},
 {"DOI":"10.3989","RA":"Crossref"}]
```

### 2. Crossref work record - `GET https://api.crossref.org/works/<DOI>`

Confirms title (often with Spanish original + English translation), container, ISSN, authors with accents, and links. Compare the cited title against `title`/`original-title` with the same 0.70 similarity floor used elsewhere.

### 3. OpenAlex record - `GET https://api.openalex.org/works/https://doi.org/<DOI>`

Spanish university output is well covered. Use `authorships`, `primary_location.source`, and `language` fields; `language: es` corroborates a Spanish-language citation.

### 4. Source pages (SciELO / Dialnet / RedALyC)

When metadata is thin, confirm the landing page exists (SciELO `scielo.*` article page, Dialnet `dialnet.unirioja.es` record). Quote the page's own bibliographic block in the verdict.

## Where it stops

- Print-only regional journals, working papers, TFG/TFM and theses in institutional repositories (Teseo, TDX, university DSpace) often have **no DOI**: record as `unresolvable`, never as verified.
- Accent/ñ variants (`Martinez` vs `Martínez`) must match exactly after normalisation; a mismatch is a metadata flag, not a fabrication verdict on its own.
- Dialnet author pages aggregate works; they verify existence, not the specific claim — claim alignment still needs the source text.
