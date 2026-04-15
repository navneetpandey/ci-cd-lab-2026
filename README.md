# CI/CD with GitHub Actions — Hands-On Lab

> **Course**: CI/CD with GitHub Actions: Level Up Your Code Game!
> **Instructor**: Navneet K Pandey (Finn.no)
> **Date**: April 2026

---

## What You'll Build

You'll take a simple Python calculator app and progressively add automation — from running tests on every push to a full deployment pipeline.

```
Exercise 1          Exercise 2              Exercise 3
─────────          ──────────              ──────────

  push               push                    push
   │                  │                       │
   ▼                  ▼                       ▼
┌──────┐        ┌──────────┐          ┌──────────────┐
│ Test │        │ Test     │          │ Test         │
│      │        │ (3.10)   │          │ (3.11-3.13)  │
└──┬───┘        │ (3.11)   │          └──────┬───────┘
   │            │ (3.12)   │                 │
   ▼            │ (3.13)   │          ┌──────┴───────┐
  Done          └────┬─────┘          │ Lint         │
                     │                └──────┬───────┘
                ┌────┴─────┐                 │
                │ Lint     │          ┌──────┴───────┐
                └────┬─────┘          │ Build        │
                     │                │ (artifact)   │
                     ▼                └──────┬───────┘
                    Done                     │
                                      ┌──────┴───────┐
                                      │ Deploy       │
                                      │ (main only)  │
                                      └──────────────┘
```

---

## Prerequisites

