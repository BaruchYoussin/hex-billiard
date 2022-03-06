import numpy as np
import mpmath as mp
import matplotlib.axes
import general_lib
import colors_lib


def _to_mpf(value) -> mp.mpf:
    """Converts a value into mp.mpf; if it is not a string or an mpf, first converts into a string and then to mpf."""
    if not isinstance(value, mp.mpf):
        value = str(value)
    return mp.mpf(value)


def _get_ticks(ticks_start, ticks_end, ticks_num, low, high) -> tuple:
    """Create ticks for a plot obtained by rescaling.

    :param ticks_start: The first tick value, possibly a string for mpmath.
    :param ticks_end: The last tick value, possibly a string for mpmath.
    :param ticks_num: The total number of ticks including the start and the end.
    :param low, high: The low and the high values for rescaling the data.
    :returns scaled_ticks, ticks
        (scaled_ticks are compared with the scaled data while ticks is a list of strings which are displayed.
    """
    ticks_start = _to_mpf(ticks_start)
    ticks_end = _to_mpf(ticks_end)
    tick_values = mp.linspace(ticks_start, ticks_end, ticks_num)
    scaled_ticks = general_lib.rescale_array(np.array(tick_values), low, high).tolist()
    mp.pretty = True
    ticks = [str(tick) for tick in tick_values]
    return scaled_ticks, ticks


def mpf_plot(axes: matplotlib.axes.Axes, plotting_data: list, xlow, xhigh, ylow, yhigh, xticks_num: int,
             yticks_num: int, xticks_start=None, xticks_end=None, yticks_start=None, yticks_end=None) -> None:
    """Plot the data after clipping, even if clipping goes beyond machine precision by using mpmath.

    :param axes: whether to plot.
    :param plotting_data: a list of tuples (xdata, ydata, color) or (xdata, ydata, color, kwargs)
        where xdata and ydata are array-like
        of equal length, color is one color to plot them, and kwargs, if present, are passed to axes.plot(..).
        The following default values override the default values of axes.plot(..):
        linestyle="", marker=".", markersize=1.
    :param xlow: the lower limit to clip on the x axis, possibly a string for mpmath.
    :param xhigh: the upper limit to clip on the x axis, possibly a string for mpmath.
    :param ylow: the lower limit to clip on the y axis, possibly a string for mpmath.
    :param yhigh: the upper limit to clip on the y axis, possibly a string for mpmath.
    :param xticks_num: The total number of xticks including the start and the end.
    :param yticks_num: The total number of yticks including the start and the end.
    :param xticks_start: The first value of xtick, possibly a string for mpmath; default: xlow.
    :param xticks_end: The last value of xtick, possibly a string for mpmath; default: xhigh.
    :param yticks_start: The first value of ytick, possibly a string for mpmath; default: ylow.
    :param yticks_end: The last value of ytick, possibly a string for mpmath; default: yhigh.
    """
    xlow = _to_mpf(xlow)
    xhigh = _to_mpf(xhigh)
    ylow = _to_mpf(ylow)
    yhigh = _to_mpf(yhigh)
    if xticks_start is None:
        xticks_start = xlow
    if xticks_end is None:
        xticks_end = xhigh
    if yticks_start is None:
        yticks_start = ylow
    if yticks_end is None:
        yticks_end = yhigh
    axes.set_xlim(0, 1)
    axes.set_ylim(0, 1)
    scaled_xticks, xticks = _get_ticks(xticks_start, xticks_end, xticks_num, xlow, xhigh)
    scaled_yticks, yticks = _get_ticks(yticks_start, yticks_end, yticks_num, ylow, yhigh)
    axes.set_xticks(scaled_xticks, xticks)
    axes.set_yticks(scaled_yticks, yticks)
    for one_plot in plotting_data:
        assert len(one_plot) in [3, 4]
        if len(one_plot) == 3:
            xdata, ydata, color = one_plot
            kwargs = {}
        else:
            xdata, ydata, color, kwargs = one_plot
        clipped_x, clipped_y = general_lib.clip_pair_of_arrays(xdata, ydata, xlow, xhigh, ylow, yhigh)
        scaled_x = general_lib.rescale_array(clipped_x, xlow, xhigh)
        scaled_y = general_lib.rescale_array(clipped_y, ylow, yhigh)
        if "linestyle" not in kwargs:
            kwargs["linestyle"] = ""
        if "marker" not in kwargs:
            kwargs["marker"] = "."
        if "markersize" not in kwargs:
            kwargs["markersize"] = 1
        axes.plot(scaled_x, scaled_y, color=color, **kwargs)


def get_data_and_color(orbit_filename: str, color_name: str, *args) -> tuple:
    """Returns (x_array, y_array, color, *args) given the names of the orbit file and the color."""
    orbit = general_lib.unpickle(orbit_filename)
    return orbit[:, 1], orbit[:, 2], colors_lib.get_plotting_color(color_name), *args
