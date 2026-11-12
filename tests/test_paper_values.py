"""Check that the code reproduces every number printed in the paper.

Run:  python -m unittest discover tests
"""
import unittest
from quantum_limits import calc


def close(a, b, rel=0.06):
    return abs(a - b) <= rel * abs(b)


class PaperValues(unittest.TestCase):
    def test_exchange_rates(self):
        e = calc.exchange_rates()
        self.assertTrue(close(e["gpu_cost_per_op"], 6.9e-19))
        self.assertTrue(close(e["today_ratio"], 4.6e11))
        self.assertTrue(close(e["central_ratio"], 2.3e15))
        self.assertTrue(close(e["generous_ratio"], 1.4e13))

    def test_revenue_per_dollar(self):
        r = calc.revenue_per_dollar()
        self.assertTrue(close(r["IonQ"][2], 0.088))
        self.assertTrue(close(r["IonQ excl. foundry"][2], 0.074))
        self.assertTrue(close(r["IonQ dilution x"], 2.35))
        self.assertTrue(close(r["Rigetti"][2], 0.066))
        self.assertTrue(close(r["D-Wave"][2], 0.056))
        self.assertTrue(close(r["Quantinuum"][2], 0.026))
        self.assertTrue(close(r["Quantum Computing Inc"][2], 0.012))
        names = ["IonQ", "Rigetti", "D-Wave", "Quantinuum", "Quantum Computing Inc"]
        self.assertTrue(close(sum(r[n][0] for n in names), 751.5))     # about $750M
        self.assertTrue(close(sum(r[n][1] for n in names), 12719.6))   # about $12.7B

    def test_grover(self):
        g = calc.grover()
        self.assertTrue(close(g["classical_seconds"], 100))
        self.assertTrue(close(g["quantum_seconds"], 78500))
        self.assertTrue(close(g["time_breakeven_N"], 1e18))
        self.assertTrue(close(g["time_breakeven_years_one_gpu"], 3.2))
        self.assertTrue(close(g["quantum_cost_central"], 1.2e6))
        self.assertTrue(close(g["quantum_cost_generous"], 7.4e3))
        self.assertTrue(close(g["cost_breakeven_N_central"], 3.2e26, rel=0.1))
        self.assertTrue(close(g["cost_breakeven_N_generous"], 1.1e22, rel=0.1))
        self.assertTrue(close(g["cost_breakeven_years_one_gpu_central"], 1e9, rel=0.1))
        self.assertTrue(close(g["cost_breakeven_years_one_gpu_generous"], 36000, rel=0.1))

    def test_cost_per_answer(self):
        a = calc.cost_per_answer()
        self.assertTrue(close(a[("Shor RSA-2048", "central")], 9.6e6))
        self.assertTrue(close(a[("Shor RSA-2048", "generous")], 0.57e6))
        self.assertTrue(close(a[("Chemistry run", "central")][0], 4.2e6))
        self.assertTrue(close(a[("Chemistry run", "central")][1], 5.5e6))
        self.assertTrue(close(a[("Chemistry run", "generous")][0], 0.25e6))
        self.assertTrue(close(a[("Amplitude estimation", "central")], 86e3))
        self.assertTrue(close(a[("Amplitude estimation", "generous")], 510))

    def test_other_appendix(self):
        f = calc.affordability()
        self.assertEqual(f["required_profit"], 10e9)
        self.assertTrue(close(f["revenue_needed_at_margin"], 33e9))
        lo, hi = calc.machines_implied()
        self.assertTrue(close(lo, 86) and close(hi, 142))
        self.assertTrue(close(calc.ibm_share(), 0.0018))
        m = calc.market_size()
        self.assertTrue(close(m[0], 4.6e9) and close(m[1], 7.0e9))
        fr = calc.fridges()
        self.assertTrue(close(fr["count"][0], 33) and close(fr["count"][1], 50))

    def test_runs_and_joint_chance(self):
        rc = calc.runs_ceiling()
        self.assertTrue(close(rc["runs"][0], 333) and close(rc["runs"][1], 2500))
        j = calc.joint_chance()
        self.assertTrue(close(j["independent_central"], 0.00225))
        self.assertTrue(close(j["independent_upper"], 0.0091))
        self.assertTrue(close(j["correlated"][0], 0.0094) and close(j["correlated"][1], 0.030))

    def test_crossovers(self):
        x = calc.crossovers()
        self.assertTrue(800 <= x["factoring_money_bits_central"] <= 820)
        self.assertTrue(700 <= x["factoring_money_bits_generous"] <= 720)
        self.assertTrue(540 <= x["factoring_time_bits_1000_cores"] <= 560)
        self.assertTrue(780 <= x["factoring_time_bits_1e+06_cores"] <= 800)
        self.assertTrue(890 <= x["factoring_wall_bits"] <= 910)
        self.assertTrue(close(x["rsa2048_core_years"], 6.3e14, rel=0.1))
        self.assertTrue(close(x["grover_wall_N"], 6e21, rel=0.1))
        self.assertTrue(close(x["grover_quantum_years_at_wall"], 190, rel=0.1))
        self.assertTrue(close(x["femoco_determinants"], 3.8e30, rel=0.1))

    def test_state_vector(self):
        self.assertTrue(close(calc.state_vector_bytes(50), 1.8e16))


