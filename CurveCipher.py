# Curve Cipher
# 曲路密码，包含加密码与解密
# -*- coding: utf-8 -*-

def create_list(n):
    lst = []
    for i in range(n):
        lst.append('')
    return lst


def curve(code, mode):
    if mode == "decrypt":
        cut_ = code.find(' ')
        back = code.split(" ")
        back.reverse()
        result = {}
        str = ''
        parity = 1
        for col in back:
            if parity == 1:
                for i in range(cut_):
                    # print col[i]
                    str = result.get(i)
                    if str is None: str = ''
                    new = str + col[i]
                    result[i] = new
                parity = 0
            else:
                col = col[::-1]
                for i in range(cut_):
                    # print col[i]
                    str = result.get(i)
                    if str is None: str = ''
                    new = str + col[i]
                    result[i] = new
                parity = 1
        # print result
        result_str = ''
        for res in result:
            # print result.get(res)
            result_str = result.get(res) + result_str
        return result_str
    # encrypt part
    elif mode == "encrypt":
        text = code.replace(" ", "")
        # 取出质数
        elen = len(text)
        field = []
        for i in range(2, elen):
            if (elen % i == 0):
                field.append(i)
        # 开始做切割
        result_return = ''
        for f in field:
            result_dict = []
            q = elen / f
            q_start = 0
            for q_i in range(q):
                result_dict.append(text[q_start:q_start + f])
                q_start += f
            # print "切成表格：", result_dict
            col = create_list(f)
            for dict_i in range(len(result_dict)):
                for char_i in range(len(result_dict[dict_i])):
                    col[char_i] += (result_dict[dict_i][char_i])
            # print "取出表格每一列：", col
            result = ''
            col.reverse()
            for parity in range(len(col)):
                # print parity
                col_single = col[parity]
                if parity % 2 == 0:
                    col_single = col_single[::-1]
                result += col_single + " "
            # 保存结果
            result_return += "每%s位一行分解：%s" % (f, result) + "\n"
            # print "%s %s" % (f, result)
        return result_return



# plaintext = """Thequickbrownfoxjumpsoverthelazydog"""
code = """gesfc inpho dtmwu qoury zejre hbxva lookT"""

plaintext = """I love you!"""
# code = """!yo leu ovI"""

print curve(plaintext, mode="encrypt")
print curve(code, mode="decrypt")

