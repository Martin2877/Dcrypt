# -*- coding: utf-8 -*-
# Caesar cipher
# 凯撒密码加解密


code = """I love you!"""

sr1 = "abcdefghijklmnopqrstuvwxyz"
sr2 = sr1.upper()
sr = sr1 + sr1 + sr2 + sr2
st = code
sResult = ""
for rot in range(26):
    for j in st:
        if j == " ":
            sResult = sResult + " "
            continue
        i = sr.find(j)
        if i > -1:
            sResult = sResult + sr[i + rot]
    print "ROT%s:%s" % (rot, sResult)
    sResult = ''
