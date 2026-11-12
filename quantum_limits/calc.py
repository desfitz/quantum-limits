"""Every calculation in the paper's Appendix A and Sections 6.4, 7.2 and 8.2.

Each function names its section, returns plain numbers, and uses only inputs.py.
Standard library only; runs on Linux, macOS and Windows with Python 3.8+.
"""
import math
from . import inputs as I


def annual_cost(machine_cost):
    """A = machine cost / write-off years + running cost per year (A.4)."""
    return machine_cost / I.WRITE_OFF_YEARS + I.RUNNING_COST_PER_YEAR


def price_per_hour(machine_cost):
    """P = A / 8,766 (A.4)."""
    return annual_cost(machine_cost) / I.HOURS_PER_YEAR


def cost_per_op(price_hour, ops_per_second):
    """p = P / (3,600 x f) (A.4)."""
    return price_hour / (I.SECONDS_PER_HOUR * ops_per_second)


def exchange_rates():
    """Cost of one quantum operation in GPU operations (A.4, Section 7.1)."""
    gpu = cost_per_op(I.GPU_PRICE_PER_HOUR, I.GPU_OPS_PER_SECOND)
    today = cost_per_op(I.IBM_PRICE_PER_HOUR, I.IBM_NOISY_GATES_PER_SECOND)
    out = {"gpu_cost_per_op": gpu, "today_ratio": today / gpu, "table": {}}
    for label, mc in (("$1B", 1e9), ("$2B", 2e9)):
        for f in (1e3, 1e4, 1e5, 1e6):
            out["table"][(label, f)] = cost_per_op(price_per_hour(mc), f) / gpu
    out["central_ratio"] = out["table"][("$2B", 1e4)]
    out["generous_ratio"] = out["table"][("$1B", 1e6)]
    return out


def revenue_per_dollar():
    """r = R / K (A.1), plus IonQ excluding the foundry and dilution."""
    R = sum(I.IONQ_REVENUE.values())
    K = sum(I.IONQ_CAPITAL.values())
    shares = I.IONQ_SHARES
    dil = shares["Nov 2026"] / shares["Mar 2022"]
    out = {"IonQ": (R, K, R / K), "IonQ excl. foundry": (R - I.IONQ_FOUNDRY_Q3_2026, K,
           (R - I.IONQ_FOUNDRY_Q3_2026) / K), "IonQ dilution x": dil,
           "IonQ 2022 holder's remaining fraction": 1 / dil}
    for name, (r, k) in I.OTHER_COMPANIES.items():
        out[name] = (r, k, r / k)
    return out


def grover():
    """A.3 time comparison and A.11 cost break-even."""
    c_c = 1 / I.GROVER_GPU_ITEMS_PER_SECOND
    rounds = math.pi / 4 * math.sqrt(I.GROVER_N)
    out = {"classical_seconds": I.GROVER_N * c_c}
    c_q = I.GROVER_GATES_PER_ROUND / I.NONCLIFFORD_GATES_PER_SECOND["central"]
    out["quantum_seconds"] = rounds * c_q
    nstar_time = (c_q / c_c) ** 2
    out["time_breakeven_N"] = nstar_time
    out["time_breakeven_years_one_gpu"] = nstar_time * c_c / (I.HOURS_PER_YEAR * 3600)
    c_c1000 = c_c / 1000
    n1000 = (c_q / c_c1000) ** 2
    out["time_breakeven_N_1000gpu"] = n1000
    out["time_breakeven_years_1000gpu"] = n1000 * c_c1000 / (I.HOURS_PER_YEAR * 3600)
    # Cost break-even: 0.785 sqrt(N) q = N c
    c_item = c_c * I.GPU_PRICE_PER_HOUR / I.SECONDS_PER_HOUR
    out["classical_cost"] = I.GROVER_N * c_item
    for case, mc in (("central", 2e9), ("generous", 1e9)):
        f = I.NONCLIFFORD_GATES_PER_SECOND[case]
        p_s = price_per_hour(mc) / I.SECONDS_PER_HOUR
        q_round = I.GROVER_GATES_PER_ROUND / f * p_s
        out["quantum_cost_" + case] = rounds * q_round
        nstar = (math.pi / 4 * q_round / c_item) ** 2
        out["cost_breakeven_N_" + case] = nstar
        out["cost_breakeven_years_one_gpu_" + case] = nstar * c_c / (I.HOURS_PER_YEAR * 3600)
    return out


