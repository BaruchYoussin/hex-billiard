# calculate the validation versions of the orbits with the initial points in billiard_hex.initial_points_30
import numpy as np
import mpmath as mp
import pickle
import time

import general_lib
import billiard_hex

mp.mp.dps = 40
num_iterations = 50000

for initial_point in billiard_hex.initial_points_30:
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
# Created orbits_hex/orbit_hex_phi0.26p0.44734020841438477prec40n_iter50000.pkl in 785.747363989 sec (process time 784.995048041 sec)
# Created orbits_hex/orbit_hex_phi0.261p0.44734020841438477prec40n_iter50000.pkl in 775.335753783 sec (process time 774.69491049 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.447prec40n_iter50000.pkl in 750.107222411 sec (process time 749.734263321 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.4473prec40n_iter50000.pkl in 743.033718022 sec (process time 742.968536758 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.448prec40n_iter50000.pkl in 742.560690915 sec (process time 742.501891535 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.4474prec40n_iter50000.pkl in 750.050662928 sec (process time 749.927463003 sec)
