#!/usr/bin/env python3
"""
filler_stats.py — Disfluency / filler-word counter for interview transcripts.

Usage:
    python3 filler_stats.py "/path/to/transcript.srt"
    python3 filler_stats.py transcript.vtt
    python3 filler_stats.py transcript.txt

Works on .srt, .vtt, or plain-text transcripts. Strips SRT/VTT index lines and
timestamps, then counts common English filler words, stutters (repeated short
words), and run-on "and"-starts. Also estimates spoken duration from the first
and last timestamps and reports a per-minute filler density.

Prints a JSON blob to stdout. Counts cover the whole transcript (both speakers)
unless you pre-split by speaker — the trend is reliable even if the absolute is
slightly high because most filler clusters in the candidate's longer answers.
"""
import sys
import re
import json


TIMESTAMP_RE = re.compile(
    r"(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})"
)
INDEX_LINE_RE = re.compile(r"^\d+\s*$")


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def parse(path):
    """Return (spoken_text, first_seconds, last_seconds)."""
    raw = read_text(path)
    first_ts = None
    last_ts = None
    text_lines = []
    for line in raw.splitlines():
        m = TIMESTAMP_RE.search(line)
        if m:
            start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            end = int(m.group(5)) * 3600 + int(m.group(6)) * 60 + int(m.group(7))
            if first_ts is None or start < first_ts:
                first_ts = start
            if last_ts is None or end > last_ts:
                last_ts = end
            continue
        if INDEX_LINE_RE.match(line):
            continue
        if line.strip().upper() == "WEBVTT":
            continue
        text_lines.append(line)
    return "\n".join(text_lines), first_ts, last_ts


def count(pattern, text):
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def main():
    if len(sys.argv) < 2:
        print("usage: python3 filler_stats.py <transcript.srt|.vtt|.txt>", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    text, first_ts, last_ts = parse(path)

    counts = {
        "um": count(r"\bum\b", text),
        "uh": count(r"\buh\b", text),
        "hmm": count(r"\bhmm+\b", text),
        "you_know": count(r"\byou know\b", text),
        "like": count(r"\blike\b", text),
        "yeah": count(r"\byeah\b", text),
        "so_sentence_start": count(r"(?im)^\s*so\b", text),
        "stutter_the_the": count(r"\bthe the\b", text),
        "stutter_i_i": count(r"\bI I\b", text),
        "and_line_starts": count(r"(?im)^\s*and\b", text),
    }
    hesitation_total = counts["um"] + counts["uh"] + counts["hmm"]

    # word count (rough, latin-script)
    words = re.findall(r"[A-Za-z']+", text)
    word_count = len(words)

    duration_sec = None
    density_per_min = None
    if first_ts is not None and last_ts is not None and last_ts > first_ts:
        duration_sec = last_ts - first_ts
        minutes = duration_sec / 60.0
        if minutes > 0:
            density_per_min = round(hesitation_total / minutes, 2)

    result = {
        "file": path,
        "counts": counts,
        "hesitation_total_um_uh_hmm": hesitation_total,
        "latin_word_count": word_count,
        "estimated_spoken_duration_sec": duration_sec,
        "estimated_spoken_duration_hms": (
            f"{duration_sec // 3600:02d}:{(duration_sec % 3600) // 60:02d}:{duration_sec % 60:02d}"
            if duration_sec is not None else None
        ),
        "hesitation_per_minute": density_per_min,
        "note": (
            "Counts cover the whole transcript (both speakers). Most filler "
            "clusters in the candidate's longer answers, so the trend is reliable "
            "even if the absolute is slightly high."
        ),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
