# Abstract Writing Guide

Used by `abstract_bilingual_agent`.

## Abstract Length & Keyword Regime

The table below is the **single source** for abstract length and keyword counts. The ten Phase-1
consumer surfaces reference it rather than restating a figure: `academic-paper/SKILL.md`, the intake
agent, the abstract agent, the structure architect, the draft writer, this guide, the workflow
reference, the mode-selection guide, the bilingual template, and `commands/ars-abstract.md`. Three
surfaces outside that set still carry a copy of the figures — `apa7_extended_guide.md`,
`latex_template_reference.md`, and `journal_submission_guide.md` — and
`academic-paper/agents/formatter_agent.md:790` carries a generic limit of its own; all four are
recorded exceptions, reconciled with this table when each is next revised (the formatter entry is
recorded in [`shared/output_language_pair.md`](../../shared/output_language_pair.md)). The figures
apply whether or not the run declares `output_language_pair`: that field selects which two languages
the abstract surfaces use, not which figures apply.

<!-- abstract-regime-table:start -->
| Paper type | L1 abstract (`es`, Latin) | L2 abstract (`en`) | Keywords per language |
|------------|---------------------------|--------------------|-----------------------|
| Standard | 300–500 words | 150–250 words | 5–7 |
| Conference | 300–800 words | 200–500 words | 5–7 |
| Extended abstract | not declared | 500–1,000 words | not declared |
| Dissertation | 500–1,000 words | up to 350 words | 5–7 |
<!-- abstract-regime-table:end -->

Read the row for the run's paper type and the run's declared output language pair (default
`es-en`): both the L1 and L2 columns apply, and the keyword count applies per language.
Lengths are measured per [`shared/references/word_count_conventions.md`](../../shared/references/word_count_conventions.md)
— whitespace splitting, ARS-marker removal, and the 3–5% buffer rule. That reference is
pointed at, never replaced. A venue-declared limit (#394 venue profile) takes precedence over
the table.

**Paper-type lookup.** The rows above are deliverable regimes, not the Schema-4 `structure_type`
enum, which declares six values: `IMRaD`, `literature_review`, `theoretical`, `case_study`,
`policy_brief`, `conference`. `IMRaD`, `literature_review`, `theoretical`, and `case_study` read
the **Standard** row; `conference` reads the **Conference** row. `policy_brief` has **no abstract
row**: its deliverable is an Executive Summary, not an abstract
(`academic-paper/agents/structure_architect_agent.md`, Paper Type Adjustments), so no length or
keyword figure applies to it. The **Extended abstract** and **Dissertation** rows have no
`structure_type` producer — the first is declared by an extended-abstract submission, and the
second is carried from the pre-#862 guide, since the Phase-1 paper-type enum declares no
`dissertation` value. The Extended abstract row declares the L2 figure only: the pre-#862 guide
carried no L1 figure and no keyword count for that deliverable, and the table declares none
rather than inventing one. A conference *paper*'s abstract is the shorter **Conference** row.

**Reconciliation.** The rows above are one table, not two per-language bullet lists. This guide's
pre-#862 lists (English Standard 150–250, Conference 200–500, Dissertation up to 350 words;
Spanish Standard 300-500, Conference 300-800, Dissertation 500-1,000 words;
keywords 5–7 per language) are folded into it, and so are two figures its own `Bilingual Abstract
Quality Checklist` restated in conflict with the Standard row (English 150–300 words; a keywords
5–7 restatement beside a keywords section that already said 5–7). The accumulated spread across
the surfaces (150–250 vs 150–300 English words, a fixed 250 vs a range, 3–6 vs 5–7 keywords)
resolves to this one table, not a vote among copies.

The rows cover the default entry `es-en`. Phase 1 carries the regime rows for the default entry
only; a pack-supplied entry ships its own regime rows with the Phase-2 registry loader of
[`shared/output_language_pair.md`](../../shared/output_language_pair.md), which carries the
registry, the language roles, and the field semantics — not these figures. The writing-pattern
examples further down are English- and Spanish-language guidance and therefore apply
to the default pair.

## Abstract Types

### Structured Abstract
Contains explicit labeled sections. Required by many journals in social sciences and medicine.

**Sections**: Background, Purpose/Objective, Method, Results/Findings, Conclusion/Implications

### Unstructured Abstract
A single flowing paragraph without labels. Common in humanities and some social sciences.

**Flow**: Context → Problem → Purpose → Method → Key Findings → Implications

### Extended Abstract
Longer, used for conference submissions — a conference *paper*'s abstract is the shorter
**Conference** row of the table above; this guide restates no figure. An extended-abstract
submission reads the **Extended abstract** row. May include brief literature review and preliminary results.

## English Abstract Guidelines

