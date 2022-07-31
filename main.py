# this main.py serves as a run script
# this structure is probably an over-kill for a simple calculation,
# but it serves a way to show basic understanding of using python in a
# more structured way to benefit large scale projects.

import pandas as pd
import classes.Reins_QS as reins

# setup local folders for inputs and outputs, need to replace accordingly
in_dir = r'//Users/longwu/PycharmProjects/Reins_QS/z_inputs/'
out_dir = r'//Users/longwu/PycharmProjects/Reins_QS/z_outputs/'

# setup file names for inputs
# PX_reins_parameters.csv contains reins layer structures for Program X
# PX_aglr.csv contains annual gross loss ratio schedules
pa_reins_para_fn = 'PA_reins_parameters.csv'
pb_reins_para_fn = 'PB_reins_parameters.csv'
pa_aglr_fn = 'PA_aglr.csv'
pb_aglr_fn = 'PB_aglr.csv'

# import inputs
pa_reins_par = pd.read_csv(in_dir + pa_reins_para_fn)
pb_reins_par = pd.read_csv(in_dir + pb_reins_para_fn)

pa_aglr = pd.read_csv(in_dir + pa_aglr_fn)
pb_aglr = pd.read_csv(in_dir + pb_aglr_fn)

# inputs are properties for object QS, which currently contains the methods for
# cumulative gross loss ratios (cglr) and cumulative reinsured loss (crl)
p_a = reins.QS(pa_aglr, pa_reins_par)
p_b = reins.QS(pb_aglr, pb_reins_par)

# calculate crl
pa_crl = p_a.crl()
pb_crl = p_b.crl()

# add Programs ID
pa_crl['Programs'] = "A"
pb_crl['Programs'] = "B"

# combine both into one table
output = pd.concat([pa_crl, pb_crl])

# output to csv
output.to_csv(out_dir + "cumulative_reinsured_losses.csv", index=False)

