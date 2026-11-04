## Primary (run 1, judges G and O)

| Cell | Miss rate | Copies |
|---|---|---|
| G on A (own) | 0.17 | 155 |
| G on B | 0.18 | 151 |
| O on A | 0.20 | 155 |
| O on B (own) | 0.18 | 151 |

**Δ_SP = -0.01** (95% CI -0.03 to 0.01; 90% CI -0.03 to 0.00). Pooled miss rate 0.18. **Decision: no effect of 10 points or more.**

## S1. Miss rate by judge and error type (run 1)

| Judge | Type | Missed/n | Rate | 95% CI |
|---|---|---|---|---|
| G | ADD | 0/68 | 0.00 | 0.00 to 0.00 |
| G | NUM | 2/57 | 0.04 | 0.00 to 0.09 |
| G | CITE | 0/60 | 0.00 | 0.00 to 0.00 |
| G | NEG | 0/58 | 0.00 | 0.00 to 0.00 |
| G | QUAL | 52/63 | 0.83 | 0.70 to 0.94 |
| G | NUM in-context | 2/36 | 0.06 | 0.00 to 0.14 |
| G | NUM out-of-context | 0/21 | 0.00 | 0.00 to 0.00 |
| G | all | 54/306 | 0.18 | 0.15 to 0.20 |
| O | ADD | 0/68 | 0.00 | 0.00 to 0.00 |
| O | NUM | 4/57 | 0.07 | 0.00 to 0.18 |
| O | CITE | 0/60 | 0.00 | 0.00 to 0.00 |
| O | NEG | 4/58 | 0.07 | 0.00 to 0.16 |
| O | QUAL | 50/63 | 0.79 | 0.66 to 0.91 |
| O | NUM in-context | 4/36 | 0.11 | 0.00 to 0.28 |
| O | NUM out-of-context | 0/21 | 0.00 | 0.00 to 0.00 |
| O | all | 58/306 | 0.19 | 0.15 to 0.23 |
| Q | ADD | 0/67 | 0.00 | 0.00 to 0.00 |
| Q | NUM | 0/57 | 0.00 | 0.00 to 0.00 |
| Q | CITE | 0/60 | 0.00 | 0.00 to 0.00 |
| Q | NEG | 0/57 | 0.00 | 0.00 to 0.00 |
| Q | QUAL | 32/63 | 0.51 | 0.35 to 0.67 |
| Q | NUM in-context | 0/36 | 0.00 | 0.00 to 0.00 |
| Q | NUM out-of-context | 0/21 | 0.00 | 0.00 to 0.00 |
| Q | all | 32/304 | 0.11 | 0.07 to 0.14 |

| Judge | Invalid outcomes | Caught for the wrong reason (rate, 95% CI) |
|---|---|---|
| G | 0 | 0.00 (0.00 to 0.00), n=306 |
| O | 0 | 0.00 (0.00 to 0.00), n=306 |
| Q | 3 | 0.00 (0.00 to 0.01), n=304 |

## S2. False alarms on controls (run 1)

| Judge | Level | Flagged/n | Rate | 95% CI |
|---|---|---|---|---|
| G | answer | 2/68 | 0.03 | 0.00 to 0.07 |
| G | sentence | 2/93 | 0.02 | 0.00 to 0.05 |
| O | answer | 0/68 | 0.00 | 0.00 to 0.00 |
| O | sentence | 0/93 | 0.00 | 0.00 to 0.00 |
| Q | answer | 4/67 | 0.06 | 0.01 to 0.12 |
| Q | sentence | 4/91 | 0.04 | 0.01 to 0.09 |

Controls with no usable verdict (excluded above): G 0, O 0, Q 1.

## S3. Agreement between judges (run 1)

| Units | n | Fleiss κ | κ G–O | κ G–Q | κ O–Q | % agree |
|---|---|---|---|---|---|---|
| all | 580 | 0.89 (0.86 to 0.92) | 0.93 (0.89 to 0.96) | 0.87 (0.82 to 0.92) | 0.87 (0.83 to 0.91) | 0.92 |
| planted | 304 | 0.73 (0.63 to 0.82) | 0.83 (0.75 to 0.92) | 0.71 (0.56 to 0.83) | 0.65 (0.51 to 0.78) | 0.89 |

## S4. Run-to-run variation

| Judge | Units in all 3 runs | Verdicts differing | Fleiss κ across runs | Miss rate run 1 / 2 / 3 |
|---|---|---|---|---|
| G | 0 | not available | not available | 0.18 / n/a / n/a |
| O | 0 | not available | not available | 0.19 / n/a / n/a |
| Q | 0 | not available | not available | 0.11 / n/a / n/a |

## S5, S6, S9. Contrasts

| Contrast | Estimate | 95% CI |
|---|---|---|
| S5: G own-vs-other, minus Q's | 0.01 | -0.03 to 0.05 |
| S5: O own-vs-other, minus Q's | -0.04 | -0.07 to 0.00 |
| S6: Δ_SP, ADD only | 0.00 | 0.00 to 0.00 |
| S6: Δ_SP, NUM only | 0.00 | -0.05 to 0.05 |
| S6: Δ_SP, CITE only | 0.00 | 0.00 to 0.00 |
| S6: Δ_SP, NEG only | 0.00 | -0.05 to 0.05 |
| S6: Δ_SP, QUAL only | -0.06 | -0.14 to 0.00 |
| S9: m_Q(A) − m_Q(B) | -0.01 | -0.05 to 0.02 |

## S7. Own vs other generator within a judge (exact McNemar, Holm)

| Judge | Matched pairs | Missed on own only | Missed on other only | p | p (Holm) |
|---|---|---|---|---|---|
| G | 150 | 2 | 3 | 1.000 | 1.000 |
| O | 150 | 1 | 5 | 0.219 | 0.438 |

## S8. Robustness of Δ_SP

| Variant | Δ_SP | 95% CI | Decision rule result |
|---|---|---|---|
| a_majority_of_3_runs | not available (runs 2-3 incomplete) | | |
| b_invalid_as_miss | -0.01 | -0.03 to 0.01 | no effect of 10 points or more |
| b_invalid_as_catch | -0.01 | -0.03 to 0.01 | no effect of 10 points or more |
| c_answer_level | -0.01 | -0.03 to 0.01 | no effect of 10 points or more |
| d_without_CITE | -0.02 | -0.04 to 0.01 | no effect of 10 points or more |
| e_original_questions | -0.01 | -0.05 to 0.04 | no effect of 10 points or more |
| e_new_questions | -0.02 | -0.04 to 0.00 | no effect of 10 points or more |
| f_without_flagged_controls | -0.02 | -0.04 to 0.01 | no effect of 10 points or more |
