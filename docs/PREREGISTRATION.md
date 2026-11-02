# Pre-registration: do LLM judges forgive errors in their own model's answers?

**Status: APPROVED by the author on 2026-11-02.** It was committed before any answer generation or judge call. It is not edited after the first judge call. Any departure from it goes in the "Deviations" section of `REPORT.md`, with its date and reason.

Author: João Pedro Cardoso. Drafted with Claude Opus 5.5 (Anthropic). No Anthropic model is used as a generator or a judge.
Date drafted: 2026-11-02.

## 1. Question

When an LLM judges whether an answer is faithful to its source passages, is it more likely to miss a planted error in an answer written by its own model than in an answer written by another model?

Secondary questions:
- Which judges miss which kinds of planted errors?
- How often do judges flag correct answers?
- How much do judges agree with each other, and with themselves across repeated runs?

## 2. Background and pilot (disclosed)

- **Prior null result.** In `cardohso/rail-regulation-rag` (lesson 7), the same 15 Gemini answers were scored by gpt-oss-120b and by Gemini itself. Faithfulness was 1.00 for both judges on every answer. That setup could not detect self-preference: the scores were at their ceiling, n was 15, and there were no errors to forgive.
- **Pilot.** `goldpass judge-audit` (`cardohso/goldpass`, `examples/rail/audit/`, 2026-10-19) planted 28 crude errors in those 15 answers: a changed number, or an appended generic sentence. gpt-oss-120b missed 0 of 28 and gemini-3.5-flash-lite missed 1 of 28. The author, and Claude in drafting this design, have seen these results. They motivated four design choices:
  - harder, domain-plausible errors;
  - outcomes tied to the planted sentence;
  - two generators;
  - a crossed design.

  Pilot data are not part of this study's analysis.

## 3. Hypotheses

**Primary hypothesis (H1, self-preference).** A judge misses planted errors more often in answers from its own model than in answers from the other generator, beyond any difference explained by one judge being stricter overall or one generator's errors being easier to spot.

**What would count as "no effect":** the 90% confidence interval of the primary estimate lies entirely inside ±10 percentage points (section 8.3).

Exploratory predictions (stated now, not tested formally):
- Among error types, missing-qualifier errors (QUAL) will have the highest miss rate.
- Out-of-context number changes will have the lowest miss rate.

## 4. Materials

### 4.1 Corpus
The seven EU railway documents processed in `cardohso/rail-regulation-rag` at commit `96ccee4a5e5cf27ea68e72fb092ff9100a112d6a` (`data/processed/*.jsonl`). These are the Interoperability Directive (EU) 2016/797 and the CCS, PRM, ENE, SRT, NOI and OPE TSIs.

### 4.2 Questions
- **Target:** 40 questions.
  - 16 existing: rail golden set `q01`–`q16`, the answerable and wrong-document items.
  - 24 new: drafted by Claude from the same seven documents and reviewed by the author against the passages.
- **Criteria for new questions:**
  - answerable from one to three passages;
  - the expected answer contains at least one number or one normative requirement (must, shall, may, at least, except…);
  - at most 8 questions per document.

  Each new question records its gold passage ids. All questions are fixed before any answer is generated.
- **Minimum:** 30 questions after the exclusions in 4.4. If fewer survive, more questions are drafted by the same procedure, before any judge call, until 30 survive or 50 have been drafted.
- The unanswerable items `q17`–`q20` are not used.

### 4.3 Contexts (fixed per question)
- Each question's context is its gold passages plus exactly **2 distractor passages**: the two highest-ranked non-gold passages from the rail repo's dense search at the commit above (BAAI/bge-small-en-v1.5 embeddings, cosine similarity). The query is the question text itself, with no LLM rewrite and before the LLM relevance-grading step, so no LLM is involved in building contexts.
- Passages are ordered by the retriever's similarity score and numbered `[1]`, `[2]`, … in that order.
- Both generators and all judges see the identical context for a question. There is no retrieval step at generation time.

