## 4. F2 conversion-stage vs behavioral fidelity (stratified 20% sample, SIR arm)

| unit type | n | conversion-stage recovery | behavioral recovery |
|---|---|---|---|
| conditional_constraint | 4 | 0.00 | 0.00 |
| designed_unknown_flag | 2 | 0.00 | 0.00 |
| entity_ref | 42 | 0.00 | 0.00 |
| exception_of_exclusion | 2 | 0.00 | 0.00 |
| exclusion | 10 | 0.00 | 0.00 |
| modality | 8 | 0.00 | 0.00 |
| priority_preference | 6 | 0.00 | 0.00 |
| quantity_unit | 18 | 0.00 | 0.11 |
| temporal_qualifier | 26 | 0.00 | 0.00 |

Unknown-probe handling (designed probes; doc AND artifact must declare undeterminacy):
- `designed_unknown_flag`: 0/2 handled (0%)
- `entity_ref`: 0/2 handled (0%)
- `priority_preference`: 0/2 handled (0%)

_Note (CP instrumentation limit): CP gold constraints are internal ids checked against the emitted plan; leaf-value containment cannot attribute CP losses per unit type. CP F2 is therefore reported qualitatively via K_err/doc_valid/silent-error rather than per-unit._

## 5. H2 variance module (20 CP items x 5 reps @ T=0.7)

| arm | items | modal-answer agreement | outcome entropy (bits) | mean score |
|---|---|---|---|---|
| NL-opt | 20 | 0.71 | 0.94 | 0.323 |
| JSON | 20 | 0.41 | 1.74 | 0.838 |
| CSIR-SIR | 20 | 0.76 | 0.70 | 0.086 |

## 6. Replication (H1 condition 3)

- Stochastic module (10 stratified items x 3 reps @ T=0.7, seeds 201–203), SIR vs strongest baseline:
  - CP vs JSON: fold gate-deltas [-0.8, -1.0, -0.7] → sign-consistent: **True** (-)
  - EX vs JSON: fold gate-deltas [-0.1, 0.0, 0.0] → sign-consistent: **False** (-)
  - TU vs JSON: fold gate-deltas [-1.0, -0.9, -1.0] → sign-consistent: **True** (-)
- Item-split module (primary, 3 folds):
  - CP: fold gate-deltas [-0.6875, -0.625, -0.625] → sign-consistent: **True**
  - EX: fold gate-deltas [0.0, -0.0625, -0.0625] → sign-consistent: **False**
  - TU: fold gate-deltas [-0.9375, -0.875, -1.0] → sign-consistent: **True**

## 7. F3 round-trip stability

- F3 probe not run/empty.
