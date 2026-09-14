from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class DeviceTestRecord:
    """One fictional device-test result used only for the workshop."""

    device_id: str
    temperature_c: float
    voltage_v: float
    test_results: Mapping[str, bool]
    retest_count: int = 0

    @property
    def passed(self) -> bool:
        return bool(self.test_results) and all(self.test_results.values())


@dataclass(frozen=True)
class BatchSummary:
    batch_id: str
    record_count: int
    yield_percent: float
    disposition: str
    reasons: tuple[str, ...]
