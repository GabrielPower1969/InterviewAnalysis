---
name: interview-analysis
description: >-
  Analyze a recorded job-interview transcript (usually an .srt / .vtt with
  timestamps, but plain text works too) and produce a polished, self-contained
  HTML debrief report that scores the candidate across 8 dimensions, counts
  filler/disfluency words, builds a timeline of key moments, adds an industry
  perspective, and gives concrete "prepare next time / say next time" advice.
  Use this WHENEVER the user shares an interview recording, transcript, SRT/VTT
  file, or asks to review/score/评分/复盘/分析 an interview — even if they don't
  say the word "report". If they also attach a JD (job description) or résumé,
  fold those in for a tailored fit analysis; if they don't, still produce the
  full report. The candidate is the person being interviewed and is the subject
  of the scoring (not the interviewer). Reports are written in the user's own
  language (default Chinese) with verbatim English quotes from the transcript.
---

# Interview Analysis & Debrief Report

Turn a raw interview recording (transcript) into an actionable coaching report.
The user records their own interviews, exports a transcript (usually `.srt` with
timestamps and lots of filler words and messy phrasing), and wants a rigorous,
honest, multi-dimensional analysis delivered as a single HTML file with a
convenient index so they can jump to any section: what was good, what was weak,
what to fix, and how to prepare next time.

## Inputs

- **CV / résumé — REQUIRED.** Often a PDF. It anchors the "Tech Match" scoring
  and, crucially, the prepare-next-time story bank and quantified-wins table
  (surface strong numbers the candidate failed to say out loud). If the user
  didn't attach one, ask for it before generating the report.
- **Interview record — REQUIRED, one of two forms:**
  - a **transcript**: `.srt` / `.vtt` (timestamps let you cite moments like
    `17:13`) or plain `.txt`; **or**
  - an **audio/video file** (`.mp3` / `.m4a` / `.wav` / `.mp4` …). Transcribe it
    locally first — prefer `whisper` (or `whisper.cpp` / `ffmpeg` + whisper) if
    installed, outputting `.srt` so you keep timestamps; if no local
    transcription tool is available, tell the user and ask for a transcript
    export instead. Never upload the media to any external service.
- **JD (job description) — optional but STRONGLY recommended.** With a JD,
  tailor "Tech Match" and "Motivation & Fit" to the actual role; without it,
  still produce the full report scored against reasonable expectations for the
  role you can infer, and note the limitation in the footer.
- The transcript may be **bilingual** or contain a duplicated translation block
  (e.g. English interview followed by a Chinese machine translation). Analyze
  the **original spoken language** portion; ignore the duplicated translation
  except to disambiguate a garbled line.

## Privacy (this skill is offline-first)

Everything runs locally: reading files, filler stats, report generation. Do not
send the CV, JD, transcript, or media to any external service or URL. The
generated report is a local HTML file the user may choose to share themselves.
Do not embed personal contact details (phone, email, address) from the CV into
the report — use the candidate's name only.

## Workflow

1. **Read everything first.** Read the full transcript (chunk large files with
   `offset`/`limit` — SRTs are big). Read the JD and résumé if provided. Large
   files may be truncated; keep reading until you have the whole interview,
   including the candidate's own post-interview self-reflection if recorded (it
   is gold for the Self-awareness dimension).

2. **Identify who is who.** Figure out which speaker is the **candidate** (the
   user / interviewee — the one being scored) and which is the **interviewer**.
   Note the role, company, and interview type (screen / behavioral / technical /
   system design / final).

3. **Run the filler/disfluency stats.** Use `scripts/filler_stats.py` to get
   objective counts (um, uh, hmm, "you know", "like", stutters like "the the" /
   "I I", run-on "and"-starts). These numbers anchor the Communication section
   and give the user a measurable target. See "Filler stats" below.

4. **Score the 8 dimensions (1–5 each).** Read `references/rubric.md` for the
   full rubric and what each score means. Be honest and specific — a report that
   rates everything 4/5 is useless. Every claim should be backed by a
   **timestamped verbatim quote** from the transcript. Compute a weighted
   overall score (see rubric).

5. **Add your own industry perspective.** The user explicitly wants more than a
   scorecard — they want your view on what this career path (e.g. Solutions
   Engineer, SWE, Data, PM) looks like in the current tech market, where the
   role is heading (esp. the impact of AI), and how the candidate's profile sits
   within it. Be a knowledgeable coach, not a rubric robot.