- A GitHub account (free)
- A web browser (that's it — no local setup needed!)
- Basic command line knowledge

---

## Setup (5 minutes)

### Step 1: Fork this repository

1. Click the **Fork** button (top-right of this page)
2. Keep the default settings
3. Click **Create fork**

### Step 2: Verify the app works

Go to the **Actions** tab in your forked repo. It should be empty — we haven't added any workflows yet. That's about to change.

### Step 3: Explore the code

```
ci-cd-lab/
├── app/
│   ├── calculator.py    ← The app: add, subtract, multiply, divide
│   └── main.py          ← CLI entry point
├── tests/
│   └── test_calculator.py  ← 10 tests for the calculator
├── requirements.txt     ← Dependencies (pytest, ruff)
└── .github/
    └── workflows/       ← This is where YOUR workflows will go
```

---

## How GitHub Actions Works

When you push code, GitHub looks for YAML files in `.github/workflows/` and runs them.

```
                     YOUR REPOSITORY
                     ═══════════════
                           │
                     git push / PR
                           │
                           ▼
               ┌───────────────────────┐
               │  .github/workflows/   │
               │  ┌─────────────────┐  │
               │  │   ci.yml        │  │◄── GitHub reads this file
               │  └─────────────────┘  │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │   GitHub spins up     │
               │   a fresh Linux VM    │◄── Called a "Runner"
               │   (ubuntu-latest)     │
               └───────────┬───────────┘
                           │
                    Runs your steps:
                    1. Checkout code
                    2. Setup Python
                    3. Install deps
                    4. Run pytest
                           │
                    ┌──────┴──────┐
                    │             │
                 PASS ✓        FAIL ✗
               (green)        (red)
```

### Key Concepts

| Concept | What it is | Analogy |
|---------|-----------|---------|
| **Workflow** | A `.yml` file in `.github/workflows/` | A recipe |
| **Event** | What triggers it (`push`, `pull_request`) | "Start cooking when guests arrive" |
| **Job** | A group of steps that run on one machine | A course in the meal |
| **Step** | One command or action | A single instruction |
| **Runner** | The machine that runs your job | The kitchen |
| **Action** | A pre-built reusable step | A kitchen appliance |

### YAML Structure (annotated)

```yaml
name: CI                        # ← Name shown in the Actions tab
                                #
on: [push, pull_request]        # ← When to run (the trigger)
                                #
jobs:                           # ← What to do
  test:                         #   ← Job name (you choose this)
    runs-on: ubuntu-latest      #   ← Which runner (machine) to use
    steps:                      #   ← Ordered list of things to do
      - uses: actions/checkout@v6         # Use a pre-built action
      - run: echo "Hello, CI!"           # Run a shell command
```

---

## Exercise 1: Your First CI Pipeline (15 min)

**Goal**: Run tests automatically on every push.

### Step 1: Create the workflow file

In your forked repo on GitHub:

1. Click **Add file** → **Create new file**
2. Name it: `.github/workflows/ci.yml`
3. Paste this content:

```yaml
name: CI - Run Tests

on:
  push:
  pull_request:

jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest --verbose
```

4. Click **Commit changes** (commit directly to `main`)

### Step 2: Watch it run

1. Go to the **Actions** tab
2. You should see your workflow running (yellow spinner)
3. Click on it to see the live logs
4. Wait for the green checkmark ✓

```
What you'll see in the Actions tab:

┌─────────────────────────────────────────┐
│ CI - Run Tests                          │
│                                         │
│  ✓ Checkout code           2s           │
│  ✓ Set up Python           8s           │
│  ✓ Install dependencies    5s           │
│  ✓ Run tests              3s            │
│                                         │
│  Status: ✓ Success                      │
└─────────────────────────────────────────┘
```

### Step 3: Break it! (intentionally)

1. Edit `app/calculator.py`
2. Change the `add` function to return the wrong value:
   ```python
   def add(a: float, b: float) -> float:
       return a - b  # BUG! This should be a + b
   ```
3. Commit and push
4. Go to Actions → watch it **FAIL** (red ✗)
5. Click on the failure → read the error → **this is the CI value!**

### Step 4: Fix it

1. Change it back to `return a + b`
2. Commit and push
3. Watch it go green again ✓

**Congratulations!** You just experienced the core CI loop:
`code → push → automated test → feedback → fix → push → green`

---

## Exercise 2: Multi-Version Testing + Linting (15 min)

**Goal**: Test on 4 Python versions in parallel. Add code quality checks.

### What's new in this exercise

```
Exercise 1:           Exercise 2:
1 job, 1 version      2 jobs, 4 versions (running in parallel!)

┌──────┐              ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ Test │              │ 3.10 │ │ 3.11 │ │ 3.12 │ │ 3.13 │
│ 3.12 │              └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘
└──────┘                 └────┬───┘        └────┬───┘
                              │                 │
                         ┌────┴─────────────────┘
                         │
                    ┌────┴────┐
                    │  Lint   │
                    └─────────┘
```

### Step 1: Update your workflow

Replace `.github/workflows/ci.yml` with the content from `exercises/02-matrix-and-lint.yml`.

Key things to notice:

```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12", "3.13"]
```

This single block creates **4 parallel jobs** — one per version.

```yaml
- name: Cache pip packages
  uses: actions/cache@v5
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

This caches dependencies so subsequent runs are faster.

### Step 2: Watch the matrix in action

Go to Actions → you'll see 5 jobs (4 test + 1 lint) running in parallel.

### Step 3: Trigger a lint failure

1. Edit `app/calculator.py`
2. Add an unused import at the top:
   ```python
   import os  # unused — Ruff will catch this!
   ```
3. Commit and push
4. The **test jobs will pass** but the **lint job will fail**
5. Read the error — Ruff tells you exactly what's wrong

### Step 4: Fix and verify

Remove the unused import, push, watch everything go green.

---

## Exercise 3: Full CI/CD Pipeline (20 min)

**Goal**: Build a complete pipeline with test → lint → build → deploy.

### The pipeline visualized

```
                         git push to main
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │Test 3.11 │   │Test 3.12 │   │Test 3.13 │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
             └───────────────┼───────────────┘
                             │
                     ┌───────┴────────┐
                     ▼                ▼
               ┌──────────┐    ┌──────────┐
               │   Lint   │    │  (wait)  │
               └────┬─────┘    └──────────┘
                    │
                    ▼
              ALL PASSED?
               │       │
              YES      NO → Stop here (no deploy)
               │
               ▼
         ┌──────────┐
         │  Build   │  ← Creates an artifact
         └────┬─────┘
              │
              ▼
         On main branch?
          │         │
         YES        NO → Stop here
          │
          ▼
     ┌──────────┐
     │  Deploy  │  ← Downloads artifact, deploys
     └──────────┘
```

### Key concepts in this exercise

**`needs`** — Job dependencies:
```yaml
build:
  needs: [test, lint]   # Build only runs after test AND lint pass
deploy:
  needs: build          # Deploy only runs after build passes
```

**`if`** — Conditional execution:
```yaml
deploy:
  if: github.ref == 'refs/heads/main'  # Only deploy from main
```

**Artifacts** — Passing data between jobs:
```yaml
# In the build job:
- uses: actions/upload-artifact@v7    # Save output

# In the deploy job:
- uses: actions/download-artifact@v8  # Retrieve it
```

### Step 1: Create a feature branch

1. In GitHub, click the branch dropdown → type `my-feature` → **Create branch**
2. Replace `.github/workflows/ci.yml` with `exercises/03-full-pipeline.yml`
3. Commit to `my-feature`

### Step 2: Observe — no deploy on feature branch

Go to Actions. You'll see test + lint + build run, but **deploy is skipped**. That's the `if: github.ref == 'refs/heads/main'` guard.

### Step 3: Create a Pull Request

1. Go to **Pull requests** → **New pull request**
2. Compare `my-feature` → `main`
3. Create the PR
4. Watch the checks run on the PR — this is how teams gate merges

### Step 4: Merge and deploy

1. Once checks pass, click **Merge pull request**
2. Go to Actions → now you'll see the **deploy job runs!**
3. Click into the deploy job → read the simulated deployment output

**You've just built a real CI/CD pipeline!**

---

## How This Maps to the Real World

```
YOUR LAB                          REAL-WORLD EQUIVALENT
────────                          ─────────────────────
pytest --verbose          →       Run 1000s of unit + integration tests
ruff check .              →       ESLint, SonarQube, security scans
echo "Deploying..."       →       docker push + kubectl apply
build-info.txt artifact   →       Docker image, JAR file, npm package
if: github.ref main       →       Environment protection rules + approvals
```

At Finn.no, every code change goes through a pipeline like Exercise 3 — but with additional stages for security scanning, container building, and Kubernetes deployment.

---

## Bonus Challenges

If you finish early, try these:

### Challenge A: Add a badge to your README
Add this to the top of your README (replace `YOUR-USERNAME`):
```markdown
![CI](https://github.com/YOUR-USERNAME/ci-cd-lab/actions/workflows/ci.yml/badge.svg)
```

### Challenge B: Add a manual trigger
Add `workflow_dispatch` to your `on:` block so you can trigger the workflow manually:
```yaml
on:
  push:
  pull_request:
  workflow_dispatch:  # Adds a "Run workflow" button in the Actions tab
```

### Challenge C: Add a new function + test
1. Add a `power(base, exponent)` function to `calculator.py`
2. Add tests for it in `test_calculator.py`
3. Push and watch CI validate your work

---

## Quick Reference

### Common workflow triggers
```yaml
on:
  push:                          # Any push
  push:
    branches: [main]             # Push to main only
  pull_request:                  # Any PR
  schedule:
    - cron: "0 9 * * 1"         # Every Monday at 9 AM
  workflow_dispatch:             # Manual button
```

### Common actions
| Action | Purpose |
|--------|---------|
| `actions/checkout@v6` | Get your code |
| `actions/setup-python@v6` | Install Python |
| `actions/cache@v5` | Cache dependencies |
| `actions/upload-artifact@v7` | Save build outputs |
| `actions/download-artifact@v8` | Retrieve build outputs |

### Useful pytest flags
```bash
pytest --verbose        # Show each test name
pytest --tb=short       # Shorter error output
pytest -x               # Stop on first failure
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Workflow doesn't run | Check file is in `.github/workflows/` (exact path!) |
| YAML parse error | Check indentation — YAML uses spaces, not tabs |
| Tests pass locally but fail in CI | Check Python version matches |
| Lint fails | Read the Ruff error message — it tells you exactly what to fix |
