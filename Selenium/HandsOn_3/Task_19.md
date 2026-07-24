# Task 19 — Automation ROI Calculation

**Definition:** Test automation ROI measures whether the time invested in building and
maintaining an automated test is recovered through time saved across repeated executions,
compared to running the same test manually every time.

**Given:**
- Automating the test: 4 hours (240 minutes) one-time cost.
- Manual execution: 30 minutes per run.
- 20% maintenance overhead per run **after the 10th run**.

**Calculation (break-even without maintenance overhead):**
```
runs_to_break_even = automation_cost / manual_cost_per_run
                    = 240 minutes / 30 minutes
                    = 8 runs
```
So automation pays for itself after **8 runs**, before the 10th-run maintenance overhead
kicks in — meaning the investment is already recovered before overhead applies.

**Accounting for 20% maintenance overhead after run 10:**
From run 11 onward, each automated run effectively costs `30 min * 1.20 = 36 min`
"worth" of upkeep-adjusted value (i.e., the automated run still executes near-instantly,
but 20% of a manual-run-equivalent of engineering time is spent per run on maintenance).
Even with this overhead, since automated execution itself takes minutes rather than 30,
the cumulative time saved after run 8 continues to grow every run thereafter — the
20% maintenance tax reduces the *rate* of savings after run 10 but does not erase the
break-even already achieved at run 8.
