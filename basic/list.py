#! python3 
# -*- coding: UTF-8 -*-
# ���X�g�i�z��j�̊�{

#���X�g�錾�@JavaScript�Ɠ���
squares = [1,4,9,16,25]
print(squares)

#������⑼�V�[�P���X�I�u�W�F�N�g���l�̓Y�����A�N�Z�X���\�B
print(squares[0])
print(squares[-1])
print(squares[-3:])

#�S���X�g�v�f���X���C�X�����ꍇ�͐V�������X�g�R�s�[��ԋp����B
newSqu = squares[:]
print("Original List:" + str(squares))
print("Copied List:" + str(newSqu))

#���X�g�͉ς̂��ߗv�f�̓��e��ύX�ł���B�������^�͖��Ȃ�
newSqu[1] = 'hello'
print("Original List:" + str(squares))
print("Copied List:" + str(newSqu))

#���X�g�̘A�����\
newSqu = newSqu + ['HeyHeyHeeey!','GYaaaaaAAA!!']
print("Copied List:" + str(newSqu))

#append()���g���Ė����ɗv�f��ǉ����邱�Ƃ��B
newSqu.append(32111)
print("Copied List:" + str(newSqu))

#�X���C�X���g���đ�����\�B
newSqu[2:4] = [0,0,1]
print("Copied List:" + str(newSqu))

#�폜���\�B
newSqu[2:5] = []
print("Copied List:" + str(newSqu))
#�S���폜
newSqu[:] = []
print("Copied List:" + str(newSqu))

#len�֐��ŗv�f�����擾�\�B
print("Original List len:" + str(len(squares)))

#����q���\�B�������z��B
listlist = [[1,3,5],['a','b','c']]
print("[0][1] :" + str(listlist[0][1]))
print("[1][2] :" + str(listlist[1][2]))

#����͖ʔ����B
#for���Ń��X�g�쐬���\�B
# i * 2 ��z��v�f�Ƃ��ĕԋp����B�����range(10)��10��J��Ԃ��B
numbers = [i * 2 for i in range(10)]
print(numbers)
print(len(numbers))

#�ǂ݂ɂ������ȉ��̒ʂ�
#  [1 for i in range(3)] �Œl��1�̗v�f��3�����X�g���쐬
#   ��L��range(4)��4��J��Ԃ��B
#   [1,1,1]�̃��X�g���S�������Q�����z�񂪊����B
numbers2 = [[1 for i in range(3)] for j in range(4)]
numbers2[0][1] = 2
print(numbers2)

#���X�g����e�ϐ��ւ̑�����ł���B����͕֗������B
number3 =  [i for i in range(3) ]
number3_0, number3_1, number3_2 = number3
print(number3)
print(str(number3_0) + " " + str(number3_1) + " " + str(number3_2))
