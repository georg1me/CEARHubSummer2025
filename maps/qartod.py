import pandas as pd
import numpy as np


class Qartod:

    def __init__(self, path):
        self.df = pd.read_csv(path)


    def gross_range_test(self):

        return

    # Spike test checks for data points where

    def spike_test(self, method=1, column=' water_level', threshold=0.007, std=False, window=4):
        df = self.df.copy()
        df['diff'] = df[column].diff()

        if not std:
            df['spiked'] = df['diff'].abs() >= threshold
        else:
            df['spiked'] = df['diff'].abs() >= df['diff'].rolling(window=window).std()

        df['fixed'] = df[column]
        df.loc[df['spiked'], 'fixed'] = np.nan

        if method == 1:
            df.loc[df['spiked'], 'fixed'] = df[column].rolling(window=window).mean()
        elif method == 2:
            df.loc[df['spiked'], 'fixed'] = df[column].rolling(window=window).median()

        return df

    def roc_test(self):

        return

    def flat_line(self):

        return


test = Qartod("../burton.csv")
test.spike_test()

