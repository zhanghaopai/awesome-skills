# Clean code and change hygiene

- Descriptive names; functions express one coherent operation and minimize side effects.
- Prefer explicit parameters and return types; avoid surprising mutable global state.
- Remove duplication at the level of meaningful business rules; don't prematurely deduplicate accidental similarity.
- Separate validation, orchestration, algorithms, IO, presentation, and error translation where responsibilities differ.
- Write explanatory comments for non-obvious decisions and domain assumptions, not redundant narration.
- Review files >300 lines, functions >50 lines, or classes carrying several independent responsibilities; these are prompts to inspect, not hard failures.
- Preserve backward compatibility where required. Add tests for edge cases, invalid input, regression, and algorithmic boundaries.
- Only change files relevant to the task. Run available formatters, linters, builds and targeted tests.
- When checks cannot run, report the missing dependency or environment blocker rather than asserting success.
