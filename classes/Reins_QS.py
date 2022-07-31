import functions.apply_layers as layering


class QS:
    def __init__(self, aglr, reins):
        '''
        :param aglr: annual gross loss ratios
        :param reins: reinsured layer schedules
        '''
        self.aglr = aglr
        self.reins = reins

    # calculate cumulative gross loss ratio
    def cglr(self):
        df = self.aglr.copy()
        df.iloc[:, 1:] = df.iloc[:, 1:].cumsum(axis=1)
        return df

    # calculate cumulative reinsured loss
    def crl(self):
        df = self.cglr().copy()
        df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x: layering.lr_pct_layers(x, reins_skd=self.reins))
        return df

