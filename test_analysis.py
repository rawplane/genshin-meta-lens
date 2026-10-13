import polars as pl
import pytest
from analysis import (
    load_and_clean_data,
    compute_pull_meta,
    compute_constellation_efficiency,
    compute_role_element_matrix,
    compute_stat_powercreep,
)

CSV_PATH = "genshin_impact.csv"


def test_load_and_clean_data():
    df = load_and_clean_data(CSV_PATH)
    assert isinstance(df, pl.DataFrame)
    assert len(df) == 103
    assert "release_year" in df.columns
    assert "release_version_num" in df.columns
    assert "pulls_per_banner" in df.columns
    assert df["release_date"].dtype == pl.Date
    assert df["release_year"].dtype in (pl.Int32, pl.Int64)
    # Check pulls_per_banner non-negative
    assert (df["pulls_per_banner"] >= 0).all()


def test_compute_pull_meta():
    df = load_and_clean_data(CSV_PATH)
    meta_df = compute_pull_meta(df)
    assert isinstance(meta_df, pl.DataFrame)
    assert "character_name" in meta_df.columns
    assert "pull_rank" in meta_df.columns
    # top character has pull_rank 1
    top = meta_df.filter(pl.col("pull_rank") == 1)
    assert len(top) == 1


def test_compute_constellation_efficiency():
    df = load_and_clean_data(CSV_PATH)
    const_df = compute_constellation_efficiency(df)
    assert isinstance(const_df, pl.DataFrame)
    assert "c1_retention" in const_df.columns
    assert "c6_retention" in const_df.columns
    assert "investment_tier" in const_df.columns
    # retention between 0 and 1 or valid float
    assert (const_df["c6_retention"] >= 0).all()


def test_compute_role_element_matrix():
    df = load_and_clean_data(CSV_PATH)
    role_df = compute_role_element_matrix(df)
    assert isinstance(role_df, pl.DataFrame)
    assert "role" in role_df.columns
    assert "element" in role_df.columns
    assert "character_count" in role_df.columns
    assert "avg_pulls" in role_df.columns
    assert len(role_df) > 0


def test_compute_stat_powercreep():
    df = load_and_clean_data(CSV_PATH)
    stat_df = compute_stat_powercreep(df)
    assert isinstance(stat_df, pl.DataFrame)
    assert "release_year" in stat_df.columns
    assert "rarity" in stat_df.columns
    assert "mean_atk" in stat_df.columns
    assert "mean_hp" in stat_df.columns
    assert "mean_def" in stat_df.columns
    assert len(stat_df) > 0
