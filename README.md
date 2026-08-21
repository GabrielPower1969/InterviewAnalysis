# Interview Analysis — AI Interview Debrief Skill 面试复盘分析技能

**English** | [中文](#中文说明)

An open-source, **offline-first** AI skill that turns your recorded job interviews into a professional HTML debrief report — scored across 8 dimensions, with filler-word statistics, a segment-by-segment replay guide (with the interviewer's questions, your actual answers, and 60-second expert model answers), an industry perspective, and a concrete prepare-next-time plan.

Works with **Claude Code** (primary), and is compatible with **Cursor** and **OpenAI Codex CLI** via `AGENTS.md`.

> No API key purchase is required to share or use this skill. It is just files — whoever runs it uses their own AI coding tool (Claude Code / Cursor / Codex) and their own subscription. Nothing is ever uploaded by the skill itself.

---

## What you get

A single self-contained HTML report (dark, responsive, no external assets) with a sticky index:

| # | Section | What it does |
|---|---------|--------------|
| 00 | Overview & verdict | Overall score gauge, strongest / costliest moment, key theme |
| 01 | 8-dimension scorecard | Tech match, depth, structure, impact, ownership, growth, motivation, communication (1–5 each) |
| 02–09 | Per-dimension deep dives | ✅ wins / ⚠️ losses, timestamped verbatim quotes, "fix next time" box |
| 10 | Fluency analysis | Objective um/uh/stutter counts + per-minute density + practice targets |
| 11 | Timeline | Key moments, color-coded good / neutral / bad |
| 12 | **Segment-by-segment replay** | The centerpiece: for every segment — the interviewer's original question, your actual answer (key points + verbatim), what went wrong, how to improve, and on heavy-loss questions a **60-second expert model answer** you can rehearse |
| 13 | Industry perspective | Where this role & your profile sit in the current market |
| 14–16 | Prepare / tactics / reverse questions | Story bank (STAR-L), quantified-wins table, in-the-moment tactics, tailored questions to ask back |
| 17 | One-line verdict | Top-3 priority actions |

**Dark by default, with a day mode.** A ☀️/🌙 toggle in the top-right switches between the dark palette and a light one, and remembers your choice.


### 🎧 Audio-synced playback (when you supply the recording)

If you hand the skill the audio/video alongside the transcript, the report ships wired to it:

- **Every timestamp becomes a ▶ play button** — click any moment in the timeline, segment guide, or a quoted line and the built-in player jumps straight there. Reading "you hedged here" is one thing; hearing it is another.
- **A live caption track with an on/off toggle** follows the audio as it plays, so you can read and listen at once. Captions are embedded in the HTML, so it all works offline by double-clicking the file.
- Output is a **folder** holding the recording, the transcript, and the report together — share the folder and everything keeps working.
- Captions use the classic subtitle look — **yellow with a black outline** — so they stay readable over either theme.


## Inputs

| Input | Required? | Notes |
|---|---|---|
| **CV / résumé** | ✅ Required | PDF is fine. Anchors fit scoring + the story bank |
| **Interview record** | ✅ Required (one of two) | a) transcript `.srt` / `.vtt` / `.txt` (timestamps preferred), or b) audio/video — transcribed **locally** (e.g. [whisper](https://github.com/openai/whisper)), never uploaded |
| **JD (job description)** | ⭐ Strongly recommended | Enables role-tailored fit analysis; report still works without it |

## Install

### Claude Code (primary)

```bash
git clone https://github.com/GabrielPower1969/InterviewAnalysis.git
cp -r InterviewAnalysis/skills/interview-analysis ~/.claude/skills/
```

Then in any Claude Code session, just share your CV + transcript (or audio) and say **"analyze this interview"** — the skill triggers automatically. Or invoke explicitly: `/interview-analysis`.

### Cursor

Add a project rule pointing at the skill instructions (Cursor reads `AGENTS.md` automatically in recent versions; otherwise):

```
Settings → Rules → Add rule → "For interview analysis tasks, follow the
instructions in skills/interview-analysis/SKILL.md of this repo."
```

### OpenAI Codex CLI

Codex reads the repo's `AGENTS.md` automatically. Clone the repo, put your CV / JD / transcript inside (or reference absolute paths), and ask for an interview analysis.

## Privacy

- **Offline-first**: reading files, filler statistics (`scripts/filler_stats.py`, pure local Python), and report generation all happen locally.
- The skill instructs the AI to never upload your CV / transcript / media to any external service, and to keep personal contact details out of the report.
- Your interview data stays in your folders; only the skill files live in this repo. No sample interviews, CVs, or personal data are included.

## Repository layout

```
skills/interview-analysis/
├── SKILL.md                     # The skill: workflow, inputs, report structure
├── references/rubric.md         # 8-dimension scoring rubric (1–5 levels, weights)
├── assets/report_template.html  # Self-contained HTML report template (+ audio player & captions)
└── scripts/
    ├── filler_stats.py          # Offline filler/disfluency counter (srt/vtt/txt)
    └── srt_to_cues.py           # Transcript -> inline caption cues for the report
```

## License

MIT — see [LICENSE](LICENSE).

---

# 中文说明

一个开源、**离线优先**的 AI 技能：把你的面试录音变成一份专业的 HTML 复盘报告——八维评分、吞吐词统计、逐段精读（含面试官原问、你的原答、以及可直接照着练的 60 秒专家范例回答）、行业视角、以及下次面试的备战清单。

以 **Claude Code** 为主，通过 `AGENTS.md` 兼容 **Cursor** 和 **OpenAI Codex CLI**。

> 分享或使用本技能**无需购买 API key**——它只是一组文件，谁使用就用谁自己的 AI 编程工具（Claude Code / Cursor / Codex）和订阅额度。技能本身不会上传任何数据。

## 报告内容

单个自包含 HTML 文件（深色主题、响应式、无外部依赖），带固定目录索引：

| # | 版块 | 说明 |
|---|------|------|
| 00 | 总览与结论 | 综合评分仪表盘、最强/最伤时刻、关键主题 |
| 01 | 八维评分卡 | 技术匹配、深度、表达结构、业务影响、协作、成长、动机、沟通（各 1–5 分） |
| 02–09 | 逐维度详评 | ✅ 做得好 / ⚠️ 掉分点、带时间戳的原话引用、「下次这样修」 |
| 10 | 吞吐词分析 | um/uh/结巴客观计数 + 每分钟密度 + 可量化练习目标 |
| 11 | 时间线速览 | 高光/中性/失分关键时刻 |
| 12 | **逐段精读** | 核心版块：每段给出面试官原问、你的回答重点（含原话）、问题在哪、怎么提高；强烈失分题附**🎯 60 秒专家范例回答**，可对着音频逐段复盘、照着练 |
| 13 | 行业视角 | 这个岗位和你的画像在当前市场的位置 |
| 14–16 | 备战清单 / 临场战术 / 反问银行 | STAR-L 故事库、量化战绩表、临场行为修正、定制反问 |
| 17 | 一句话总结 | 三条最高优先级行动 |

**默认夜间模式，另配白天模式。** 右上角 ☀️/🌙 按钮一键切换深浅配色，选择会被记住。


### 🎧 音频联动（提供录音时自动启用）

把录音和转录一起交给技能，报告会直接和音频挂上钩：

- **每个时间戳都是一个 ▶ 播放按钮**——时间线、逐段精读、引用原话，点哪里就从哪里开始播。看到「你这里犹豫了」和亲耳听到，感受完全不同。
- **实时字幕 + 开关**，跟着音频滚动，可边听边读；字幕内嵌在 HTML 里，双击打开即可离线使用。
- 输出是一个**文件夹**，录音、转录、报告三件套放在一起——整个文件夹分享出去，功能照常。
- 字幕采用经典电视字幕样式——**外黑里黄**（黄字黑描边），在深色和浅色背景下都清晰。


## 输入

| 输入 | 是否必需 | 说明 |
|---|---|---|
| **简历 CV** | ✅ 必选 | PDF 即可，用于匹配度评分和故事库挖掘 |
| **面试记录** | ✅ 必选（二选一） | a) 文字转录 `.srt` / `.vtt` / `.txt`（带时间戳最佳）；或 b) 音频/视频——用本地工具（如 [whisper](https://github.com/openai/whisper)）转录，**绝不上传** |
| **JD 职位描述** | ⭐ 强烈推荐 | 有 JD 可做针对岗位的匹配分析；没有也能出完整报告 |

## 安装

### Claude Code（主要方式）

```bash
git clone https://github.com/GabrielPower1969/InterviewAnalysis.git
cp -r InterviewAnalysis/skills/interview-analysis ~/.claude/skills/
```

之后在任意 Claude Code 会话中，把简历 + 转录（或音频）发给它，说一句**「分析这个面试」**即可自动触发；也可以显式调用 `/interview-analysis`。

### Cursor

添加一条项目规则指向技能说明（新版 Cursor 会自动读取 `AGENTS.md`；否则）：

```
设置 → Rules → 新建规则 → 「面试分析任务请遵循本仓库
skills/interview-analysis/SKILL.md 中的说明。」
```

### OpenAI Codex CLI

Codex 会自动读取仓库的 `AGENTS.md`。克隆仓库后，把简历 / JD / 转录放进来（或引用绝对路径），然后请求做面试分析即可。

## 隐私

- **离线优先**：读文件、吞吐词统计（`scripts/filler_stats.py`，纯本地 Python）、报告生成全部在本地完成。
- 技能明确要求 AI 不得把简历/转录/音视频上传到任何外部服务，且报告中不包含电话、邮箱等个人联系方式。
- 你的面试数据留在你自己的文件夹里；本仓库只包含技能文件，不含任何示例面试、简历或个人数据。

## 许可证

MIT — 见 [LICENSE](LICENSE)。
