import string
flag = ''
str_cmp = 'mkO5kb_sc_Dr4D_iYe?'
# print(string.printable)
for ele in str_cmp:
    for i in string.printable:
        if (ord(i)-97) & 0xff > 25:
            if (ord(i)-65) & 0xff > 25:
                v8 = ord(i)
            else:
                v8 = ord(i)-16
                if(ord(i)+10) & 0xff <= 90:
                    v8 = ord(i)+10
        else:
            v8 = ord(i)-16
            if (ord(i)+10) & 0xff <= 122:
                v8 = ord(i)+10
        if chr(v8)==ele:
            flag+= i
            break
print(flag)
# caE5ar_is_Th4T_yOu?