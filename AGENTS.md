# Agent Instructions (Cursor / OpenAI Codex / other AI coding tools)

This repository contains **interview-analysis**, an offline interview-debrief
skill authored for Claude Code but usable by any capable AI coding agent.

## When the user asks for an interview analysis / 面试复盘 / 面试分析

Follow the instructions in **`skills/interview-analysis/SKILL.md`** exactly. In short:

1. **Collect inputs**: CV (required); interview transcript `.srt`/`.vtt`/`.txt`
   OR an audio/video file (required, one of the two — transcribe media locally,
   e.g. with whisper; never upload it); JD (optional, strongly recommended).
2. Read the full transcript (chunked if large), identify candidate vs
   interviewer.
3. Run `python3 skills/interview-analysis/scripts/filler_stats.py <transcript>` for
   objective disfluency counts.
4. Score 8 dimensions per `skills/interview-analysis/references/rubric.md` with
   timestamped verbatim quotes.
5. Generate a single self-contained HTML report from
   `skills/interview-analysis/assets/report_template.html`, filling every section —
   including the segment-by-segment section with the interviewer's original
   question, the candidate's actual answer, and 60-second expert model answers
   on heavy-loss segments.
6. If an audio/video file is available, wire the report to it: render every
   timestamp as `<button class="pb" data-t="SECONDS">MM:SS</button>`, and embed
   the caption cues from
   `python3 skills/interview-analysis/scripts/srt_to_cues.py <transcript>` into
   the `{{CUES_JSON}}` placeholder so the live-caption toggle works offline.
7. Save the report next to the transcript — as a folder holding the media,
   transcript, and report together when audio sync is on — and present it to
   the user.

## Hard rules

- Offline only: never send the CV, JD, transcript, or media to any external
  service.
- Keep personal contact details (phone, email, address) out of the report.
- Write the report in the user's language (default Chinese) with verbatim
  quotes kept in their original language.
