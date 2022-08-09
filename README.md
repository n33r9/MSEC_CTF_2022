# MSEC_CTF_2022
[RE warm up](https://github.com/n33r9/MSEC_CTF_2022/tree/master/re/re00_warmup)

![](https://github.com/n33r9/MSEC_CTF_2022/blob/master/re/re00_warmup/image/warmup.png)

*Đề bài cho file CTF.exe, thực hiện một vài thao tác kiểm tra đơn giản -> file PE64*
![](https://github.com/n33r9/MSEC_CTF_2022/blob/master/re/re00_warmup/image/checkfile.png)
Thử chạy file, nhập string bất kỳ và nhận được "Try more!"

![](https://github.com/n33r9/MSEC_CTF_2022/blob/master/re/re00_warmup/image/runfile.png)

Load file vào IDA64, chương trình yêu cầu người dùng nhập input, sau đó đưa input qua 1 vòng lặp, tiến hành biến đổi và cuối cùng so sánh với chuỗi ký tự: "mkO5kb_sc_Dr4D_iYe?"
![](https://github.com/n33r9/MSEC_CTF_2022/blob/master/re/re00_warmup/image/ida64.png)

Đọc đoạn mã hóa lúc đầu, mình đã cảm thấy có gì đó rất giống mã hóa caesar với key =10, nhưng mà không hiểu sao không thử check luôn mà vẫn ngồi code:v. Code xong thì flag ra không có ý nghĩa lắm (Do mình không để ý check điều kiện số âm với unsigned_int8). Tuy nhiên, các ký tự đầu của flag lại ra gần giống caesar, lúc này mình mới dùng [tool decode online](https://www.dcode.fr/shift-cipher)
![](https://github.com/n33r9/MSEC_CTF_2022/blob/master/re/re00_warmup/image/decode.png)

**Flag: MSEC{caE5ar_is_Th4T_yOu?}**

*Dưới đây là code sau khi đã sửa:*
```python
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
```

