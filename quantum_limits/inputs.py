"""Every input used in "The Economic Limits of Quantum Computing" (working paper).

Each input has a central value and, where the paper bounds it, a low and a high
value plus the end that is GENEROUS to quantum computing. Change any value here
and rerun `python run_all.py` to see every result recomputed.

Units: dollars, seconds, hours, as named. Ref numbers point to the paper's
reference list; "assumption" means the author's stated assumption.
"""

HOURS_PER_YEAR = 8766          # 365.25 x 24
SECONDS_PER_HOUR = 3600

# --- Classical GPU (H100 class) -------------------------------------------
GPU_PRICE_PER_HOUR = 2.50      # $; on-demand range $1.99-12.29, Oct 2026 (ref 86)
GPU_OPS_PER_SECOND = 1e15      # ~989e12 dense 16-bit ops/s (ref 87)

# --- Quantum today (IBM cloud) ---------------------------------------------
IBM_PRICE_PER_HOUR = 5760      # $96 a minute list price (ref 62)
IBM_NOISY_GATES_PER_SECOND = 5e6   # 1,000 circuits/s x 5,000 gates (ref 62)

# --- Fault-tolerant machine, about 2030 ------------------------------------
MACHINE_COST = {"central": 2e9, "generous": 1e9}   # $; assumption, a floor (ref 95)
WRITE_OFF_YEARS = 5                                 # assumption
RUNNING_COST_PER_YEAR = 100e6                       # $; assumption
NONCLIFFORD_GATES_PER_SECOND = {"low": 1e3, "central": 1e4, "high": 1e5, "generous": 1e6}
SPEEDUP_VS_PUBLISHED = {"central": 1.0, "generous": 10.0}  # generous: 10x faster than published run times

# --- Published run times and gate counts -----------------------------------
SHOR_RSA2048_SECONDS = 7 * 86400                    # under one week (ref 40)
CHEM_RUN_HOURS = (73, 96)                           # FeMoco / P450 (ref 51)
AMPLITUDE_EST_T_DEPTH = 54e6                        # derivative pricing (ref 84)
AMPLITUDE_EST_CLASSICAL_SECONDS = 1.0               # ~1 s of classical computing (ref 84)

# --- Grover example (Appendix A.3) -----------------------------------------
GROVER_N = 1e12                     # items searched; assumption
GROVER_GPU_ITEMS_PER_SECOND = 1e10  # assumption
GROVER_GATES_PER_ROUND = 1000       # assumption

# --- Revenue and capital, $ millions (Appendix A.1) ------------------------
IONQ_REVENUE = {"2021": 2.1, "2022": 11.1, "2023": 22.0, "2024": 43.1,       # refs 97-98
                "2025": 130.0, "Q1 2026": 64.7, "Q2 2026": 80.1,            # refs 2-3
                "Q3 2026": 173.8}                                           # ref 1
IONQ_CAPITAL = {"2021 listing": 636.0, "Mar 2025": 372.6, "Jul 2025": 1000.0,  # refs 99, 6
                "Oct 2025": 2000.0, "Oct 2026": 2000.0}                         # refs 5, 4
IONQ_FOUNDRY_Q3_2026 = 83.5        # SkyWater revenue in Q3 2026 (ref 1)
IONQ_SHARES = {"Mar 2022": 197_671_494, "Oct 2026": 432_462_651,           # refs 106-107
               "Nov 2026": 432_462_651 + 32_233_274}                     # + Elisity shares, ref 111
OTHER_COMPANIES = {  # revenue to date, capital raised ($M)
    # Rigetti: revenue to Q3 2026 incl. $1.4M Q3 (refs 18-19, 156); capital $840M + $100M CHIPS shares (refs 18, 27, 133)
    # D-Wave: revenue to Q3 2026 incl. $4.5M Q3 (ref 155); capital refs 15-16
    # Quantinuum: capital incl. $1.68B gross IPO, 28M shares at $60 (refs 9, 11, 12, 126)
    # Quantum Computing Inc: revenue to Q3 2026 incl. $9.5M Q3 (refs 22, 136, 138)
    "Rigetti": (62.1, 940.0), "D-Wave": (66.1, 1170.0),
    "Quantinuum": (76.2, 2961.0), "Quantum Computing Inc": (20.2, 1640.0)}

# --- IBM share (Appendix A.7) ----------------------------------------------
IBM_SIGNINGS = 1000.0    # $M, 2017-2024 (ref 66)
IBM_SIGNING_YEARS = 8
IBM_REVENUE = 69100.0    # $M, trailing twelve months to mid-2026 (ref 67)

