# calculate the orbits with the initial points in billiard_hex.initial_points_other
import numpy as np
import mpmath as mp
import pickle
import time

import general_lib
import billiard_hex


for (num_orbit, initial_point) in enumerate(billiard_hex.initial_points_other):
    mp.mp.dps = billiard_hex.num_digits_other[num_orbit]
    num_iterations = billiard_hex.num_iter_other[num_orbit]
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
# Created orbits_hex/orbit_hex_phi0.2612p0.44734020841438477prec50n_iter500000.pkl in 7939.238752212 sec (process time 7937.052607677 sec)
# Created orbits_hex/orbit_hex_phi0.26123p0.44734020841438477prec1000n_iter150000.pkl in 8256.414038841 sec (process time 8255.819200738 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.480689prec50n_iter50000.pkl in 766.546897183 sec (process time 766.527431964 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.4806888855prec150n_iter50000.pkl in 875.132815364 sec (process time 875.066043756 sec)
# Created orbits_hex/orbit_hex_phi0.06476110449368037p0.4806888855prec500n_iter150000.pkl in 4480.486867958 sec (process time 4480.181494025 sec)
