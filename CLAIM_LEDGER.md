# Claim Ledger

Canonical registry of material research claims. Rules:

- Every claim gets a row here **at registration time**, before it influences any decision or report.
- Finding labels are restricted to the charter's authorized set: `Observation`, `Historical Claim`, `Hypothesis`, `Experimental Result`, `Potential Novelty`, `Known Prior Art`, `Unresolved`, `Falsified`, `Candidate Contribution`.
- Only the Research Director may set *Candidate Contribution*, and only after prior-art and red-team review.
- Rows are append-only; corrections happen by adding a new row superseding the old one (`Superseded by` in Director disposition).
- LLM agreement is not evidence. Search snippets alone are not sources.

## Schema

| Field | Meaning |
|---|---|
| Claim ID | `C-NNN` sequential |
| Date | ISO date of registration |
| Agent | Role that produced the claim |
| Finding label | One of the nine charter labels |
| Claim | The precise assertion |
| Evidence/source | Source ID(s) from BIBLIOGRAPHY, experiment ID, or file path |
| Source location | Page/section/figure where available |
| Confidence | High / Medium / Low |
| Interpretation | What the agent takes it to mean for the project |
| Relevance | Which hypothesis/question it bears on |
| Competing explanation | Best alternative account of the same evidence |
| Prior-art status | `not-checked` / `checked-clean` / `prior-art-found: <ID>` / `n/a` |
| Red-team status | `not-reviewed` / `objections: <IDs>` / `cleared` / `n/a` |
| Replication status | `single-run` / `replicated` / `failed-replication` / `not-applicable` |
| Director disposition | `open` / `accepted` / `rejected` / `needs-work` / `superseded-by: <C-NNN>` |

## Ledger

| Claim ID | Date | Agent | Label | Claim | Evidence/source | Location | Conf. | Interpretation | Relevance | Competing explanation | Prior-art | Red team | Repl. | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

_No claims registered yet._
