flag=''
init_str= 'mkO5kb_sc_Dr4D_iYe?'
for ele in init_str:
    if ord(ele) <= 122 and ord(ele)>90: 
        if ord(ele) <=106:
            flag+=chr(ord(ele)+16)
        else:
            flag+=chr(ord(ele)-10)        
    elif ord(ele)<=90:
        if ord(ele)<=74:
            flag+=chr(ord(ele)+16)
        else:
            flag+=chr(ord(ele)-10)   
    else: 
        flag+=chr(ord(ele))
print(flag)