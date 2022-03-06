import mpmath as mp
import general_lib


def _theta_to_one_arc(theta):
    return (theta - mp.pi/6) % (mp.pi/3) + mp.pi/3


def h(theta):
    transformed_theta = _theta_to_one_arc(theta)
    sin = mp.sin(transformed_theta)
    return mp.sqrt((9/4) * mp.cos(transformed_theta) ** 2 + (3/2) * sin ** 2) + (1/2) * sin


def h_deriv(theta):
    transformed_theta = _theta_to_one_arc(theta)
    sin = mp.sin(transformed_theta)
    cos = mp.cos(transformed_theta)
    return cos/2 - (3 * cos * sin) / (4 * mp.sqrt((9/4) * cos ** 2 + (3/2) * sin ** 2))


def filename(phi: mp.mpf, p: mp.mpf, n_decimals_in_name: int, num_iter: int, precision: int = None) -> str:
    """The name of the file containing the orbit."""
    if precision is None:
        precision = mp.mp.dps
    return f"orbits_hex/orbit_hex_phi{mp.nstr(phi, n=n_decimals_in_name)}p{mp.nstr(p, n=n_decimals_in_name)}prec{precision}n_iter{num_iter}.pkl"


param_boundary = general_lib.parametric_from_supporting(h, h_deriv)

# Orbits calculated in the files orbits_30.py and (validation) orbits_30_val.py:
mp.mp.dps = 40
initial_points_30 = [(mp.mpf("0.26"), mp.mpf("0.44734020841438477")),
                     (mp.mpf("0.261"), mp.mpf("0.44734020841438477")),
                     (mp.mpf("0.2612330773570752"), mp.mpf("0.447")),
                     (mp.mpf("0.2612330773570752"), mp.mpf("0.4473")),
                     (mp.mpf("0.2612330773570752"), mp.mpf("0.448")),
                     (mp.mpf("0.2612330773570752"), mp.mpf("0.4474"))]
colors_30 = ["brown" , "blue", "red", "green" , "cyan", "orange"]

# Orbits calculated in the files orbits_other.py and (validation) orbits_other_val.py:
mp.mp.dps = 1100
initial_points_other = [(mp.mpf("0.2612"), mp.mpf("0.44734020841438477")),
                        (mp.mpf("0.26123"), mp.mpf("0.44734020841438477")),
                        (mp.mpf("0.06476110449368037"), mp.mpf("0.480689")),
                        (mp.mpf("0.06476110449368037"), mp.mpf("0.4806888855")),
                        (mp.mpf("0.06476110449368037"), mp.mpf("0.4806888855"))]
colors_other =["magenta", "cyan", "red", "blue", "blue"]
# These orbits have varying values of the precision and number of iterations:
num_digits_other = [50, 1000, 50, 150, 500]
num_digits_val_other = [60, 1050, 60, 170, 550]
num_iter_other = [500000, 150000, 50000, 50000, 150000]
num_iter_val_other = [50000, 150000, 50000, 50000, 150000]
