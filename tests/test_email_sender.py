import json
import pytest
from pathlib import Path


@pytest.fixture
def email_list(tmp_path):
    csv = tmp_path / "list.csv"
    csv.write_text("email,name\njohn@example.com,John\njane@example.com,Jane\n")
    return csv


@pytest.fixture
def body_file(tmp_path):
    f = tmp_path / "body.md"
    f.write_text("Hello {{name}},\n\nThis is a test email.\n\nRegards,\nThe Team")
    return f


def test_load_email_list(email_list):
    from tools.email_sender import load_email_list
    recipients = load_email_list(str(email_list))
    assert len(recipients) == 2
    assert recipients[0]["email"] == "john@example.com"
    assert recipients[0]["name"] == "John"


def test_load_email_list_missing_file():
    from tools.email_sender import load_email_list
    with pytest.raises(FileNotFoundError):
        load_email_list("/nonexistent/list.csv")


def test_personalise_body(body_file):
    from tools.email_sender import personalise_body
    body = body_file.read_text()
    result = personalise_body(body, {"name": "Alice", "email": "alice@example.com"})
    assert "Alice" in result
    assert "{{name}}" not in result


def test_dry_run_returns_preview(email_list, body_file, capsys):
    from tools.email_sender import send_campaign
    result = send_campaign(
        subject="Test subject",
        body=body_file.read_text(),
        list_path=str(email_list),
        dry_run=True
    )
    assert result["status"] == "dry-run"
    assert result["recipient_count"] == 2
    captured = capsys.readouterr()
    assert "DRY RUN" in captured.out
