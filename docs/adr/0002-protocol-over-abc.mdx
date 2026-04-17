# ADR-0002: Protocol Over ABC for Adapter Contracts

## Status
Accepted

## Context
rag-axis needs adapter contracts for LLMs, embedders, and vector stores
that allow users to bring their own implementations without inheriting
from rag-axis base classes. ABC (Abstract Base Class) requires explicit
inheritance, creating tight coupling between user code and the library.
This contradicts Design Principle P6 (Boundaries Absorb Provider Volatility).

## Decision
All adapter contracts are defined as `typing.Protocol` with `runtime_checkable`.
Users implement the Protocol structurally — no inheritance required.
Any class that implements the required methods satisfies the contract.

## Consequences
- Zero coupling between user adapter code and rag-axis internals
- Users can wrap any existing client without subclassing
- Protocol compliance is checkable via `isinstance` at runtime
- Adapter contracts are versioned independently of implementations

## Alternatives Considered
- **ABC with abstract methods**: Rejected. Forces inheritance, tight coupling.
- **Duck typing with no contract**: Rejected. No static analysis support,
  no runtime validation, violates P1 (Zero Silent Failures).
- **Pydantic validators on input**: Rejected. Adds overhead at every call site.