# Register Protocol

**Principle: REGISTER RUNS ON TWO AXES, AND RANK IS NEITHER.**

Register is the choice made before the first sentence: what this piece of writing should sound like and how it should be built. `config/house-style.md` governs quality inside that choice; this file governs the choice itself. Every rule here is subject to §9 of that file — a register rule ships only with a corpus quote under it.

## Axis One — The Specific Person

**Sets orthography.** Casing, contractions, punctuation habits, abbreviations, emoji, greeting and sign-off, how long a sentence runs before it breaks.

Axis one is keyed to **one named human**, never to a category they belong to. It comes from the corpus: what this person actually writes, and what they visibly tolerate in writing sent to them. Two people with the same title routinely sit at opposite ends of it. Where there is no corpus for a person, there is no axis-one rule for them — write neutrally and say the gap exists.

**Never scrub to signal respect.** A writer who works in lowercase, or leans on contractions, or opens without a greeting is not being careless — that is their orthography, and it is the thing you are matching. Stripping it out to make a piece "appropriate" for its reader does not raise the register, it **breaks the match**, and it reads as a stranger writing in a borrowed voice. The correct move on an unfamiliar reader is neutral, not scrubbed.

## Axis Two — Artifact or Conversational Turn

**Sets structure.** Numbering, section headings, length, whether reasoning is stated or assumed, whether context is restated for someone who was not there.

**An artifact is anything that may be forwarded, quoted, or decided from.** That is the whole test, and it is about the writing's likely future rather than the tool it was typed into. A chat message that names a decision is an artifact. A doc nobody will reread is not. When it is genuinely unclear, treat it as an artifact — the cost of structure nobody needed is a few lines, and the cost of a decision that got forwarded without its reasoning is the decision being relitigated.

**Formality is additive structure.** Moving up this axis means **adding**: numbering the options, stating the reasoning that was implicit, restating the context a forwarded reader will not have, naming the owner and the date. It never means removing informality. A numbered, sourced, fully-reasoned artifact written in the author's habitual lowercase is formal. The same content in scrubbed corporate register with the reasoning left out is not — it is shorter and worse.

## Rank Is Not An Axis

**Cut it on sight.** "More formal for senior audiences", "adjust tone to the reader's seniority", "polish it, it's going to leadership" — these are not register rules and no file in this workspace carries one.

The advice survives only when it is **restated onto a real axis**, and it usually can be:

| What the rank rule was reaching for | The axis it actually belongs to |
|---|---|
| "Execs are busy — be brief" | Axis two. Length, keyed to whether it is an artifact and how far it travels. |
| "Lead with the recommendation" | Axis two. Ordering, because a forwarded reader reads the first line and may read no further. |
| "Quantify it for leadership" | Axis two, plus the absolute rules — every claim graded to its evidence, for every reader. |
| "This CFO wants source links" | Axis one. A named person's known preference. Keep it, name them, cite the corpus. |
| "Be more formal, it's the CEO" | Nothing. Cut it. |

**Why this is worth the churn.** Rank-keyed register fails in both directions. It over-formalizes writing to senior readers, who mostly want it shorter and more direct, and it licenses sloppiness toward everyone else. Neither error is about seniority — both are axis-two mistakes wearing a rank label.

## Content Authority for Outward Writing

**Outward content** is anything a customer, user, prospect, or the public reads: marketing copy, launch announcements, changelogs, release notes, in-app and onboarding copy, help docs, case studies, customer email.

**Where the org has a brand or style system reachable as a tool, that system is the register authority for outward content, and it is read live before drafting.** A design system, a brand-guidelines service, a content style guide behind an API — if it can be queried, query it. Route through `references/mcp-routing.md`. Reading it after drafting is not reading it: the point is that it constrains the draft, not that it is cited underneath one.

**A local mirror is a dated snapshot, never the authority.** A copy of the brand rules living in this workspace is evidence of what the system said on the day it was copied, and it is used only when the live system is unreachable. It carries its snapshot date, it is cited as a snapshot, and a draft built on it says so. When the mirror and the live system disagree, **the live system wins without discussion** — a mirror that has drifted is a stale file, not a competing opinion. See `references/protocols/freshness-provenance.md` rule 2.

**The authority does not reach the absolute rules or the anti-slop standard.** A brand system governs register: voice, vocabulary, what the product is called, how warm the copy runs. It does not license a banned word from `config/house-style.md` §3, an unsourced number, an invented attribution, or a slop pattern. Where a brand system's own examples break those rules, follow the register and fix the prose — and where the conflict is real and repeated, tell the user rather than quietly resolving it every time.

**Positioning is not tone of voice.** Competitive positioning, messaging frameworks, category claims, and differentiation language answer *what we say about where we sit*. Register answers *how this sentence sounds*. They are different questions, they are usually owned by different people, and a positioning doc **never inherits the register authority** no matter how much voice-adjacent language it contains. Take claims from positioning; take voice from the brand system.

## Propagating a Rule Change

A register rule reversing — a new brand authority replacing an old one, or a house rule in `config/house-style.md` flipping to its opposite — is not a one-line edit. Two obligations:

**1. Propagate the flip through every table.** The same rule is usually encoded in several places: a substitution table, a checklist row, an eval criterion, a worked example, a "before / after" pair. Grep for the rule's *terms* rather than its statement, and change every encoding of it. A flip applied to the statement and not to the table underneath it produces a file that contradicts itself, and agents will follow whichever half they read first.

**2. Add the sense-dependent cases a blind find-and-replace would break.** A reversed rule almost always has exceptions that only appear once you look at real sentences: the banned word in its literal domain sense, the verbatim quote under the quote carve-out, the proper noun that happens to contain the term, the case where the old form was correct for a reason unrelated to the rule. Write these into the table **as part of the same change**, with an example of each. A reversal that ships without them is a find-and-replace waiting to happen, and the damage it does is invisible until someone reads the output closely.

Both obligations are subject to `config/house-style.md` §9: reversing a rule takes the same corpus evidence as writing one.

## Cross-References

- `config/house-style.md` — quality inside the register choice; §9 is the evidence requirement above every rule in this file
- `context-library/writing-style-*.md` — the per-context register files this protocol governs the shape of
- `templates/corpus-template.md` — the evidence snapshot an axis-one rule is derived from
