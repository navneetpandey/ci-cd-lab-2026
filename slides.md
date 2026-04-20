---
marp: true
theme: default
paginate: true
backgroundColor: #f8f9fa
color: #2d3436
style: |
  section {
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
    padding: 40px 60px;
    font-size: 28px;
  }
  h1 {
    color: #0984e3;
    font-weight: 700;
    border-bottom: 3px solid #74b9ff;
    padding-bottom: 8px;
  }
  h2 { color: #2d3436; font-weight: 600; }
  h3 { margin-top: 8px; margin-bottom: 4px; }
  code {
    background: #dfe6e9;
    color: #d63031;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  pre {
    background: #2d3436 !important;
    border-radius: 10px;
    padding: 16px !important;
  }
  pre code {
    background: transparent !important;
    color: #dfe6e9 !important;
    font-size: 0.72em;
    line-height: 1.4;
  }
  pre code .hljs-attr,
  pre code .hljs-keyword,
  pre code .hljs-selector-tag,
  pre code .hljs-title,
  pre code .hljs-section { color: #74b9ff !important; }
  pre code .hljs-string,
  pre code .hljs-number,
  pre code .hljs-literal { color: #55efc4 !important; }
  pre code .hljs-comment { color: #b2bec3 !important; }
  pre code .hljs-built_in,
  pre code .hljs-type,
  pre code .hljs-name { color: #fd79a8 !important; }
  pre code .hljs-symbol,
  pre code .hljs-bullet { color: #ffeaa7 !important; }
  table { font-size: 0.8em; margin: 0 auto; }
  th { background: #0984e3; color: white; padding: 6px 14px; }
  td { padding: 6px 14px; border-bottom: 1px solid #dfe6e9; }
  blockquote {
    border-left: 4px solid #0984e3;
    background: #e8f4fd;
    padding: 10px 18px;
    border-radius: 0 8px 8px 0;
    font-style: italic;
  }
  .hl {
    background: #e8f4fd;
    border-radius: 8px;
    padding: 12px 18px;
    border-left: 4px solid #0984e3;
  }
---

<!-- _backgroundColor: #0984e3 -->
<!-- _color: white -->
<!-- _paginate: false -->

<br>

# <!-- fit --> CI/CD with GitHub Actions

## Level Up Your Code Game!

<br>

Automating Your Software Development Workflow

**Navneet K Pandey** — Finn.no | April 2026

---

# The Problem

<div style="display:flex; gap:24px; margin-top:16px;">
<div style="flex:1; background:#ffeaa7; border-radius:10px; padding:20px;">

### Without CI/CD
- Push code Friday at 5 PM
- Monday: production is on fire
- "Who broke it?" — nobody knows
- Debugging at 3 AM
- Merge conflicts pile up

</div>
<div style="flex:1; background:#55efc4; border-radius:10px; padding:20px;">

### With CI/CD
- Push code anytime
- Tests catch bugs in **2 minutes**
- Git blame shows which commit
- Deploy with confidence
- Small merges = small conflicts

</div>
</div>

> Without CI/CD, bugs are discovered by **users**. With CI/CD, bugs are discovered by **robots**.

---

# CI — Continuous Integration

Merge small changes often. Let a robot test them every time.

<div style="display:flex; gap:30px; align-items:center;">
<div style="flex:1;">

```
     Write code
         │
         ▼
     git push
         │
         ▼
  ┌──────────────┐
  │  Automated   │── FAIL ──→ Fix it
  │    Tests     │            & push again
  └──────┬───────┘
         │
       PASS
         │
         ▼
   Merge to main
```

</div>
<div style="flex:1;">

### The key rule:

**Integrate small changes often.**
Don't hoard code for weeks.

### Requirements:
1. A shared repository (GitHub)
2. Frequent commits
3. **Automated tests** ← non-negotiable

</div>
</div>

---

# CD — Continuous Delivery

The autopilot flies the approach and aligns everything perfectly.

Then it says: **"Ready to land, Captain."**

The pilot decides when to touch down.

<div class="hl">

Code is always **ready** to deploy. A human presses the button.

</div>

```
No automation  ──→  CI  ──→  Continuous Delivery  ──→  Continuous Deployment
                                    ↑                          ↑
                              Most teams                 Netflix, GitHub
```

---

# CD — Continuous Deployment

The autopilot flies the approach, checks every parameter, and **lands the plane itself**.

The pilot monitors dashboards and can take over — but doesn't need to.

<div class="hl">

Code goes to production **automatically** after tests pass. No human gate.

</div>

```
No automation  ──→  CI  ──→  Continuous Delivery  ──→  Continuous Deployment
                                                              ↑
                                                     Requires: high test
                                                     confidence, monitoring,
                                                     rollback capability
```

---

# The Autopilot Analogy

Why Continuous Deployment requires **more** discipline, not less:

| Autopilot Landing | Continuous Deployment |
|---|---|
| Checks altitude, speed, alignment | Runs tests, lint, security scans |
| Lands automatically if all checks pass | Deploys automatically if all checks pass |
| Pilot monitors dashboards | Team monitors Grafana & alerts |
| Pilot can take manual control | Team can rollback |
| Requires extreme system trust | Requires extreme test confidence |
| Aborts if conditions are wrong | Build fails if tests fail |

<div class="hl">

It's not reckless — it requires **more testing**, **more monitoring**, and **better rollback** than manual deployment.

</div>

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> GitHub Actions 101

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.1em;">
Your new best friend
</p>

---

# What is GitHub Actions?

GitHub's built-in CI/CD tool. **Free** for public repos.

<div style="display:flex; gap:24px;">
<div style="flex:1;">

> A robot that reads your `.github/workflows/*.yml` files and runs them when something happens in your repo.

### The key insight:

GitHub gives you a **fresh virtual machine**, runs your commands, and **throws it away**. Every run starts clean.

</div>
<div style="flex:1;">

```
You push code
     │
     ▼
GitHub reads
.github/workflows/*.yml
     │
     ▼
Spins up fresh
Ubuntu VM (runner)
     │
     ▼
Runs your steps
     │
     ▼
Reports: ✓ or ✗
     │
     ▼
Destroys the VM
```

</div>
</div>

---

# Key Concepts

```
WORKFLOW   ← the .yml file itself
  │
  ├── EVENT    ← "when should this run?"  (push, pull_request, schedule)
  │
  └── JOBS     ← "what groups of work?"   (run in PARALLEL by default)
       │
       └── STEPS  ← "what commands?"      (run SEQUENTIALLY)
            │
            ├── uses:  ← pre-built action (someone else wrote it)
            └── run:   ← shell command (you write it)
```

<div style="display:flex; gap:16px; margin-top:12px;">
<div class="hl" style="flex:1;">

**Jobs** run in **parallel** unless you add `needs`

</div>
<div class="hl" style="flex:1;">

**Steps** within a job run **sequentially**

</div>
<div class="hl" style="flex:1;">

`uses` = import a library
`run` = write your own code

</div>
</div>

---

# YAML — The Language of Workflows

Two rules: **spaces not tabs** and **indentation = structure**

```yaml
name: CI                            # Name shown in the Actions tab

on: [push, pull_request]            # When to run (the trigger)

jobs:                               # What to do
  test:                             #   Job name (you choose this)
    runs-on: ubuntu-latest          #   Which runner (machine) to use
    steps:                          #   Ordered list of things to do
      - name: Checkout code
        uses: actions/checkout@v6           # Use a pre-built action
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: pip install -r requirements.txt  # Run a shell command
      - name: Run tests
        run: pytest --verbose                 # The moment of truth!
```

---

# What Can GitHub Actions Automate?

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px;">
<div style="background:white; border-radius:10px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Testing
Run your test suite on every push. Catch bugs before they reach users.

</div>
<div style="background:white; border-radius:10px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Code Quality
Linting, formatting, static analysis. Keep the codebase clean.

</div>
<div style="background:white; border-radius:10px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Build & Deploy
Build Docker images, deploy to cloud, publish packages.

</div>
<div style="background:white; border-radius:10px; padding:18px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Notifications
Send Slack messages, post PR comments, create issues.

</div>
</div>

<br>

**If you can do it in a terminal, GitHub Actions can automate it.**

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> Exercise 1

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.2em;">
Your First CI Pipeline — open your laptops!
</p>

---

# Exercise 1: Setup

<div style="display: flex; gap: 40px; align-items: flex-start;">
<div style="flex: 1;">

### Step 1: Fork the repository

**https://github.com/navneetpandey/ci-cd-lab-2026**

### Step 2: Create the workflow file

1. Click **Add file** → **Create new file**
2. Name it: `.github/workflows/ci.yml`
3. Paste the content from `exercises/01-basic-ci.yml`
4. Commit to `main`

### Step 3: Watch it run!

Go to the **Actions** tab. See the yellow spinner?

</div>
<div style="flex: 0 0 200px; text-align: center; padding-top: 10px;">

![QR w:200](qr-repo.png)

**Scan to open repo**

</div>
</div>

<div class="hl">

A machine just woke up in a data center somewhere **because you pushed code**.

</div>

---

# Exercise 1: Break It!

1. Edit `app/calculator.py` — change `add` to return the wrong value:

```python
def add(a: float, b: float) -> float:
    return a - b  # BUG! This should be a + b
```

2. Commit and push → go to **Actions** → watch it **FAIL**

```
FAILED tests/test_calculator.py::test_add_positive_numbers
  assert add(2, 3) == 5
  AssertionError: assert -1 == 5
```

3. **Fix it** → change back to `return a + b` → push → green ✓

<div class="hl">

**The CI loop:** push → fail → read error → fix → push → pass

</div>

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> Going Deeper

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.1em;">
Matrix, caching, and job dependencies
</p>

---

# Matrix Strategy — Test on Multiple Versions

One config block. **Four parallel jobs.**

<div style="display:flex; gap:24px;">
<div style="flex:1;">

```yaml
strategy:
  matrix:
    python-version:
      - "3.10"
      - "3.11"
      - "3.12"
      - "3.13"
```

</div>
<div style="flex:1.2;">

```
GitHub copies your job 4 times:

        ┌──────────┐
        │   push   │
        └────┬─────┘
   ┌────┬────┴───┬────┐
   ▼    ▼        ▼    ▼
 3.10  3.11    3.12  3.13
   ✓    ✓        ✗    ✓

 All run AT THE SAME TIME.
```

</div>
</div>

<div class="hl">

Real teams test across OS, database versions, and language versions — all in parallel from one config block.

</div>

---

# Caching — Speed Up Your Builds

<div style="display:flex; gap:24px; margin-top:16px;">
<div style="flex:1; text-align:center; background:#fab1a0; border-radius:10px; padding:20px;">

### Without Cache
Install deps: **45s** x4 runs
Total: **180s**

</div>
<div style="flex:1; text-align:center; background:#55efc4; border-radius:10px; padding:20px;">

### With Cache
First: **45s** / Then: **3s** x3
Total: **54s**

</div>
</div>

```yaml
- uses: actions/cache@v5
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

`hashFiles` = cache busts automatically when `requirements.txt` changes.

---

# Job Dependencies — `needs`

<div style="display:flex; gap:24px;">
<div style="flex:1; text-align:center;">

### Without `needs`

```
     push
      │
   ┌──┴──┐
   ▼     ▼
 Test  Deploy
  ✗      ✓

Deploy ran even
though tests failed!
```

**Broken code is live.**

</div>
<div style="flex:1; text-align:center;">

### With `needs`

```
     push
      │
      ▼
    Test
      │
    PASS?
   │     │
  YES    NO → stop
   │
   ▼
 Deploy ✓
```

**Deploy only if tests pass.**

</div>
</div>

```yaml
deploy:
  needs: [test, lint]    # Both must pass before deploy starts
```

---

# Branch Protection

**Feature branches get tested. Main branch gets deployed.**

<div style="display:flex; gap:24px; margin-top:16px;">
<div style="flex:1; background:white; border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Push to feature branch
- Test ✅ Lint ✅ Build ✅
- Deploy ⏭️ **SKIPPED**

*"Not main branch"*

</div>
<div style="flex:1; background:white; border-radius:10px; padding:20px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### Push to main
- Test ✅ Lint ✅ Build ✅
- Deploy ✅ **RUNS!**

*"Deploying now."*

</div>
</div>

```yaml
deploy:
  if: github.ref == 'refs/heads/main'
```

*The feature branch is the rehearsal. Main is the performance.*

---

# The Full Pipeline

```
                       git push to main
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
      ┌──────────┐   ┌──────────┐   ┌──────────┐
      │Test 3.11 │   │Test 3.12 │   │Test 3.13 │     ← parallel
      └────┬─────┘   └────┬─────┘   └────┬─────┘
           └───────────────┼───────────────┘
                           │
                     ┌─────┴─────┐
                     │   Lint    │             ← needs: [test]
                     └─────┬─────┘
                           │
                     ┌─────┴─────┐
                     │   Build   │             ← needs: [test, lint]
                     └─────┬─────┘
                           │
                     ┌─────┴─────┐
                     │  Deploy   │             ← needs: build + if: main
                     └───────────┘
```

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> Exercise 2 & 3

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.2em;">
Build the full pipeline — back to your laptops!
</p>

---

# Exercise 2: Matrix + Linting

1. Replace your workflow with `exercises/02-matrix-and-lint.yml`
2. Push → watch **5 jobs** run in parallel (4 test + 1 lint)
3. **Break the linter**: add `import os` to top of `calculator.py`
4. Watch tests **pass** but lint **fail** — read the error
5. Remove the unused import → push → all green

<div style="display:flex; gap:16px; margin-top:16px;">
<div class="hl" style="flex:1;">

**Tests answer:** "Does the code **work**?"

</div>
<div class="hl" style="flex:1;">

**Linting answers:** "Is the code **clean**?"

</div>
</div>

You need both.

---

# Exercise 3: Full CI/CD Pipeline

1. **Create a branch**: `my-feature` from `main`
2. Replace workflow with `exercises/03-full-pipeline.yml`
3. Commit to `my-feature` → deploy is **skipped**
4. **Open a Pull Request** to main → checks run on the PR
5. **Merge** → deploy **runs!**

```
Feature branch:                  After merge to main:

  Test  ✓                          Test  ✓
  Lint  ✓                          Lint  ✓
  Build ✓                          Build ✓
  Deploy ⏭️ SKIPPED                Deploy ✅ RUNS!
```

You've just built a real CI/CD pipeline!

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> Best Practices

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.1em;">
The rules that separate student projects from production
</p>

---

# Best Practices

<div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px; font-size:0.9em;">
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 1. Keep workflows focused
One workflow, one purpose.

</div>
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 2. Use specific triggers
Don't run on every push to every branch.

</div>
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 3. Cache dependencies
First run: 45s. Cached: 3s.

</div>
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 4. Don't commit secrets
Use **GitHub Secrets**. Bots scan every public push.

</div>
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 5. Use Marketplace actions
20,000+ pre-built actions available.

</div>
<div style="background:white; border-radius:10px; padding:16px; box-shadow:0 2px 8px rgba(0,0,0,0.06);">

### 6. Pin action versions
`@v6` for student projects. SHA for production.

</div>
</div>

---

# Security: Pin Your Actions

```yaml
# Student project — convenient:
uses: actions/checkout@v6

# Production — secure (exact commit SHA):
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v6.0.2
```

<div class="hl" style="margin-top:16px;">

### Real-world incident (2024)

The action `tj-actions/changed-files` was **compromised**. An attacker hijacked the `@v35` tag and injected malicious code. Every project using `@v35` ran the attacker's code. Projects pinned by SHA were **unaffected**.

</div>

*Student project: tags are fine. Production with credentials: always pin by SHA.*

---

<!-- _backgroundColor: #2d3436 -->
<!-- _color: #74b9ff -->

<br><br><br>

# <!-- fit --> Quiz Time!

<p style="color: rgba(255,255,255,0.6); text-align: center; font-size: 1.1em;">
Talk to your neighbor for 30 seconds, then answer together.
</p>

---

# Quiz — Question 1

### You're trying to be a CI purist. Which habit aligns?

<br>

a) Deploying code on Fridays, just before leaving for the weekend

b) Frequently integrating code, even if it's only 50% tested

c) Integrating code changes multiple times a day, with automated testing

d) Writing code for a month, then integrating it all at once

---

# Quiz — Answer 1

### c) Integrating multiple times a day, with automated testing

<div class="hl" style="margin-top:20px;">

**Why not b?** Frequently integrating *without tests* isn't CI — it's just frequent pushing. The **automated testing** part is non-negotiable.

</div>

---

# Quiz — Question 2

### Continuous Deployment is like...?

<br>

a) A carefully planned, once-a-year code release party

b) An autopilot that lands the plane after verifying every parameter

c) Sending a letter by snail mail

d) Keeping your code always ready to deploy, whenever you feel like it

---

# Quiz — Answer 2

### b) An autopilot that lands after verifying every parameter

<div class="hl" style="margin-top:20px;">

**Note:** Option d) is Continuous **Delivery**, not Deployment. Delivery = ready to go, human decides. Deployment = fully automated.

</div>

---

# Quiz — Question 3

### Your job needs a machine. Which setting picks the runner?

<br>

a) `steps`

b) `runs-on`

c) `uses`

d) `name`

---

# Quiz — Answer 3

### b) `runs-on`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest    # ← This picks the machine
```

Options: `ubuntu-latest`, `windows-latest`, `macos-latest`, or self-hosted runners.

---

# Quiz — Question 4

### The `needs` keyword means...?

<br>

a) "This job is super needy and requires constant attention"

b) "This job can only run if these other jobs are successful"

c) "This job needs more coffee"

d) "This job is optional"

---

# Quiz — Answer 4

### b) "This job can only run if these other jobs are successful"

```yaml
deploy:
  needs: [test, lint]    # Deploy waits for both to pass
```

---

# Quiz — Question 5

### Where do GitHub Actions workflows live?

<br>

a) In a secret, hidden folder

b) In a folder named `.github/workflows/`

c) In the cloud

d) In your dreams

