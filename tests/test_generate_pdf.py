import subprocess
import sys
from pathlib import Path

AI_AGENT_DIR = Path(__file__).parent.parent


def _run(args):
    return subprocess.run(
        [sys.executable, "tools/generate_pdf.py"] + args,
        capture_output=True, text=True, cwd=str(AI_AGENT_DIR)
    )


def test_new_flags_in_help():
    """All new flags must appear in --help output."""
    result = _run(["--help"])
    for flag in ["--input", "--template", "--output", "--client"]:
        assert flag in result.stdout, f"Missing flag in help: {flag}"


def test_template_choices_in_help():
    """All template names from the spec must be listed in --help."""
    result = _run(["--help"])
    for template in ["competitor_analysis", "seo_audit", "media_plan",
                     "performance_report", "campaign_kickoff", "onboarding",
                     "influencer_brief"]:
        assert template in result.stdout, f"Missing template: {template}"


def test_default_input_path_is_analysis_json():
    """Without --input, the tool must attempt to read .tmp/analysis.json."""
    result = _run([])  # no flags — default behaviour
    # Must reference analysis.json specifically in the error output
    combined = result.stderr + result.stdout
    assert "analysis.json" in combined, (
        f"Expected error referencing analysis.json but got:\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
