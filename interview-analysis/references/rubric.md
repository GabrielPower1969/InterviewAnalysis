# Scoring Rubric — 8 Dimensions

Score each dimension **1–5** (halves allowed, e.g. 3.5). Every score must be
justified with at least one **timestamped verbatim quote** from the transcript.
Calibrate honestly — the whole point is improvement, so a report where
everything is 4/5 has failed.

## What the 1–5 scale means (general)

- **5 — Excellent.** Would stand out positively to a strong interviewer. Crisp,
  concrete, evidence-backed, well-structured.
- **4 — Good / above bar.** Solid, hire-signal, minor polish needed.
- **3 — At bar / passable.** Neither helps nor hurts much; the raw material is
  there but under-delivered.
- **2 — Below bar.** Actively costs signal; confusing, generic, or evasive.
- **1 — Poor.** A red flag for the role.

---

## 1. 技术匹配度 · Tech Match

Does the candidate's stack overlap the role, and can they go past name-dropping?

- Stack overlaps the JD (or reasonable role expectations): cloud, K8s, CI/CD,
  IaC, data pipelines, relevant languages/frameworks, domain (e.g. automotive).
- Can give **real project detail**, not just nouns — tool names, versions, key
  design decisions, tradeoffs. A named technology that survives 3 layers of
  follow-up is "real"; one that collapses into "I can't remember" is a gap.
- Responds to the interviewer's stated context (e.g. "we're migrating Jenkins →
  GitHub Actions", "we use Postgres") with something targeted.

Red flags: forgetting names of tools they claim to have used; shrinking their
contribution ("someone else implemented it"); answering "how would you generally"
when asked "what did you specifically do".

## 2. 技术深度与问题解决 · Depth & Problem Solving

Can they tell a complete **problem → investigation → root cause → solution →
prevention** chain?

- Gets concrete: probe config, service mesh, security groups, backup/restore,
  schema fields, metrics — not just "we did a migration".
- Surfaces a genuine **root-cause insight** ("the first step was wrong, so
  everything downstream was off").
- Willing to discuss **mistakes** and what changed in the process afterward.

Red flags: leading with mechanism instead of outcome so the interviewer has to
keep asking "so what was the value?"; no numbers anywhere; self-interrupting a
good story into incoherence.

## 3. 表达结构与故事性 · Structure & Narrative

Is each answer **answer-first (BLUF)** and shaped as
背景→挑战→行动→结果→反思 (Situation→Task→Action→Result→Reflection)?

- Opens with a one-sentence summary/headline, then details.
- Avoids meandering, repetition, and burying the main line.
- **Understands the question before answering** — huge signal. Repeatedly
  answering the wrong thing (and needing many rounds of clarification) is one of
  the most costly, most common, most fixable failures.

Red flags: answers that start with "um… hmm… there's a thing I'm thinking…";
run-on "and… and… and…" chains; the interviewer re-asking the same question 3+
times.

## 4. 业务结果与影响 · Impact

Do they connect technical work to business value, ideally quantified?

- States outcomes: cost saved, reliability up, latency down, delivery faster,
  revenue/GMV, adoption.
- **Quantifies**, even relatively ("cut a class of failures sharply", "migrated
  X services", "86.5h → 0.5h").
- Shows they know where their work sits in the business, not just the tech.

Red flags: impact stuck at "positive result"/"better than before"; and the
classic — strong quantified wins sitting *in their résumé* that they never once
say out loud. Surface those in the report's prepare-next-time section.

## 5. 协作与 Ownership · Collaboration & Ownership

- Cross-team / cross-timezone / with-developers stories.
- Proactive driver vs passive executor; owner of a meaningful project.
- "When it breaks I own it and coordinate the fix" attitude.

Red flags: language that dilutes their own role ("another guy did it", "I don't
do the detailed part") without a compensating "the part I drove was…". Honesty
about scope is fine, but they should reclaim the part they owned.

## 6. 自我认知与学习成长 · Self-awareness & Growth

- Knows their strengths/weaknesses and can state them without either bravado or
  self-erasure.
- Has a **proactive learning** story (new tech, tool, framework) with motive →
  method → result.
- Turns past mistakes/challenges into growth narratives.
- A candid post-interview self-reflection (if recorded) is strong meta-awareness
  — credit it and build the coaching on it.

Red flags: admitting "I'm not familiar with this" with no follow-up "but here's
how I'd get up to speed"; no growth story at all.

## 7. 动机与文化匹配 · Motivation & Fit

- Clearly expresses who they are, what they want, why *this* team/company.
- Aligns their values / working style with the company's culture (automation,
  cost-efficiency, AI tooling, mission).
- Asks **high-quality reverse questions** showing they care about succeeding
  here, not just salary/remote.

Red flags: generic "why this company"; not connecting to the company's actual
mission/values; only basic logistics questions at the end.

## 8. 语言与沟通 · Communication

- Clear, short sentences for complex ideas.
- Adjusts depth to the interviewer's background (neither over-flexing nor too
  shallow).
- Gives a one-line summary before a long story.
- For non-native speakers: judge **clarity and structure**, not accent. Heavy
  filler, stutters, and run-ons that impede understanding count against; the fix
  is pausing instead of filling and leading with a main-clause sentence. Note
  when fluency visibly improves on a well-prepared story — it proves the issue
  is retrieval-under-ambiguity, not language itself.

Anchor this dimension with the objective filler stats from `filler_stats.py`.

---

## Overall score

Compute a weighted average. Default weights (tune to the role — e.g. weight Tech
Match and Depth higher for a deep technical role, Communication and Fit higher
for a customer-facing / Solutions / PM role):

| Dimension | Default weight |
|---|---|
| Tech Match | 15% |
| Depth & Problem Solving | 15% |
| Structure & Narrative | 15% |
| Impact | 15% |
| Collaboration & Ownership | 10% |
| Self-awareness & Growth | 10% |
| Motivation & Fit | 10% |
| Communication | 10% |

Map the overall to a verdict tag:
- **≥4.2** Strong — clear advance.
- **3.5–4.1** Solid — likely advance, specific polish.
- **2.8–3.4** Borderline — has the material, under-delivered; coachable.
- **<2.8** Below bar — needs substantial work before the next loop.

The gauge in the template fills by `overall/5` of the circumference
(dasharray ≈ `overall/5 * 490`).

---

## Industry-perspective section (your own POV)

The user explicitly wants more than a rubric — add a section with your read on:

- **The role in the current market.** What is this archetype (Solutions/Forward-
  Deployed Engineer, SWE, Data, PM, SRE…) actually valued for right now, and how
  is AI reshaping it (e.g. when code's marginal cost drops, the scarce skills
  become rapid prototyping, translating tech→business value, and communicating
  to non-technical stakeholders).
- **Where this candidate sits.** Honestly place their profile in that landscape
  — what's timely about it, what the market is hungry for, and the single
  highest-leverage gap between them and strong offers (often packaging, not
  capability).
- **The evaluator's subtext.** Decode what the interviewer was *really* probing
  (e.g. "given an ambiguous problem, will they figure it out?", "can both
  customers and engineers understand them?", "does their work become business
  value?") so the candidate can aim future answers at it.

Be a knowledgeable, candid coach. Ground opinions in what actually happened in
the transcript.
