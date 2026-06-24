# Memory Index

<!--
This file is the index for the persistent memory system.
Each line is a pointer to a memory file with a short description.
Keep entries under 150 characters. This file is injected every turn via hook.

Filename prefix convention (determines injection tier):
  user_     → universal: injected every turn (who the user is)
  feedback_ → universal: injected every turn (behavioral rules)
  project_  → contextual: loaded once per session, then on demand
  reference_→ contextual: loaded once per session, then on demand

Format: - [Title](filename.md) -- one-line description

Examples (delete these when you add real entries):
- [User Example](user_example.md) -- placeholder showing user_ format (delete me)
- [Feedback Example](feedback_example.md) -- placeholder showing feedback_ format (delete me)
- [Project Example](project_example.md) -- placeholder showing project_ format (delete me)
- [Reference Example](reference_example.md) -- placeholder showing reference_ format (delete me)
-->
