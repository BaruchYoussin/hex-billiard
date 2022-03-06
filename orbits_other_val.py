# calculate the validation versions of the orbits with the initial points in billiard_hex.initial_points_other
import numpy as np
import mpmath as mp
import pickle
import time

import general_lib
import billiard_hex


for (num_orbit, initial_point) in enumerate(billiard_hex.initial_points_other):
    mp.mp.dps = billiard_hex.num_digits_val_other[num_orbit]
    num_iterations = billiard_hex.num_iter_val_other[num_orbit]
    initial_phi, initial_p = initial_point
    perf_counter_start = time.perf_counter_ns()
    process_counter_start = time.process_time_ns()
    orbit = general_lib.calculate_orbit(parametric_boundary=billiard_hex.param_boundary, initial_phi=initial_phi,
                                        initial_p=initial_p, num_iterations=num_iterations)
    perf_counter_end = time.perf_counter_ns()
    process_counter_end = time.process_time_ns()
    perf_time = (perf_counter_end - perf_counter_start) / 1e9
    process_time = (process_counter_end - process_counter_start) / 1e9

    filename = billiard_hex.filename(initial_phi, initial_p, n_decimals_in_name=20, num_iter=num_iterations)
    with open(filename, "wb") as file:
        pickle.dump(orbit, file)
    print(f"Created {filename} in {perf_time} sec (process time {process_time} sec)")
# Created orbits_hex/orbit_hex_phi0.2612p0.44734020841438477prec60n_iter50000.pkl in 871.574853114 sec (process time 870.944534401 sec)
# Created orbits_hex/orbit_hex_phi0.26123p0.44734020841438477prec1050n_iter150000.pkl in 8931.005047007 sec (process time 8929.799286289 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.480689prec60n_iter50000.pkl in 812.397826961 sec (process time 812.364374308 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.4806888855prec170n_iter50000.pkl in 922.504438106 sec (process time 922.506010748 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.4806888855prec550n_iter150000.pkl in 4903.872310978 sec (process time 4903.619610111 sec)
