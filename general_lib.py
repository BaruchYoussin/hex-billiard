import pickle

import mpmath as mp
import numpy as np


def parametric_from_supporting(supporting_function, deriv_of_supporting):
    """Construct parametric representation of a curve given its supporting function.

    :param supporting_function: takes mpmath.mpf and returns mpmath.mpf.
    :param deriv_of_supporting: takes mpmath.mpf and returns mpmath.mpf.
    :returns a function that takes the parameter value and returns the x, y coordinates of a plane point.
    """
    def parametric(parameter_value):
        complex_result = supporting_function(parameter_value) + deriv_of_supporting(parameter_value) * mp.j
        complex_result *= mp.exp(mp.j * parameter_value)
        return complex_result.real, complex_result.imag

    return parametric


def deriv_acos(x):
    return mp.mpf(-1) / mp.sqrt(mp.mpf(1) - x * x)


def projection_of_point_onto_direction(point: tuple, direction: mp.mpf) -> mp.mpf:
    """Returns the projection of a given point onto a given direction."""
    exp = mp.exp(mp.j * direction)
    return (mp.matrix(point).T * mp.matrix([exp.real, exp.imag]))[0,0]


def intersect_line_with_parametric_billiard_boundary(parametric_boundary, phi:mp.mpf, p:mp.mpf,
                                                     tolerance=None) -> mp.mpf:
    """Finds the left intersection point of a directed straight line with a parametric billiard boundary.

    :param parametric_boundary: a function mp.mpf -> (mp.mpf, mp.mpf) parametrizing the boundary as a function
        of the direction of its tangent given as the signed angle to the Ox axis.
    :param phi: The signed angle between the Ox axis and the normal to the line which is counterclockwise
        from the line direction.
    :param p: The signed distance from the origin to the line in the direction of the above normal.
    :param tolerance: The tolerance for the squared error to be used in the numeric root finding.
        Default: 10 ** (-2 * mp.mp.dps).
        (Since findroot temporarily increases dps by 6, this assumes that the derivative of the error function
            is < 10 ** 6.)
    :returns The value of the parameter corresponding to the second intersection point of the line with the boundary.
    """
    if tolerance is None:
        tolerance = mp.mpf(10) ** (-1.5 * mp.mp.dps)
    return mp.findroot(
        lambda parameter_value: projection_of_point_onto_direction(parametric_boundary(parameter_value), phi) - p,
        (phi, phi + mp.pi), solver="pegasus", tol=tolerance)


def reflect_line_at_point(parameter_value_of_point: mp.mpf, direction_of_line: mp.mpf) -> mp.mpf:
    """Reflect a directed straight line w.r. to a billiard boundary parametrized by its tangent direction.

    :param parameter_value_of_point: The parameter value of the reflection point on the boundary (which should lie
        on the reflected line).
    :param direction_of_line: The signed angle from the Ox axis to the line direction.
    :returns The direction of the reflected line = (2 * parameter_value_of_point - direction_of_line) modulo 2 pi.
    """
    return (2 * parameter_value_of_point - direction_of_line) % (2 * mp.pi)


def reflect_line_at_boundary(phi: mp.mpf, p:mp.mpf, parametric_boundary, tolerance=None) -> tuple:
    """Reflect a straight line w.r. to the billiard boundary.

    :param phi: The signed angle between the Ox axis and the normal to the line which is counterclockwise
        from the line direction.
    :param p: The signed distance from the origin to the line in the direction of the above normal.
    :param parametric_boundary: a function mp.mpf -> (mp.mpf, mp.mpf) parametrizing the boundary as a function
        of the direction of its tangent given as the signed angle to the Ox axis.
    :param tolerance: The tolerance for the squared error to be used in the numeric root finding.
        Default: 10 ** (-2 * mp.mp.dps).
        (Since findroot temporarily increases dps by 6, this assumes that the derivative of the error function
            is < 10 ** 6.)
    :returns (phi, p) of the reflected line.
    """
    parameter_value_at_intersection = intersect_line_with_parametric_billiard_boundary(
        parametric_boundary, phi=phi, p=p, tolerance=tolerance)
    reflected_phi = reflect_line_at_point(parameter_value_at_intersection, phi)
    reflected_p = projection_of_point_onto_direction(parametric_boundary(parameter_value_at_intersection),
                                                     reflected_phi)
    return reflected_phi, reflected_p


def iterate_function(fn, init_value, num_iter: int, *args, **kwargs) -> list:
    """Apply a function iteratively and return a list of all the results.

    :param fn: The function to apply; the initial and repeated values are substituted in its first parameter, unless
        init_value is a tuple, in which case it is unpacked into the first parameters.
    :param init_value: The initial value, possibly a tuple.
    :param num_iter: The number of iterations to apply.
    :param args: Additional positional arguments to supply to fn after the first parameter.
    :param kwargs: Additional keyword arguments to supply to fn.
    :returns The list [init_value, first result, ...], the total of num_iter + 1 elements.
    """
    def iterator_fn():
        nonlocal init_value
        for n in range(num_iter):
            yield init_value
            init_value = fn(*(init_value if isinstance(init_value, tuple) else (init_value,)), *args, **kwargs)
        yield init_value

    return list(iterator_fn())


def calculate_orbit(parametric_boundary, initial_phi: mp.mpf, initial_p:mp.mpf, num_iterations: int) -> np.array:
    """Create an orbit as an np.array with rows (num_point, phi, p) starting with (0, initial_phi, initial_p)."""
    initial_phi = mp.mpf(initial_phi)
    initial_p = mp.mpf(initial_p)
    result_list = iterate_function(
        lambda n, phi, p: (n + 1, *reflect_line_at_boundary(phi, p, parametric_boundary)),
        init_value=(0, initial_phi, initial_p), num_iter=num_iterations)
    return np.array(result_list)


def unpickle(filename):
    """Unpickle a pkl file"""
    with open(filename, "rb") as file:
        return pickle.load(file)


def clip_pair_of_arrays(x: np.array, y: np.array, xlow, xhigh, ylow, yhigh) -> tuple:
    """Clip a pair of numeric arrays (considered as a list of points in the plane) by a rectangle.

    :param x: the array of the x coordinates, 1-dim.
    :param y: the array of the y coordinates, 1-dim of the same length as x.
        :param xlow: the lower limit to clip on the x axis
    :param xhigh: the upper limit to clip on the x axis
    :param ylow: the lower limit to clip on the y axis
    :param yhigh: the upper limit to clip on the y axis
    :returns x_coords, y_coords of the points that lie in the rectangle (possibly as views on the original x, y).
    """
    condition_array = (x >= xlow) & (x <= xhigh) & (y >= ylow) & (y <= yhigh)
    return x.compress(condition_array, axis=0), y.compress(condition_array, axis=0)


def rescale_array(array: np.ndarray, low, high) -> np.ndarray:
    """Rescale an array making the low value equal 0 and the high value equal 1."""
    return (array - low) / (high - low)


def circled_discrepancy(array_1, array_2, modulus):
    """Returns the max difference between array_1 and array_2 (must be of the same shape) modulo modulus."""
    diff = np.abs((array_2 % modulus)  - (array_1 % modulus))
    return np.minimum(diff, modulus - diff).max()
