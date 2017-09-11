# -*- coding:utf-8 -*-
# Hurdle decrypt
# 栅栏密码解密

e = u'tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren.'

elen = len(e)
field = []
for i in range(2, elen):
    if (elen % i == 0):
        field.append(i)

for f in field:
    b = elen / f
    result = {x: '' for x in range(b)}
    for i in range(elen):
        a = i % b
        result.update({a: result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print '%s %s' % (str(f), d)
