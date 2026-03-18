import os
os.system("pip install requests")
import marshal,codecs,binascii,zlib,bz2,pyfiglet,os,time,dis,lzma,gzip,base64
from sys import stdout
import subprocess as sp
import sys,random, base64, getpass, re
from py_compile import compile as _compile
from rich.panel import Panel as nel
from rich import print as cetak
import requests,subprocess
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
A = "\033[1;91m"#الاحمر
B = "\033[1;90m"#الرصاصي
C = "\033[1;97m"#الابيض
E = "\033[1;92m"#الاخضر
H = "\033[1;93m"#الاصفر
K = "\033[1;94m"#البنفسجي
L = "\033[1;95m"#وردي
M = "\033[1;96m"#السمائي
R = '\x1b[1;31m' #احمر 
G = '\x1b[1;32m' #اخضر
B = '\x1b[0;94m' #بنفسجي
Y = '\x1b[1;33m' #اصفر
E = '\033[91m' #احمر
###############
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a16 = '\x1b[38;5;48m'  # أخضر فاتح
M = '\033[2;36m' #سماوي
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a40 = '\x1b[38;5;117m'  # أزرق سماوي
def clr():
	os.system("clear")
def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)
def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		print('Exit!')
os.system('clear')
import requests
import re
from rich.panel import Panel as Ch
from rich import print as code
a =	'/033[31m'
s =	'/033[32m'
d =    '/033[33m'
g =	'/033[34m'
def DEKoo():
	print(a16+'▭▬'*20)
	print(a20+'╰─ 1. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗺𝗮𝗥𝗦𝗛𝗮𝗟     ')
	print(a20+'╰─ 2. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗺𝗮𝗥𝗦𝗛𝗮𝗟 3.7    ')
	print(a20+'╰─ 3. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗕𝗮𝗦𝗘32    ')
	print(a20+'╰─ 4. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗕𝗮𝗦𝗘64    ')
	print(a20+'╰─ 5. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗕𝗮𝗦𝗘16    ')
	print(a20+'╰─ 6. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗕𝗮𝗦𝗘85    ')
	print(a20+'╰─ 7. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙡𝙖𝙢𝙗𝙙𝙖.𝙢𝙖𝙧𝙨𝙝𝙖𝙡.𝙗𝙖𝙨𝙚64.𝙯𝙡𝙞𝙗    ')
	print(a20+'╰─ 8. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙡𝙖𝙢𝙗𝙙𝙖    ')
	print(a20+'╰─ 9. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗘𝗺𝗢𝗜𝗝    ')
	print(a20+'╰─ 10. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗛𝙚𝙭    ')
	print(a20+'╰─ 11. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙥𝙮𝙘    ')
	print(a20+'╰─ 12. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙡𝙯𝙢𝙖.𝙯𝙡𝙞𝙗    ')
	print(a20+'╰─ 13. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗕𝗜𝗡𝗮𝗦𝗖𝗜𝗜    ')
	print(a20+'╰─ 14. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗭𝗟𝗜𝗕,𝗕𝗮𝗦𝗘    ')
	print(a20+'╰─ 15. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗚𝗭𝗜𝗣    ')
	print(a20+'╰─ 16. 𝗗𝗘𝗖𝗢𝗗𝗘 𝗖𝗢𝗗𝗘𝗖𝗦    ')
	print(a20+'╰─ 17. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙨𝙢𝙥𝙡𝙚 𝙥𝙮𝙘    ')
	print(a20+'╰─ 18. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙨𝙢𝙥𝙡𝙚 𝙥𝙮𝙘2    ')
	print(a20+'╰─ 19. 𝗗𝗘𝗖𝗢𝗗𝗘 𝙡𝙯𝙢𝙖    ')
	print(a20+'╰─ 0. 𝗘𝗫𝗘𝗧    ')
	print(a16+'▭▬'*20)
      
