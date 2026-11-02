# Tests and completion gate

- For behavior changes, create or update regression tests that demonstrate the intended contract.
- For numerical/domain calculations, cover boundary conditions, units, tolerances, assumptions and independently validated expected results.
- Keep pure domain rules testable without UI, database, filesystem, or network setup.
- Before declaring completion, inspect diffs for accidental edits, dependencies, unused abstractions and duplicated rules.
- Report the tests and static checks actually executed, with outcomes. Never fabricate test results.
- Consider the architecture-review skill for major feature additions or refactors; it does not automatically run on each edit.
