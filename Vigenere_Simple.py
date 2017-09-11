# -*- coding:utf-8 -*-
# Vigenere decrypt
# 维吉尼亚密码

from pycipher import Vigenere
print Vigenere('CULTURE').encipher('Hellow! How are you.')
print Vigenere('CULTURE').decipher('JYWEINLQQLKYPSW')
