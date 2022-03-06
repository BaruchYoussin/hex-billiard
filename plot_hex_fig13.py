# Create Fig 12 of the paper
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
                        for (i, (phi, p)) in enumerate(billiard_hex.initial_points_other[:2])]
filenames_and_colors = filenames_and_colors[1:] + [("orbits_hex/singular_orbit_5_12_prec100.pkl", "black",
                                                {"markersize": 10})]

mp.mp.dps = 50

orbits_data_and_colors = [plotting_lib.get_data_and_color(*filename_and_color) for filename_and_color
                          in filenames_and_colors]
# limit orbit number 0, the second chaos orbit, to 130,000 points only:
phi_array, p_array, color = orbits_data_and_colors[0]
orbits_data_and_colors[0] = (phi_array[:130000], p_array[:130000], color)

# plot the origin of the second chaos orbit, which is definite chaos:
phi_chaos, p_chaos = billiard_hex.initial_points_other[1]
chaos_origin_plotting_data = (np.array([phi_chaos]), np.array([p_chaos]), colors_lib.get_plotting_color("black"),
                              {"markersize": 4})
plotting_lib.mpf_plot(ax, orbits_data_and_colors + [chaos_origin_plotting_data],
                      xlow=0.261229, xhigh=0.261235, ylow=0.447335,
                      yhigh=0.447345, xticks_num=7, yticks_num=6)
ax.set_xlabel("phi", loc="right")
ax.set_ylabel("p", loc="top", rotation=0)
# plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
fig.savefig("plots_hex/plot_hex_fig13.png")
