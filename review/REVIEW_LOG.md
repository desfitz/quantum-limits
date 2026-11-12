# Review log for The Economic Limits of Quantum Computing (v26)

Cross-model verification log: every point raised by the AI reviewers (Gemini, Grok, ChatGPT, Microsoft Copilot), and how each was resolved against primary sources. Published with the code, as the paper's statement on AI use says.

## Cross-model verification log

First round run on 5 November 2026. Gemini and Grok reviewed draft v2; Grok was run by the author directly, because the browser extension used to drive the others cannot open grok.com. ChatGPT gave an initial review of draft v2 (C1-C5). Microsoft Copilot, which runs on OpenAI's models, was then run by the author on draft v9; it gave a general assessment rather than following the instruction, and it saw this log, so it was not independent of the other reviews. A second round ran on draft v25.1 on 11 November 2026, with the same instruction, in fresh sessions of Gemini, Grok and Copilot, each given the PDF; Claude drove all three through the author's browser. All three recommended publication as a working paper and found no fatal factual flaw. Their points are logged below as R2-G (Gemini), R2-K (Grok) and R2-C (Copilot), and the changes made are in draft v25.2.

### The round-2 reviewers' closing summaries

On 11 November 2026 draft v25.1 went for a second round of review to three AI systems from three companies: Google's Gemini Pro, xAI's Grok Expert and Microsoft's Copilot. Each was asked to check the facts, the references and the reasoning, and to give a verdict. This is AI review, not peer review. Their closing summaries are quoted below, word for word. Every point they raised, and what was done about it, is logged below (rows R2-G, R2-K and R2-C).

**Gemini Pro (Google):**

> "This is a highly rigorous, exceptionally well-argued piece of structural analysis that brings necessary empirical gravity to a field dominated by vendor optimism. I strongly recommend publication as a working paper. The step-by-step Fermi estimation provides exactly the objective framework that enterprise strategists and public policy planners need to evaluate systemic inefficiencies and capital allocation. Before final release, the only mandatory change is addressing the commercial viability of a government-monopsony market; treating code-breaking as a non-commercial dead-end ignores how defense contracting sustains major technology sectors. Integrating this nuance will fully bulletproof the paper's economic limits framework."

- **Required change, made.** A state buyer can keep a few vendors alive, as a defence business of a few machines (Sections 8.5 and 10; Appendix B, R2-G4).

**Grok Expert (xAI):**

> "I would recommend publication as a working paper. The piece is transparent, methodologically careful, and fills a genuine gap: a publicly checkable Fermi assessment of quantum computing's commercial economics that distinguishes value-to-users from revenue-to-vendors and that tests conclusions at the ends of ranges favourable to quantum. The AI-assisted research plus multi-model verification protocol is unusually rigorous for this literature, and the appendix arithmetic is reproducible in principle."

- **Required changes, made.** The chemistry comparison now uses the 2025 record exact calculation, and the seven assumptions behind the 1-3% odds are set out in a table readers can change (Sections 6.4 and 8.2; Appendix B, R2-K1 and R2-K4).

**Copilot (Microsoft):**

> "The draft is substantially stronger than most independently produced quantum-industry analyses because: it shows its arithmetic, it cites sources extensively, it distinguishes physics from economics, it makes falsifiable predictions, it explicitly logs previous review comments. The paper reads more like a transparent Fermi-analysis notebook than advocacy. That is a strength." ... "After this second-round review, I do not find a fatal factual flaw in the core thesis."

- **Required changes, made.** Model results are labelled as this paper's estimates, absolute wording is softened, and a new part tests the strongest case against the paper (Sections 6.4, 6.5, 7 and 10; Appendix B, R2-C4 and R2-C11).

**Reviewers**

