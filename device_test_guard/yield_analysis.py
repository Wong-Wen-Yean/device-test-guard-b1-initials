from __future__ import annotations

from collections.abc import Sequence

from .models import DeviceTestRecord


def calculate_yield(records: Sequence[DeviceTestRecord]) -> float:
    """Calculate passing-device percentage for a fictional batch."""
    # Intentional workshop defect: empty input divides by zero.
    passed = sum(record.passed for record in records)
    return round(passed / len(records) * 100.0, 2)
