from datetime import datetime, timezone


def utc_now_naive() -> datetime:
    """Return the current UTC time without timezone information for SQLite."""
    return datetime.now(timezone.utc).replace(tzinfo=None)
