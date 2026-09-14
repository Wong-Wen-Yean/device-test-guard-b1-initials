# DTG-201: trustworthy batch analysis

As a test engineering team member, I need the batch analyser to handle boundary readings, empty batches, and duplicate device identifiers so that its result is predictable and reviewable.

## Fictional training rules

- Temperature is accepted from 10.0 C through 85.0 C, inclusive.
- Voltage is accepted from 0.8 V through 1.2 V, inclusive.
- An empty batch has 0.0% yield and must be held.
- Duplicate device identifiers make the batch invalid and must be held.
- A valid batch at or above the target yield is released.
- A valid batch below target may be retested once; otherwise it is held.

## Acceptance evidence

All unit tests pass, the change is peer-reviewed, and the GitHub Actions check succeeds. These values are invented for training and must not be treated as Intel specifications.
