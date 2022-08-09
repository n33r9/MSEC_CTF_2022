import string
flag=['m','k','O','5','k','b','_','s','c','_','D','r','4','D','_','i','Y','e','?']
str_cmp= 'mkO5kb_sc_Dr4D_iYe?'
j=0
print(string.printable)
for i in string.printable:
    if ord(i)-97 >25:
        if ord(i)-65>25:
            if (i in str_cmp):
                flag[str_cmp.index(i)]=i
        else:
            j= ord(i)-16
            if(ord(i)+10)<=90:
                j=ord(i)+10
            if (chr(j)in str_cmp):
                flag[str_cmp.index(chr(j))]=i
    else:
        j=ord(i)-16
        if ord(i)+10<=122:
            j=ord(i)+10
        if (chr(j)in str_cmp):
                flag[str_cmp.index(chr(j))]=i
                
for i in flag:
    print(i)
  
    
# flag='caE+kXUiY_:h*D__O[5'