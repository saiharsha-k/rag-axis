# ADR-0001: Frozen Dataclass Over Pydantic BaseModel for Domain Objects

## Status
Accepted

## Context
rag-axis operates a live query pipeline where retrieval, reranking,
and context assembly run on the hot path under real-time latency constraints.
Pydantic BaseModel instantiation is approximately 8x more expensive than
a standard Python class. Attribute access is 50% slower than dataclasses.
Using BaseModel for internal domain objects (Document, Chunk, CostReport)
would introduce measurable overhead on every query.

## Decision
All internal domain objects are `@dataclass(frozen=True)`.
Pydantic BaseModel is used only at external boundaries:
config ingestion, provider response parsing, and user-facing API types.

## Consequences
- Zero validation overhead on the hot path
- Immutability enforced at the type level (supports Invariant I7)
- Domain objects cannot be accidentally mutated between pipeline stages
- Engineers must validate once at the boundary and pass clean objects inward

## Alternatives Considered
- **Pydantic BaseModel everywhere**: Rejected. Unacceptable hot-path overhead.
- **attrs**: Valid alternative. Rejected in favour of stdlib dataclasses
  to minimise dependencies in rag_axis.core.
- **Plain dicts**: Rejected. No type safety, no IDE support, no contract enforcement.