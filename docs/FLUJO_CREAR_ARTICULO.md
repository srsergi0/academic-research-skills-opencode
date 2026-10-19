# Cómo crear un artículo completo (flujo end-to-end)

Guía práctica para pasar de una idea a un PDF publicable con este port en OpenCode.
Idioma de trabajo: español + inglés (`es-en`). Backend PDF: `tachyon-tex-cli`.

## Requisitos

- Este repo copiado en tu proyecto: carpeta `.opencode/` + `MODE_REGISTRY.md`.
- OpenCode con un modelo capaz (recomendado: sesión con modelo frontera).
- Node.js 22+ (solo para compilar el PDF; el resto es prompt + Markdown).
- No necesitas instalar nada global: `npx --yes github:srsergi0/tachyon-tex-cli` descarga el binario verificado a tu caché de usuario.

## El flujo en 30 segundos

```
IDEA
  │  /ars-plan  o  /ars-full
  ▼
1. INVESTIGACIÓN (deep-research) ──► RQ + metodología + bibliografía + síntesis
  │  checkpoint: confirmas pregunta y plan  ✓ tú decides
  ▼
2. ESCRITURA (academic-paper) ──► esquema → borrador → resumen ES/EN
  │  checkpoint: apruebas el esquema antes de redactar  ✓ tú decides
  ▼
2.5 INTEGRIDAD (pipeline) ──► pasaporte + verificación de citas y claims
  │  checkpoint: revisas el informe (PASS / flags)  ✓ tú confirmas
  ▼
3. REVISIÓN (academic-paper-reviewer) ──► 5 informes + decisión editorial simulada
  │  checkpoint: aceptas / corrección menor / mayor / rechazo  ✓ tú decides
  ▼
4. CORRECCIÓN (academic-paper) ──► respuesta a revisores + borrador revisado
  │  checkpoint: confirmas los cambios  ✓ tú decides
  ▼
3'. RE-REVISIÓN ──► verificación de que se resolvió lo pedido (máx. 2 rondas)
  ▼
4.5 INTEGRIDAD FINAL ──► verificación profunda, tolerancia cero
  │  checkpoint: informe final  ✓ tú confirmas
  ▼
5. FINALIZACIÓN ──► MD / LaTeX / PDF vía tachyon-tex  (/ars-pdf)
  │  checkpoint: eliges formato  ✓ tú decides
  ▼
6. RESUMEN DEL PROCESO ──► memoria del proceso + autoevaluación de colaboración
  ▼
PAPER PUBLICABLE
```

## Paso a paso

### 0. Elige el punto de entrada

| Tu situación | Comando | Qué pasa |
|---|---|---|
| Tengo solo una idea | `/ars-full` | Pipeline completo desde cero (recomendado la primera vez) |
| Quiero planificar antes de escribir | `/ars-plan` | Diálogo socrático capítulo por capítulo, sin redactar aún |
| Ya tengo bibliografía o borrador | `/ars-full I already have a draft...` | El pipeline entra a mitad (integridad primero, Stage 2.5) |
| Solo necesito el estado de la arte | `/ars-lit-review "tu tema"` | Revisión bibliográfica anotada, sin pipeline |
| Ya tengo manuscrito y quiero cribarlo | `/ars-reviewer` | Panel de revisión simulada + hoja de ruta de cambios |
| Solo compilar un `.tex` a PDF | `/ars-pdf` | Compila con tachyon-tex (Tectonic por defecto) |
| Ver el PDF mientras edito | `/ars-preview` | Recarga el PDF en el navegador al guardar |

### 1. Investigación — fija la pregunta (lo más importante)

```
/ars-full
Tu: "Quiero escribir sobre el impacto de la IA en la evaluación universitaria en España"
```

El skill `deep-research` (13 agentes) produce, en orden:
1. **Pregunta de investigación (RQ)** + colección INSIGHT.
2. **Metodología**: diseño, estrategia de búsqueda (SciELO, Dialnet, Scopus, WoS...), protocolo de verificación de fuentes.
3. **Bibliografía anotada** con verificación (Semantic Scholar / OpenAlex / Crossref) — lo que no se verifica se marca, no se inventa.
4. **Síntesis** + riesgos/sesgos + revisión ética.

**Tu trabajo aquí:** responder al diálogo socrático y **confirmar la RQ y la metodología**. Todo lo demás cuelga de esto. Un mal RQ = mal paper. Si dudas entre dos enfoques, dilo; el Mentor está para eso, no para cerrarlo rápido.

### 2. Escritura — esquema primero, borrador después

Con el RQ confirmado, `academic-paper` (12 agentes):
1. **Ficha del paper** (Paper Configuration Record): tipo IMRaD/revisión/caso, formato de cita (APA 7ª por defecto), par de idiomas `es-en`.
2. **Esquema + mapa de argumentos** → lo revisas y apruebas.
3. **Borrador** por secciones, con huecos explícitos `[MATERIAL GAP]` donde falte material tuyo (datos, acceso a fuentes). El agente no rellena con invención.
4. **Resumen bilingüe** ES+EN de redacción independiente (no traducción literal) + palabras clave.
5. Si hay figuras: verificación de formato (tablas, APA) y hasta 2 rondas de corrección.