6. **Generate the HTML report** from `assets/report_template.html`. It is a
   self-contained (no external assets), dark-themed, responsive file with a
   sticky table-of-contents index. Fill in every section. See "Report structure"
   below for the required sections.

7. **Wire up audio sync when you have the media file** (see below). Skip when
   the user only supplied a transcript.

8. **Save & deliver.** Save next to the transcript with a descriptive name:
   `面试分析报告_<Company>_<Role>_<YYYY-MM-DD>.html` (or English equivalent).
   When audio sync is on, deliver a **folder** holding all three files —
   the media, the transcript, and the report — because the player uses a
   relative path. Then surface it to the user (open in the browser pane / send
   the file).

## 🎧 Audio sync + captions (when a media file is available)

Reviewing a debrief is far more useful when the user can hear the moment being
critiqued, so whenever the interview audio/video exists, ship the report wired
to it. The template already carries the whole mechanism; you supply three things:

1. **Play buttons.** Render every timestamp in the report as
   `<button class="pb" data-t="518">08:38</button>` — `data-t` is the position
   in **seconds**. Clicking seeks the player and starts playback. Do this for
   timeline entries, segment ranges, quotes, and any timestamp cited in the
   dimension write-ups; that's what makes the report navigable by ear.
2. **The caption track.** Run
   `python3 scripts/srt_to_cues.py <transcript.srt> --stats` and paste the JSON
   into the `{{CUES_JSON}}` placeholder. It is embedded inline rather than
   fetched because browsers block `fetch()` on `file://`, and users open these
   reports by double-clicking. A toggle in the player bar turns the live
   captions on/off and remembers the choice.
3. **`{{AUDIO_FILENAME}}`** — the media file's name, referenced relatively, so
   keep the report in the same folder as the media.

Captions render in the classic subtitle style — **yellow fill with a black
outline** (外黑里黄), at a size meant to be read at a glance while listening.
That styling is what keeps them legible over either theme, so leave it alone
unless the user asks otherwise.

Copy the media and transcript next to the report so the folder is
self-contained and shareable as a unit. If there is no media file, delete the
audio-sync block from the template and render timestamps as plain text.

## Report structure (required sections, in this order)

Keep the sticky index in sync with these anchors. Each dimension gets its own
navigable section.

0. **总览与结论 / Overview** — candidate, role, company, date, duration; an
   overall score gauge; a 3-bullet TL;DR verdict (strongest moment, most costly
   moment, the one key theme); a row of stat tiles (overall score, total filler
   count, and 1–2 other punchy stats).
1. **八维评分卡 / Scorecard** — all 8 dimensions as labeled score bars, color-
   coded (green ≥3.5, yellow 3.0, red ≤2.5), plus a one-line pattern read.
2. **逐维度详评 / Per-dimension deep dives (×8)** — each with: score + a
   達標/合格/待提升 badge, a two-column "✅ 做得好 / ⚠️ 掉分点" split, at least one
   timestamped verbatim quote, and a highlighted **"下次这样修 / Fix next time"**
   box with a concrete, trainable action.
3. **吞吐词 / Fluency analysis** — the objective filler counts as stat tiles, and
   2–3 quantified targets (e.g. "cut um/uh from ~7/min to ≤3/min").
4. **时间线速览 / Timeline** — a vertical timeline of ~10 key moments,
   color-dotted good / neutral / bad, each with a timestamp and one-line note.
   Include the candidate's post-interview self-reflection if present.
5. **逐段精读 / Segment-by-segment (REQUIRED, centerpiece)** — this is what the
   user reviews while re-listening to the audio, so it must cover the **WHOLE
   interview end-to-end**, broken into every meaningful Q&A / topic unit
   (typically 15–20 segments for a 40-min interview — do NOT collapse to a
   handful). **Also analyze the back-and-forth exchanges** (clarification loops,
   interviewer interjections, follow-up probes), not just the main answers —
   those loops are where a lot of signal is won or lost. Each segment gets a
   prominent **timestamp range** (left rail so they can scrub to it), a topic
   title with a good/neutral/bad tag, and these labeled lines:
   - **面试官原问 (seg-q):** quote/reconstruct the interviewer's actual question
     so the user instantly recalls what was asked. If the transcript garbled it
     (ASR noise), reconstruct a clean version and mark it 复原. For an exchange,
     show the key back-and-forth turns.
   - **我的回答·重点 (seg-a):** the candidate's ACTUAL answer, summarized to its
     key points **with a short verbatim snippet** — so the user can recall what
     they said without replaying. This pairs with 面试官原问 to reconstruct the
     moment from memory.
   - **问题在哪 (seg-prob):** the specific problem (skip/soften for good segments).
   - **下次怎么提高 (seg-fix):** the concrete fix.
   - **🎯 60秒范例回答 (seg-model, REQUIRED on every heavy-loss or high-stakes
     segment):** a ready-to-rehearse model answer — "if a top candidate answered
     this, they'd say: …" — written in the **language the candidate will actually
     speak** (usually English for an English interview), ~110–150 words (≈60s),
     structured answer-first. This is the single most useful thing for the user:
     a script they can practice. Put it on the weakest/most-important 3–5
     segments, not on trivially fine ones.

   Use the `.seg` component and the `.seg-model` box in the template.