def cost_per_answer():
    """Section 7.2 and A.11: cost of one answer, central and generous."""
    out = {}
    for case, mc in (("central", 2e9), ("generous", 1e9)):
        p_s = price_per_hour(mc) / I.SECONDS_PER_HOUR
        sp = I.SPEEDUP_VS_PUBLISHED[case]
        out[("Shor RSA-2048", case)] = I.SHOR_RSA2048_SECONDS / sp * p_s
        lo, hi = I.CHEM_RUN_HOURS
        out[("Chemistry run", case)] = (lo * 3600 / sp * p_s, hi * 3600 / sp * p_s)
        f = I.NONCLIFFORD_GATES_PER_SECOND[case]
        out[("Amplitude estimation", case)] = I.AMPLITUDE_EST_T_DEPTH / f * p_s
    out[("Amplitude estimation", "classical")] = (I.AMPLITUDE_EST_CLASSICAL_SECONDS *
                                                  I.GPU_PRICE_PER_HOUR / I.SECONDS_PER_HOUR)
    return out


def affordability():
    """A.5: required profit and vendor revenue grid."""
    out = {"required_profit": I.COST_OF_CAPITAL * I.INVESTMENT_TO_FT["low"],
           "central_revenue": (I.USER_VALUE["central_low"] * I.VENDOR_SHARE["central_low"],
                               I.USER_VALUE["central_high"] * I.VENDOR_SHARE["central_high"])}
    out["grid"] = {(u, s): u * s for u in I.USER_VALUE["grid"] for s in I.VENDOR_SHARE["grid"]}
    out["revenue_needed_at_margin"] = out["required_profit"] / I.OPERATING_MARGIN
    return out


def machines_implied():
    """A.6: McKinsey 2035 revenue divided by annual cost per machine."""
    a = annual_cost(I.MACHINE_COST["central"])
    return tuple(v / a for v in I.MCKINSEY_2035_REVENUE)


def ibm_share():
    """A.7: s = (S / Y) / Q."""
    return (I.IBM_SIGNINGS / I.IBM_SIGNING_YEARS) / I.IBM_REVENUE


def market_size():
    """A.8: M = C + D + F."""
    return (sum(v[0] for v in I.MARKET_PARTS.values()),
            sum(v[1] for v in I.MARKET_PARTS.values()))


def fridges():
    """A.9: n = q / k; cost = n x p."""
    n_hi = I.PHYSICAL_QUBITS / I.QUBITS_PER_FRIDGE[0]
    n_lo = I.PHYSICAL_QUBITS / I.QUBITS_PER_FRIDGE[1]
    return {"count": (n_lo, n_hi), "cost": (n_lo * I.FRIDGE_PRICE[0], n_hi * I.FRIDGE_PRICE[1])}


def runs_ceiling():
    """Section 6.4: vendor revenue / cost per run and per study."""
    rev_lo, rev_hi = 2e9, 10e9
    runs = (rev_lo / 6e6, rev_hi / 4e6)
    studies = (rev_lo / 500e6, rev_hi / 50e6)
    gen_runs = 30e9 / 0.3e6
    gen_studies = (30e9 / 30e6, 30e9 / 3e6)
    return {"runs": runs, "studies": studies, "generous_runs": gen_runs,
            "generous_studies": gen_studies}


def joint_chance():
    """Section 8.2: product of the author's judged chances (replace them!)."""
    prod = lambda xs: math.prod(xs)
    lows = [c[1] for c in I.CONDITIONS]
    highs = [c[2] for c in I.CONDITIONS]
    central = prod(I.CENTRAL_JUDGMENT)
    upper = prod(highs)
    # Hardware conditions 1-3 moving together: treat as one condition at 0.5-0.7
    corr_lo = 0.5 * prod(I.CENTRAL_JUDGMENT[3:])
    corr_hi = 0.7 * prod(highs[3:])
    return {"independent_central": central, "independent_upper": upper,
            "lowest": prod(lows), "correlated": (corr_lo, corr_hi)}


def state_vector_bytes(n_qubits):
    """Section 7: brute-force memory, 16 bytes per complex amplitude."""
    return 16 * 2 ** n_qubits