#      zcn = nel(seov2,style='green')
#      cetak(nel(zcn,title='',style='red'))
#@SY6SY
def ahm():
    b = input("x1b[1;31m[x1b[1;31mDEKoox1b[1;31m] 033[1;97m> - Enter File marshal : ")
    am = ('x1b[38;5;51m','x1b[38;5;63m ','x1b[38;5;73m2','x1b[38;5;83m8','x1b[38;5;93m0','x1b[38;5;103m0')
    for i in range(50):
        time.sleep(.1)
        sys.stdout.write('rDecode marshal ...>>> ')
        sys.stdout.flush()
    print()  # İndentation düzeltildi, döngüden çıkarıldı.

    a = open(b, 'rb').read()  # Dosyayı binary olarak oku.
    m = False
    k = b""  # Byte string olarak başlat.
    n = 0
    for x in a:
        if x == 39 and a[n-1] == 98:  # ASCII karakter kodlarını kullanarak kontrol et.
            m = True
            n += 1
            continue
        if m and x == 39 and a[n-1] != 92:  # Escape karakterini kontrol et.
            break
        if m:
            k += bytes([x])  # Byte olarak ekle.
        n += 1

    # Byte string'i doğrudan marshal.loads'a geçir.
    exec(marshal.loads(k))
 

def unmarszlib():
        try:
            files = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File marshal 3.7: ")
        except:
            exit("")
        if len(files) == 0:
              exit("")
        try:
            bk = open(files,"r").read()
        except IOError:
            print("file tidak ada")
            exit()
        bk = bk.replace("import","import uncompyle6,")
        bk = bk.replace("exec(","uncompyle6.main.decompile(3.7,")
        bk = bk.replace(")))",")),open(\"hasil.py\",\"w\"))")
        exec(bk)
def exit():
        print('الله وياك مع السلامه ')
        sys.exit()
def ex():
        print('الله وياك مع السلامه ')
        sys.exit()
#@SY6SY
def men():
            
            file=input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("DEKoo.py","w").write(data2)            
            os.system("python DEKoo.py > DEKoo.py")
            DEKoo=str(open("DEKoo.py","r").read())
            data3=f"""#Decode By  @De6ko\nimport marshal\nexec(marshal.loads({DEKoo}))"""
            open("DEKoo.py","w").write(data3)
            print("marshal-magic DEKoo.py -m normal -o DEKoo.py")
            print('')
            print('\n') 
            print('[•] Decode Done √')
            #DEKoo()
########################(decode lambda+ emoji)
#DEKoo
def lamb():
      print("------------------------------------------")
      file_nme = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File Lambda : ")
      print("------------------------------------------")
      try:
        with open(file_nme, 'r') as file:
              Hussein = file.read()
              NB_JG = Hussein.replace("exec", "print")
        with open(file_nme, 'w') as file:
              file.write(NB_JG)
  
              print("The first step  completed successfully ✅")
              os.system("clear")
              subprocess.run(['python3', f'{file_nme}'])
      #        open("DEKoo.py","w").write()
      except FileNotFoundError:
            print("The file was not found. Please select from the list below 👇🏻")
            os.system("ls")
      except Exception as e:
            print(f"Erorr : {e}")


#DEKoo
def emoji():
     # print("------------------------------------------")
      file_name = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File emoji: ")
      #print("------------------------------------------")
      try:
        with open(file_name, 'r') as file:
              Hussein = file.read()
              NB_JG = Hussein.replace("exec", "print")
        with open(file_name, 'w') as file:
              file.write(NB_JG)
              
              print("The first step  completed successfully ✅")
              os.system("clear")
              subprocess.run(['python3', f'{file_name}'])
      except FileNotFoundError:
            print("The file was not found. Please select from the list below 👇🏻")
            os.system("ls")
      except Exception as e:
            print(f"Erorr : {e}")
#############(decode base )########################
#DEKoo
def decode_base64_file():
    decode_base64 = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File base64:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base64, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b64decode(encoded_data)
        
    with open("Decode_base64.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base64.")
          #DEKoo()
