from unittest import TestCase
import mpmath as mp
import billiard_hex


class Test(TestCase):
    def test__theta_to_one_arc(self):
        mp.mp.dps = 30
        self.assertEqual(mp.pi/2, billiard_hex._theta_to_one_arc(0))
        self.assertEqual(mp.pi/3, billiard_hex._theta_to_one_arc(mp.pi/6))
        self.assertEqual(mp.pi/2, billiard_hex._theta_to_one_arc(mp.pi/3))
        self.assertEqual(399 * mp.pi/600, billiard_hex._theta_to_one_arc(99 * mp.pi/600))

    def test_h(self):
        mp.mp.dps = 30
        self.assertEqual((1/2) + mp.sqrt(3/2), billiard_hex.h(0))
        self.assertAlmostEqual(mp.sqrt(3), billiard_hex.h(mp.pi/2), places=10)

    def test_h_deriv(self):
        mp.mp.dps = 100
        delta = mp.mpf(1e-30)
        self.assertAlmostEqual(mp.mpf(0), billiard_hex.h_deriv(0), 100)
        self.assertAlmostEqual((billiard_hex.h(5 * delta) - billiard_hex.h(4 * delta)) / delta,
                               billiard_hex.h_deriv(mp.mpf("4.5") * delta), places=70)
        self.assertAlmostEqual(0, billiard_hex.h_deriv(mp.pi/2), 100)
        self.assertAlmostEqual((billiard_hex.h(mp.pi/12 + delta) - billiard_hex.h(mp.pi/12)) / delta,
                               billiard_hex.h_deriv(mp.pi/12), places=30)
        self.assertAlmostEqual((billiard_hex.h(11 * mp.pi/24 + delta) - billiard_hex.h(11 * mp.pi/24)) / delta,
                               billiard_hex.h_deriv(11 * mp.pi/24), places=30)
