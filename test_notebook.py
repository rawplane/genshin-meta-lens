import json
from pathlib import Path
import nbformat


def test_notebook_structure_and_syntax():
    nb_path = Path("genshin_meta_analysis.ipynb")
    assert nb_path.exists(), "Notebook file must exist"

    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    assert len(nb.cells) >= 10, "Notebook should contain at least 10 cells"

    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    markdown_cells = [c for c in nb.cells if c.cell_type == "markdown"]

    assert len(code_cells) >= 5, "Notebook should contain at least 5 code cells"
    assert (
        len(markdown_cells) >= 5
    ), "Notebook should contain at least 5 markdown cells"

    # Verify key sections exist
    md_text = "\n".join(c.source for c in markdown_cells)
    assert "Executive Summary" in md_text
    assert "Popularity & Pull Meta" in md_text
    assert "Constellation Efficiency" in md_text
    assert "Element & Role Ecosystem" in md_text
    assert "Powercreep Analysis" in md_text
