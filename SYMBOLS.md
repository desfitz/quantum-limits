# Symbols, algorithm by algorithm (paper Section 7.4, Appendix A.12)

Capital N always counts things to process. Lower-case n is always a number of bits in a key.
Neither is a number of qubits.

| Algorithm | Size | Classical work | Quantum work | Code |
|---|---|---|---|---|
| Grover search | N = candidate answers | N checks at 1e10/s per GPU | 0.785 x sqrt(N) rounds of 0.1 s; about log2(N) qubits | `grover()`, `crossovers()` |
| Amplitude estimation | eps = precision; N = paths = (s/eps)^2 | grows as 1/eps^2 | grows as 1/eps (about sqrt(N)) | `crossovers()` keys `ae_*` |
| Factoring (Shor) | n = bits in the key; the number is about 2^n | number field sieve, calibrated to RSA-250 (829 bits, 2,700 core-years) | 4.96 days x (n/2048)^3 | `factoring_classical_core_years`, `factoring_quantum_seconds` |
| Exact chemistry (FCI) | m orbitals, a and b electrons of each spin; N = C(m,a) x C(m,b) determinants | grows with N | a power of m; about 2m qubits plus working qubits | `crossovers()` keys `femoco_*` |

Common symbols: T_c, T_q time (s); C_c, C_q cost ($); P classical machines; f error-corrected
non-Clifford gates a second (1e4 central, 1e6 generous); P_s price of one quantum machine-second
($15.8 central, $9.4 generous); time crossover T_q = T_c; money crossover C_q = C_c;
classical time wall T_c = 1 year on 1e6 machines.

Note: the Grover time crossover in the code rounds pi/4 = 0.785 to 1, as the paper does in A.3;
keeping it lowers each crossover N by a factor of 0.62 (same order of magnitude).
