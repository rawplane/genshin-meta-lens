from pathlib import Path

def test_readme_exists_and_contains_core_sections():
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md should exist"
    content = readme_path.read_text(encoding="utf-8")
    assert len(content) > 500, "README.md should be comprehensive"
    
    # Required sections
    assert "# Genshin Impact Meta Data Analysis" in content
    assert "Executive Summary" in content
    assert "Meta Tier & Pull Analysis" in content
    assert "Constellation Efficiency" in content
    assert "Base Stat Powercreep" in content
    assert "Interactive Notebook" in content
    assert "Installation & Setup" in content
    
    # Key data points
    assert "103" in content  # 103 characters
    assert "Furina" in content or "furina" in content
    assert "Bennett" in content or "bennett" in content
