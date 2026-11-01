# apple-design

A Claude skill that lets an AI coding agent design mobile, desktop, and web apps the way Apple does, by following the complete [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/).

What is inside

- `SKILL.md`: the skill entry point: how to work, the eight principles, non-negotiable rules, platform snapshot, review checklist, and an index of every HIG page.
- `guides/`: the working material
  - `workflow.md`: step-by-step process from brief to review, with a design spec template
  - `design-tokens.md`: all the numbers (sizes, type scales, colors, contrast, materials, icons, gestures, shortcuts), generated from the reference pages
  - `components.md`, `patterns.md`, `technologies.md`: decision tables plus an entry for every HIG component, pattern, input, and technology
  - `foundations.md`: condensed rules from the eighteen Foundations pages
  - `platforms.md`: what changes on iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo, and games
  - `web.md`: translation of the guidelines to web apps (CSS tokens, breakpoints, HTML and ARIA mapping)
  - `diagrams.md`: what Apple's 411 diagrams and anatomy illustrations show, reviewed image by image
- `references/`: all 173 HIG pages as Markdown in Apple's hierarchy, each with its source URL. `INDEX.md` lists them with summaries.
- `scripts/update.py`: re-downloads the HIG and regenerates `references/`.

Install

With the open Agent Skills CLI (works for Claude Code, Cursor, Codex, Copilot, Gemini CLI, Windsurf, and other agents that read `SKILL.md`):

```bash
npx skills add solaymanhaider/apple-design
```

Add `-g` for a global install, `-a cursor` (or another agent name) to target one agent, or `--copy` to copy instead of symlink. See https://skills.sh for the CLI.

Manual install for Claude Code:

```bash
git clone https://github.com/solaymanhaider/apple-design ~/.claude/skills/apple-design
```

Or per project:

```bash
git clone https://github.com/solaymanhaider/apple-design .claude/skills/apple-design
```

Then ask your agent to design or review an app for an Apple platform or the web, or invoke `/apple-design`.

Update the references

```bash
python3 scripts/update.py
```

The guides are hand-written from the references; re-check them after an update if Apple changed a page.

Content of the HIG is copyright Apple Inc., reproduced here for reference use.
