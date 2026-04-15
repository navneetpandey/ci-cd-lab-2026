# Updated Slide Deck Outline (2026)

> Recommended structure: **interleave theory with practice**.
> Don't front-load all theory — students retain more when they
> DO something right after learning it.

---

## Part 1: Why Should You Care? (10 min)

### Slide 1 — Title
CI/CD with GitHub Actions: Level Up Your Code Game!
Navneet K Pandey (Finn.no) — April 2026

### Slide 2 — The Problem (show, don't tell)
**Visual**: Two-panel comic
- Left: Developer pushes code Friday at 5 PM → production is on fire Monday
- Right: Developer pushes code → automated tests catch the bug in 2 minutes

"Without CI/CD, bugs are discovered by users.
With CI/CD, bugs are discovered by robots."

### Slide 3 — CI Explained
**Continuous Integration**: Merge code frequently, test automatically.

**Visual — the CI loop**:
```
  Write code
      │
      ▼
  git push
      │
      ▼
  Automated tests ──── FAIL → Fix → push again
      │
    PASS
      │
      ▼
  Merge to main
```

Key point: "Integrate small changes often. Don't hoard code for weeks."

### Slide 4 — CD Explained (two flavors)
**Visual — the spectrum**:
```
Manual          Continuous         Continuous
deploy          Delivery           Deployment
  │                │                   │
  ▼                ▼                   ▼
Human pushes    Human approves     Fully automated
a button        → auto deploys     after tests pass
```

- **Delivery** = always READY to deploy (human decides when)
- **Deployment** = automatically deploys after tests pass (no human)

Most teams start with Delivery and graduate to Deployment.

### Slide 5 — Why Bother? (concrete benefits)
| Without CI/CD | With CI/CD |
|---------------|-----------|
| "It works on my machine" | Works on every machine (the runner proves it) |
| Bugs found by users | Bugs found in 2 minutes by pytest |
| "Who broke main?" | Git blame + CI tells you exactly which commit |
| Deploy anxiety | Deploy confidence |
| Merge conflicts pile up | Small, frequent merges = small conflicts |

---

## Part 2: GitHub Actions 101 (10 min)

### Slide 6 — What is GitHub Actions?
GitHub's built-in CI/CD tool. Free for public repos.

"A robot that reads your `.github/workflows/*.yml` files
and runs them when something happens in your repo."

### Slide 7 — Key Concepts (visual hierarchy)
**Visual — the nesting**:
```
Repository
 └── .github/workflows/
      └── ci.yml                 ← WORKFLOW (the file)
           │
           ├── on: push          ← EVENT (the trigger)
           │
           └── jobs:
                └── test:        ← JOB (group of steps)
                     │
                     ├── runs-on: ubuntu-latest  ← RUNNER
                     │
                     └── steps:
                          ├── uses: actions/checkout@v4  ← ACTION
                          └── run: pytest                ← COMMAND
```

### Slide 8 — YAML: The Language of Workflows
Show annotated YAML (the one from the lab README).
Highlight: "Spaces, not tabs. Indentation matters."

### Slide 9 — What Can It Automate?
Grid of icons/cards:
- Run tests
- Check code style
- Build Docker images
- Deploy to production
- Security scanning
- Publish packages
- Send notifications
- Anything you can script!

---

## Part 3: Hands-On Exercise 1 (15 min)

### Slide 10 — LIVE EXERCISE: Your First CI Pipeline

"Open your laptop. Fork the repo. Let's do this together."

Show the QR code / link to the lab repo.

Walk through Exercise 1 from the README:
1. Fork → Create workflow → Push → Watch it run
2. Break the code → Watch it fail → Fix it → Watch it pass

**This is the most important moment in the course.**
Students need to see the red → green loop in their own repo.

---

## Part 4: Going Deeper (10 min)

### Slide 11 — Matrix Strategy
**Visual — parallelism**:
```
One workflow file creates FOUR parallel jobs:

strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12", "3.13"]

          ┌───────────┐
          │   push    │
          └─────┬─────┘
       ┌────┬───┴───┬────┐
       ▼    ▼       ▼    ▼
     3.10  3.11   3.12  3.13    ← All run at the same time!
       │    │       │    │
       ▼    ▼       ▼    ▼
      ✓    ✓       ✗    ✓      ← Python 3.12 found a bug!
```