| System | Company | Model and version | Date run | Items raised | Items found correct |
| --- | --- | --- | --- | --- | --- |
| ChatGPT | OpenAI | ChatGPT, Think mode (free plan) | 5 Nov 2026 | Verdict, four areas of concern, 3 facts | 2 corrections; 1 already made |
| Gemini | Google | Gemini 3.1 Pro (Gemini app, Pro plan) | 5 Nov 2026 | 9 | 2 corrections; 3 improvements in part |
| Grok | xAI | Grok app (version not captured; run by the author) | 5 Nov 2026 | 10 | 2 corrections; 5 improvements in full or part |
| Microsoft Copilot | Microsoft (OpenAI models) | Copilot in Edge, paid plan (model not captured; run by the author) | 5 Nov 2026 | 8 | 7 improvements in full or part; no fact or reference check |
| Gemini (round 2) | Google | Gemini Pro, consumer app; driven by Claude in Chrome | 11 Nov 2026 | 2 facts, 1 reference list, 5 improvements, verdict | 1 correction (Quantinuum IPO); 4 references added |
| Grok (round 2) | xAI | Grok Expert; driven by Claude in Chrome | 11 Nov 2026 | 2 facts, 1 reference list, 5 improvements, verdict | 2 corrections, including the chemistry record |
| Copilot (round 2) | Microsoft | Copilot (Auto); driven by Claude in Chrome | 11 Nov 2026 | 10 wording and fact points, 2 reference lists, 2 improvements, verdict | 1 correction (roadmap claim); wording of model outputs throughout |

**Log**

| # | Raised by | Part | Claim or section | What the system said | Primary source checked | Disposition | Change made or reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | Gemini | A fact | 3.2: CHIPS recipients | The list omits Diraq, which signed a $38M letter of intent | Commerce release²⁶; HPCwire²⁸ | Accepted | Diraq (up to $38M, silicon spin qubits) added to Section 3.2 |
| G2 | Gemini | A fact | 3.1: IonQ warrant gain of $896M | Figure not in the primary release; unsure of its source | IonQ Q3 2026 release¹, which states a non-cash warrant gain of $896.2M | Rejected | The figure is in the cited release |
| G3 | Gemini | B reference | Reference list | Reference 21 is missing from the numbering | Paper's own reference list | Rejected | Reference 21 is present in the paper; it was dropped only from the condensed text sent for review |
| G4 | Gemini | B reference | All 78 references | All exist, work and support their claims, checked "in categorical groups" | n/a | Noted | Not a usable check: no reference was checked individually, and classic papers without links were not flagged. Each reference will be opened individually before release |
| G5 | Gemini | B missing work | Introduction | The companion paper is named but not in the references | Zenodo record of the companion paper | Accepted | Added as reference⁷⁹ |
| G6 | Gemini | C improvement | Section 5 | Treats quantum and classical as rivals; the industry model is hybrid, with quantum as an accelerator inside GPU workflows | IonQ's NVIDIA Superion deployment¹; Oracle hosting Helios⁸ | Accepted in part | Hybrid paragraph added to Section 5. The cost per useful answer (Section 7) is unchanged by hybrid use |
| G7 | Gemini | C improvement | Section 7 | The $500M a year machine cost ignores silicon-spin designs claiming very low cost per qubit | Commerce release names Diraq's silicon-spin work²⁶; no published cost curve found yet | Accepted in part | Section 7 now states the assumption reflects superconducting and photonic machines |
| G8 | Gemini | C improvement | Section 8.1 | User value could justify public subsidy beyond vendor revenue | n/a (argument) | Accepted in part | One sentence added to Section 8.1 |
| G9 | Gemini | C improvement | Section 8.3 | Quantify the electricity and infrastructure needed to cool millions of qubits | Not yet sourced | Open | To be sourced before release |

