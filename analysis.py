"""Genshin Impact Meta Analysis Core Pipeline.

Provides clean Polars data loading, metric calculation,
constellation efficiency analysis, role matrix, and powercreep metrics.
"""

from typing import Union
import polars as pl


def load_and_clean_data(csv_path: str = "genshin_impact.csv") -> pl.DataFrame:
    """Load and clean character dataset from CSV."""
    df = pl.read_csv(csv_path)

    # Standardize column mappings if original column names present
    rename_map = {
        "name": "character_name",
        "weapon": "weapon_type",
        "lvl_90_HP": "base_hp_90",
        "lvl_90_ATK": "base_atk_90",
        "lvl_90_DEF": "base_def_90",
        "constellation_0_pull": "c0_pulls",
        "constellation_1_pull": "c1_pulls",
        "constellation_2_pull": "c2_pulls",
        "constellation_3_pull": "c3_pulls",
        "constellation_4_pull": "c4_pulls",
        "constellation_5_pull": "c5_pulls",
        "constellation_6_pull": "c6_pulls",
        "constellation_7_pull": "c7_pulls",
    }
    existing_renames = {k: v for k, v in rename_map.items() if k in df.columns}
    if existing_renames:
        df = df.rename(existing_renames)

    # Cast dates and derive temporal features
    df = df.with_columns(
        pl.col("release_date").str.to_date("%Y-%m-%d").alias("release_date"),
        pl.col("release_date")
        .str.to_date("%Y-%m-%d")
        .dt.year()
        .alias("release_year"),
        pl.col("banner_versions")
        .str.extract(r"(\d+\.\d+)", 1)
        .cast(pl.Float64)
        .fill_null(1.0)
        .alias("release_version_num"),
        pl.when(pl.col("num_banners") > 0)
        .then(pl.col("pulled_count") / pl.col("num_banners"))
        .otherwise(0.0)
        .alias("pulls_per_banner"),
    )

    return df


def compute_pull_meta(df: pl.DataFrame) -> pl.DataFrame:
    """Compute overall pull popularity, rank, and banner efficiency."""
    meta_df = df.with_columns(
        pl.col("pulled_count")
        .rank(method="dense", descending=True)
        .alias("pull_rank"),
        pl.col("pulls_per_banner")
        .rank(method="dense", descending=True)
        .alias("banner_pull_rank"),
    ).sort("pull_rank")

    return meta_df


def compute_constellation_efficiency(df: pl.DataFrame) -> pl.DataFrame:
    """Calculate constellation retention rate and investment tiers."""
    const_df = df.with_columns(
        pl.when(pl.col("c0_pulls") > 0)
        .then(pl.col("c1_pulls") / pl.col("c0_pulls"))
        .otherwise(0.0)
        .alias("c1_retention"),
        pl.when(pl.col("c0_pulls") > 0)
        .then(pl.col("c2_pulls") / pl.col("c0_pulls"))
        .otherwise(0.0)
        .alias("c2_retention"),
        pl.when(pl.col("c0_pulls") > 0)
        .then(pl.col("c6_pulls") / pl.col("c0_pulls"))
        .otherwise(0.0)
        .alias("c6_retention"),
    ).with_columns(
        pl.when(pl.col("c6_rate") >= 0.04)
        .then(pl.lit("Whale Target (High C6 Rate)"))
        .when(pl.col("c1_retention") >= 0.35)
        .then(pl.lit("Moderate Investment (C1-C2 Stop)"))
        .otherwise(pl.lit("F2P Friendly (C0 Complete)"))
        .alias("investment_tier")
    )

    return const_df


def compute_role_element_matrix(df: pl.DataFrame) -> pl.DataFrame:
    """Analyze character distribution and popularity across Element and Role."""
    # Split comma separated roles and explode
    exploded = (
        df.with_columns(pl.col("roles").str.split(","))
        .explode("roles")
        .with_columns(pl.col("roles").str.strip_chars().alias("role"))
    )

    matrix = (
        exploded.group_by(["role", "element"])
        .agg(
            pl.len().alias("character_count"),
            pl.col("pulled_count").mean().round(1).alias("avg_pulls"),
            pl.col("pulls_per_banner")
            .mean()
            .round(1)
            .alias("avg_pulls_per_banner"),
        )
        .sort(["role", "character_count"], descending=[False, True])
    )

    return matrix


def compute_stat_powercreep(df: pl.DataFrame) -> pl.DataFrame:
    """Aggregate base level 90 stats by release year and rarity."""
    powercreep = (
        df.group_by(["release_year", "rarity"])
        .agg(
            pl.len().alias("character_count"),
            pl.col("base_atk_90").mean().round(1).alias("mean_atk"),
            pl.col("base_hp_90").mean().round(1).alias("mean_hp"),
            pl.col("base_def_90").mean().round(1).alias("mean_def"),
            pl.col("base_atk_90").max().alias("max_atk"),
        )
        .sort(["release_year", "rarity"])
    )

    return powercreep
