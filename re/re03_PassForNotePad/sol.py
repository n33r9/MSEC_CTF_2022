from sys import argv, exit
from Cryptodome.Cipher import DES
import hashlib, base64

pass_in_file= '81dc9bdb52d04dc20036dbd8313ed055'
key = password[6] + password[5] + password[0] + password[2]
m = hashlib.md5(key.encode('utf-8'))
key = m.digest()
key = key.hex()