| # | Raised by | Part | Claim or section | What the system said | Primary source checked | Disposition | Change made or reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K1 | Grok | A fact | Quantinuum 99.9995% | The figure is a distance-7 color-code memory result per correction round, not a gate or operation error | Independent analysis of the preprint⁸¹ | Accepted | Abstract, Section 4 text and table now say memory per round, and give the logical gate error, 7 in 100,000 |
| K2 | Grok | A fact | IBM's CHIPS award | IBM's foundry is a subsidiary, Anderon; the award was finalized in September | Quantum Computing Report⁸² | Accepted | Section 3.2 now names Anderon, the $1B IBM match and the Albany site |
| K3 | Grok | A fact | IonQ warrant gain $896M | Consistent with reporting, but confirm against the 10-Q | IonQ release¹ states $896.2M | Noted | Confirm against the 10-Q before release |
| K4 | Grok | A fact | Eleven headline figures | Confirmed; no claim found false | Same primary sources as the paper | Noted | No change |
| K5 | Grok | B reference | All references | Largely exist and support their claims; suggested missing work in general terms only | n/a | Noted | Not an item-by-item check; no specific missing papers named. Each reference will be opened individually before release |
| K6 | Grok | C improvement | Section 7 | Add a sensitivity table for gate rate and machine cost | Paper's own inputs | Accepted | Table added to Appendix A.4; conclusion holds across the range |
| K7 | Grok | C improvement | Section 6 | Accuracy on one high-value catalyst could be worth hundreds of millions to one user | n/a (argument) | Accepted | Sentence added to Section 6.3 |
| K8 | Grok | C improvement | Section 9 | Governments fund strategic capabilities that never pay commercially | n/a (argument) | Accepted in part | Paragraph added to Section 9 on when public funding lasts |
| K9 | Grok | C improvement | Section 3 | Separate quantum from foundry revenue; quantify dilution | IonQ release¹ | Accepted in part | Foundry-excluded ratio already in A.1; dilution measure open |
| K10 | Grok | C improvement | Section 10 | Make the "what would change" tests falsifiable | n/a | Accepted | First test now states the accuracy or cost gain and a one-year classical challenge |

| # | Raised by | Part | Claim or section | What the system said | Primary source checked | Disposition | Change made or reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | ChatGPT | A fact | Infleqtion Q2 2026 revenue | Revised from $12.6M to $13.5M, with prior-year timing adjusted; table is stale | Infleqtion release of 17 Aug 2026⁸³ | Accepted | Table now $13.5M, noting the restatement; FY26 guidance raised to about $45.1M |
| C2 | ChatGPT | A fact | Government funding $40.9B | Covers all quantum technology, not computing alone | The Quantum Insider tracker⁶⁴ | Accepted | Sections 3.2 and 8.2 now say all quantum technology; treated as an upper bound for computing |
| C3 | ChatGPT | A fact | CHIPS letters of intent | Diraq's letter omitted | Commerce announcements²⁶˒²⁸ | Already made | Diraq's $38M was added in v3 after Gemini's review (G1); ChatGPT reviewed draft v2 |