---

# Quiz — Answer 5

### b) In `.github/workflows/`

You created files there three times today. This should be automatic by now.

---

# Quiz — Question 6: Find the Bug!

### What's wrong with this workflow?

```yaml
name: CI
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - name: Run tests
        run: pytest
```

*Take 60 seconds. Talk to your neighbor.*

---

# Quiz — Answer 6

### Missing `actions/checkout`!

The runner has Python but **no code**. Pytest fails with "no tests found."

```yaml
steps:
  - uses: actions/checkout@v6        # ← This was missing!
  - uses: actions/setup-python@v6
    with:
      python-version: "3.12"
  - run: pytest
```

<div class="hl">

The machine starts **empty**. Always checkout first. Most common beginner mistake.

</div>

---

<!-- _backgroundColor: #0984e3 -->
<!-- _color: white -->

<br>

# <!-- fit --> What You Learned Today

<div style="display:flex; gap:16px; margin-top:24px;">
<div style="background:rgba(255,255,255,0.15); border-radius:10px; padding:18px; flex:1;">

### Exercise 1
Basic CI
Tests on push
Red/green loop

</div>
<div style="background:rgba(255,255,255,0.15); border-radius:10px; padding:18px; flex:1;">

### Exercise 2
Matrix testing
Code linting
Caching

</div>
<div style="background:rgba(255,255,255,0.15); border-radius:10px; padding:18px; flex:1;">

### Exercise 3
Full pipeline
Artifacts
Branch protection

</div>
</div>

You went from **no automation** to a **full CI/CD pipeline** in 90 minutes.

---

<!-- _backgroundColor: #0984e3 -->
<!-- _color: white -->
<!-- _paginate: false -->

<br>

# <!-- fit --> Now Go Automate All the Things!

<div style="display: flex; align-items: center; gap: 30px; margin-top: 20px;">
<div style="flex: 1;">

**https://github.com/navneetpandey/ci-cd-lab-2026**

Questions? Reach out anytime.

</div>
<div style="flex: 0 0 180px; text-align: center;">

![QR w:180](qr-repo.png)

</div>
</div>
