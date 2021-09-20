import unittest
from anglecalc import *

class TestAngleCalc(unittest.TestCase):
  def test_boundTo180(self):
    # Given Examples
    self.assertAlmostEqual(boundTo180(360), 0)
    self.assertAlmostEqual(boundTo180(270), -90)
    self.assertAlmostEqual(boundTo180(-450), -90)

    # Additional Tests
    self.assertAlmostEqual(boundTo180(450), 90)
    self.assertAlmostEqual(boundTo180(0), 0)
    self.assertAlmostEqual(boundTo180(180), -180)
    self.assertAlmostEqual(boundTo180(-180), -180)
    self.assertAlmostEqual(boundTo180(540), -180)
    self.assertAlmostEqual(boundTo180(195), -165)
    self.assertAlmostEqual(boundTo180(200.999), -159.001)

  # def test_isAngleBetween(self):
    # Given Examples
    # self.assertEqual(isAngleBetween(-90, -180, 110), True)
    # self.assertEqual(isAngleBetween(-90, -180, 80), True)