| # | Raised by | Part | Claim or section | What the system said | Primary source checked | Disposition | Change made or reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C4 | ChatGPT | Verdict | Whole paper | Would not recommend publication in its current form: problems with quantitative method, quantum-versus-classical costs, classification of algorithms and evidence for major conclusions | A general verdict, without detailed reasons | Accepted in part | Addressed through M1-M7 below and the Fermi bounds; draft v25.1 went back to Gemini, Grok and Copilot in round 2 (rows R2 below) |
| C5 | ChatGPT | A fact | Sections 4 and 5 | Company announcements treated as independent technical validation; "logical error" and "quantum advantage" worded more broadly than the results | Quantinuum preprint;⁸¹ Google release³⁸ | Accepted | Company-reported results now labelled as such in Section 4 |
| M1 | Copilot | C improvement | Section 7 | Customers buy answers, not operations: cost per operation overstates the case | n/a (argument; also raised by the author) | Accepted | Section 7 rewritten around cost per answer, with the per-operation price kept as the exchange rate a speed-up must beat, and a new algorithm-by-algorithm table (7.2) |
| M2 | Copilot | C improvement | Section 8 | Market may be underestimated: new applications, downstream value, platform effects | n/a | Accepted in part | Market sensitivity table added (A.5), running user value to $100 billion and vendor share to 30% |
| M3 | Copilot | C improvement | Sections 8 and 10 | "Two or three surviving builders" is too confident | n/a | Accepted | Recast as a scenario that follows from the assumptions |
| M4 | Copilot | C improvement | Whole paper | Add a strongest-counterarguments section | n/a | Accepted | Section 8.4, other issues considered |
| M5 | Copilot | C improvement | Appendix A | Give confidence ranges for major estimates | n/a | Accepted | Register (A.10) now gives a range and the end generous to quantum for every estimate |
| M6 | Copilot | C improvement | Section 10 | Separate technical from economic feasibility; tone down absolute conclusions | n/a | Accepted | Section 10 rewritten accordingly |
| M7 | Copilot | C improvement | Section 8 | Sensitivity analysis on market size, not just cost | n/a | Accepted | As M2 |
| M8 | Copilot | Assessment | Whole paper | Scores the paper 8.5 out of 10 overall and 9 out of 10 as a working paper | n/a | Noted | Copilot saw this log before reviewing |
| R2-G1 | Gemini | A fact | Quantinuum IPO, Sections 3.1 and 3.3 | Raised $1.68 billion gross (28 million shares at $60), not $1.71 billion | Quantinuum pricing and closing releases (3 and 6 Jun 2026); prospectus¹²⁶ | Accepted | Reverted to $1.68 billion; the v25 change was wrong. A.1, Figure 1 and the code updated |
| R2-G2 | Gemini | A fact | Colossus 2, Appendix A.13 | About 555,000 GPUs in total; no record of a further 440,000 announced | State of AI index¹¹⁶; Runtime Wire¹⁵⁸ | Rejected in part | Kept: the index records 440,000 announced; added xAI's aim to more than double its chip count by the end of 2026 |
| R2-G3 | Gemini | B reference | Missing literature | Should cite Beverland et al. 2022, Gidney and Ekera 2021, Preskill 2018 and Childs et al. 2018 | The four papers¹⁵⁹⁻¹⁶² | Accepted | Refs 159-162 added in Sections 7.1, 4, 5 and 6.4 |
| R2-G4 | Gemini | C improvement | Sections 8.5 and 9 | A government buyer can sustain listed vendors, as in defence (Palantir, Anduril); its one required change | Palantir Q3 2026 results¹⁶³ | Accepted | Added to 8.5 and Section 10: a state buyer can keep a few vendors alive, as a defence business of a few machines |
| R2-G5 | Gemini | C improvement | Section 8.4 | Quantum's value may lie in energy efficiency if classical computing hits an energy wall | Section 8.4 power estimate ᴱ¹⁴ | Rejected in part | Where quantum wins it also uses less energy, but energy is a small part of either machine's cost; no change |
| R2-G6 | Gemini | C improvement | Section 8.2 | The 1-3% odds assume today's algorithms | Section 10 | Accepted | Sentence added to 8.2 |
| R2-G7 | Gemini | C improvement | Section 7.1 | Model a cheaper silicon-spin machine separately | Diraq foundry result¹⁴⁹ | Accepted | Sentence added to 7.1: a tenth of the central cost lies inside the generous case |
| R2-G8 | Gemini | C improvement | Section 5 | Hybrid methods could shrink the quantum step | Best published run times⁵¹ | Accepted in part | Sentence added to Section 5 |
| R2-G9 | Gemini | Verdict | Whole paper | Strongly recommends publication as a working paper; one required change (R2-G4) | Not applicable | Accepted | Required change made |
| R2-K1 | Grok | A fact | Classical anchor, Sections 6.4 and A.14 | Superseded: a 2025 exact calculation reached about 10^15 determinants on 1,000 nodes in 34.5 hours, with lossless compression | Shayit et al., Nature Communications 2025¹⁶⁴ | Accepted | Record added to 6.4 with its effect: crossover about 30 orbitals, quantum about twice as cheap at 30. The table keeps the half-filled 2024 anchor, the end favourable to quantum; code chem\_crossover\_2025\_record. Conclusion unchanged |
| R2-K2 | Grok | A fact | Section 3.3 introduction | Says D-Wave and Rigetti figures are for Q2; the profiles use Q3 | Company Q3 releases¹⁵⁵˒¹⁵⁶ | Accepted | Corrected: only Infleqtion is at Q2 |
| R2-K3 | Grok | B reference | Missing literature | Cite the 2025 exact-CI record, distributed selected CI (arXiv:2503.10335), newer FeMoco-scale estimates, classical competitors for pricing and search | Ref 164 | Accepted in part | Ref 164 added; the others are noted for the next version |
| R2-K4 | Grok | C improvement | Section 8.2 | Tabulate the seven assumptions so readers can substitute their own | 8.2 table | Already made | Table already there; sentence added on how far any one judgment moves the result |
| R2-K5 | Grok | C improvement | Section 6.4 | Treat continuing classical progress as a first-class uncertainty | Ref 164 | Accepted | New bullet in 6.4: the newer record narrows the window |
| R2-K6 | Grok | C improvement | Section 8.5 | How many machines would give meaningful learning? | Learning rate ᴱ²² | Accepted | Added: about 9 machines halve the cost, 75 cut it by three quarters, 1,300 by 90% |
| R2-K7 | Grok | C improvement | Section 6.5 | Concrete high-value examples and historical analogues | Not applicable | Noted | For the next version |
| R2-K8 | Grok | Verdict | Whole paper | Recommends publication as a working paper; must fix K1 and K4 first | Not applicable | Accepted | Both done |
| R2-C1 | Copilot | A fact | Section 4 | "Commercially useful" is a judgment | Not applicable | Accepted | Now "of demonstrated commercial value" |
| R2-C2 | Copilot | A fact | Section 4, topological qubits | Separate device evidence from a demonstrated topological qubit | Ref 148 | Accepted | Reworded |
| R2-C3 | Copilot | A fact | Abstract and Section 4 | "Honestly factored 15" needs its definition | Refs 53, 114 | Accepted | Definition stated: Shor's algorithm without shortcuts that use the known answer |
| R2-C4 | Copilot | A fact | Sections 6.4, 6.5 and 7 | Model outputs (crossover, market, operation-cost ratio, "at any price") read as facts | Not applicable | Accepted | Labelled as this paper's estimates; "beyond any foreseeable machine" |
| R2-C5 | Copilot | A fact | Section 6.4 | The classical edge is likely understated | Ref 164 | Accepted | As R2-K1 |
| R2-C6 | Copilot | A fact | Section 6.4 | "Largest GPU campus in the world, about 10^6 GPUs" needs qualifying | Ref 116 | Accepted | Now "about twice the largest built so far" |
| R2-C7 | Copilot | A fact | Section 4 | "No public roadmap reaches that scale before the early 2030s" | Roadmap table¹⁵³ | Accepted | Corrected: IonQ's roadmap claims 2 million physical qubits in 2030; IBM's schedule gives 2033 |
| R2-C8 | Copilot | A fact | Abstract, Section 5 | IBM signings are bookings; "only two of ten" is a judgment | Ref 66 | Accepted | Wording changed |
| R2-C9 | Copilot | B reference | Refs 64, 66, 81, 112, 115, 153-154 | Verify carefully; they carry weight | v16 reference check | Already made | Checked in the v16 reference check and round 1; trackers described as independent secondary sources; no change |
| R2-C10 | Copilot | B reference | Missing literature | Aaronson on utility, Microsoft primary paper and a skeptic, neutral-atom fault-tolerance papers, neural quantum states, more resource estimates, economic history | Refs 148, 152 | Accepted in part | Majorana analysis and the Harvard fault-tolerance paper already cited; the rest noted for the next version |
| R2-C11 | Copilot | C improvement | Section 10 | Model the strongest opposing case | Sections 6.5, 7.4, 8.2 | Accepted | New "The strongest case against this paper": six cases tested |
| R2-C12 | Copilot | C improvement | Section 10 | What if the machine is 100 times cheaper? | Code | Accepted | Tested: crossover moves only from about 25 to about 23 orbitals; search still breaks even only past the one-week wall |
| R2-C13 | Copilot | Verdict | Whole paper | Recommends publication as a working paper; must relabel model outputs, soften absolute claims and model the opposing case first | Not applicable | Accepted | All three done |

