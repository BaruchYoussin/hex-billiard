# Calculate the validation difference of the orbits with initial points in billiard_hex.initial_points_other .
import numpy as np
import mpmath as mp
import pickle

import general_lib
import billiard_hex

num_decimals_in_name = 20

for (num_orbit, initial_point) in enumerate(billiard_hex.initial_points_other):
    main_orbit_dps = billiard_hex.num_digits_other[num_orbit]
    validation_dps = billiard_hex.num_digits_val_other[num_orbit]
    mp.mp.dps = main_orbit_dps
    initial_phi, initial_p = initial_point
    main_orbit_num_iter = billiard_hex.num_iter_other[num_orbit]
    validation_num_iter = billiard_hex.num_iter_val_other[num_orbit]
    validation_length = validation_num_iter + 1
    main_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, main_orbit_num_iter,
                                          precision=main_orbit_dps)
    validation_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, validation_num_iter,
                                                precision=validation_dps)
    with open(main_filename, "rb") as file:
        main_data = pickle.load(file)[:validation_length, 1:]
    with open(validation_filename, "rb") as file:
        validation_data = pickle.load(file)[:, 1:]
    discrepancy_phi = general_lib.circled_discrepancy(main_data[:, 0], validation_data[:, 0], 2 * mp.pi)
    discrepancy_p = np.abs(main_data[:, 1] - validation_data[:, 1]).max()
    print(f"The max difference for orbit {num_orbit} is {mp.nstr(max(discrepancy_phi, discrepancy_p), n=3)}")
# The max difference for orbit 0 is 2.21e-20
# The max difference for orbit 1 is 3.14
# The max difference for orbit 2 is 3.68e-36
# The max difference for orbit 3 is 1.46e-94
# The max difference for orbit 4 is 6.32e-368

# The discrepancy for the orbit 1 is large; calculate the discrepancy with less iterations:
num_orbit = 1
main_orbit_dps = billiard_hex.num_digits_other[num_orbit]
validation_dps = billiard_hex.num_digits_val_other[num_orbit]
mp.mp.dps = main_orbit_dps
initial_phi, initial_p = billiard_hex.initial_points_other[num_orbit]
main_orbit_num_iter = billiard_hex.num_iter_other[num_orbit]
main_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, main_orbit_num_iter,
                                      precision=main_orbit_dps)
validation_filename = billiard_hex.filename(initial_phi, initial_p, num_decimals_in_name, main_orbit_num_iter,
                                            precision=validation_dps)
with open(main_filename, "rb") as file:
    main_data = pickle.load(file)[:, 1:]
with open(validation_filename, "rb") as file:
    validation_data = pickle.load(file)[:, 1:]
for validation_num_iter in [140000, 130000, 120000, 100000]:  # decreasing
    validation_length = validation_num_iter + 1
    main_data = main_data[:validation_length, :]
    validation_data = validation_data[:validation_length, :]
    discrepancy_phi = general_lib.circled_discrepancy(main_data[:, 0], validation_data[:, 0], 2 * mp.pi)
    discrepancy_p = np.abs(main_data[:, 1] - validation_data[:, 1]).max()
    print(
        f"The max difference for {validation_num_iter} iterations is {mp.nstr(max(discrepancy_phi, discrepancy_p), n=3)}"
    )
# The max difference for 140000 iterations is 3.14
# The max difference for 130000 iterations is 6.7e-48
# The max difference for 120000 iterations is 2.1e-127
# The max difference for 100000 iterations is 1.56e-213
