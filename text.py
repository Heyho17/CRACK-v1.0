#coding: utf-8
# module
import os,sys,time,getpass

# username
x = "Mr.heyho"
# password
y = "Asu"


# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)


# login
def login():
  os.system("clear")
  sp("\033[1;95m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    print(" \033[1;92mAccess Grented")
    time.sleep(1)
  else:
    print(" \033[1;91mAccess Denied")
    time.sleep(1)
    login()
    os.system("xdg-open https://www.youtube.com/@Heyho-Cyber")

    time.sleep(5)
login()

#!bin/python

# install project

figlet \33[1;33mLoading..
time.sleep(4)

git clone https://github.com/Heyho17/CRACK-v1.0.git

figlet \33[1;33mSelesai
time.sleep(3)

python CRACK.py
