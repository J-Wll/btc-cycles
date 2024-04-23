"""common utils for artists"""

from __future__ import annotations

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd


class ColorBar:
    """color bar

    Args:
        bitcoin (Bitcoin): bitcoin object

    Attributes:
        norm (matplotlib.Normalize): normalize
        cmap (matplotlib.Colormap): colormap
    """

    def __init__(self, bitcoin: Bitcoin):
        self._set_cmap(bitcoin)

    def _set_cmap(self, bitcoin: Bitcoin) -> None:
        """set colors"""
        self.norm = mcolors.Normalize(
            vmin=bitcoin.prices["distance_ath_perc"].min(),
            vmax=bitcoin.prices["distance_ath_perc"].max(),
        )
        self.cmap = plt.get_cmap("cool")


class ProgressLabels:
    """progress labels

    Args:
        bitcoin (Bitcoin): bitcoin object

    Attributes:
        labels (Series): labels
        predicted_halving_str (str): predicted halving string
    """

    def __init__(self, bitcoin: Bitcoin):
        self._create_labels(bitcoin)

    def _create_labels(self, bitcoin: Bitcoin) -> None:
        self.labels = []

        for progress in [0.00, 0.25, 0.50, 0.75]:
            self.labels.append(
                bitcoin.prices[
                    abs((bitcoin.prices["cycle_progress"] - progress)) < 0.0005
                ]
                .groupby("cycle_id")
                .first()
                .reset_index()
            )

        self.labels = pd.concat(self.labels)
        self.labels["cycle_progress"] = self.labels["cycle_progress"].apply(
            lambda x: round(x, 2)
        )
        # concat groupby objects as formatted strings
        self.labels = self.labels.groupby("cycle_progress")["Date"].apply(
            lambda x: "".join(
                f"{label}\n" for label in x.dt.strftime("%d-%m-%Y").to_list()
            )
        )

        self.predicted_halving_str = r"$\bf{{{} \: (predicted)}}$".format(
            bitcoin.predicted_halving_date.strftime("%d-%m-%Y")
        )

        self.labels.iloc[0] = self.labels.iloc[0] + self.predicted_halving_str
