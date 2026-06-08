# Sebastian production fork

This installed package is maintained for Sebastian's Home Assistant setup.

Base upstream release: thecem/octopus_germany v0.0.95
Fork tag: sebastian-stable-v0.0.95-1

Production deltas:

- Keep `UPDATE_INTERVAL = 15` minutes instead of upstream's 1-minute development/test interval.
- Keep schema exploration disabled in production.
- Keep integration debug logging disabled in production.
- Fix Python 3 multiple-exception syntax in `sensor.py` before installing; upstream v0.0.95 as fetched does not pass `compileall`.
- Point manifest documentation/issue links at the Sebastian fork for provenance.

Do not blindly overwrite this package from upstream HACS without re-applying these production deltas.
