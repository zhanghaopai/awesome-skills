
---
name: architecture-review
description: >
  Review code architecture for SOLID violations,
  God Classes, excessive coupling, circular dependencies,
  and maintainability problems. Use when reviewing
  implementations, refactoring, or architecture changes.
---

# Architecture Review

Inspect the relevant code and module structure.

## Review Checklist
1. Single Responsibility Principle violations
2. Open-Closed Principle violations
3. Dependency inversion violations
4. God Classes and oversized methods
5. Circular dependencies
6. Duplicated business logic
7. Missing extension points
8. Unnecessary abstractions

## Output
For each finding, report:
- File and location
- Architectural issue
- Severity
- Recommended refactoring
- Expected impact

Prioritize concrete findings over speculative advice.
Do not rewrite working code without authorization.