# --- Market and affordability (Appendix A.5, A.8) ---------------------------
INVESTMENT_TO_FT = {"low": 100e9, "high": 150e9}      # $ to fault tolerance by 2032
COST_OF_CAPITAL = 0.10                                # assumption
USER_VALUE = {"central_low": 20e9, "central_high": 50e9, "grid": [10e9, 30e9, 100e9]}
VENDOR_SHARE = {"central_low": 0.10, "central_high": 0.20, "grid": [0.10, 0.20, 0.30]}
OPERATING_MARGIN = 0.30                               # assumption, sensitivity note
MARKET_PARTS = {"chemistry software": (1.59e9, 1.59e9),       # ref 56
                "AI drug discovery": (2.9e9, 5.1e9),          # ref 57
                "materials informatics": (0.13e9, 0.28e9)}    # ref 58
MCKINSEY_2035_REVENUE = (43e9, 71e9)                           # ref 60

# --- Refrigerators (Appendix A.9) -------------------------------------------
PHYSICAL_QUBITS = 1_000_000
QUBITS_PER_FRIDGE = (20_000, 30_000)    # ref 65
FRIDGE_PRICE = (5e6, 10e6)              # ref 65

# --- Joint chance of the commercial case (Section 8.2) ----------------------
# Author's judged chance that each generous value is reached: (low, high).
CONDITIONS = [
    ("Fault tolerance at scale by about 2032", 0.5, 0.7),
    ("1,000,000 non-Clifford gates a second", 0.3, 0.5),
    ("$1 billion machine", 0.5, 0.6),
    ("Classical and AI keep failing on strongly correlated chemistry", 0.5, 0.6),
    ("$100 billion a year of user value", 0.2, 0.3),
    ("Vendors keep 30%", 0.3, 0.4),
    ("Two or three competitors", 0.5, 0.6),
]
CENTRAL_JUDGMENT = [0.6, 0.4, 0.5, 0.5, 0.25, 0.3, 0.5]

# --- Crossovers (Section 7.4, Appendix A.12) ---------------------------------
RSA250_BITS = 829
RSA250_CORE_YEARS = 2700          # ref 109
CORE_HOUR_PRICE = 0.03            # $; assumption
SHOR_RSA2048_DAYS = 4.96          # ref 40
CLASSICAL_FLEET_GPUS = 1e6        # large AI campus; assumption for the time wall
YEAR_SECONDS = 3.156e7            # one year
WALL_SECONDS = 7 * 86400          # one week: the classical time wall (a year is of no practical interest)
GPU_MEMORY_BYTES = 80e9           # per H100-class GPU, for the chemistry memory edge
FEMOCO_RUN_HOURS = 85             # mid-point of 73-96 h (ref 51)
FEMOCO_ORBITALS = 54
SHOR_RSA2048_TOFFOLIS = 6.5e9     # 'more than 6.5 billion' (ref 40)
SHOR_RSA2048_LOGICAL_QUBITS = 1400
AE_LOGICAL_QUBITS = 8000          # ref 84
FCI_RECORD_CORE_HOURS = 256 * 40 * 113.6   # ref 115
FCI_RECORD_DETERMINANTS = 1.3e12  # 26 electrons in 23 orbitals (ref 110)
FEMOCO_ACTIVE_SPACE = (54, 54)    # electrons, orbitals (ref 50)

# --- Biggest machines compared (Section 7, A.13) -----------------------------
BIGGEST_GPU_FLEET = 1e6           # Colossus 2: 550,000 + 440,000 announced (ref 116)
FLEET_GIGAWATTS = 1.5             # assumption
COST_PER_GIGAWATT = 55e9          # $50-60B (ref 117)
POWER_PRICE_KWH = 0.08            # $; assumption
GPU_MEMORY_FLEET_BYTES = 1e6 * 192e9
BIGGEST_QC_LOGICAL_QUBITS = 2000  # IBM target, 2033 or later (refs 95, 118)
QC_YEARLY_COST = 500e6            # central: $2B machine over 5 years + $100M a year

# --- Exact chemistry on both machines, market, learning curve (6.4, 6.5, 8.5; A.14) ---
FCI_RECORD_COST = 3.5e4           # $; 1.16e6 core-hours x $0.03 (refs 110, 115)
FCI_RECORD_DETERMINANTS_ACTUAL = 1.3e12
SIM_MARKET = (5e9, 7e9)           # $ a year (A.8)
SHARE_STRONGLY_CORRELATED = (0.05, 0.10, 0.15)   # low, central, high; assumption
SHARE_EXACT_BEYOND_EDGE = (0.10, 0.20, 0.40)     # assumption
LEARNING_RATE = (0.15, 0.20)      # cost fall per doubling of units built; assumption

# --- 2025 compressed exact-CI record (ref 164), sensitivity for Section 6.4 ---
CI2025_CORES = 128_000          # 1,000 Perlmutter nodes x 128 cores
CI2025_HOURS = 34.5
CI2025_DETERMINANTS = 1.05e15   # complex 2-spinor determinants (HBrTe X2C-CASCI)
CI2025_REAL_EQUIV = 2.0         # complex arithmetic ~ twice a nonrelativistic calculation (ref 164)
CORE_HOUR_PRICE_CI = 0.03       # $ per core-hour, as for the 2024 anchor (refs 110, 115)
