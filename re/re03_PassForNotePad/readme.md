Bài cho file exe, có biểu tượng con trăn, kích thước file lại tương đối lớn, ta nghĩ ngay đến đưa .exe về file .py

- Dùng https://github.com/extremecoders-re/pyinstxtractor
để convert .exe to .pyc, tool này sẽ vừa convert, vừa gợi ý cho bạn file nào là file entry, chạy version python bao nhiêu.

- Dùng https://github.com/rocky/python-uncompyle6 để decompile file .pyc. Tuy nhiên, trước đó bạn phải sửa header của file .pyc cho đúng với phiên bản python 3.6 của nó (copy 16 byte đầu của một file .pyc trong thư viện python 3.6)

- decompile xong, ta thu được file .py

Chạy thử để nắm được cách thức hoạt động của file .exe ban đầu: encrypt và decrypt text file theo cú pháp đã được định sẵn, với đuôi file được encrypt là .mta. File được giải nén với mật khẩu thỏa mãn điều kiện. 

Khi có được source code file .py, ta cho in ra biến password_in_file

password_in_file = d_inp[:32]
    print(password_in_file)
    d_inp = d_inp[32:]
    # print(d_inp)
    key = password[6] + password[5] + password[0] + password[2]
    m = hashlib.md5(key.encode('utf-8'))
    key = m.digest()
    key = key.hex()
    if key != password_in_file:
        print('Wrong password!')
        return
        
key sau khi được mã hóa MD5 thì đem so sánh với password in file, ta decode password_in_file online, thu được key ban đầu chưa bị mã hóa 1234. Như vậy 1,2,3,4 sẽ lần lượt là ký tự thứ 7,6,1,3 của pass cần nhập để decrypt. 
Ta chạy chương trình với pass thỏa mãn điều kiện trên và thu được flag trong file secret.txt