#DEKoo
def decode_base16_file():
    decode_base16 = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File base16:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base16, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b16decode(encoded_data)
        
    with open("Decode_base16.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base16.py.")
        #  DEKoo()
#DEKoo        
def decode_base32_file():
    decode_base32 = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File base32:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base32, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b32decode(encoded_data)
        
    with open("Decode_base32.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base32.py.") 
         # DEKoo()
#DEKoo      
def decode_base85_file():
    decode_base85 = input("\x1b[1;31m[\x1b[1;31mDEKoo\x1b[1;31m] \033[1;97m> - Enter File base85:  ")
    #decode_base64_file(decode_base64)
    with open(decode_base85, 'rb') as file:
        encoded_data = file.read()
        decoded_data = base64.b85decode(encoded_data)
        
    with open("Decode_base85.py", 'wb') as file:
          file.write(decoded_data)
          print("تم فك تشفير الملف وحفظ النص المفكوك في ملف Decode_base85.py.") 
          #DEKoo()
#DEKoo             
def decode_hex():
    filename = input("Enter the name of the encoded file: ")
    with open(filename, "rb") as f:
              encoded_data = f.read().hex()
              decoded_data = bytes.fromhex(encoded_data)
              decoded_filename = f"{filename}_decoded.py"
    with open(decoded_filename, "wb") as f:
              f.write(decoded_data)
              print(f"File {filename} decoded successfully and saved as {decoded_filename}")
           #   DEKoo()
#DEKoo
def lzm_zlb():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko    *_*')
	else:
			DEKoo()
#@SY6SY
def zlb():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko  *_*')
	else:
			DEKoo()
#DEKoo
def lzm():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko  *_*')
	else:
	      DEKoo()
#DEKoo
def cods():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko   *_*')
	else:
			
			DEKoo()
#DEKoo
def binasci():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko  *_*')
	else:
			DEKoo()
#DEKoo
def gzp_base():
#
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko  *_*')
	else:
			DEKoo()
#DEKoo			
def zlib_base():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko   *_*')
	else:
			DEKoo()
#DEKoo
def smple_pyc():
#		 #()
		clr()
		while True:
			Ty = input(a9+'input your file : ')
			Tr = input(a12+'output your file : ')
			com = f'pycdc {Ty} > {Tr}'
			os.system(com)
			slow(G+'  by @De6ko  *_*')
		else:
			DEKoo()
#DEKoo	
def smple_pyc2():
#		 #()
		clr()
		while True:
			Ty = input('input your file : ')
			Tr = input('output your file : ')
			com = f'uncompyle6 {Ty} > {Tr}'
			os.system('uncompyle6 {Ty} > {Tr}')
			slow('  by @De6ko  *_*')
		else:
			DEKoo()
#DEKoo
def gzp():
#	 #()
	clr()
	while True:
			file = input(a9+'input your file : ')
			filer = input(a12+'output your file : ')
			com = f'marshal-magic {file} -o {filer} '
			os.system(com)
			slow(G+'  by @De6ko  *_*')
	else:
			DEKoo()
#DEKoo




DEKoo()				
se = int(input("choice : "))
if se == 1:
	ahm()
elif se == 2:
	unmarszlib()
elif se == 3:
      decode_base64_file()
elif se == 4:
	decode_base32_file()
elif se == 5:
	decode_base16_file()
elif se == 6:
	decode_base85_file()
elif se == 7:
	men()
elif se == 8:
	lamb()
elif se == 9:
	emoji()
elif se == 10:
       decode_hex()
elif se == 11:
      ex()
elif se == 12:
      lzm_zlb()
elif se == 13:
	binasci()
elif se == 14:
	zlib_base()
elif se == 15:
	gzp()
elif se == 16:
	cods()
elif se == 17:
	smple_pyc()
elif se == 18:
	smple_pyc2()
elif se == 19:
       lzm()
elif se == 0:
	exit()
#DEKoo()		
if __name__ == "__main__":
	DEKoo()