6. **行业视角 / Industry perspective** — your POV on the role, the market, and
   where the candidate sits (the section that makes this more than a rubric).
7. **下次「准备」清单 / Prepare-next-time** — a pre-interview checklist: a story
   bank (5 reusable STAR-L stories drawn from THEIR real material), a "quantified
   wins" table pulled from their résumé/achievements, and company homework.
8. **下次「临场」战术 / Say-next-time tactics** — in-the-moment behavior fixes
   (clarify ambiguous questions, answer-first/BLUF, tie back to business, pause
   instead of filler, reclaim ownership).
9. **反问银行 / Reverse-question bank** — 5–6 high-signal questions tailored to
   the specific company/role, each with a one-line "why this lands".
10. **一句话总结 / One-line verdict** — a callout + the top-3 highest-priority
   actions as a checklist.

Keep the sticky TOC numbering in sync when you add the segment section (it
shifts the later section indices by one).

## Filler stats

Run from the skill directory:

```bash
python3 scripts/filler_stats.py "/path/to/transcript.srt"
```

It prints a JSON blob with counts for `um`, `uh`, `hmm`, `you know`, `like`,
`yeah`, stutters (`the the`, `I I`, etc.), `and`-line-starts, an estimated
spoken duration from the timestamps, and a per-minute filler density. Use these
verbatim in the Fluency section. Note honestly that counts cover the whole
transcript (both speakers) unless a speaker split is available — the trend is
reliable even if the absolute is slightly high. If the script can't run, count a
representative sample yourself and say it's an estimate.

## Principles

- **Be honest and specific, not flattering.** The user wants to improve. Name
  the weakest dimensions plainly and show the exact moments (with timestamps)
  where signal was lost. Also name genuine strengths — over-criticism is as
  useless as over-praise.
- **Quote, don't paraphrase.** Anchor every judgment in a real line from the
  transcript with its timestamp. This is what makes the report credible.
- **Mine their own material for the fixes.** The best "prepare next time" story
  bank and "quantified wins" table come from the candidate's own résumé and the
  things they half-said in the interview — surface the strong numbers they
  *failed* to mention. Don't invent achievements.
- **Write in the user's language** (default Chinese) with English quotes kept
  verbatim. Match how the user talks to you.
- **One self-contained HTML file.** No external CSS/JS/fonts/images — everything
  inline so it opens anywhere and can be shared. Use the provided template.
- **Dark by default, with a ☀️/🌙 toggle.** The template ships both palettes as
  CSS variables (`:root` dark, `:root[data-theme="light"]` light) and a
  top-right toggle whose choice persists. Dark is the default because that is
  how the user reads these. When you add new colours, define them as variables
  and give them a light-theme value too — a hardcoded dark hex will break the
  day mode.
- **Tailor when you can, deliver regardless.** JD present → tailored fit. JD
  absent → still ship the full report.

## Files

- `references/rubric.md` — the full 8-dimension scoring rubric, what each 1–5
  level means, scoring weights, and guidance for the industry-perspective
  section. Read this before scoring.
- `assets/report_template.html` — the self-contained HTML skeleton (all CSS
  included) with `{{PLACEHOLDER}}` markers and reusable component snippets
  (score bar, dimension card, timeline event, stat tile, reverse-question,
  and the optional audio-player + caption block).
  Copy it and fill it in; don't hand-roll CSS.
- `scripts/filler_stats.py` — disfluency counter for SRT/VTT/text transcripts.
- `scripts/srt_to_cues.py` — converts a transcript into the inline cue array
  that powers the report's live captions.