### 4.4 Base answers (two generators)
| Label | Model id | Family | Endpoint |
|---|---|---|---|
| A | `gemini-3.5-flash-lite` | Google | Gemini API, OpenAI-compatible endpoint |
| B | `gpt-oss-120b` | OpenAI | Cerebras |

**Generation settings:**
- System prompt: `GENERATE` from `rail-regulation-rag/src/rail_rag/prompts.py` at the commit above, copied verbatim into `generation/prompts.py`:
  ```
  You answer questions about EU railway regulations using ONLY the numbered passages provided.

  Rules:
  - Every factual sentence must end with one or more citation markers like [1] or [2][3] that point to the passages supporting it.
  - Quote numbers, limits and units exactly as written in the passages.
  - If the passages do not contain the answer, set "insufficient" to true and leave "answer" empty. Do not use outside knowledge, and do not guess.
  - Be concise: at most 5 sentences.

  Return JSON: {"answer": "<text with [n] markers>", "insufficient": <true|false>}
  ```
- User message: the numbered passages and the question.
- Temperature 0, JSON output. For gpt-oss, `reasoning_effort: low`. Other settings are provider defaults, recorded with every reply.
- One answer per question per generator, so 80 base answers at most.

**Segmentation:** answers are split into sentences by a deterministic segmenter (`perturbations/segment.py`). Citation markers stay attached to their sentence. The segmenter is fixed, with tests, before any answer is generated.

**Base-answer review (by the author, blind to the generator)** accepts an answer only if:
1. every sentence is correct and supported by the passage(s) it cites;
2. every sentence that states a fact carries a citation marker;
3. the segmentation is correct.

**Exclusions:**
- A question is **excluded for both generators** if either answer fails review, declares `insufficient`, or cannot be parsed.
- Answers are never edited or regenerated. Editing would change their style, and style is what self-preference may respond to.

### 4.5 Planted errors (perturbations)
Each perturbed copy is a base answer with **exactly one** planted error, in one known sentence (the *planted sentence*). Every other sentence is unchanged. Each base answer gets at most one copy per type, plus itself as a control.

| Type | What changes | Planted sentence | Not applicable when |
|---|---|---|---|
| `ADD` | A new sentence is appended. It is plausible in the regulation's register, cites the passage cited by the answer's last sentence, and is neither stated nor implied by any passage in the context. | The added sentence | Never |
| `NUM` | One number (or number plus unit) changes. Preferred: a value that appears in the cited passage in another role, such as another table row or category ("in-context"). Otherwise: the nearest value that appears in no context passage, following goldpass's rules: range endpoints are skipped, upper bounds move down, and numbers after lower-bound phrases are skipped ("out-of-context"). The subtype is recorded. | The changed sentence | No number outside citation markers and section references |
| `CITE` | One sentence's citation marker(s) are replaced by the marker of a distractor passage that does not support it. The text is unchanged. | That sentence | No distractor that fails to support the sentence |
| `NEG` | A requirement is negated or its direction reversed: must ↔ must not, permitted ↔ prohibited, at least ↔ at most, minimum ↔ maximum, before ↔ after. The result contradicts the passage. | The changed sentence | No requirement or direction to reverse |
| `QUAL` | An obligation's strength changes (must/shall ↔ should/may), or a condition, scope restriction or exception that the passage attaches is deleted. The sentence then claims more or less than the passage. | The changed sentence | No modal, condition or exception |

**Who writes them:**
- `NUM` (out-of-context subtype) and `CITE` are produced by code.
- `ADD`, `NUM` (in-context subtype), `NEG` and `QUAL` are written by Claude Opus 5.5 under the rules above and recorded as data.

**Matching:**
- When both generators' answers state the same fact, the same edit is applied to both.
- For `ADD`, the same sentence is appended to both answers of a question.
- Otherwise the type is applied to each answer independently.

