<p align="center">
  <strong>✈️ your AI writes like a LinkedIn post. make it write like a Boeing manual.</strong>
</p>

<p align="center">
  An agent skill that makes LLMs write plain English with the discipline of <a href="https://www.asd-ste100.org/">ASD-STE100 Simplified Technical English</a>,<br>
  the controlled language aerospace has used since 1983 so that a tired mechanic cannot misread an instruction.<br>
  Layman-readable by default, STE-strict on request.
</p>

<p align="center">
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/SKILL.md-open_standard-blue?style=flat" alt="Agent Skills"></a>
  <a href="skills/simple-korean/SKILL.md"><img src="https://img.shields.io/badge/version-0.1.0-blue?style=flat" alt="version 0.1.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat" alt="MIT"></a>
  <a href="https://github.com/raeperd/SimpleKorean/stargazers"><img src="https://img.shields.io/github/stars/raeperd/SimpleKorean?style=flat&logo=github&color=yellow" alt="GitHub stars"></a>
</p>

This repository is a fork of [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) that is being adapted to Korean. The rule set below is still the English one from upstream.

Works in every agent that reads the [Agent Skills standard](https://agentskills.io): Claude Code, Cursor, VS Code Copilot, OpenAI Codex, Gemini CLI, Goose, OpenCode, and about 25 more. One folder, no dependencies, MIT.

## Install

Any agent, with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add raeperd/SimpleKorean
```

This installs the skill only. It does not install the session hook or the output style below, so setting `outputStyle` to `simple-korean:simple-korean` without the plugin does nothing. Use the Claude Code plugin for those.

Claude Code plugin, with the session hook and the output style:

```bash
claude plugin marketplace add raeperd/SimpleKorean && claude plugin install simple-korean@simple-korean
```

The output style is named `simple-korean:simple-korean`. The short name does not resolve. Select it with `/config` under Output style, or put `{"outputStyle": "simple-korean:simple-korean"}` in `~/.claude/settings.json`.

Codex plugin, with the session hook:

```bash
codex plugin marketplace add raeperd/SimpleKorean
codex plugin add simple-korean@simple-korean
```

Codex asks you to trust the hook before its first run. The hooks need Node.js. Details in [`src/hooks/README.md`](src/hooks/README.md).

No skill support? Paste the rule block of [`prompts/system-prompt.md`](prompts/system-prompt.md) into your system prompt, `AGENTS.md`, or `.cursorrules`. The page ends with a 60-token version for tight budgets.

Then ask for any technical writing, or say "rewrite this with simple-korean".

## See it

Left is real, unedited Claude output. Right is the same model with the skill loaded.

<table>
<tr>
<th width="50%">Without skill</th>
<th width="50%">With skill</th>
</tr>
<tr>
<td valign="top">

> Leveraging sqlpipe's robust architecture, users can seamlessly synchronize their Postgres tables to S3 with minimal configuration overhead. Before getting started, you should ensure that your AWS credentials have been properly configured — this is crucial for avoiding frustrating permission issues down the line.

</td>
<td valign="top">

> sqlpipe copies your Postgres tables to S3. It needs one configuration file.
>
> Before you start, make sure that your AWS credentials are correct. If they are not, S3 rejects the upload with a permission error.

</td>
</tr>
</table>

More rewrites in [`examples/before-after.md`](examples/before-after.md): READMEs, runbooks, incident reports, error messages, release notes.

## The rules

Two registers in [`SKILL.md`](skills/simple-korean/SKILL.md), about 1,700 tokens.

The reply, every chat answer:

| Rule | What it kills |
|---|---|
| Prose only: no headers, bullets, bold, tables | The wall of formatting around a one-line answer |
| First sentence answers | The preamble |
| No em-dashes | The spliced half-thought |
| Define a concept term in a few words | Jargon the reader has to look up |
| No contractions, openers, or closers | "Great question!" and "Hope this helps!" |

The document: docs, READMEs, runbooks, error messages, release notes:

| Rule | What it kills |
|---|---|
| Max 20 words per instruction, 25 per description | The run-on sentence |
| Condition before command | Trailing "...if the flag is set" that readers execute too late |
| Simple tenses, active voice | "has been updated", ", making it easy to..." |
| No should/would/may/might | Hedging. `can`, `will`, `must` survive |
| One word = one meaning, whole document | check/verify/confirm/validate roulette |
| Keep articles, keep "that" | Telegraph style. STE is short, not terse |
| No bold lead-ins, no heading over two sentences | Decoration that hides the fact |
| State the fact, not its importance | "crucial", "robust", "not just X, it is Y" |

Two modes. Plain, the default, is all of the above. Strict adds the STE dictionary discipline when you name STE, ASD-STE100, or compliance. The reply stays Plain in every mode.

## FAQ

Does this make output STE-certified? No. Nothing does, because ASD certifies no tool. Strict mode gets close. Word-level rulings live in the official standard, a [free download](https://www.asd-ste100.org/request.html).

Will my docs sound robotic? They will sound like Airbus manuals: flat and impossible to misread. For docs that is the whole point. Keep your voice for your blog.

Why not just prompt "write clearly"? "Clearly" is an opinion. "No sentence over 20 words" is a spec. Agents follow specs.

Why a 40-year-old aerospace standard? It is maintained (Issue 9, January 2025), numbered, and testable. It is also a near-perfect negative of every AI writing tell.

## Contributing

Open an issue for questions and bug reports. Pull requests are welcome. Run `python3 evals/ste_lint.py --self-test` and `python3 evals/check_numbers.py` before you push. Say in the PR whether an agent wrote the code, and do not add attribution trailers.

## License

MIT for everything here. The repo paraphrases the rules for teaching and reproduces no spec text or dictionary content. Unofficial project, not affiliated with or endorsed by ASD or STEMG. ASD-STE100 is a registered trademark of ASD.
