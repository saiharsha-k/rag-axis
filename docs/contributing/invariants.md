# Invariant Checklist

Every PR must pass this checklist before review.
Invariants are never relaxed in a minor or patch release.

## Checklist

- [ ] I1: Every Chunk has parent_doc_id, position, and embedding_model_id
- [ ] I2: No silent truncation — ContextTruncationEvent emitted if context is dropped
- [ ] I3: Every RetrievalResult has a confidence signal or ConfidenceUnknown
- [ ] I4: No adapter suppresses a provider error into generic Exception
- [ ] I5: rag_axis.core has zero provider-specific runtime dependencies
- [ ] I6: No circular imports — dependency direction is one-way
- [ ] I7: No in-place mutation of result objects after construction

## If Your PR Requires Relaxing an Invariant

It is a breaking change. Bump the major version.
Open an ADR before writing code.
Get explicit approval before merging.