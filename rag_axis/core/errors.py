from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class RagAxisError(Exception):
    """Base class for all fatal rag-axis errors. System cannot continue."""

    message: str
    context: dict[str, Any] = field(default_factory=dict)
    run_id: str = ""

    def __str__(self: RagAxisError) -> str:
        return self.message


@dataclass(frozen=True)
class DegradedError(RagAxisError):
    """Base class for degraded-mode errors. System continues; warning is emitted."""


# ---------------------------------------------------------------------------
# Fatal errors
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MissingProvenanceError(RagAxisError):
    """Raised at Chunk construction when provenance fields are absent (I1)."""


@dataclass(frozen=True)
class CorpusVersionMismatchError(RagAxisError):
    """Raised at adapter init when embedder model_id != corpus embedding_model (F4)."""


@dataclass(frozen=True)
class EmptyRetrievalError(RagAxisError):
    """Raised when retrieval returns zero results and no fallback is configured."""


@dataclass(frozen=True)
class OutputSchemaError(RagAxisError):
    """Raised when LLM output does not conform to the expected output schema."""


@dataclass(frozen=True)
class DocumentLoadError(RagAxisError):
    """Raised when a document loader fails to read or parse a source."""


@dataclass(frozen=True)
class UnsupportedFormatError(RagAxisError):
    """Raised when a loader receives a file format it cannot handle."""


@dataclass(frozen=True)
class InputGuardError(RagAxisError):
    """Raised when an input guard rejects the incoming query."""


@dataclass(frozen=True)
class OutputGuardError(RagAxisError):
    """Raised when an output guard rejects the generated response."""


# ---------------------------------------------------------------------------
# Typed adapter errors (I4 — no adapter may raise bare Exception)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RateLimitError(RagAxisError):
    """Provider rate limit hit during an adapter call."""


@dataclass(frozen=True)
class ContextLengthError(RagAxisError):
    """Input exceeds the provider's maximum context length."""


@dataclass(frozen=True)
class ProviderSchemaError(RagAxisError):
    """Provider returned a response that does not match the expected schema."""


@dataclass(frozen=True)
class TransportError(RagAxisError):
    """Network or transport failure during a provider call."""


@dataclass(frozen=True)
class RerankerTimeoutError(RagAxisError):
    """Reranker did not respond within the configured timeout."""


@dataclass(frozen=True)
class RerankerUnavailableError(RagAxisError):
    """Reranker service is unavailable."""


@dataclass(frozen=True)
class LLMTimeoutError(RagAxisError):
    """LLM did not respond within the configured timeout."""


# ---------------------------------------------------------------------------
# Degraded errors (DegradedError — system continues, warning emitted)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ScoreCollapseWarning(DegradedError):  # noqa: N818
    """Score distribution too narrow to produce meaningful ranking (F9).

    Emitted when max(scores) - min(scores) < 0.05.
    Named *Warning intentionally: this is a non-fatal signal, not an error.
    """


@dataclass(frozen=True)
class StaleIndexError(DegradedError):
    """Corpus index age exceeds the configured staleness threshold (F13)."""


@dataclass(frozen=True)
class FallbackActivatedWarning(DegradedError):  # noqa: N818
    """A guard triggered a fallback strategy instead of raising fatally.

    Named *Warning intentionally: fallback activation is informational.
    """
