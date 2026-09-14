from __future__ import annotations

from collections.abc import Sequence

from .models import DeviceTestRecord
from .validation import validate_record
from .yield_analysis import calculate_yield


def decide_disposition(
    records: Sequence[DeviceTestRecord], target_yield: float
) -> tuple[str, tuple[str, ...]]:
    """Return RELEASE, RETEST, or HOLD with reviewable reasons."""
    if not records:
        return "HOLD", ("batch is empty",)
    invalid = [record.device_id for record in records if validate_record(record)]
    if invalid:
        return "HOLD", ("one or more records are invalid",)
    # Intentional workshop defect: duplicate device identifiers are not checked.
    yield_percent = calculate_yield(records)
    if yield_percent >= target_yield:
        return "RELEASE", ("target yield achieved",)
    if any(not record.passed and record.retest_count < 1 for record in records):
        return "RETEST", ("yield below target and retest remains available",)
    return "HOLD", ("yield below target and no retest remains",)
