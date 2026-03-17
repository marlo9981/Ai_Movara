import pytest


def test_parse_ddg_results_extracts_fields():
    from tools.seo_analyzer import parse_ddg_results
    # web_search() already normalises to {title, url, snippet} — pass that format through
    raw = [
        {"title": "Best AI tools", "url": "https://example.com", "snippet": "AI is changing everything"},
        {"title": "AI trends 2026", "url": "https://other.com", "snippet": "Latest trends in AI"}
    ]
    results = parse_ddg_results(raw)
    assert len(results) == 2
    assert results[0]["title"] == "Best AI tools"
    assert results[0]["url"] == "https://example.com"
    assert "AI" in results[0]["snippet"]


def test_parse_ddg_results_empty():
    from tools.seo_analyzer import parse_ddg_results
    assert parse_ddg_results([]) == []


def test_format_keyword_output_returns_string():
    from tools.seo_analyzer import format_keyword_output
    results = [
        {"title": "Keyword one", "url": "https://a.com", "snippet": "About keyword one"},
    ]
    output = format_keyword_output("AI tools", results)
    assert "AI tools" in output
    assert "Keyword one" in output


def test_format_keyword_output_no_results():
    from tools.seo_analyzer import format_keyword_output
    output = format_keyword_output("obscure query", [])
    assert "no results" in output.lower() or "unavailable" in output.lower()
