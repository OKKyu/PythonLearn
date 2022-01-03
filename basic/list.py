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

#����q���\�B
listlist = [[1,3,5],['a','b','c']]
print("[0][1] :" + str(listlist[0][1]))
print("[1][2] :" + str(listlist[1][2]))




