# Architecture boundaries and Open–Closed Principle

- Organize modules by business capability; clarify ownership of each data model and rule.
- A class/module should have one primary reason to change (SRP), not one method or one arbitrary file-size target.
- Define stable contracts for change-prone behavior. Prefer new implementations and explicit registration for new variants (OCP).
- Preserve substitutability: implementations respect interface invariants, errors and semantics (LSP).
- Small, client-focused interfaces (ISP); high-level domain logic does not import infrastructure details (DIP).
- Enforce one-way dependencies. UI/infrastructure can depend on application/domain contracts; domain must not depend on UI or persistence SDKs.
- Avoid broad `utils` dumping grounds, cyclic dependencies, and concrete service creation deep inside business logic.
- Do not introduce plugins, factories, or interfaces without demonstrable benefit. Maintain simplicity (KISS).
- When extending an existing system, examine public contracts and prefer incremental compatibility-preserving modifications.
- Before implementing: identify the owning module, dependency direction, intended extension point, test seam, and likely change surface.
