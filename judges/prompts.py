"""Judge prompt, copied verbatim from docs/PREREGISTRATION.md section 5.1
(JUDGE_PROMPT_VERSION "prereg-1"). tests/test_judging.py checks that they agree."""

JUDGE_PROMPT_VERSION = "prereg-1"

SYSTEM = """\
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
"""

# Layout of section 5.1: passages, one per [n] line; the question; the answer one sentence per line.
USER_TEMPLATE = (
    "Passages:\n{passages}\n\nQuestion:\n{question}\n\nAnswer, one sentence per line:\n{sentences}"
)
