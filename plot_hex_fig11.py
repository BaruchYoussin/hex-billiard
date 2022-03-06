# Create Fig 11 of the paper
import matplotlib.pyplot as plt
import mpmath as mp

import plotting_lib
import billiard_hex

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots(dpi=1200, figsize=(6.4, 3.2))

filenames_and_colors = [(billiard_hex.filename(phi, p, 20, 500000, 30), billiard_hex.colors_30[i])
                        for (i, (phi, p)) in enumerate(billiard_hex.initial_points_30)]
filename_0_others = billiard_hex.filename(*billiard_hex.initial_points_other[0], 20, billiard_hex.num_iter_other[0],
                                            billiard_hex.num_digits_other[0])
filenames_and_colors = filenames_and_colors + [(filename_0_others, billiard_hex.colors_other[0]),
                                               ("orbits_hex/singular_orbit_5_12_prec100.pkl", "black",
                                                {"markersize": 10})]

mp.mp.dps = 50

plotting_lib.mpf_plot(ax,
                      [plotting_lib.get_data_and_color(*filename_and_color) for filename_and_color
                       in filenames_and_colors],
                      xlow=0.26, xhigh=0.263, ylow=0.4465,
                      yhigh=0.4485, xticks_num=7, yticks_num=5)
ax.set_xlabel("phi", loc="right")
ax.set_ylabel("p", loc="top", rotation=0)
# plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
fig.savefig("plots_hex/plot_hex_fig11.png")
