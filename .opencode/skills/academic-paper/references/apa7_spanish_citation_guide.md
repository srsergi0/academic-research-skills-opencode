# APA 7.0 Complete Guide for Spanish Citations

Spanish APA 7.0 citation format guide based on the 7th edition (Manual de Publicaciones de la APA). This guide is the Spanish-language companion to `apa7_extended_guide.md`, used by `citation_compliance_agent`, `draft_writer_agent`, and `formatter_agent`.

> Scope note: APA has a single 7th edition; there is no separate "Spanish APA". The rules below are the standard APA 7th rules plus the points where Spanish orthography and naming change the surface form (accents, enye, compound surnames, narrative "y").

## Spanish Journal Articles

### Basic Format

```
Author1, & Author2 (Year). Article title in sentence case. Journal Name, Volume(Issue), Pages. https://doi.org/xxxxx
```

### Examples

**Single author**:
```
García Márquez, G. (2024). El impacto de la natalidad en las estrategias de las universidades privadas. Revista de Educación Superior, 15(2), 45-68. https://doi.org/10.1234/res.2024.0502.03
```

**Two authors** (parenthetical uses `&`, narrative uses `y`):
```
(Martínez, R., & López Fernández, A., 2023)
Martínez y López Fernández (2023) sostienen que...
```

**Three or more authors** (abbreviate from the first in-text citation):
```
Pérez et al. (2022) / (Pérez et al., 2022)
```

### Spanish-specific rules

1. **Compound surnames**: keep both parts and particles (`García Márquez, G.`, `De la Torre, M.`, `López Fernández, A.`). Never reduce to the second surname alone.
2. **Accents and ñ**: always kept (`Martínez`, `Muñoz`, `Hernández`). Accentless forms are spelling errors.
3. **Narrative vs parenthetical**: narrative uses `y` (Martínez y López, 2023); parenthetical uses `&` (Martínez & López, 2023).
4. **Alphabetical order**: letter by letter; `ñ` orders after `n` (RAE alphabet).
5. **Title case**: article and chapter titles in sentence case; journal and book titles in title case + italics.
6. **Translated works**: `Original Author (Trad. Apellido, N., Año). *Título*. Editorial. (Obra original publicada en AAAA)`.

## Spanish Books

```
Apellido, N. (Año). *Título del libro en cursiva*. Editorial.
```

## Spanish Book Chapters

```
Apellido, N. (Año). Título del capítulo. En N. Apellido (Ed.), *Título del libro* (pp. xx-xx). Editorial.
```

## Web Sources in Spanish

```
Organismo. (Año, día de mes). *Título de la página*. https://ejemplo.es/ruta
```

### Mixed Spanish-English Reference Handling

- Single alphabetical reference list (no separate script sections).
- Spanish uses standard parentheses: (Autor, Año).
- Same author with Spanish and English works: one list, ordered alphabetically then by year (add a/b for same-year works).

### Format Conversion Notes (Spanish Papers)

**Spanish APA → Chicago (author-date)**: keep author order and accents; Chicago notes-bibliography uses full first names where APA uses initials — expand only if the venue requires it.

**Spanish APA → IEEE**: numbered brackets in citation order; reference list keeps accents and ñ; `y`/`&` distinction disappears (`A. García Márquez and R. Martínez`).

**Spanish paper format conventions**:
- Decimal comma in Spanish prose (3,14), but keep the DOI/URL verbatim.
- Quotation marks: angular «» preferred (RAE); `"..."` accepted if the venue uses them — be consistent.
- Never strip accents to "simplify" LaTeX: use `babel spanich` + T1/`lmodern` (this port compiles with tachyon-tex-cli).
