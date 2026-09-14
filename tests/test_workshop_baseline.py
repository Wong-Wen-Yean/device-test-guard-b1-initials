import unittest

from device_test_guard.disposition import decide_disposition
from device_test_guard.models import DeviceTestRecord
from device_test_guard.validation import validate_record
from device_test_guard.yield_analysis import calculate_yield


def record(device_id: str, passed: bool = True, temperature: float = 25.0, voltage: float = 1.0, retest_count: int = 0):
    return DeviceTestRecord(device_id, temperature, voltage, {"logic": passed}, retest_count)


class WorkshopBaselineTests(unittest.TestCase):
    def test_valid_temperature_boundaries_are_inclusive(self):
        self.assertEqual(validate_record(record("LOW", temperature=10.0)), ())
        self.assertEqual(validate_record(record("HIGH", temperature=85.0)), ())

    def test_voltage_outside_range_is_rejected(self):
        self.assertIn("voltage is outside the training range", validate_record(record("X", voltage=1.21)))

    def test_yield_is_calculated_as_percentage(self):
        rows = [record("A"), record("B"), record("C"), record("D", passed=False)]
        self.assertEqual(calculate_yield(rows), 75.0)

    def test_empty_batch_yield_is_zero(self):
        self.assertEqual(calculate_yield([]), 0.0)

    def test_good_batch_is_released(self):
        self.assertEqual(decide_disposition([record("A"), record("B")], 90.0)[0], "RELEASE")

    def test_low_yield_can_be_retested(self):
        self.assertEqual(decide_disposition([record("A"), record("B", passed=False)], 90.0)[0], "RETEST")

    def test_duplicate_device_identifiers_hold_batch(self):
        self.assertEqual(decide_disposition([record("A"), record("A")], 90.0)[0], "HOLD")


if __name__ == "__main__":
    unittest.main()
