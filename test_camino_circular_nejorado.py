import unittest
import camino_circular_nejorado

class Test_camino(unittest.TestCase):

    def test_case_one(self):
        magic = [2,4,5,2]
        dist = [4,3,1,3]
        result = camino_circular_nejorado.optimalPoint(magic,dist)
        self.assertEqual(result,1)

    def test_case_two (self):
        magic = [2,4,5,2,1]
        dist = [4,3,1,3,4]   
        result = camino_circular_nejorado.optimalPoint(magic,dist)
        self.assertEqual(result,1) 

if __name__ == '__main__':
    unittest.main()        