if __name__ == "__main__":
    unittest.main()


class EdgeValues(unittest.TestCase):
    def test_edge(self):
        e = calc.edge_costs()
        self.assertTrue(close(e["A_gpu"], 4.2e8, rel=0.02))
        self.assertTrue(close(e["search"]["central"]["C"], 230, rel=0.05))
        self.assertTrue(close(e["monte_carlo"]["generous"]["C"], 0.95, rel=0.05))
        self.assertEqual(e["factoring"]["bits"], 899)
        self.assertTrue(close(e["factoring"]["central"]["C"], 0.11, rel=0.05))
        self.assertTrue(close(e["chem_record"]["central"]["C"], 11, rel=0.1))
        self.assertTrue(close(e["chem_edge"]["central"]["C"], 0.0018, rel=0.05))


class BiggestMachines(unittest.TestCase):
    def test_biggest(self):
        b = calc.biggest_machines()
        self.assertTrue(close(b["fleet_week_own"], 3.4e8, rel=0.05))
        self.assertTrue(close(b["week"]["quantum_cost"], 9.6e6, rel=0.05))
        self.assertTrue(close(b["month"]["search_one_gpu_cost"], 76, rel=0.05))
        self.assertTrue(close(b["month"]["mc_one_gpu_cost"], 160, rel=0.05))
        self.assertTrue(2200 < b["week"]["factor_bits"] < 2400)
        self.assertFalse(b["day"]["chem_fits_biggest_machine"])


class ChemistryChain(unittest.TestCase):
    def test_crossover(self):
        c = calc.chem_crossover()
        self.assertTrue(24.3 < c["crossover_central"] < 25.0)
        self.assertTrue(21.5 < c["crossover_generous"] < 23.0)
        r30 = [r for r in c["rows"] if r["m"] == 30][0]
        self.assertTrue(close(r30["classical"], 6.5e8, rel=0.05))
        self.assertTrue(close(r30["quantum"], 8.3e5, rel=0.05))

    def test_market_and_learning(self):
        mk = calc.market_where_it_matters()
        self.assertTrue(close(mk["today_central"], 1.2e8, rel=0.1))
        self.assertTrue(close(mk["machines"]["value_high"], 20, rel=0.01))
        lc = calc.learning_curve(20)
        self.assertTrue(close(lc["rate_20"], 0.38, rel=0.05))


class Record2025(unittest.TestCase):
    def test_new_record_narrows_window(self):
        r = calc.chem_crossover_2025_record()
        self.assertTrue(close(r["cost_per_det_ratio"], 430, rel=0.1))   # "about 400 times"
        self.assertTrue(close(r["crossover_central"], 29.5, rel=0.05))   # "about 30 orbitals"
        self.assertTrue(close(r["crossover_generous"], 27.3, rel=0.05))  # "about 27"
        self.assertTrue(close(r["quantum_advantage_at_30"], 1.8, rel=0.15))  # "about twice"