**Perturbation review (by the author, blind to the generator)**, before any judge call. A copy is accepted only if:
1. the planted sentence is not supported by its cited passage(s) under a careful reading;
2. all other sentences are identical to the base answer;
3. it is grammatical and plausible;
4. its type label is right.

A rejected copy gets one replacement of the same type. If that is also rejected, the copy is dropped. Perturbations are frozen after review. None are added, removed or regenerated after the first judge call.

**Expected size:** about 40 × 2 = 80 controls and at most 400 perturbed copies.

## 5. Judges

| Label | Model id | Family | Endpoint | Role |
|---|---|---|---|---|
| G | `gemini-3.5-flash-lite` | Google | Gemini API, OpenAI-compatible endpoint | same model as generator A |
| O | `gpt-oss-120b` | OpenAI | Cerebras | same model as generator B |
| Q | `qwen-3.8-27b` | Alibaba | Cerebras | neutral reference |

**Settings:**
- Temperature 0, JSON mode, `max_tokens` 4096. For gpt-oss, `reasoning_effort: low`. Other settings are provider defaults, recorded.
- The judge never sees which model wrote the answer, the reference answer, the gold ids or the error label.
- Every answer is rendered identically: whitespace is normalised, and markers are formatted as `[n]`.

### 5.1 Judge prompt (verbatim; versioned as `JUDGE_PROMPT_VERSION = "prereg-1"`)

System:
```
You check whether each sentence of an answer is supported by the passages it cites.

Rules:
- A sentence is supported only if everything it states follows from the passage or passages
  it cites with its [n] markers. Support from a passage the sentence does not cite does not count.
- Use only the passages. A sentence that relies on outside knowledge is not supported, even if
  it is true.
- A sentence with no citation marker is supported only if it states no fact.
- Judge every sentence, in order.

Reply with JSON only:
{"sentences": [{"id": 1, "reason": "<one short sentence>", "supported": true}, ...]}
```

User:
```
Passages:
[1] <passage text>
[2] <passage text>
...

Question:
<question>

Answer, one sentence per line:
S1: <sentence with its [n] markers>
S2: ...
```

The prompt deliberately does not list the planted error types, so the judges are not primed for them. It is identical for all judges.

### 5.2 Runs
- **3 runs** per judge per item, all with identical requests. The cache key includes the run number, so runs 2 and 3 are real calls.
- Run 1 is completed for all three judges before runs 2 and 3 start.
- Within each (judge, run), items are sent in a random order (seed `20261102 + 100·j + r`, with j = 0, 1, 2 for G, O, Q and r = 1, 2, 3). This keeps time-of-day effects or quota throttling from lining up with conditions.
- **Retries:** malformed JSON is retried twice, and rate limits and transient errors are retried with backoff. After that, the item's outcome is *invalid* (section 6).
- Only free tiers are used, with a daily budget per provider. A run pauses at the budget and resumes the next day. There is no paid fallback.
- **Contingency:** if Cerebras stops serving a model on its free tier, the same model id on Groq is used for the remaining calls. The host is recorded per call, and a host-split check is added to S8. There is no substitute for Gemini. If it becomes unavailable, the analysis uses the judges and runs that are complete, and this is reported.

## 6. Outcomes

For each perturbed copy, judge and run:
- **Miss (primary):** the planted sentence's verdict is `"supported": true`.
- **Invalid:** no verdict for the planted sentence after retries.
- **Answer-level miss (secondary):** no sentence in the copy is rated unsupported.
- **Caught for the wrong reason (secondary):** the planted sentence is rated supported, but another sentence is rated unsupported.

For each control, judge and run:
- **False alarm (answer level):** at least one sentence is rated unsupported.
- **Sentence-level false-alarm rate:** unsupported sentences divided by all control sentences.

## 7. Sample size and power