"One line of YAML. Four parallel environments. Zero extra cost."

### Slide 12 — Caching (new slide)
**Visual — before vs after**:
```
Without cache:              With cache:
Install deps: 45s           Install deps: 3s (cached!)
Total time: 90s             Total time: 48s
```

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

"The `hashFiles` trick: cache busts automatically when requirements.txt changes."

### Slide 13 — Job Dependencies (needs)
**Visual — the pipeline flow**:
```
Without `needs`:             With `needs`:
(all jobs run at once)       (jobs run in order)

┌──────┐ ┌──────┐ ┌──────┐  ┌──────┐
│ Test │ │ Lint │ │Deploy│  │ Test │──┐
└──────┘ └──────┘ └──────┘  └──────┘  │
                              ┌──────┐│
  Deploy runs even if         │ Lint │─┤
  tests fail!                 └──────┘ │
                              ┌────────┴┐
                              │  Build  │
                              └────┬────┘
                              ┌────┴────┐
                              │ Deploy  │
                              └─────────┘
                              Deploy only runs
                              if everything passes
```

### Slide 14 — Branch Protection
**Visual — the gate**:
```
Feature branch:              Main branch:
─────────────                ────────────
  Test ✓                       Test ✓
  Lint ✓                       Lint ✓
  Build ✓                      Build ✓
  Deploy: SKIPPED              Deploy: ✓ RUNS!

  if: github.ref == 'refs/heads/main'
```

"Feature branches get tested. Main branch gets deployed."

---

## Part 5: Hands-On Exercise 2 + 3 (25 min)

### Slide 15 — LIVE EXERCISE: Matrix + Linting
Walk through Exercise 2:
- Add matrix, watch 4 jobs spawn
- Add unused import, watch lint fail
- Fix, watch it pass

### Slide 16 — LIVE EXERCISE: Full Pipeline
Walk through Exercise 3:
- Create feature branch
- Open PR — observe no deploy
- Merge — observe deploy runs

---

## Part 6: Best Practices & Wrap-Up (10 min)

### Slide 17 — Best Practices
1. **Keep workflows focused** — one workflow, one purpose
2. **Use specific triggers** — don't run on every push to every branch
3. **Cache dependencies** — saves minutes per run
4. **Pin action versions** — `@v4` for convenience, SHA for security
5. **Don't commit secrets** — use GitHub Secrets (Settings → Secrets)
6. **Use Marketplace actions** — don't reinvent the wheel

### Slide 18 — Security: Pin Your Actions (new slide)
```yaml
# Convenient (tag can be hijacked):
uses: actions/checkout@v4

# Secure (exact commit SHA):
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
```

"In a student project: tags are fine.
In production: always pin by SHA."

### Slide 19 — The Marketplace
GitHub Actions Marketplace = pre-built actions for everything.
20,000+ actions. Search at github.com/marketplace?type=actions

### Slide 20 — What You Learned Today
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Exercise 1  │     │  Exercise 2  │     │  Exercise 3  │
│              │     │              │     │              │
│  Basic CI    │ ──▶ │  Matrix +    │ ──▶ │  Full CI/CD  │
│  (test)      │     │  Linting     │     │  Pipeline    │
└──────────────┘     └──────────────┘     └──────────────┘

You went from "no automation" to "full pipeline" in 1 hour.
```

---

## Part 7: Quiz (10 min)

### Slide 21-28 — Quiz questions
Keep your existing quiz (slides 18-31), but consider adding:

**NEW practical quiz question**:
```
"What's wrong with this workflow?"

name: CI
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pytest
```

Answer: Missing `actions/checkout` — the code isn't on the runner yet!

---

## Timing Guide

| Part | Duration | Type |
|------|----------|------|
| 1. Why CI/CD? | 10 min | Theory |
| 2. GitHub Actions 101 | 10 min | Theory |
| 3. Exercise 1 | 15 min | Hands-on |
| 4. Going Deeper | 10 min | Theory |
| 5. Exercise 2 + 3 | 25 min | Hands-on |
| 6. Best Practices | 10 min | Theory |
| 7. Quiz | 10 min | Interactive |
| **Total** | **~90 min** | |

Theory and practice are interleaved so students never sit
through more than 10 minutes of slides without doing something.
