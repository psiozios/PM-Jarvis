# Skill Chains

Multi-skill workflow sequences for common PM activities. Each chain lists skills in order. When a skill completes, check its Cross-Skill Links and offer the next step. Offer one nudge; do not auto-run.

---

## Daily PM Workflow

1. `/daily-plan` - prioritized plan with meeting context
2. Take raw meeting notes or record during meetings
3. `/meeting-notes` - process each meeting into structured notes + action items
4. `/slack-message` - draft any follow-up communications

## Weekly PM Cycle

1. Monday: `/weekly-plan` - set the week's priorities tied to quarterly goals
2. Daily: follow the Daily PM Workflow above
3. Friday: `/weekly-review` - reflect on what shipped, slipped, and was learned
4. Friday: `/status-update` - send weekly stakeholder update

## PRD Lifecycle

1. `/user-research-synthesis` - synthesize research informing the feature
2. `/impact-sizing` - size the opportunity before committing
3. `/prd-draft` - draft the PRD at the appropriate stage
4. `/prd-review-panel` - multi-perspective review from 7 agents
5. `/create-tickets` - break into engineering tickets
6. `/launch-checklist` - plan the launch
7. `/feature-results` - analyze post-launch results
8. Feed learnings back into next cycle

## Strategic Planning

1. `/define-north-star` - validate or set the North Star metric
2. `/metrics-framework` - build the leading/lagging indicator hierarchy
3. `/write-prod-strategy` - write the full product strategy
4. `/prioritize` - classify and prioritize the backlog

## Sales Intelligence

1. `/win-loss-analysis` - synthesize sales call notes and churn interviews
2. `/competitor-analysis` - enrich with competitive context
3. `/write-prod-strategy` - update positioning based on findings
4. `/prd-draft` - spec product gaps blocking deals

## Pre-Launch Risk

1. `/pre-mortem` - surface failure modes (2-4 weeks before go-live)
2. `/launch-checklist` - embed mitigations into the launch plan
3. `/decision-doc` - document go/no-go rationale

## Quarterly Planning

1. `/okr-planning` - create or critique quarterly OKRs
2. `/board-deck` - prepare the quarterly business review
3. `/status-update` - share OKR progress with stakeholders through the quarter

## Incident Response

1. `/post-mortem` - blameless retrospective after incident or miss
2. `/root-cause-analysis` - deeper investigation of specific failure modes
3. `/sprint-planning` - reprioritize next sprint around highest-impact fixes

## New Feature Research

1. `/opportunity-sizing` - validate market size and strategic fit
2. `/survey-builder` - run a PMF or JTBD survey to qualify demand
3. `/interview-guide` - run discovery interviews
4. `/voice-of-customer` - synthesize cross-channel signals
5. `/prd-draft` - spec the feature with research-backed requirements

## Build with AI (for PMs who code)

1. `/cto-consult` - get pushback on the idea and a phased plan
2. `/explore-codebase` - understand the relevant code
3. `/execution-plan` - create a tracked step-by-step plan
4. `/code-first-draft --from-plan` - implement each step
5. `/code-review` - review the implementation
6. `/update-docs` - update documentation
7. `/create-tickets --quick` - capture issues found along the way

## Code Quality

1. `/code-review` - review changes
2. `/peer-review` - verify findings from another AI tool's review
3. `/create-tickets` - turn confirmed issues into fix tickets

## Learning While Building

1. Hit an unfamiliar concept during any development skill
2. `/learning-mode` - understand the concept at three depth levels
3. Return to the development skill

## Design-Led Prototyping

1. `/design-direction` - set the visual tone (parameters, style preset, anti-patterns)
2. `/generate-ai-prototype --with-taste` - inject direction into AI tool prompts
3. `/prototype-feedback --design` - evaluate against direction with 7-dimension scoring
4. Iterate until the prototype matches the intended feel

## Design Audit and Improve

1. `/design-audit` - assess current state of an existing UI or competitor
2. `/design-direction` - set the target aesthetic for improvements
3. `/prototype` - build an improved version following the new direction
4. `/prototype-feedback --design` - validate the improvement

## PRD with Design Direction

1. `/prd-draft` - define the feature requirements
2. `/design-direction --for-prd` - add a Design Direction section to the PRD
3. `/prd-review-panel` - validate (designer sub-agent checks direction fit)

## Second Brain (compounding knowledge)

1. `/second-brain init <focus>` - scaffold a focus area wiki
2. `/second-brain ingest <source>` - process sources one at a time
3. Seven skills auto-offer to file outputs into the brain
4. `/second-brain query` or `/second-brain prep` before PRDs, strategy docs, or decisions
5. Weekly: `/second-brain lint` for contradictions + `/second-brain explore` for connections
