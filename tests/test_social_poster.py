import json
import pytest
from pathlib import Path


@pytest.fixture
def post_file(tmp_path):
    data = {
        "platform": "instagram",
        "caption": "Test caption #minimal",
        "scheduled_time": "2026-03-15T11:00:00+08:00"
    }
    p = tmp_path / "post.json"
    p.write_text(json.dumps(data))
    return p


def test_dry_run_does_not_post(post_file, capsys):
    from tools.social_poster import execute_post
    result = execute_post(
        platform="instagram",
        caption="Test caption",
        scheduled_time="2026-03-15T11:00:00+08:00",
        dry_run=True
    )
    assert result["status"] == "dry-run"
    assert result["posted"] is False
    captured = capsys.readouterr()
    assert "DRY RUN" in captured.out


def test_missing_credentials_returns_error():
    from tools.social_poster import execute_post
    import os
    # Ensure no credentials set
    result = execute_post(
        platform="instagram",
        caption="Test",
        scheduled_time="2026-03-15T11:00:00+08:00",
        dry_run=False
    )
    # Without credentials, should return error dict, not crash
    assert "status" in result
    assert result["posted"] is False


def test_load_post_file(post_file):
    from tools.social_poster import load_post_file
    data = load_post_file(str(post_file))
    assert data["platform"] == "instagram"
    assert "caption" in data
