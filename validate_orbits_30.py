# Calculate the validation difference of the orbits with initial points in billiard_hex.initial_points_30 .
import numpy as np
import mpmath as mp
import pickle

import general_lib
import billiard_hex

main_orbit_num_iter = 500000
validation_num_iter = 50000
main_orbit_dps = 30
validation_dps = 40
num_decimals_in_name = 20

mp.mp.dps = main_orbit_dps

for (i, initial_point) in enumerate(billiard_hex.initial_points_30):
    initial_phi, initial_p = initial_point
    validation_length = validation_num_iter + 1
    main_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, main_orbit_num_iter,
                                          precision=main_orbit_dps)
    validation_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, validation_num_iter,
                                                precision=validation_dps)
    with open(main_filename, "rb") as file:
        main_data = pickle.load(file)[:validation_length, 1:]
    with open(validation_filename, "rb") as file:
        validation_data = pickle.load(file)[:, 1:]
    print(f"The max difference for orbit {i} is {mp.nstr(np.abs(main_data - validation_data).max(), n=3)}")
# The max difference for orbit 0 is 2.33e-21
# The max difference for orbit 1 is 3.86e-20
# The max difference for orbit 2 is 1.59e-19
# The max difference for orbit 3 is 6.78e-18
# The max difference for orbit 4 is 5.02e-20
# The max difference for orbit 5 is 3.02e-18