**Tu trabajo aquí:** aprobar el esquema, aportar lo que solo tú tienes (datos, acceso, criterio) y decidir qué huecos se quedan fuera del alcance.

### 2.5 Integridad — el filtro antes de revisar

El pipeline genera el **Material Passport** (`passport.yaml`): qué se afirma, con qué fuente, con qué localizador (`<!--anchor:...-->`) y qué experimento/procedencia declara cada claim.

Chequeo de 7 modos de fallo típicos de IA (citas alucinadas, resultados inventados, metodología fabricada, atajos, etc.). Resultado: PASS, o lista de sospechas a corregir (máx. 3 rondas de arreglo).

**Tu trabajo aquí:** leer el informe y confirmar, o pedir correcciones. Sin tu OK no se avanza.

### 3. Revisión — cinco revisores que no se callan

`academic-paper-reviewer` monta un panel: encaje en revista + 3 revisores de campo + abogado del diablo. Recibes informes por criterio con evidencia citada del manuscrito, decisión editorial simulada (Aceptar / Menor / Mayor / Rechazar) y hoja de ruta de revisión.

**Tu trabajo aquí:** decidir el veredicto que aceptas y la estrategia de respuesta. Puedes pedir modo guiado (`/ars-reviewer` en modo guided) para discutir punto por punto.

### 4. Corrección — responder, no solo cambiar

Con `/ars-revision-coach` conviertes los comentarios en plan de cambios; con `/ars-revision` se reescribe el borrador y se genera la **respuesta a revisores punto por punto** + informe de qué cambió y por qué.

**Tu trabajo aquí:** confirmar que cada cambio refleja tu criterio (el agente propone, tú dispones).

### 3'. Re-revisión — verificar, no reescribir

Se comprueba que cada objeción quedó resuelta, con matriz de trazabilidad (objeción → cambio → verificado SÍ/NO). Límite: **2 rondas de revisión en total**; después se avanza a cierre.

### 4.5 Integridad final — tolerancia cero

Re-verificación profunda (100 % de claims registrados). Si algo falla, se vuelve a 4'. Sin atajos: lo que no se puede verificar no se publica como verificado.

### 5. Finalización — del Markdown al PDF

```
/ars-pdf
```

1. El `formatter_agent` produce el `.tex` (plantillas APA/IEEE/Chicago, `babel spanish`, sin pila CJK).
2. `tachyon-tex` lo compila: `npx --yes github:srsergi0/tachyon-tex-cli main.tex --json` (motor Tectonic; si usas biblatex/Biber o LuaLaTeX, cambia solo a `--engine latexmk`).
3. Obtienes MD + `.tex` + PDF. DOCX vía Pandoc si lo necesitas.

**Tu trabajo aquí:** elegir formato y revisar el PDF final (nunca des por bueno un PDF sin abrirlo).

### 6. Cierre — memoria del proceso

Se genera el acta del proceso: decisiones tomadas, concesión del abogado del diablo, calidad de la colaboración (1–100) y matriz de trazabilidad final. Útil para responder a revisores reales y para auditoría.

## Reglas de oro

1. **Tú decides en cada ✓.** Si el agente intenta avanzar sin tu confirmación, páralo: ningún checkpoint es opcional.
2. **Nada de prisa en el Stage 1.** El 80 % de la calidad se juega en la pregunta y la metodología.
3. **Desconfía de lo cómodo:** si el abogado del diablo cede demasiado rápido ante tus réplicas, pídele que sostenga el ataque con evidencia (protocolo de concesión: solo cede con prueba).
4. **`[MATERIAL GAP]` es sagrado.** Donde ponga eso falta material tuyo; no lo borres ni lo dejes rellenar con generalidades.
5. **Verifica las citas clave tú mismo** (las 5–10 que sostienen tu contribución), aunque el pipeline diga PASS. El muestreo no sustituye tu criterio.
6. **Un claim, una fuente, un localizador.** Si no puedes señalar de dónde sale cada afirmación fuerte, el paper aún no está listo.
7. **El español manda en estilo:** tildes y ñ siempre, «y» en narrativa vs «&» entre paréntesis, apellidos compuestos completos (García Márquez, no Márquez).

## Si algo sale mal

| Síntoma | Qué hacer |
|---|---|
| El agente se pone a redactar sin esquema | Vuelve a `/ars-plan`; el esquema se aprueba antes de redactar |
| Integridad marca citas sospechosas | Pide la lista, verifica tú las 3–5 críticas, descarta o sustituye |
| La revisión simulada es demasiado amable | Pide al abogado del diablo un segundo asalto con la evidencia en contra |
| El PDF no compila | Lee el primer error del log (`--keep-logs`), corrige la fuente, recompila (máx. 3 intentos antes de pedir ayuda) |
| Te pierdes entre stages | Pregunta `status`: el orquestador resume en qué stage estás y qué falta |

## Qué NO hace este flujo

- No ejecuta experimentos ni recoge datos (los declaras tú en el pasaporte).
- No garantiza que un manuscrito inventado de forma consistente sea detectado.
- No sustituye la revisión por pares real ni la responsabilidad autoral: quien firma eres tú.
