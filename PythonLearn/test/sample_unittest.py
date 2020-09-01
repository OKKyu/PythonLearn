#!python3
# -*- coding:utf-8 -*-
'''
  this code is sample that how to use of unittest package.
  coding proccess is similar to JUnit of Java.
'''
import unittest
from test_target import sum_two_num

class TestSum(unittest.TestCase):
    '''
      using unittest library
      step one: Making one class that extended unittest.TestCase class.
    '''
    
    def setUp(self):
        '''
          step two: If it is need to preparing before test, shoud be override setUp method.
        '''
        print("start setup")
    
    def tearDown(self):
        '''
          step tree: If it is need that proccessing after test, shoud be override tearDown method.
        '''
        print("start tearDown")    
    
    def test1(self):
        '''
          step four: Please write test case in original method.
          caution: Name of methods needs to start "test" chars.
                   example: testCase1, test1, testAbnormal001.
        '''
        self.assertEqual(sum_two_num(1,2),3)
        self.assertEqual(sum_two_num(4,2),6)
        self.assertEqual(sum_two_num(-1,3),2)
        self.assertEqual(sum_two_num(0,0),0)
        
    def test2(self):
        '''
          step four: Please write test case in original method.
        '''
        with self.assertRaises(TypeError):
            sum_two_num("",2)
        with self.assertRaises(TypeError):
            sum_two_num(3,"")
        with self.assertRaises(TypeError):
            sum_two_num(None,1)
        with self.assertRaises(TypeError):
            sum_two_num(-4,None)
        with self.assertRaises(TypeError):
            sum_two_num([],1)
        with self.assertRaises(TypeError):
            sum_two_num(9,[])
        
if __name__ == "__main__":
    unittest.main()
    
'''
notes:
 if run commandline is below:
    python -m unittest sample_unittest.py
    
 if you want to only one testcase, below:
    python -m unittest sample_unittest.test1

 

'''
