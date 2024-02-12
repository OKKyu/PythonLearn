#! python3
# -*- coding:utf-8 -*-
'''
  Question Auto Creator
    This program can product question automatic and random.
    You can use this script for your practice to Basic-Engineer-Examination.
'''
import sys
import random


def prac_conv_DecToN(t="b"):
    '''
      t= b(byte), o(octet), x(hex)
    '''
    val = random.randint(1, 100)

    print("convert from " + str(val) + "(decimal) to " + t + ", what the answer is ?")
    ans = input()
    cnv_val = format(val, t)
    chk = (cnv_val == ans.lower())
    print("conv to {}:{}, your ans:{}, {}".format(t, cnv_val, ans, chk))

    return int(chk)


def prac_conv_NtoDec(t="b"):
    '''
      t= b(byte), o(octet), x(hex)
    '''
    val = [random.randint(1, 100)]

    print("convert from " + format(val, "#" + t) + "(" + t + ")" + ", what the answer is ?")
    ans = input()
    chk = (str(val) == ans.lower())
    print("conv to ten:{}, your ans:{}, {}".format(val, ans, chk))

    return int(chk)


desc = []
desc.append(['practice convert from decimal to N base.', prac_conv_DecToN])
desc.append(['practice convert from N base to decimal.', prac_conv_NtoDec])

if __name__ == "__main__":
    # Checking number of commandline args.
    if len(sys.argv) < 3:
        print("there are incorrect args, please input args correctly.")
        print("arg1:practice type arg2:number of questions")
        print("if arg2=0, you can read about arg1\'s explanation.")
        sys.exit(1)

    if sys.argv[2] <= "0":
        # Explaining about practice type.
        if int(sys.argv[1]) >= 0 and int(sys.argv[1]) < len(desc):
            print("practice type " + sys.argv[1] + "  is below...")
            print(desc[int(sys.argv[1])][0])
        else:
            print("index out of range. Please input arg1 into between 1 to " + str(len(desc)))
            for i in range(len(desc)):
                print("type " + str(i) + " ->  " + desc[i][0])
    else:
        question_variations = ["b", "o", "x"]

        prac_num = int(sys.argv[2])
        print("practice try num is : " + str(prac_num))

        print("let\'s start!!")

        correct_num = 0
        for i in range(prac_num):
            prac_maker = desc[int(sys.argv[1])][1]
            correct_num += prac_maker(random.choice(question_variations))

        print("your score is below... Can you get complete? (^~^)")
        print("right/total  {}/{}".format(correct_num, prac_num))
        print("")
