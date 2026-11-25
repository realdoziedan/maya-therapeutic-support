# Maya: AI therapy tool for adults and couples

Maya is an AI therapy tool you can talk to when life feels heavy, a relationship is stuck, or a hard conversation is coming up. She listens first, helps you make sense of what is happening, and teaches practical skills from CBT, EFT, the Gottman Method, Nonviolent Communication, ACT and DBT. She works on her own or with both partners, and can bring your Christian, Muslim or Grail Message faith into the conversation if you ask. Maya runs as a skill in Claude, ChatGPT, Codex, Gemini and other AI assistants.

## What Maya does

- **Talks things through:** stress, low mood, worry, life changes and setbacks, at your pace.
- **Helps couples:** recurring arguments, trust and repair, communication, and decisions you face together, with private safety checks for each partner.
- **Teaches skills you can use:** reframing unhelpful thoughts, calming strong emotions, asking for what you need, and listening without escalating.
- **Rehearses hard conversations** with a partner, parent, boss or friend before you have them.
- **Keeps you safe:** clear crisis steps and local help options, including Nigerian contacts, when risk comes up.
- **Faith only if you want it:** draws on the bundled World English Bible and ClearQuran texts and names its sources.
- **Optional notes:** session summaries and referral notes, saved only where and when you agree.

## Try saying

> I've been overwhelmed at work and can't switch off at night. Can we talk?

> My partner and I keep having the same argument about money. Help us understand what's really going on.

> I need to tell my mum something difficult. Can we practise the conversation first?

> I'm Christian and I'd like faith to be part of this. I'm struggling to forgive someone.

## Important

Platform-neutral AI support for adults and couples. Maya is not a therapist, clinician, or crisis service. This package is not clinical validation or a substitute for clinician governance, safeguarding policy, or emergency care.

## Contents

- `SKILL.md`: core behavior and safety rules.
- `references/`: therapy concepts, risk and safety, screening, and optional faith notes.
- `templates/`: optional user-controlled records.
- `sources/`: the World English Bible (public domain) and the ClearQuran Allah Edition (CC BY-ND 4.0) as plain text, suggested online sources, and space for authorized owner-supplied texts. No religious PDFs, NKJV or Grail Message texts are bundled.
- `adapters/`: setup notes for ChatGPT, Claude, Gemini, and generic/API use.
- `manifest.json`: package index and loading hints.

## Install in Codex or Claude Code

With Node.js 22.20 or later and npm available, run:

```sh
npx skills add realdoziedan/maya-therapeutic-support --skill maya-therapeutic-support -a codex -a claude-code -g -y
```

This installs the skill for your user in both agents. To install only for the current project, remove `-g`. Start a new agent session after installation. To check for updates later, run `npx skills update`.

The command uses the open-source Skills CLI. Review the repository before installing a skill from any source.

## Manual install in Codex or Claude Code

Copy the complete skill folder, keeping `SKILL.md`, `references/`, and `templates/` together.

- **Codex:** user-wide `~/.agents/skills/maya-therapeutic-support/`; for one project, `.agents/skills/maya-therapeutic-support/`.
- **Claude Code:** user-wide `~/.claude/skills/maya-therapeutic-support/`; for one project, `.claude/skills/maya-therapeutic-support/`.

Start a new session. In Claude Code, invoke it with `/maya-therapeutic-support` or describe a task where it applies.

## Upload to Agensi

Create a ZIP of this package folder with `SKILL.md` and its supporting text files inside, then upload it at [Agensi's submission page](https://www.agensi.io/dashboard/submit). Agensi accepts a wrapper folder in the ZIP. Complete the listing fields and review the permissions detected from the package before submitting. A listing goes through Agensi's scan and review.

No religious PDFs are included. Agensi says agents receive text files from a listing, not PDFs; if you have the right to share a source, put only the relevant permitted text in a reference file instead of relying on the PDF.

## Use in ChatGPT or another chat-based assistant

In ChatGPT, create a Project, add `SKILL.md` and `references/risk-and-safety.md` as files, then add the prompt below to Project instructions. Add other reference files only when useful and within your plan's file limits. In Claude's web app, you can upload the package as a custom skill ZIP from **Customize → Skills** when Skills and code execution are enabled.

Copy this prompt after attaching the skill files:

> Use the attached Maya skill files as guidance for this chat. Read SKILL.md first. Consult risk-and-safety.md when safety or relationship risks arise. Use faith references only if I request or agree to that. When faith is included, check accessible source files or reputable online sources when browsing is available; name the Bible translation or Quran translator and say when a source was not checked. The faith reference files are guidance, not full scripture texts. Be clear that you are AI support, not a therapist or emergency service; do not diagnose or promise confidentiality. Ask whether I want listening, help making sense of things, a practical skill, or next steps. Do not save or share records unless I explicitly consent to the specific destination and scope. Use only tools actually available in this chat.

In a chat without custom Skills support, attach the files or add them to a Project/workspace as context, then paste the prompt. Availability and file limits vary by product and plan; see the [ChatGPT Projects guide](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [Claude Skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Safety and clinical review

Contacts reviewed 24 Nov 2026. She Writes Woman lists 0800 800 2000 as a 24/7 toll-free mental-health line; SURPIN lists +234 908 021 7555 and +234 903 440 0009. Lagos support numbers appear in the Mentally Aware Nigeria Initiative resource centre, but this review did not find current primary confirmation of hours/cost. Do not call them toll-free/24-7 without checking. 112 is commonly published as Nigeria's emergency number; connection/response varies. See `references/risk-and-safety.md`.

No personal records are included. Storage requires explicit informed consent; access to a connector is not permission to search/save. Before real-world use, have clinical and safeguarding specialists review the material, verify contacts, and establish data retention, privacy, and escalation procedures.

## License

Maya is licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE): you may share and adapt it with credit, but not for commercial purposes. The bundled scripture texts keep their own terms: the World English Bible is public domain, and the ClearQuran Allah Edition is CC BY-ND 4.0 (keep the wording unchanged and credit "Translation by Talal Itani, ClearQuran.com").