def _nfs_L(bits):
    """Number field sieve work, L(n) = exp(1.923 (ln N)^(1/3) (ln ln N)^(2/3))."""
    ln_n = bits * math.log(2)
    return math.exp((64 / 9) ** (1 / 3) * ln_n ** (1 / 3) * math.log(ln_n) ** (2 / 3))


def factoring_classical_core_years(bits):
    return I.RSA250_CORE_YEARS * _nfs_L(bits) / _nfs_L(I.RSA250_BITS)


def factoring_quantum_seconds(bits, case="central"):
    return I.SHOR_RSA2048_DAYS * 86400 * (bits / 2048) ** 3 / I.SPEEDUP_VS_PUBLISHED[case]


def crossovers():
    """Section 7.4 / A.12: time and money crossovers and the classical time wall."""
    out = {}
    core_year_cost = I.CORE_HOUR_PRICE * I.HOURS_PER_YEAR
    for case, mc in (("central", 2e9), ("generous", 1e9)):
        p_s = price_per_hour(mc) / I.SECONDS_PER_HOUR
        b = 300
        while factoring_classical_core_years(b) * core_year_cost < factoring_quantum_seconds(b, case) * p_s:
            b += 1
        out["factoring_money_bits_" + case] = b
    for cores in (1e3, 1e6):
        b = 300
        while factoring_classical_core_years(b) * I.YEAR_SECONDS / cores < factoring_quantum_seconds(b):
            b += 1
        out["factoring_time_bits_%g_cores" % cores] = b
    b = 300
    while factoring_classical_core_years(b) / I.CLASSICAL_FLEET_GPUS < I.WALL_SECONDS / I.YEAR_SECONDS:
        b += 1
    out["factoring_wall_bits"] = b
    out["rsa2048_core_years"] = factoring_classical_core_years(2048)
    out["rsa2048_quantum_cost_central"] = factoring_quantum_seconds(2048) * price_per_hour(2e9) / I.SECONDS_PER_HOUR
    # Grover
    c_c = 1 / I.GROVER_GPU_ITEMS_PER_SECOND
    c_q = I.GROVER_GATES_PER_ROUND / I.NONCLIFFORD_GATES_PER_SECOND["central"]
    for p in (1, 1e3, 1e6):
        out["grover_time_N_%g_gpus" % p] = (c_q / (c_c / p)) ** 2
    n_wall = I.WALL_SECONDS * I.CLASSICAL_FLEET_GPUS / c_c
    out["grover_wall_N"] = n_wall
    out["grover_quantum_years_at_wall"] = math.pi / 4 * math.sqrt(n_wall) * c_q / I.YEAR_SECONDS
    # Amplitude estimation: precision tightening needed
    q_s = I.AMPLITUDE_EST_T_DEPTH / I.NONCLIFFORD_GATES_PER_SECOND["central"]
    out["ae_time_tightening_1gpu"] = q_s / I.AMPLITUDE_EST_CLASSICAL_SECONDS
    a = cost_per_answer()
    out["ae_money_tightening"] = a[("Amplitude estimation", "central")] / a[("Amplitude estimation", "classical")]
    # Chemistry
    e, m = I.FEMOCO_ACTIVE_SPACE
    dets = math.comb(m, e // 2) ** 2
    out["femoco_determinants"] = dets
    out["femoco_past_record"] = dets / I.FCI_RECORD_DETERMINANTS
    return out


def edge_costs():
    """Section 7 'Start at the edge' and A.13: the largest problem 10^6 machines finish in one week,
    the same computation on a quantum machine, and C = B / A (quantum cost over classical cost)."""
    W, P = I.WALL_SECONDS, I.CLASSICAL_FLEET_GPUS
    A_gpu = P * W / 3600 * I.GPU_PRICE_PER_HOUR
    A_cpu = P * W / 3600 * I.CORE_HOUR_PRICE
    Ps = {"central": price_per_hour(I.MACHINE_COST["central"]) / 3600,
          "generous": price_per_hour(I.MACHINE_COST["generous"]) / 3600}
    f = {"central": I.NONCLIFFORD_GATES_PER_SECOND["central"], "generous": I.NONCLIFFORD_GATES_PER_SECOND["generous"]}
    out = {"A_gpu": A_gpu, "A_cpu": A_cpu}
    # Search
    N = W * P * I.GROVER_GPU_ITEMS_PER_SECOND
    y = math.pi / 4 * math.sqrt(N) * I.GROVER_GATES_PER_ROUND
    out["search"] = {"N": N, "x_label_qubits": math.ceil(math.log2(N)), "y": y,
                     **{k: {"seconds": y / f[k], "B": y / f[k] * Ps[k], "C": y / f[k] * Ps[k] / A_gpu} for k in Ps}}
    # Monte Carlo (amplitude estimation)
    t = math.sqrt(W * P / I.AMPLITUDE_EST_CLASSICAL_SECONDS)
    y = I.AMPLITUDE_EST_T_DEPTH * t
    out["monte_carlo"] = {"tightening": t, "x": I.AE_LOGICAL_QUBITS, "y": y,
                          **{k: {"seconds": y / f[k], "B": y / f[k] * Ps[k], "C": y / f[k] * Ps[k] / A_gpu} for k in Ps}}
    # Factoring
    cy = P * W / I.YEAR_SECONDS
    b = 300
    while factoring_classical_core_years(b) < cy:
        b += 1
    out["factoring"] = {"bits": b, "x": I.SHOR_RSA2048_LOGICAL_QUBITS * b / 2048,
                        "y": I.SHOR_RSA2048_TOFFOLIS * (b / 2048) ** 3,
                        **{k: {"seconds": factoring_quantum_seconds(b, k),
                               "B": factoring_quantum_seconds(b, k) * Ps[k],
                               "C": factoring_quantum_seconds(b, k) * Ps[k] / A_cpu} for k in Ps}}
    # Chemistry: run time scaled as m^3 from FeMoco (assumption)
    def chem(m, electrons, A):
        tq = I.FEMOCO_RUN_HOURS * (m / I.FEMOCO_ORBITALS) ** 3 * 3600
        d = {"m": m, "determinants": math.comb(m, electrons // 2) ** 2, "y": tq * f["central"], "A": A}
        for k in Ps:
            s = tq / I.SPEEDUP_VS_PUBLISHED[k]
            d[k] = {"seconds": s, "B": s * Ps[k], "C": s * Ps[k] / A}
        return d
    out["chem_record"] = chem(23, 26, I.FCI_RECORD_CORE_HOURS * I.CORE_HOUR_PRICE)
    out["chem_edge"] = chem(29, 28, A_gpu)
    out["chem_edge_memory_determinants"] = P * I.GPU_MEMORY_BYTES / 8
    return out


def biggest_machines():
    """Section 7 'The biggest machines, side by side' and A.13."""
    week = 7 * 86400
    capex = I.FLEET_GIGAWATTS * I.COST_PER_GIGAWATT
    own_week = (capex / 5 + I.FLEET_GIGAWATTS * 1e6 * I.HOURS_PER_YEAR * I.POWER_PRICE_KWH) / 52.18
    out = {"fleet_capex": capex, "fleet_week_own": own_week,
           "fleet_week_rent": (I.BIGGEST_GPU_FLEET * 168 * 2.5, I.BIGGEST_GPU_FLEET * 168 * 5.0)}
    f = I.NONCLIFFORD_GATES_PER_SECOND["central"]
    for name, t in (("day", 86400), ("week", week), ("month", 30 * 86400)):
        q = f * t
        rounds = q / I.GROVER_GATES_PER_ROUND
        n_items = (rounds / (math.pi / 4)) ** 2
        tight = t / (I.AMPLITUDE_EST_T_DEPTH / f)
        bits = 2048 * (t / (I.SHOR_RSA2048_DAYS * 86400)) ** (1 / 3)
        m = I.FEMOCO_ORBITALS * (t / (I.FEMOCO_RUN_HOURS * 3600)) ** (1 / 3)
        mi = int(m)
        out[name] = {
            "ops": q, "quantum_cost": I.QC_YEARLY_COST * t / I.YEAR_SECONDS,
            "search_items": n_items, "search_one_gpu_s": n_items / I.GROVER_GPU_ITEMS_PER_SECOND,
            "search_one_gpu_cost": n_items / I.GROVER_GPU_ITEMS_PER_SECOND / 3600 * I.GPU_PRICE_PER_HOUR,
            "mc_tightening": tight, "mc_one_gpu_s": tight ** 2 * I.AMPLITUDE_EST_CLASSICAL_SECONDS,
            "mc_one_gpu_cost": tight ** 2 * I.AMPLITUDE_EST_CLASSICAL_SECONDS / 3600 * I.GPU_PRICE_PER_HOUR,
            "factor_bits": bits, "factor_logical_qubits": I.SHOR_RSA2048_LOGICAL_QUBITS * bits / 2048,
            "factor_classical_core_years": factoring_classical_core_years(round(bits)),
            "chem_orbitals": m, "chem_bytes": math.comb(mi, mi // 2) ** 2 * 8,
            "chem_fits_biggest_machine": math.comb(mi, mi // 2) ** 2 * 8 <= I.GPU_MEMORY_FLEET_BYTES,
        }
    return out


def _dets(m):
    return math.comb(m, m // 2) * math.comb(m, m - m // 2)


def chem_crossover(m_range=range(22, 36)):
    """Section 6.4 / A.14: exact chemistry, classical vs quantum cost by orbitals."""
    ps_c = price_per_hour(I.MACHINE_COST["central"]) / 3600
    ps_g = price_per_hour(I.MACHINE_COST["generous"]) / 3600
    edge_dets = I.GPU_MEMORY_FLEET_BYTES / 8
    rows = []
    for m in m_range:
        n = _dets(m)
        tq = I.FEMOCO_RUN_HOURS * (m / I.FEMOCO_ORBITALS) ** 3 * 3600
        cl = I.FCI_RECORD_COST * n / I.FCI_RECORD_DETERMINANTS_ACTUAL
        rows.append({"m": m, "determinants": n, "classical": cl if n <= edge_dets * 1.5 else None,
                     "quantum": tq * ps_c, "quantum_generous": tq / I.SPEEDUP_VS_PUBLISHED["generous"] * ps_g,
                     "quantum_hours": tq / 3600})
    def cross(key):
        prev = None
        for r in rows:
            if r["classical"] and r[key] <= r["classical"]:
                if prev is None:
                    return r["m"]
                a = math.log(prev[key] / prev["classical"]); b = math.log(r[key] / r["classical"])
                return prev["m"] + a / (a - b)
            prev = r
        return None
    return {"rows": rows, "crossover_central": cross("quantum"), "crossover_generous": cross("quantum_generous")}


def market_where_it_matters():
    """Section 6.5 / A.14: today's budgets and value-based vendor revenue; machines kept busy."""
    lo = I.SIM_MARKET[0] * I.SHARE_STRONGLY_CORRELATED[0] * I.SHARE_EXACT_BEYOND_EDGE[0]
    mid = sum(I.SIM_MARKET) / 2 * I.SHARE_STRONGLY_CORRELATED[1] * I.SHARE_EXACT_BEYOND_EDGE[1]
    hi = I.SIM_MARKET[1] * I.SHARE_STRONGLY_CORRELATED[2] * I.SHARE_EXACT_BEYOND_EDGE[2]
    value = (2e9, 10e9)
    machines = {k: v / I.QC_YEARLY_COST for k, v in (("today", mid), ("value_low", value[0]), ("value_high", value[1]))}
    return {"today_low": lo, "today_central": mid, "today_high": hi, "vendor_value": value, "machines": machines}


def learning_curve(machines=20):
    """Section 8.5 / A.14: cost multiplier after building `machines` units."""
    d = math.log2(machines)
    return {"doublings": d, **{"rate_%d" % round(r * 100): (1 - r) ** d for r in I.LEARNING_RATE}}


def chem_crossover_2025_record(m_range=range(22, 36)):
    """Section 6.4 sensitivity: the same comparison anchored to the 2025 compressed record (ref 164)."""
    cost = I.CI2025_CORES * I.CI2025_HOURS * I.CORE_HOUR_PRICE_CI
    dets = I.CI2025_DETERMINANTS * I.CI2025_REAL_EQUIV
    saved = (I.FCI_RECORD_COST, I.FCI_RECORD_DETERMINANTS_ACTUAL)
    try:
        I.FCI_RECORD_COST, I.FCI_RECORD_DETERMINANTS_ACTUAL = cost, dets
        r = chem_crossover(m_range)
    finally:
        I.FCI_RECORD_COST, I.FCI_RECORD_DETERMINANTS_ACTUAL = saved
    r["cost_per_det_ratio"] = (saved[0] / saved[1]) / (cost / dets)
    at30 = next(x for x in r["rows"] if x["m"] == 30)
    r["quantum_advantage_at_30"] = at30["classical"] / at30["quantum"]
    return r
