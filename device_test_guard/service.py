from __future__ import annotations

from collections.abc import Iterable

from .disposition import decide_disposition
from .models import BatchSummary, DeviceTestRecord
from .yield_analysis import calculate_yield


def analyse_batch(
    batch_id: str,
    records: Iterable[DeviceTestRecord],
    target_yield: float = 90.0,
) -> BatchSummary:
    """Analyse one fictional batch and return reviewable evidence."""
    materialised = tuple(records)
    yield_percent = calculate_yield(materialised)
    disposition, reasons = decide_disposition(materialised, target_yield)
    return BatchSummary(
        batch_id=batch_id,
        record_count=len(materialised),
        yield_percent=yield_percent,
        disposition=disposition,
        reasons=reasons,
    )
