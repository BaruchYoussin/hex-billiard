from unittest import TestCase
import numpy as np
import mpmath as mp
import plotting_lib


class Test(TestCase):
    def test_to_mpf(self):
        mp.mp.dps = 50
        self.assertEqual(mp.mpf("0.1"), plotting_lib._to_mpf(0.1))
        self.assertEqual(mp.mpf("0.135123665221742145526159"),
                         plotting_lib._to_mpf(mp.mpf("0.135123665221742145526159")))
        self.assertEqual(mp.mpf("0.135123665221742145526159"),
                         plotting_lib._to_mpf("0.135123665221742145526159"))

    def test_get_ticks(self):
        scaled_ticks, ticks = plotting_lib._get_ticks(1.04, 1.05, 3, 1.04, 1.05)
        self.assertTrue(np.abs(np.array([mp.mpf(0), mp.mpf(0.5), mp.mpf(1)]) - np.array(scaled_ticks)).max() < 1e-13)
        self.assertEqual(["1.04", "1.045", "1.05"], ticks)
        scaled_ticks, ticks = plotting_lib._get_ticks("1.04", "1.05", 3, 1.04, 1.05)
        self.assertTrue(np.abs(np.array([mp.mpf(0), mp.mpf(0.5), mp.mpf(1)]) - np.array(scaled_ticks)).max() < 1e-13)
        self.assertEqual(["1.04", "1.045", "1.05"], ticks)
        scaled_ticks, ticks = plotting_lib._get_ticks("1.04", "1.05", 3, mp.mpf("1.04"), mp.mpf("1.05"))
        self.assertTrue(np.abs(np.array([mp.mpf(0), mp.mpf(0.5), mp.mpf(1)]) - np.array(scaled_ticks)).max() < 1e-13)
        self.assertEqual(["1.04", "1.045", "1.05"], ticks)
        mp.mp.dps = 50
        scaled_ticks, ticks = plotting_lib._get_ticks("1.040450456783456454564357", "1.040450456783456454564358", 3,
                                                      mp.mpf("1.040450456783456454564357"),
                                                      mp.mpf("1.040450456783456454564358"))
        self.assertTrue(np.abs(np.array([mp.mpf(0), mp.mpf(0.5), mp.mpf(1)]) - np.array(scaled_ticks)).max() < 1e-13)
        self.assertEqual(["1.040450456783456454564357", "1.0404504567834564545643575", "1.040450456783456454564358"],
                         ticks)
        scaled_ticks, ticks = plotting_lib._get_ticks("1.040450456783456454564357", "1.040450456783456454564358", 3,
                                                      mp.mpf("1.040450456783456454564355"),
                                                      mp.mpf("1.040450456783456454564359"))
        self.assertTrue(np.abs(np.array([mp.mpf(0.5), mp.mpf(0.625), mp.mpf(0.75)]) - np.array(scaled_ticks)).max()
                        < 1e-13)
        self.assertEqual(["1.040450456783456454564357", "1.0404504567834564545643575", "1.040450456783456454564358"],
                         ticks)