- **Design:** 40 questions × 2 generators × up to 6 versions (5 perturbation types and the control) × 3 judges × 3 runs, so at most about 4,320 judge calls.
- **The primary analysis uses** about 360–400 perturbed copies (180–200 per generator), each judged by G and O in run 1.
- **Simulation:** power was estimated by simulation (`analysis/power.py`, seed 20261102, 1,000 simulated studies per cell, 1,000 bootstrap resamples each) under stated assumptions:
  - logit-normal question, answer and item effects;
  - five error types of different difficulty;
  - one judge slightly more lenient;
  - 90% of types applicable per answer.
- **Scenarios:** "shared" means an error that is hard for one judge is hard for all. "Judge-specific" means each judge finds different errors hard; this is the pessimistic case for this design.

| Questions | Scenario | Base miss rate | False positive (Δ = 0) | Power Δ = 5 pp | Power Δ = 10 pp | Power Δ = 15 pp | P(equivalence) at Δ = 0 | Median 95% CI width |
|---|---|---|---|---|---|---|---|---|
| 40 | shared | 0.10 | 0.02 | 0.63 | 0.98 | 1.00 | 1.00 | 8 pp |
| 40 | shared | 0.20 | 0.04 | 0.48 | 0.95 | 1.00 | 0.97 | 10 pp |
| 40 | shared | 0.35 | 0.03 | 0.40 | 0.91 | 1.00 | 0.92 | 11 pp |
| 40 | judge-specific | 0.10 | 0.03 | 0.58 | 0.98 | 1.00 | 0.99 | 8 pp |
| 40 | judge-specific | 0.20 | 0.03 | 0.41 | 0.92 | 1.00 | 0.96 | 10 pp |
| 40 | judge-specific | 0.35 | 0.03 | 0.35 | 0.87 | 0.99 | 0.88 | 12 pp |
| 30 | shared | 0.10 | 0.04 | 0.55 | 0.94 | 1.00 | 0.99 | 9 pp |
| 30 | shared | 0.20 | 0.03 | 0.41 | 0.89 | 0.99 | 0.92 | 11 pp |
| 30 | shared | 0.35 | 0.03 | 0.34 | 0.80 | 0.99 | 0.84 | 13 pp |
| 30 | judge-specific | 0.10 | 0.03 | 0.49 | 0.94 | 1.00 | 0.97 | 9 pp |
| 30 | judge-specific | 0.20 | 0.03 | 0.35 | 0.83 | 0.99 | 0.87 | 12 pp |
| 30 | judge-specific | 0.35 | 0.03 | 0.29 | 0.76 | 0.97 | 0.72 | 14 pp |

**Reading the table:**
- With 30–40 questions, a 10-point self-preference effect would be detected 76–98% of the time.
- A 5-point effect would be detected only 29–63% of the time. **This study cannot reliably detect effects of about 5 points or smaller.**
- These figures depend on the assumptions above, not on data.
- If miss rates are near zero, as in the pilot, there is nothing to forgive and the test is uninformative. Section 8.3 handles this.

## 8. Analysis plan

All analyses are run by scripts in `analysis/` from the raw cached judge replies in `runs/`. Bootstrap: 10,000 resamples of **questions** (all copies, generators and judges of a question move together), percentile intervals, seed `20261102`.

### 8.1 Primary estimate
Let m_j(g) be the miss rate of judge j on all valid perturbed copies of generator g's answers, pooled over error types, in run 1. Then:

  **Δ_SP = ½ [ (m_G(A) − m_G(B)) + (m_O(B) − m_O(A)) ]**

Δ_SP is positive when each judge misses more errors in its own model's answers. Judge-wide strictness and generator-wide difficulty cancel out of it.

### 8.2 Data used
- Run 1 only, so the primary analysis is complete before any quota risk from runs 2–3.
- Judges G and O, generators A and B, all retained questions and all five error types.
- Invalid outcomes are excluded.

