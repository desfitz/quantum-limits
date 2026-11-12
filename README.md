# The Economic Limits of Quantum Computing - calculations

Code for the working paper *The Economic Limits of Quantum Computing: a Fermi assessment of capital, capability and quantum advantage* by Desmond Fitzpatrick, Ph.D. (ORCID 0009-0001-0534-2793).

Every number the paper computes is computed here, from inputs you can change.

## Run it

Python 3.8 or later, standard library only. Works on Linux, macOS and Windows.

```
python run_all.py                     # recompute and print every result
python -m unittest discover tests     # check the code reproduces the paper's numbers
```

## Change an assumption

All inputs live in `quantum_limits/inputs.py`, each with its source (reference number in the paper) or marked as an assumption. Where the paper gives a range, the input has a central value and a value **generous to quantum computing**. The paper's conclusions are tested at the generous end.

Examples:

- Cheaper machine: set `MACHINE_COST["central"] = 1e9`.
- Faster error-corrected gates: set `NONCLIFFORD_GATES_PER_SECOND["central"] = 1e5`.
- Different judgment of the odds in Section 8.2: edit `CENTRAL_JUDGMENT`.

## What is where

| Paper section | Function in `quantum_limits/calc.py` |
| --- | --- |
| A.1 Revenue per dollar raised, IonQ dilution | `revenue_per_dollar` |
| A.3, A.11 Grover search, time and cost break-even | `grover` |
| A.4, 7.1 Cost per operation (the exchange rate) | `exchange_rates` |
| 7.2, A.11 Cost per answer, algorithm by algorithm | `cost_per_answer` |
| A.5 Affordability and market sensitivity | `affordability` |
| A.6 Machines implied by McKinsey's forecast | `machines_implied` |
| A.7 IBM's quantum business as a share of revenue | `ibm_share` |
| A.8 Size of the simulation market | `market_size` |
| A.9 Refrigerators for a million qubits | `fridges` |
| 6.4 Ceiling on chemistry runs and studies | `runs_ceiling` |
| 8.2 Joint chance of the commercial case | `joint_chance` |
| 7 Brute-force memory for n qubits | `state_vector_bytes` |

## Links

- Paper (this version, v26): https://doi.org/10.5281/zenodo.24150083
- All versions: https://doi.org/10.5281/zenodo.24150082
- Zenodo record (paper, investor deck, code): https://zenodo.org/records/24150083
- SSRN: to follow
- Companion paper: *The Macroeconomic Limits of AI Compute*, Zenodo DOI 10.5281/zenodo.23843154 (version), 10.5281/zenodo.23406475 (all versions); code at github.com/desfitz/ai-compute-limits; SSRN abstract 7620359
- Contact: desmond.fitzpatrick@nvara.ai

## Notes

- Matches paper v26 (11 November 2026). All listed companies are at Q3 2026 except Infleqtion, which reports on 16 November 2026; its Q3 figures go into v26.1.
- `review/REVIEW_LOG.md` is the cross-model verification log: every point raised by the AI reviewers and how it was resolved.
- The probabilities in Section 8.2 are the author's judgments, not measurements. The code exists so readers can replace them.
- Not investment advice.

## Licence

MIT. See LICENSE.

See SYMBOLS.md for what N, n and every other symbol mean for each algorithm.
