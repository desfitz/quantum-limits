"""Recompute every number in "The Economic Limits of Quantum Computing".

Usage:  python run_all.py
Change any input in quantum_limits/inputs.py and run again.
Plain ASCII output; standard library only.
"""
from quantum_limits import calc


def sci(x):
    return "%.2g" % x


def money(x):
    for unit, d in (("B", 1e9), ("M", 1e6), ("k", 1e3)):
        if abs(x) >= d:
            return "$%.2f%s" % (x / d, unit)
    return "$%.4f" % x


def main():
    print("=" * 70)
    print("The Economic Limits of Quantum Computing - every calculation")
    print("=" * 70)

    e = calc.exchange_rates()
    print("\n[A.4 / 7.1] Exchange rate: cost of one operation vs one GPU operation")
    print("  GPU cost per operation        :", sci(e["gpu_cost_per_op"]), "dollars")
    print("  Quantum today (IBM cloud)     :", sci(e["today_ratio"]), "x")
    print("  Fault-tolerant, central       :", sci(e["central_ratio"]), "x  ($2B machine, 10,000 gates/s)")
    print("  Fault-tolerant, generous      :", sci(e["generous_ratio"]), "x  ($1B machine, 1,000,000 gates/s)")
    print("  Sensitivity table:")
    for (m, f), v in sorted(e["table"].items(), key=lambda kv: (kv[0][1], kv[0][0])):
        print("    %-4s machine, %9.0f gates/s : %s x" % (m, f, sci(v)))

    r = calc.revenue_per_dollar()
    print("\n[A.1] Revenue per dollar raised (cents)")
    for k, v in r.items():
        if isinstance(v, tuple):
            print("  %-22s %8.1f / %8.1f = %5.1f cents" % (k, v[0], v[1], 100 * v[2]))
    print("  IonQ shares, Oct 2026 vs Mar 2022  : %.2f x" % r["IonQ dilution x"])
    print("  2022 holder's remaining fraction   : %.0f%%" % (100 * r["IonQ 2022 holder's remaining fraction"]))

    g = calc.grover()
    print("\n[A.3 / A.11] Grover search of 10^12 items")
    print("  Classical time (one GPU)      : %.0f s" % g["classical_seconds"])
    print("  Quantum time (central)        : %.0f s (%.1f hours)" % (g["quantum_seconds"], g["quantum_seconds"] / 3600))
    print("  Time break-even, one GPU      : N =", sci(g["time_breakeven_N"]), "(%.1f years)" % g["time_breakeven_years_one_gpu"])
    print("  Time break-even, 1,000 GPUs   : N =", sci(g["time_breakeven_N_1000gpu"]), "(%.0f years)" % g["time_breakeven_years_1000gpu"])
    print("  Classical cost                :", money(g["classical_cost"]))
    for c in ("central", "generous"):
        print("  Quantum cost, %-9s       : %s; cost break-even N = %s (%.3g years of one GPU)" % (
            c, money(g["quantum_cost_" + c]), sci(g["cost_breakeven_N_" + c]), g["cost_breakeven_years_one_gpu_" + c]))

    a = calc.cost_per_answer()
    print("\n[7.2 / A.11] Cost per answer")
    for (name, case), v in a.items():
        val = " to ".join(money(x) for x in v) if isinstance(v, tuple) else money(v)
        print("  %-22s %-9s : %s" % (name, case, val))

    f = calc.affordability()
    print("\n[A.5] Affordability")
    print("  Profit needed to repay $100B at 10%  :", money(f["required_profit"]), "a year")
    print("  Revenue needed at 30% margin         :", money(f["revenue_needed_at_margin"]), "a year")
    print("  Central vendor revenue               :", " to ".join(money(x) for x in f["central_revenue"]))
    print("  Sensitivity (user value x vendor share):")
    for (u, s), v in sorted(f["grid"].items()):
        print("    user value %-7s share %3.0f%% : %s" % (money(u), 100 * s, money(v)))

    lo, hi = calc.machines_implied()
    print("\n[A.6] Machines implied by McKinsey's 2035 revenue : %.0f to %.0f" % (lo, hi))
    print("[A.7] IBM quantum signings as share of revenue  : %.2f%%" % (100 * calc.ibm_share()))
    m = calc.market_size()
    print("[A.8] Simulation software and AI market         : %s to %s" % (money(m[0]), money(m[1])))
    fr = calc.fridges()
    print("[A.9] Refrigerators for a million qubits         : %.0f to %.0f; %s to %s" % (
        fr["count"][0], fr["count"][1], money(fr["cost"][0]), money(fr["cost"][1])))

    rc = calc.runs_ceiling()
    print("\n[6.4] Ceiling on chemistry work a year, worldwide")
    print("  Central : %.0f to %.0f runs; %.0f to %.0f studies" % (rc["runs"] + rc["studies"]))
    print("  Generous: %.0f runs; %.0f to %.0f studies" % ((rc["generous_runs"],) + rc["generous_studies"]))

    j = calc.joint_chance()
    print("\n[8.2] Joint chance all seven conditions hold (author's judgments - replace them)")
    print("  Independent, central judgments : %.2f%%" % (100 * j["independent_central"]))
    print("  Independent, upper judgments   : %.2f%%" % (100 * j["independent_upper"]))
    print("  Hardware conditions together   : %.1f%% to %.1f%%" % tuple(100 * x for x in j["correlated"]))

    x = calc.crossovers()
    print("\n[7.4 / A.12] Crossovers in time and money")
    print("  Factoring money crossover (bits)  : central %d, generous %d" % (x["factoring_money_bits_central"], x["factoring_money_bits_generous"]))
    print("  Factoring time crossover (bits)   : %d vs 10^3 cores, %d vs 10^6 cores" % (x["factoring_time_bits_1000_cores"], x["factoring_time_bits_1e+06_cores"]))
    print("  Factoring classical wall (bits)   : %d (1 week on 10^6 cores)" % x["factoring_wall_bits"])
    print("  RSA-2048 classical core-years     :", sci(x["rsa2048_core_years"]), "; quantum cost", money(x["rsa2048_quantum_cost_central"]))
    print("  Grover time crossover N           : %s (1 GPU), %s (10^3), %s (10^6)" % (sci(x["grover_time_N_1_gpus"]), sci(x["grover_time_N_1000_gpus"]), sci(x["grover_time_N_1e+06_gpus"])))
    print("  Grover classical wall N           :", sci(x["grover_wall_N"]), "; quantum years there %.2g" % x["grover_quantum_years_at_wall"])
    print("  Amplitude estimation tightening   : time %s (1 GPU), money %s" % (sci(x["ae_time_tightening_1gpu"]), sci(x["ae_money_tightening"])))
    print("  FeMoco determinants               :", sci(x["femoco_determinants"]), "; times past exact record", sci(x["femoco_past_record"]))
    print("\n[7] Brute-force memory: 50 qubits = %s bytes (about 18 petabytes)" % sci(calc.state_vector_bytes(50)))
    print("\nDONE")