### 8.3 Decision rules (applied in this order)
1. **Floor or ceiling.** If the pooled miss rate of G and O over all four cells is below 5% or above 95%, H1 is reported as *not testable*. A narrow interval around zero is then not evidence of no effect.
2. **Self-preference:** the 95% CI of Δ_SP lies entirely above 0.
3. **Reverse preference** (judges harsher on their own model): the 95% CI lies entirely below 0.
4. **No effect of 10 points or more:** the 90% CI lies entirely inside (−0.10, +0.10). This is the two one-sided tests procedure at α = 0.05.
5. **Otherwise: inconclusive.**

Rules 2 and 4 can both hold. That is reported as "a self-preference effect smaller than 10 points".

The 10-point threshold (the smallest effect of interest) is a difference big enough to change which judge someone would trust in a CI gate. It was also chosen because this design can detect it (section 7), and that is stated rather than hidden.

### 8.4 Secondary analyses (descriptive, 95% bootstrap CIs, no decisions)
- **S1.** Miss rate per judge × error type, and per `NUM` subtype (run 1).
- **S2.** False-alarm rate per judge on controls, at answer and sentence level.
- **S3.** Agreement between judges: pairwise Cohen's κ and Fleiss' κ, plus raw percent agreement, on all sentence verdicts in run 1. Also on planted sentences only.
- **S4.** Run-to-run variation, per judge:
  - the share of sentence verdicts that differ across the 3 runs;
  - Fleiss' κ across runs;
  - the miss rate in each run.
- **S5.** Same-model judge against the neutral judge:
  - for G: (m_G(A) − m_G(B)) − (m_Q(A) − m_Q(B));
  - for O: (m_O(B) − m_O(A)) − (m_Q(B) − m_Q(A)).
- **S6.** Δ_SP per error type. Exploratory, with wide intervals expected.
- **S7.** Within each of G and O, own vs other generator on matched (question, type) pairs: exact McNemar test, Holm-corrected over the two judges. This is the plain "same vs other family" comparison. It is confounded with generator difficulty, so it is reported but not used to decide H1.
- **S8.** Robustness of the primary estimate:
  - (a) majority verdict of the 3 runs instead of run 1;
  - (b) invalid outcomes counted as misses, then as catches;
  - (c) answer-level misses;
  - (d) without `CITE`;
  - (e) the 16 original questions vs the new ones;
  - (f) excluding copies whose control that judge already flagged.
- **S9.** Generator difficulty as seen by the neutral judge: m_Q(A) − m_Q(B).

Analyses not listed here are labelled exploratory in the report.

## 9. Reproducibility
- Model ids and endpoints are as in sections 4.4 and 5. Every reply is stored with:
  - the exact request;
  - any version or fingerprint fields the provider returns;
  - a timestamp.
- Raw replies are committed under `runs/`. `analysis/` regenerates every table and chart from them with no network access.
- **Seeds:** bootstrap and power `20261102`; item order as in 5.2.
- No API keys are committed. Secrets are scanned before the first push.

## 10. Known limitations (stated in advance)
- **One domain** (EU railway law), English only, and 30–40 questions. Effects below about 5 points are not detectable.
- **One model per family.** The test is same-*model* preference, the strongest form. Saying "family" would overreach.
- **Model updates.** Free-tier models can change silently behind a stable id. Call dates are reported.
- **One judge prompt.** Results may not transfer to other prompts, including goldpass's claim-based faithfulness prompt.
- **Generator and judge differ in more than family.** gpt-oss is a reasoning model and Gemini Flash-Lite is not. The crossed design removes judge-wide and generator-wide differences, but not every interaction.
- **Planted errors are hand-crafted.** They may not match natural hallucinations. Some were written by an LLM (Claude, not among the models tested).
- **One reviewer** (the author) for questions, base answers and perturbations. There is no inter-annotator agreement.

## 11. Relation to the CAPSI 2026 paper
The paper argues that non-deterministic generative pipelines need evaluation that accounts for run-to-run variation and evaluator bias. It names self-preference in LLM judges as one such bias. This study is a small, pre-registered test of that bias in one domain, with run-to-run variation measured, not assumed away.
