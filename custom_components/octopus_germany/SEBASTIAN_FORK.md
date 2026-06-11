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
## sebastian-stable-v0.0.96-1 (2026-06-11)

- Based on Sebastian stable v0.0.95 fork.
- Incorporated upstream v0.0.96 service response registration (`SupportsResponse.ONLY`) and service description/doc update.
- Preserved production safety flags: `UPDATE_INTERVAL=15`, `EXPLORE_SCHEMA_ONCE=False`, `DEBUG_ENABLED=False`.
- Preserved Python 3 syntax fixes for multi-exception handlers; upstream v0.0.96 still contains invalid `except ValueError, TypeError` syntax in `sensor.py`.

