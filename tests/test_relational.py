"""Test the relational plots."""

import seaborn as sns

from atmospy import load_dataset, regplot


def test_scatter_basics():
    df = load_dataset("air-sensors-pm")

    ax = regplot(
        df,
        x="Reference",
        y="Sensor A",
    )

    assert isinstance(ax, sns.axisgrid.JointGrid)
