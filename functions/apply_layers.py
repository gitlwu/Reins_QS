import numpy as np
# this req_cols shows the way to check inputs
req_cols = ["att_lr", "det_lr", "reins_pct"]


def lr_pct_layers(lr, reins_skd):
    # ideally data validation is handled in separate import module
    assert all(i in req_cols for i in reins_skd.columns.values.tolist()), 'check col names'
    assert isinstance(lr, float), 'check loss ratio (lr) format'

    df = reins_skd.copy(deep=True)

    # add reinsurance payout %
    cds = [(lr <= df['att_lr']),
           (df['att_lr'] < lr) & (lr < df['det_lr']),
           (lr >= df['det_lr'])]
    vals = [0,
            (lr - df['att_lr'])*df['reins_pct'],
            (df['det_lr'] - df['att_lr'])*df['reins_pct']]
    df['reins_ls'] = np.select(cds, vals)
    reins_ls = df['reins_ls'].sum()
    return reins_ls

