#! python3
# -*- coding:utf-8 -*-
'''
  Question Auto Creator
    This program can product question automatic and random.
    You can use this script for your practice to Basic-Engineer-Examination.
'''
import sys
import random

def prac_conv_DecToN(t="b" ,question_num = 3):
    '''
      t= b, o, x
    '''
    vals = [ random.randint(1, 100) for x in range(question_num) ]
    correct_num = 0
    
    for i in range(question_num):
        print("convert from " + str(vals[i]) + "(decimal) to " + t + ", what the answer is ?")
        ans = input()
        cnv_val = format(vals[i], t)
        chk = (cnv_val == ans.lower())
        if chk is True:
            correct_num += 1
        
        print("conv to {}:{}, your ans:{}, {}".format(t, cnv_val, ans, chk))
        
    print("right/total::{}/{}".format(correct_num, len(vals)) )
    print("")
        
def prac_conv_NtoDec(t="b" ,question_num = 3):
    '''
      t= b, o, x
    '''
    vals = [ random.randint(1, 100) for x in range(question_num) ]
    correct_num = 0
    
    for i in range(question_num):
        print("convert from " + format(vals[i], "#" + t) + "(" + t + ")"  + ", what the answer is ?")
        ans = input()
        chk = (str(vals[i]) == ans.lower())
        if chk is True:
            correct_num += 1
        
        print("conv to ten:{}, your ans:{}, {}".format(vals[i], ans, chk))
        
    print("right/total::{}/{}".format(correct_num, len(vals)) )
    print("")
        
desc = []
desc.append(['practice convert from decimal to N base.', prac_conv_DecToN])
desc.append(['practice convert from N base to decimal.', prac_conv_NtoDec])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("there are incorrect args, please input args correctly.")
        print("arg1:practice type arg2:number of producting questions")
        sys.exit(1)
    
    if sys.argv[2] == "0":
        if int(sys.argv[1]) > 0 and int(sys.argv[1]) <= len(desc):
            print(desc[int(sys.argv[1]) -1][0])
        else:
            print("index out of range. Please input arg1 into between 1 to "+ str(len(desc)))
        
    else:
        prac_num = int(sys.argv[2])
        
        if sys.argv[1] == "1":
            prac_conv_DecToN("b", prac_num)
            prac_conv_DecToN("o", prac_num)
            prac_conv_DecToN("x", prac_num)
            
        if sys.argv[1] == "2":
            prac_conv_NtoDec("b", prac_num)
            prac_conv_NtoDec("o", prac_num)
            prac_conv_NtoDec("x", prac_num)        