# Soporte de idioma: español (migración desde chino tradicional)

Este port usa **español + inglés** como par de idiomas (`es-en`). Aguas arriba (upstream
`Imbad0202/academic-research-skills` v3.23.1) el par era chino tradicional + inglés (`zh-tw-en`).

## Qué cambió
- Registro `output_language_pair`: token por defecto `es-en` (L1 español latino, L2 inglés).
- Claves Schema-4: `abstract: {english, spanish}`, `keywords: {en, es}`; encabezados `English Abstract` / `Spanish Abstract` (`Resumen`).
- Resúmenes bilingües ES+EN de composición independiente; tarjeta en plantilla bilingüe.
- Guía de citación: `apa7_spanish_citation_guide.md` (nuevo; sustituye a la guía china).
- Ejemplo de artículo: `spanish_paper_example.md` (nuevo; sustituye al ejemplo chino).
- Protocolo de literatura: `spanish_literature_api_protocol.md` (nuevo; DOIs en español vía Crossref/SciELO/Dialnet; sustituye al protocolo CNKI/ISTIC).
- Triggers: líneas `繁体中文` eliminadas de los 5 SKILL.md (el español ya existía; el coreano se conserva tal cual aporta upstream).
- Ejemplos de diálogo socrático, modos y tablas de decisión, en español.
- Nota fija de forma de revisión (`review_form_note.md` + copias en `deep-research` y `academic-paper`): texto fijo en español.
- LaTeX: sin pila CJK/XeLaTeX; `babel spanish` + T1/`lmodern`; compilación con tachyon-tex-cli (`docs/PDF_BACKEND_TACHYON.md`).
- Autoridades de ética: filas Taiwán (`tw.hsra`) sustituidas por filas España (`es.libi`: Ley 14/2007 art. 12 CEIm y art. 4 consentimiento).
- Frases de ejemplo EQUATOR, cribado sr-screener, plantillas de financiación y demos del pipeline, en español.
- Glosario HEI, roles CRediT y ejemplos de plan de registro, en español.

## Excepciones retenidas a propósito
- `venue_disclosure_policies.md`, `disclosure_mode_protocol.md`, `top_journals_by_field.md`: datos factuales (nombres de editoriales/revistas y textos normativos literales). No son soporte de idioma; inventar equivalentes españoles sería fabricar datos. Dos líneas con esos mismos nombres en `academic-paper/SKILL.md` y `mode_selection_guide.md` se conservan por igual motivo.
- `references/changelog.md` y demás historiales: historia, no comportamiento.
- Menciones de Taiwán como **tema** de investigación en ejemplos (se conserva el tema; se cambió la lengua vehicular). Los ejemplos didácticos del pipeline y la guía de abstract sí se adaptaron a contexto español por coherencia.
- Bloques de triggers en coreano: aporte de upstream, fuera del alcance pedido.

## Registro y cardinalidad
Rige `shared/output_language_pair.md`: un par por corrida (`es-en` por defecto), cardinalidad aparte (bilingüe / solo EN / solo español) en `intake_agent.md`.
