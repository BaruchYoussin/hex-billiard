# calculate the orbits with the initial points in billiard_hex.initial_points_30
import numpy as np
import mpmath as mp
import pickle
import time

import general_lib
import billiard_hex

mp.mp.dps = 30
num_iterations = 500000

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
# Created orbits_hex/orbit_hex_phi0.26p0.44734020841438477prec30n_iter500000.pkl in 7656.475938782 sec (process time 7653.61560465 sec)
# Created orbits_hex/orbit_hex_phi0.261p0.44734020841438477prec30n_iter500000.pkl in 7490.432524914 sec (process time 7489.865215894 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.447prec30n_iter500000.pkl in 7410.24954208 sec (process time 7410.019502046 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.4473prec30n_iter500000.pkl in 7377.230925075 sec (process time 7376.718315349 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.448prec30n_iter500000.pkl in 7361.928565021 sec (process time 7361.484240534 sec)
# Created orbits_hex/orbit_hex_phi0.2612330773570752p0.4474prec30n_iter500000.pkl in 7362.078012995 sec (process time 7361.799900386 sec)
