import os,platfrom
os.system('clear')
print(' \033[1;97m Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
     os.system('chmod 777 DilSher;./DilSher')
else:
      exit(' \n\n Sorry Your Device Not Support D404 Tools')
