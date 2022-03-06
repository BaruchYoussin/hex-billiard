# Create Fig 17 of the paper
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

import colors_lib
import plotting_lib
import billiard_hex

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots(dpi=1200, figsize=(6.4, 3.2))

filenames_and_colors = [(billiard_hex.filename(phi, p, 20, billiard_hex.num_iter_other[i],
                                               billiard_hex.num_digits_other[i]),
                         billiard_hex.colors_other[i])
                        for (i, (phi, p)) in enumerate(billiard_hex.initial_points_other[:5])]
filenames_and_colors = filenames_and_colors[4:] + [("orbits_hex/singular_orbit_11_27_prec100.pkl", "black",
                                                {"markersize": 7})]

mp.mp.dps = 50

orbits_data_and_colors = [plotting_lib.get_data_and_color(*filename_and_color) for filename_and_color
                          in filenames_and_colors]
plotting_lib.mpf_plot(ax, orbits_data_and_colors,
                      xlow=0.064761, xhigh=0.0647613, ylow=0.48068887,
                      yhigh=0.4806889, xticks_num=4, yticks_num=4)
ax.set_xlabel("phi", loc="right")
ax.set_ylabel("p", loc="top", rotation=0)
# plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
fig.savefig("plots_hex/plot_hex_fig17.png")
