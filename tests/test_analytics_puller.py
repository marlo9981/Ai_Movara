import pytest
from datetime import date


def test_parse_date_range_valid():
    from tools.analytics_puller import parse_date_range
    start, end = parse_date_range("2026-01-01", "2026-03-01")
    assert start == date(2026, 1, 1)
    assert end == date(2026, 3, 1)


def test_parse_date_range_invalid():
    from tools.analytics_puller import parse_date_range
    with pytest.raises(ValueError):
        parse_date_range("not-a-date", "2026-03-01")


def test_parse_date_range_reversed():
    from tools.analytics_puller import parse_date_range
    with pytest.raises(ValueError, match="start.*before.*end"):
        parse_date_range("2026-03-01", "2026-01-01")


def test_load_csv_metrics(tmp_path):
    from tools.analytics_puller import load_csv_metrics
    csv_file = tmp_path / "metrics.csv"
    csv_file.write_text(
        "date,sessions,clicks,conversions\n"
        "2026-01-01,100,50,5\n"
        "2026-01-02,120,60,8\n"
    )
    metrics = load_csv_metrics(str(csv_file))
    assert metrics["total_rows"] == 2
    assert "sessions" in metrics["columns"]
    assert metrics["data"][0]["sessions"] == "100"


def test_load_csv_missing_file():
    from tools.analytics_puller import load_csv_metrics
    with pytest.raises(FileNotFoundError):
        load_csv_metrics("/nonexistent/file.csv")
