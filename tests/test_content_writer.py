import pytest
from pathlib import Path


def test_build_prompt_contains_brief():
    from tools.content_writer import build_prompt
    prompt = build_prompt(
        brief="Launch a new product",
        fmt="instagram",
        tone="premium",
        max_words=150,
        count=3,
        profile={"name": "Movara", "brand_voice": "minimal and premium"}
    )
    assert "Launch a new product" in prompt
    assert "Movara" in prompt


def test_build_prompt_uses_brand_voice():
    from tools.content_writer import build_prompt
    prompt = build_prompt(
        brief="Post about renovation",
        fmt="facebook",
        tone="",
        max_words=200,
        count=3,
        profile={"name": "BuildCo", "brand_voice": "authoritative and warm"}
    )
    assert "authoritative and warm" in prompt


def test_build_prompt_word_limit():
    from tools.content_writer import build_prompt
    prompt = build_prompt(
        brief="Launch a new product",
        fmt="instagram",
        tone="",
        max_words=150,
        count=3,
        profile={"name": "Movara"}
    )
    assert "150" in prompt


def test_word_limits_keys():
    from tools.content_writer import WORD_LIMITS
    for fmt in ["instagram", "facebook", "linkedin", "email", "blog", "script", "calendar", "social"]:
        assert fmt in WORD_LIMITS
        assert WORD_LIMITS[fmt] > 0


def test_output_path_email_format(tmp_path, monkeypatch):
    from tools import content_writer as cw
    monkeypatch.setattr(cw, "TMP_DIR", tmp_path)
    path = cw.get_output_path("email", "acme")
    assert path.name == "email_body_acme.md"


def test_output_path_non_email_format(tmp_path, monkeypatch):
    from tools import content_writer as cw
    monkeypatch.setattr(cw, "TMP_DIR", tmp_path)
    path = cw.get_output_path("instagram", "acme")
    assert path.name == "content_acme.md"


def test_output_path_no_client(tmp_path, monkeypatch):
    from tools import content_writer as cw
    monkeypatch.setattr(cw, "TMP_DIR", tmp_path)
    path = cw.get_output_path("blog", None)
    assert "default" in path.name