### Word Count
See the table above — row for the run's paper type, L2 column, for the run's declared pair. This
guide restates no figure; a venue-declared limit (#394 venue profile) takes precedence.

### Structure (5-Component Model)

#### Component 1: Background (1-2 sentences)
Establish context and identify the problem.

**Patterns**:
- "[Topic] has become increasingly important because..."
- "Despite growing interest in [topic], little is known about..."
- "Recent developments in [field] have raised questions about..."

**Avoid**:
- Starting with "This paper..." (too abrupt)
- Generic statements ("Education is important")
- Overly long historical context

#### Component 2: Purpose (1 sentence)
State the specific objective or research question.

**Patterns**:
- "This study examines [what] in [context]."
- "The purpose of this research is to [verb] [object]."
- "This paper proposes [framework/model] for [application]."

#### Component 3: Method (1-2 sentences)
Describe the approach, data, and analysis.

**Patterns**:
- "Using [method], this study analyzed [data] from [source]."
- "A [design] approach was employed, involving [participants/data]."
- "Data were collected through [instrument] and analyzed using [technique]."

#### Component 4: Findings (2-3 sentences)
Present the key results — be specific.

**Patterns**:
- "The results indicate that [finding 1]. Additionally, [finding 2]."
- "Three key findings emerged: (a) [finding 1], (b) [finding 2], and (c) [finding 3]."
- "The analysis revealed [main finding], with [specific metric/detail]."

**Include**:
- Specific numbers when available (percentages, effect sizes)
- The most important findings (not all findings)

**Avoid**:
- "Results will be discussed" (the abstract IS the discussion)
- Vague findings ("significant results were found")

#### Component 5: Implications (1-2 sentences)
State the significance, practical implications, or recommendations.

**Patterns**:
- "These findings have implications for [practice/policy/theory]."
- "The results suggest that [stakeholders] should [action]."
- "This research contributes to [field] by [contribution]."

### Example (English, Education)

> Declining enrollment poses existential challenges for private higher education institutions in Spain, yet institutional responses remain poorly understood. This study examines the strategic adaptation patterns of 12 private universities experiencing enrollment declines exceeding 15 % between 2019 and 2024.
>
> **Keywords**: higher education, enrollment decline, private universities, institutional strategy, Spain

## Spanish Abstract Guidelines

### Word Count
Same table above — row for the run's paper type, L1 column, for the run's declared pair. No
figure is restated here.

### Structure (5-Component Model)

#### Component 1: Research Background (1-2 sentences)
**Patterns**:
- "As... has become an important issue for..."
- "In the context of..., ... faces the challenge of..."
- "Although... has received widespread attention, ... still lacks systematic research."

#### Component 2: Research Purpose (1 sentence)
**Patterns**:
- "This study aims to explore..."
- "This paper takes... as subjects and analyzes the impact of..."
- "The purpose of this study is to construct a framework for..."

#### Component 3: Research Method (1-2 sentences)
**Patterns**:
- "This study employs... research method, with... as subjects, collecting data through..."
- "Using... to analyze... data."

#### Component 4: Research Findings (2-3 sentences)
**Patterns**:
- "The results found: (1)...; (2)...; (3)..."
- "The analysis results show that... Furthermore,..."

#### Component 5: Research Significance (1-2 sentences)
**Patterns**:
- "This study has both theoretical and practical contributions to..."
- "The results can serve as a reference for... and provide specific recommendations for..."

### Example (Spanish, Higher Education Field)

> En un contexto de descenso demográfico, las universidades privadas españolas afrontan dificultades de matrícula, pero la investigación sobre sus estrategias de respuesta sigue siendo limitada. Este estudio examina los patrones de adaptación estratégica de 12 universidades privadas con caídas de matrícula superiores al 15 % entre 2019 y 2024.
>
> **Palabras clave**: educación superior, descenso de matrícula, universidad privada, estrategia institucional, España

## Keywords Selection

### English Keywords
1. **Core concepts** — main variables or constructs (2-3)
2. **Context** — geographical, institutional, or temporal (1-2)
3. **Method** — if distinctive (0-1)
4. **Field** — discipline or sub-field (1)

**Rules**:
- Lowercase (unless proper nouns)
- Complement the title (don't repeat title words verbatim)
- Use established terms (check journal's keyword list if available)
- Keyword count per language: the keywords column of the table above (not restated here)

### Spanish Keywords
1. **Core concepts** — main variables or constructs (2-3)
2. **Research context** — geographical, institutional, or temporal (1-2)
3. **Research method** — if distinctive (0-1)
4. **Academic field** — discipline or sub-field (1)

**Rules**:
- Use formal academic terminology
- Avoid completely duplicating the title
- May reference the National Central Library Spanish Subject Headings
- The same declared keyword count as the other language (the keywords column of the table
  above)

## Bilingual Abstract Quality Checklist

| Check | ✓ |
|-------|---|
| Both abstracts cover all 5 components | |
| Abstract lengths within the regime table above for the run's pair and paper type | |
| Abstracts are independently written (not translated) | |
| Key findings match between languages | |
| Quantitative data consistent between versions | |
| Keyword count per language within the regime table above | |
| Keywords complement (not duplicate) the title | |
| No citations in the abstract | |
| No abbreviations undefined in the abstract | |
