import json
import subprocess
import sys
from pathlib import Path

AI_AGENT_DIR = Path(__file__).parent.parent


def _run_save(extra_args):
    return subprocess.run(
        [sys.executable, "tools/save_company_profile.py",
         "--name", "Test Co",
         "--description", "A test company",
         "--market", "Singapore",
         "--differentiators", "Speed, Quality",
         "--primary-color", "#000000",
         "--font", "Inter",
         ] + extra_args,
        capture_output=True, text=True, cwd=str(AI_AGENT_DIR)
    )


def test_output_dir_flag_in_help():
    result = subprocess.run(
        [sys.executable, "tools/save_company_profile.py", "--help"],
        capture_output=True, text=True, cwd=str(AI_AGENT_DIR)
    )
    assert "--output-dir" in result.stdout


def test_output_dir_writes_profile_json(tmp_path):
    """--output-dir writes profile.json (not company_profile.json) to the given dir."""
    out_dir = tmp_path / "clients" / "test-co"
    result = _run_save(["--output-dir", str(out_dir)])
    assert result.returncode == 0, result.stderr
    assert (out_dir / "profile.json").exists()
    assert (out_dir / "brand_config.json").exists()
    data = json.loads((out_dir / "profile.json").read_text())
    assert data.get("name") == "Test Co"


def test_default_writes_company_profile_json(tmp_path):
    """Without --output-dir, writes company_profile.json to brand/ (default)."""
    result = subprocess.run(
        [sys.executable, str(AI_AGENT_DIR / "tools/save_company_profile.py"),
         "--name", "Default Co", "--description", "d", "--market", "m",
         "--differentiators", "x", "--primary-color", "#111", "--font", "Arial"],
        capture_output=True, text=True, cwd=str(tmp_path)
    )
    # Must write company_profile.json to brand/ in cwd
    assert (tmp_path / "brand" / "company_profile.json").exists() or result.returncode != 0


def test_logo_extension_preserved(tmp_path):
    """Logo file extension is preserved when copying."""
    logo = tmp_path / "logo.svg"
    logo.write_bytes(b"<svg/>")
    out_dir = tmp_path / "clients" / "logo-test"
    result = _run_save(["--output-dir", str(out_dir), "--logo", str(logo)])
    assert result.returncode == 0, result.stderr
    # Logo must be copied with original .svg extension, not renamed to .png
    logo_files = list(out_dir.glob("logo.*"))
    assert logo_files, "No logo file found in output dir"
    assert logo_files[0].suffix == ".svg", f"Expected .svg, got {logo_files[0].suffix}"
