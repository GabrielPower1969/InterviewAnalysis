#!/usr/bin/env python3
"""
srt_to_cues.py — turn an .srt/.vtt transcript into the compact cue array the
report template embeds for live captions.

Usage:
    python3 srt_to_cues.py "/path/to/transcript.srt" > cues.json
    python3 srt_to_cues.py "/path/to/transcript.srt" --stats

Output is a single line of JSON: [[start_seconds, end_seconds, "text"], ...]

Paste that into the report's `{{CUES_JSON}}` placeholder. It goes inline (rather
than being fetched at runtime) so the caption track still works when the user
double-clicks the HTML — browsers block fetch() on file:// URLs.

Cues are sorted by start time and merged per subtitle block, so the binary
search in the template's caption code stays correct.
"""
import sys
import re
import json

TS = re.compile(
    r'(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{1,2}):(\d{2}):(\d{2})[.,](\d{3})'
)
INDEX_ONLY = re.compile(r'^\d+\s*$')


def to_seconds(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    cues, block = [], []
    for line in raw.splitlines() + ['']:
        if line.strip() == '':
            if block:
                start = end = None
                text = []
                for b in block:
                    m = TS.search(b)
                    if m and start is None:
                        start = to_seconds(*m.group(1, 2, 3, 4))
                        end = to_seconds(*m.group(5, 6, 7, 8))
                    elif b.strip() and not INDEX_ONLY.match(b) and b.strip().upper() != 'WEBVTT':
                        text.append(b.strip())
                if start is not None and text:
                    joined = re.sub(r'\s{2,}', ' ', ' '.join(text)).strip()
                    cues.append([round(start, 2), round(end, 2), joined])
                block = []
        else:
            block.append(line)
    cues.sort(key=lambda c: c[0])
    return cues


def main():
    if len(sys.argv) < 2:
        print('usage: python3 srt_to_cues.py <transcript.srt> [--stats]', file=sys.stderr)
        sys.exit(1)
    cues = parse(sys.argv[1])
    payload = json.dumps(cues, ensure_ascii=False, separators=(',', ':'))
    if '--stats' in sys.argv:
        print(f'cues: {len(cues)}', file=sys.stderr)
        print(f'json bytes: {len(payload)}', file=sys.stderr)
        if cues:
            print(f'first: {cues[0]}', file=sys.stderr)
            print(f'last:  {cues[-1]}', file=sys.stderr)
    print(payload)


if __name__ == '__main__':
    main()
