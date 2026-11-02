---
name: architecture-review
description: Review existing or newly modified code for SOLID, SRP, OCP, dependency direction, oversized classes, modularity, circular dependencies, and unjustified abstractions. Use for architecture reviews, major refactors and substantial feature implementation.
---

# Evidence-based architecture review

1. Inspect the actual relevant code, surrounding modules and tests; do not judge from filenames or line counts alone.
2. Reconstruct dependencies and module boundaries; identify where a new variant would require modifying stable code.
3. Check SRP, OCP, LSP, ISP, DIP, cohesion, coupling, cycles, duplicated rules, testability, and error handling.
4. Prioritize findings by severity and show exact file/location, evidence, consequences, and minimal fix.
5. Distinguish actual violations from optional design improvements; avoid speculative extra classes.
6. Propose an incremental change plan and focused tests; do not modify files unless requested.
7. If no significant findings exist, state that and note any inspection limits.

Output: Summary, evidence-backed findings (Critical/Major/Minor), minimal refactor plan, test impact.
