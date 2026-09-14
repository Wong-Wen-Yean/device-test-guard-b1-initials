# DeviceTest Guard architecture

DeviceTest Guard is a fictional, dependency-free Python teaching sample. It is not an Intel system and its values are not product specifications.

- `device_test_guard/models.py`: immutable training records and batch summaries.
- `device_test_guard/validation.py`: record input and boundary validation.
- `device_test_guard/yield_analysis.py`: deterministic batch-yield calculation.
- `device_test_guard/disposition.py`: RELEASE, RETEST, or HOLD decision.
- `device_test_guard/service.py`: orchestration for one batch.
- `tests/`: executable acceptance evidence.

Flow: records -> validate -> calculate yield -> decide disposition -> batch summary.
