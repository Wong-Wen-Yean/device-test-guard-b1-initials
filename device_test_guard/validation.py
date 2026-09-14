from __future__ import annotations

from .models import DeviceTestRecord

MIN_TEMPERATURE_C = 10.0
MAX_TEMPERATURE_C = 85.0
MIN_VOLTAGE_V = 0.8
MAX_VOLTAGE_V = 1.2


def validate_record(record: DeviceTestRecord) -> tuple[str, ...]:
    """Return validation problems for one fictional record."""
    problems: list[str] = []
    if not record.device_id.strip():
        problems.append("device_id is required")
    if not MIN_TEMPERATURE_C <= record.temperature_c <= MAX_TEMPERATURE_C:
        problems.append("temperature is outside the training range")
    if not MIN_VOLTAGE_V <= record.voltage_v <= MAX_VOLTAGE_V:
        problems.append("voltage is outside the training range")
    if not record.test_results:
        problems.append("at least one test result is required")
    if any(not isinstance(value, bool) for value in record.test_results.values()):
        problems.append("test results must be boolean")
    if record.retest_count < 0:
        problems.append("retest_count cannot be negative")
    return tuple(problems)
