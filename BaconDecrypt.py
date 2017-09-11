#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 培根解密代码
# 两种加密方式的解密


import sys


def peig1(m):
    basic1 = {
        'AAAAA': 'A',
        'AAAAB': 'B',
        'AAABA': 'C',
        'AAABB': 'D',
        'AABAA': 'E',
        'AABAB': 'F',
        'AABBA': 'G',
        'AABBB': 'H',
        'ABAAA': 'I',
        'ABAAB': 'J',
        'ABABA': 'K',
        'ABABB': 'L',
        'ABBAB': 'N',
        'ABBBA': 'O',
        'ABBBB': 'P',
        'BAAAA': 'Q',
        'BAAAB': 'R',
        'BAABA': 'S',
        'BAABB': 'T',
        'BABAA': 'U',
        'BABAB': 'V',
        'BABBA': 'W',
        'BABBB': 'X',
        'BBAAA': 'Y',
        'BBAAB': 'Z'
    }
    output = ''
    for i in range(0, len(m) - 4, 5):
        temp = m[i: i + 5]
        output += basic1[temp]
    return output


def peig2(m):
    basic2 = {
        'AAAAA': 'A',
        'AAAAB': 'B',
        'AAABA': 'C',
        'AAABB': 'D',
        'AABAA': 'E',
        'AABAB': 'F',
        'AABBA': 'G',
        'AABBB': 'H',
        'ABAAA': 'I',
        'ABAAA': 'J',
        'ABAAB': 'K',
        'ABABA': 'L',
        'ABABB': 'M',
        'ABBAA': 'N',
        'ABBAB': 'O',
        'ABBBA': 'P',
        'ABBBB': 'Q',
        'BAAAA': 'R',
        'BAAAB': 'S',
        'BAABA': 'T',
        'BAABB': 'U',
        'BAABB': 'V',
        'BABAA': 'W',
        'BABAB': 'X',
        'BABBA': 'Y',
        'BABBB': 'Z'
    }
    output = ''
    # print m
    for i in range(0, len(m) - 4, 5):
        temp = m[i: i + 5]
        # print temp, i
        try:
            output += basic2[temp]
        except:
            return
    return output


def bacon(m, mode):
    if len(m) % 5 == 0:
        l = []
        k = []
        for i in xrange(len(m) / 5):
            l.append(m[:5])
            m = m[5:]
        if mode == 1:
            for i in l:
                if i.isupper():
                    k.append(peig1(i))
                else:
                    i = i.upper()
                    k.append(peig1(i))

        elif mode == 2:
            for i in l:
                # print i
                if i.isupper():
                    k.append(peig2(i))
                else:
                    i = i.upper()
                    k.append(peig2(i))
        flag = ''
        for i in k:
            try:
                flag += i[0]
            except:
                return
        print 'plan %s : %s' % (mode, flag)


if __name__ == '__main__':
    m = r'ThEQUIcKbrOwnfOxJuMpSOvERthELAZysoBiGdOG'
    # m = r'ni ko ni ko ni ni ko ni ko ni'
    # get_list = m.split(' ')
    # 根据大小写转成AB格式
    index = 0
    n = ''
    for ab in m:
    # for ab in get_list:
        # print ab, index, n
        if ab.isupper():
        # if ab == 'ko':
            n = n + 'A'
        else:
            n = n + 'B'
        index += 1
    bacon(n, 1)
    bacon(n, 2)
