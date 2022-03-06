from unittest import TestCase

import mpmath as mp
import numpy as np
import billiard_hex
import general_lib


class Test(TestCase):
    def test_parametric_from_supporting(self):
        mp.mp.dps = 30
        point = general_lib.parametric_from_supporting(billiard_hex.h,
                                                       billiard_hex.h_deriv)(mp.mpf(0))
        self.assertAlmostEqual((1/2) + mp.sqrt(3/2), point[0], 30)
        self.assertAlmostEqual(mp.mpf(0), point[1], 30)
        self.assertNotAlmostEqual((1/2) + mp.sqrt(3/2) + mp.mpf(10) ** (-29), point[0], 30)
        self.assertNotAlmostEqual(mp.mpf(10) ** (-29), point[1], 30)
        mp.mp.dps = 500
        point = general_lib.parametric_from_supporting(
            billiard_hex.h,
            billiard_hex.h_deriv)(mp.mpf(
            "0.100000000000000005551115123125782702118158340454101562500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        ))
        self.assertAlmostEqual(
            mp.mpf(
                "1.7156011262653779326972617548985279759340783918197122098407710467224820354161734584884376476605492461233361357744131243996486701710143596286630847124174120738230776993173592671992981651983345601587469196964733323106127477875331075825482983764762089875820039544240349915881223881072483839844693579378636821665767986692395014242200319057206449005679288564868496390177621926175673072772404709905305164994490283018311028712033469246519053869467473458989087985635785033834929665877072390585959528960349809"
            ), point[0], 500)
        self.assertAlmostEqual(mp.mpf(
            "0.18295041058581159819252600080248525615077880748383247610807495558323678603550460277187657437490261325901524008147807390372576422992997323035137515491967818484020941870632105793148526405381199278848308185603961736931006731497760227134120369519544113564783688445631376345188172496048378675159605520597654866433010431039789897927595211720113071483669187036221159528906440786044838430321815701557363852135061749889882364033184510484427725036954637629262204551572658883377740599214584551324439397717048524"
        ), point[1], 500)

    def test_intersect_line_with_parametric_billiard_boundary(self):
        parametric_boundary = general_lib.parametric_from_supporting(billiard_hex.h,
                                                                     billiard_hex.h_deriv)
        mp.mp.dps = 30
        self.assertAlmostEqual(mp.mpf("2.07223695969244525778693871844"),
                               general_lib.intersect_line_with_parametric_billiard_boundary(
                                   parametric_boundary, p=mp.mpf(0), phi=mp.mpf(0.5)),
                               places=29)
        self.assertAlmostEqual(mp.mpf("1.26570980294772341078738612059"),
                               general_lib.intersect_line_with_parametric_billiard_boundary(
                                   parametric_boundary, p=mp.mpf(0.5), phi=mp.mpf(0)),
                               places=30)
        mp.mp.dps = 200
        self.assertAlmostEqual(mp.mpf(
            "2.0722369596924452577869387184388702523103740068716509068217856594391680252138438907330012387542455078685273041825504904408653352113257106422217900009262823390872471636088640429954362751218518762722236"
        ),
            general_lib.intersect_line_with_parametric_billiard_boundary(
                parametric_boundary, p=mp.mpf(0), phi=mp.mpf(0.5)),
            places=198)
        self.assertAlmostEqual(mp.mpf(
            "1.2657098029477234107873861205899405983528737082154291011906517546358312131003309778866498972684681406089800413058725026922494865056362804345018784439063084477847100404602288418496150615356996584249423"
        ),
            general_lib.intersect_line_with_parametric_billiard_boundary(
                parametric_boundary, p=mp.mpf(0.5), phi=mp.mpf(0)),
            places=199)

    def test_reflect_line_at_boundary(self):
        parametric_boundary = general_lib.parametric_from_supporting(billiard_hex.h, billiard_hex.h_deriv)
        mp.mp.dps = 30
        phi, p = general_lib.reflect_line_at_boundary(mp.mpf(0), mp.mpf(0.5), parametric_boundary)
        self.assertAlmostEqual(mp.mpf("2.53141960589544682157477224118"), phi, places=30)
        self.assertAlmostEqual(mp.mpf("0.537593984962406015037593984962"), p, places=30)
        mp.mp.dps = 200
        phi, p = general_lib.reflect_line_at_boundary(mp.mpf(0), mp.mpf(0.5), parametric_boundary, )
        self.assertAlmostEqual(mp.mpf(
            "2.5314196058954468215747722411798811967057474164308582023813035092716624262006619557732997945369362812179600826117450053844989730112725608690037568878126168955694200809204576836992301230713993168498845"
        ), phi, places=30)
        self.assertAlmostEqual(mp.mpf(
            "0.53759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601503759398496240601504"
        ), p, places=30)
        # test whether max_iter is enough (if not, findroot throws an exception):
        mp.mp.dps = 30000
        phi, p = general_lib.reflect_line_at_boundary(mp.mpf(0), mp.mpf(0.5), parametric_boundary)

    def test_iterate_function(self):
        def fn(x):
            return x + 1

        self.assertSequenceEqual(list(range(11)), general_lib.iterate_function(fn, 0, 10))

        def fn(x, a):
            return x + a

        self.assertSequenceEqual(list(range(0, 22, 2)), general_lib.iterate_function(fn, 0, 10, 2))

        def fn(x, a, b):
            return x + a + b

        self.assertSequenceEqual(list(range(0, 22, 2)), general_lib.iterate_function(fn, 0, 10, 1, 1))
        self.assertSequenceEqual(list(range(0, 22, 2)), general_lib.iterate_function(fn, 0, 10, 1, b = 1))
        self.assertSequenceEqual(list(range(0, 22, 2)), general_lib.iterate_function(fn, 0, 10, a = 1, b = 1))

        def fn(x, y, a, b):
            return x + a, y + b

        self.assertSequenceEqual(list(zip(range(11), range(1, 12))), general_lib.iterate_function(fn, (0, 1), 10, 1, 1))
        self.assertSequenceEqual(list(zip(range(11), range(1, 12))), general_lib.iterate_function(fn, (0, 1), 10,
                                                                                                  b = 1, a = 1))

    def test_calculate_orbit(self):
        parametric_boundary = general_lib.parametric_from_supporting(billiard_hex.h, billiard_hex.h_deriv)
        mp.mp.dps = 50
        init_phi = 0.1
        init_p = 0.6
        phi1, p1 = general_lib.reflect_line_at_boundary(init_phi, init_p, parametric_boundary)
        phi2, p2 = general_lib.reflect_line_at_boundary(phi1, p1, parametric_boundary)
        phi3, p3 = general_lib.reflect_line_at_boundary(phi2, p2, parametric_boundary)
        orbit = general_lib.calculate_orbit(parametric_boundary, init_phi, init_p, 3)
        print(orbit)  # mp.nstr(..) does not help: it does not go into np.array.
        # [[0 mpf('0.10000000000000000555111512312578270211815834045410156')
        #   mpf('0.59999999999999997779553950749686919152736663818359375')]
        #  [1 mpf('2.5080203180341255883385315616279374323304251200634438')
        #   mpf('0.63934102649174410935192349191712008803324803230969031')]
        #  [2 mpf('4.901404589026840728902922727138014370697514017596021')
        #   mpf('0.62647303329950155176700770027482470314042475055534409')]
        #  [3 mpf('1.0367652394856573642080403028542500176903721264680878')
        #   mpf('0.59471865413748669608554891768465030919649812557218623')]]
        self.assertTrue(np.array_equal(np.array([(0, init_phi, init_p), (1, phi1, p1), (2, phi2, p2), (3, phi3, p3)]),
                                       orbit))

    def test_clip_pair_of_arrays(self):
        x = np.array([0.1, 2.3, 0.3, 2.5])
        y = np.array([0.2, 3.4, 3.1, 0.5])
        xclipped, yclipped = general_lib.clip_pair_of_arrays(x, y, 0, 1, 0, 4)
        self.assertTrue(np.array_equal(np.array([0.1, 0.3]), xclipped))
        self.assertTrue(np.array_equal(np.array([0.2, 3.1]), yclipped))
        xclipped, yclipped = general_lib.clip_pair_of_arrays(x, y, 0, 4, 0, 1)
        self.assertTrue(np.array_equal(np.array([0.1, 2.5]), xclipped))
        self.assertTrue(np.array_equal(np.array([0.2, 0.5]), yclipped))
        mp.mp.dps = 50
        x = np.array([mp.mpf(0.1), mp.mpf(2.3), mp.mpf(0.3), mp.mpf(2.5)])
        y = np.array([mp.mpf(0.2), mp.mpf(3.4), mp.mpf(3.1), mp.mpf(0.5)])
        xclipped, yclipped = general_lib.clip_pair_of_arrays(x, y, mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(4))
        self.assertTrue(np.array_equal(np.array([mp.mpf(0.1), mp.mpf(0.3)]), xclipped))
        self.assertTrue(np.array_equal(np.array([mp.mpf(0.2), mp.mpf(3.1)]), yclipped))
        xclipped, yclipped = general_lib.clip_pair_of_arrays(x, y, mp.mpf(0), mp.mpf(4), mp.mpf(0), mp.mpf(1))
        self.assertTrue(np.array_equal(np.array([mp.mpf(0.1), mp.mpf(2.5)]), xclipped))
        self.assertTrue(np.array_equal(np.array([mp.mpf(0.2), mp.mpf(0.5)]), yclipped))



    def test_rescale_array(self):
        array = np.array([0.1, 2.3, 0.3, 2.5])
        self.assertTrue(np.allclose(np.array([-0.9, 1.3, -0.7, 1.5]), general_lib.rescale_array(array, 1, 2),
                                    rtol=0, atol=1e-15))
        array = np.array([0.2, 3.4, 3.1, 0.5])
        self.assertTrue(np.allclose(np.array([0.05, 0.85, 0.775, 0.125]), general_lib.rescale_array(array, 0, 4),
                                    rtol=0, atol=1e-15))
        mp.mp.dps = 50
        array = np.array([mp.mpf(0.1), mp.mpf(2.3), mp.mpf(0.3), mp.mpf(2.5)])
        self.assertTrue(np.abs(np.array([mp.mpf(-0.9), mp.mpf(1.3), mp.mpf(-0.7), mp.mpf(1.5)])
                                    - general_lib.rescale_array(array, mp.mpf(1), mp.mpf(2))).max() < 1e-15)
        array = np.array([mp.mpf(0.2), mp.mpf(3.4), mp.mpf(3.1), mp.mpf(0.5)])
        self.assertTrue(np.abs(np.array([mp.mpf(0.05), mp.mpf(0.85), mp.mpf(0.775), mp.mpf(0.125)])
                               - general_lib.rescale_array(array, mp.mpf(0), mp.mpf(4))).max() < 1e-15)

    def test_circled_discrepancy(self):
        array_1 = np.array([1, 2, 3, 5])
        array_2 = np.array([0.5, 2.3, 0, 2])
        self.assertEqual(0.5, general_lib.circled_discrepancy(array_1, array_2, 3.1))
        array_2 = np.array([1, 2, 0, 2])
        self.assertAlmostEqual(0.1, general_lib.circled_discrepancy(array_1, array_2, 3.1), places=10)
        mp.mp.dps = 50
        array_1 = np.array([1, 2, 3, 2 * mp.pi - 0.1])
        array_2 = np.array([1, 2, 3, 0])
        self.assertAlmostEqual(0.1, general_lib.circled_discrepancy(array_1, array_2, 2 * mp.pi))
