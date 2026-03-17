import json
import os
import pytest
from pathlib import Path


@pytest.fixture
def brand_dir(tmp_path):
    """Create a fake brand directory structure matching on-disk conventions."""
    brand = tmp_path / "brand"
    brand.mkdir()

    # Default profile — uses company_profile.json (matches existing on-disk convention)
    (brand / "company_profile.json").write_text(json.dumps({
        "name": "Movara",
        "brand_voice": "premium and minimal"
    }))
    (brand / "brand_config.json").write_text(json.dumps({
        "primary_color": "#1A1A1A",
        "font": "Inter"
    }))

    # Client profile — uses profile.json
    client_dir = brand / "clients" / "test-client"
    client_dir.mkdir(parents=True)
    (client_dir / "profile.json").write_text(json.dumps({
        "name": "Test Client Co",
        "brand_voice": "bold and direct"
    }))
    (client_dir / "brand_config.json").write_text(json.dumps({
        "primary_color": "#FF0000"
    }))

    return brand


def test_load_default_profile(brand_dir, monkeypatch):
    """load_brand() with no slug returns default company_profile.json."""
    import tools.brand_loader as bl
    monkeypatch.setattr(bl, "BRAND_DIR", brand_dir)

    profile, config = bl.load_brand()
    assert profile["name"] == "Movara"
    assert config["font"] == "Inter"


def test_load_client_profile(brand_dir, monkeypatch):
    """load_brand('test-client') returns client-specific profile.json."""
    import tools.brand_loader as bl
    monkeypatch.setattr(bl, "BRAND_DIR", brand_dir)

    profile, config = bl.load_brand("test-client")
    assert profile["name"] == "Test Client Co"
    assert config["primary_color"] == "#FF0000"


def test_missing_client_returns_empty_dicts(brand_dir, monkeypatch):
    """load_brand() with unknown slug returns empty dicts (no crash)."""
    import tools.brand_loader as bl
    monkeypatch.setattr(bl, "BRAND_DIR", brand_dir)

    profile, config = bl.load_brand("nonexistent-client")
    assert profile == {}
    assert config == {}


def test_missing_default_returns_empty_dicts(tmp_path, monkeypatch):
    """load_brand() with empty brand dir returns empty dicts."""
    import tools.brand_loader as bl
    monkeypatch.setattr(bl, "BRAND_DIR", tmp_path / "brand")

    profile, config = bl.load_brand()
    assert profile == {}
    assert config == {}


def test_active_client_env_var(brand_dir, monkeypatch):
    """load_brand() with no slug reads ACTIVE_CLIENT env var as fallback."""
    import tools.brand_loader as bl
    monkeypatch.setattr(bl, "BRAND_DIR", brand_dir)
    monkeypatch.setenv("ACTIVE_CLIENT", "test-client")

    profile, config = bl.load_brand()  # no explicit slug
    assert profile["name"] == "Test Client Co"
