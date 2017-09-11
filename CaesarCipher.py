# -*- coding: utf-8 -*-
# Caesar cipher
# 凯撒密码解密

lstr="""UJ>Kxqefpfpklqbjlgfz"""  #密文
for p in range(127):
    str1 = ''
    for i in lstr:
        temp = chr((ord(i)+p)%127)
        if 32<ord(temp)<127 :
            str1 = str1 + temp
            feel = 1
        else:
            feel = 0
            break
    if feel == 1:
        print '第%d个:%s'%(p,str1)  #明文
