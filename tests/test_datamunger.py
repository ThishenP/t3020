import unittest
from code.datamunger import *

class TestDatamunger(unittest.TestCase):



    def test_calc_total(self):
        self.assertEqual(calc_total([712,70,140,44,39,227,93,40,49,]),702)
        self.assertEqual(calc_total([811,78,146,55,51,254,103,57,67,0]),811)
        self.assertEqual(calc_total([1204,174,181,94,112,297,145,79,122,165]),1204)
        self.assertEqual(calc_total([-1204,-174,-181,-94,-112,-297,-145,-79,-122]),-1204) #all negatives
        self.assertEqual(calc_total([811,78,-146,55,51,254,-103,57,67,0]),313)  #negative and positive

    def test_check_monatonic(self):
        prev = [811,78,146,55,51,254,103,57,67,0]
        curr = [823,82,147,55,53,256,104,58,68,0] 
        #True case:
        self.assertEqual(check_monotonic(prev,curr),True)
        #False case:
        curr[2]=145
        self.assertEqual(check_monotonic(prev,curr),False)
        #check T8 is not included:
        curr[2]=147 #reset curr
        curr[8]=70 
        self.assertEqual(check_monotonic(prev,curr),True)

    def test_check_row(self):
        self.assertEqual(check_row(1,[823,82,147,55,53,256,104,58,68,0],['702','70','140','44','39','227','93','40','49','0']),True)
        #check it is not effected by empty other column because it should only check Tall-T8
        self.assertEqual(check_row(1,[823,82,147,55,53,256,104,58,68,0],['702','70','140','44','39','227','93','40','49',]),True)
        #check missing value
        self.assertEqual(check_row(1,[823,82,147,55,53,256,104,58,68,0],['702','','140','44','39','227','93','40','49','0']),False)
        
        


if __name__=='__main__':
    unittest.main()

