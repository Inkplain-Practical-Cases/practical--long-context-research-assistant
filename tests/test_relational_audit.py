"""Validate persisted research API HTTP event links without payloads."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_relational_event_audit(tmp_path):
    db = str(tmp_path / "audit.sqlite3")
    rid = provider_record_request_audit("POST", "/research", 200, 3.0, db)
    with sqlite3.connect(db) as connection:
        assert connection.execute("SELECT COUNT(*) FROM research_api_requests WHERE id=?", (rid,)).fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM research_api_events WHERE request_id=?", (rid,)).fetchone()[0] == 1
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
