from device_test_guard.models import DeviceTestRecord
from device_test_guard.service import analyse_batch


def main() -> None:
    records = [
        DeviceTestRecord("SYN-001", 25.0, 1.0, {"logic": True, "io": True}),
        DeviceTestRecord("SYN-002", 25.5, 1.0, {"logic": True, "io": False}),
    ]
    print(analyse_batch("TRAINING-BATCH", records, target_yield=90.0))


if __name__ == "__main__":
    main()
