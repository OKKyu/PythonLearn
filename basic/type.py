#! python3
# -*- coding: UTF-8 -*-
# �^�̊�{
import sys

#int��float�ADecimal�AFraction�Ȃǂ��T�|�[�g�B�r���g�C���ł͕��f���⋕����������Bj or J�ŋ����������B
#int�^���
num = 30
print("num(int) " + str(num))

#float�^���
num = 30.6
print("num(float)" + str(num))

#int�^���
num = 22
print("num(int)" + str(num))

#string�^���  JavaScript�̂悤�ɁA�ϐ��̌^�͌Œ肳��Ȃ��悤�ł���B
num = "121"
print("num(String)" + str(num))

#string�^���  �G�X�P�[�v�ɂ�\���g���B
st = '"Isn\'t," she said.'
print("st " + st)

#����������̘A�� () �ł�����A�C�ӂ̈ʒu�ŕ����̃N�H�[�e�[�V�������g���B
text = ('very long,long,long,long,long,long,long,long,long'
        ',long,long,long,long,long,long,time,agooooooo.......')
print(text)

#�ϐ��ǂ����̘A�� Java�Ɠ����� + ���g���B
text = text + 'very Evils man, Rorun Harlshead, is exist.'
print(text)

#������̓C���f�b�N�X�w�肵�Ĉꕔ�؂�o�����\�B
#char�ɕϊ����Ȃ��ł������Asubstring���v��Ȃ������B����͂���y�B
#������1�`4�����؂�o��
print('index 1 4  ' + text[0] + text[1] + text[2] + text[3])

#�E����1�`4�����؂�o��
#-0�͂Ȃ����߁A�E����؂�o���ꍇ��1�J�n�ƂȂ�B
print("index -1 -4  " + text[-1] + text[-2] + text[-3] + text[-4])

#��̂悤�Ȑ؂�o�����������Ƃ��X���C�X���T�|�[�g����Ă���B
print('index 1 4  ' + text[0:4])

#�ŏ��̃C���f�b�N�X���ȗ�����ƁA0 �ƌ��Ȃ���܂��B��Ԃ� �̃C���f�b�N�X���ȗ�����ƁA�X���C�X���镶����̃T�C�Y�Ƃ݂Ȃ���܂��B
text = 'Python'
print("text :2" + text[:2])
print("text 2:" + text[2:])

#�������immutable�B�ꕔ�������ύX���悤�Ƃ��Ă��G���[�ƂȂ�B
#text[:2] = 'Po'

#�����񒷂�len()�Ŏ擾�\�B
print('length:' + str(len(text)))