if __name__ == "__main__":
    main()

# Section 7 'Start at the edge' / A.13
e = calc.edge_costs()
print("\nCOST AT THE EDGE (one week on 10^6 GPUs or CPU cores): A, B central/generous, C = B/A")
print("  Classical cost A: GPUs $%.2g, CPU cores $%.2g" % (e["A_gpu"], e["A_cpu"]))
for k in ("search", "monte_carlo", "factoring", "chem_record", "chem_edge"):
    d = e[k]
    print("  %-12s B $%.2g / $%.2g   C %.2g / %.2g   time %.2g h / %.2g h" % (k, d["central"]["B"], d["generous"]["B"], d["central"]["C"], d["generous"]["C"], d["central"]["seconds"]/3600, d["generous"]["seconds"]/3600))

# Section 7 'The biggest machines, side by side' / A.13
b = calc.biggest_machines()
print("\nBIGGEST MACHINES: 10^6-GPU campus (build $%.2g, week $%.2g own / $%.2g-%.2g rent) vs 2,000-qubit quantum machine" % (b["fleet_capex"], b["fleet_week_own"], *b["fleet_week_rent"]))
for k in ("day", "week", "month"):
    d = b[k]
    print("  quantum %-5s $%.2g : search %.2g items (1 GPU %.2g s, $%.2g); pricing x%.0f (1 GPU %.2g s, $%.2g); key %.0f bits (%.0f qubits; classical %.2g core-yr); exact chem %.0f orbitals (fits classically: %s)" % (
        k, d["quantum_cost"], d["search_items"], d["search_one_gpu_s"], d["search_one_gpu_cost"], d["mc_tightening"], d["mc_one_gpu_s"], d["mc_one_gpu_cost"], d["factor_bits"], d["factor_logical_qubits"], d["factor_classical_core_years"], d["chem_orbitals"], d["chem_fits_biggest_machine"]))

# Sections 6.4, 6.5, 8.5 / A.14
c = calc.chem_crossover()
print("\nEXACT CHEMISTRY, SAME CALCULATION (central): crossover %.1f orbitals (generous %.1f)" % (c["crossover_central"], c["crossover_generous"]))
for r in c["rows"]:
    print("  m=%2d dets %.2g  classical %s  quantum $%.2g (%.0f h)" % (r["m"], r["determinants"], ("$%.2g" % r["classical"]) if r["classical"] else "impossible", r["quantum"], r["quantum_hours"]))
mk = calc.market_where_it_matters()
print("MARKET WHERE QUANTUM MATTERS: today $%.2g (range $%.2g-$%.2g); vendors on value $%.2g-$%.2g; machines %s" % (mk["today_central"], mk["today_low"], mk["today_high"], *mk["vendor_value"], {k: round(v, 1) for k, v in mk["machines"].items()}))
lc = calc.learning_curve(20)
print("LEARNING CURVE, 20 machines: %.1f doublings; cost x %.2f (20%%), x %.2f (15%%)" % (lc["doublings"], lc["rate_20"], lc["rate_15"]))
