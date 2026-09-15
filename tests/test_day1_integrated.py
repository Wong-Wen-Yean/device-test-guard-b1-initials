import unittest

from device_test_guard.models import DeviceTestRecord
from device_test_guard.service import analyse_batch
from device_test_guard.validation import validate_record


def record(
    device_id: str = "DEV1",
    passed: bool = True,
    temperature: float = 25.0,
    voltage: float = 1.0,
    retest_count: int = 0,
) -> DeviceTestRecord:
    return DeviceTestRecord(
        device_id, temperature, voltage, {"logic": passed}, retest_count
    )


class Day1IntegratedTests(unittest.TestCase):
    def test_temperature_just_outside_range_is_rejected(self):
        low_record = record("LOW", temperature=9.99)
        high_record = record("HIGH", temperature=85.01)
        self.assertIn(
            "temperature is outside the training range", validate_record(low_record)
        )
        self.assertIn(
            "temperature is outside the training range", validate_record(high_record)
        )

    def test_blank_device_identifier_is_rejected(self):
        blank_record = record("   ")
        self.assertIn("device_id is required", validate_record(blank_record))

    def test_empty_test_results_are_rejected(self):
        empty_results_record = DeviceTestRecord("DEV1", 25.0, 1.0, {})
        self.assertIn(
            "at least one test result is required",
            validate_record(empty_results_record),
        )

    def test_empty_batch_summary_is_zero_and_held(self):
        summary = analyse_batch("BATCH_EMPTY", [])
        self.assertEqual(summary.record_count, 0)
        self.assertEqual(summary.yield_percent, 0.0)
        self.assertEqual(summary.disposition, "HOLD")
        self.assertEqual(summary.reasons, ("batch is empty",))

if __name__ == "__main__":
    unittest.main()
