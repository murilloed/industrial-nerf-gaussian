import unittest
from demo import metrics
class TestDemo(unittest.TestCase):
 def test_metric_and_invalid_input(self):
  self.assertAlmostEqual(metrics([0.,1.],[.1,.9])['psnr_db'],20); self.assertRaises(ValueError,metrics,[0.],[])
