import os
import sys
import csv
import msvcrt as m

PKGLIST_URL = "https://pkg.longhi.me/packagelist"

print("Baixando Lista de Pacotes...")
os.system(f"mkdir C:\\Users\\{os.getlogin()}\\longhipkg")
if (os.system(f"powershell.exe Invoke-WebRequest -Uri {PKGLIST_URL} -OutFile C:\\Users\\{os.getlogin()}\\longhipkg\\packagelist.csv")) != 0:
    print("===================================")
    print("Falha ao atualizar lista de pacotes")
    print("")
    print("Verifique a conexão com a internet.")
    print("===================================")
    sys.exit(1)

global packagelist 
packagelist = []
with open(f"C:\\Users\\{os.getlogin()}\\longhipkg\\packagelist.csv", "r") as packagelistfile:
    reader = csv.reader(packagelistfile, delimiter=";")
    for pkg in reader:
        if(pkg[0] != "@packagelist"):
            packagelist.append(pkg)

global scroll
scroll = int(len(packagelist)/2) # start on the middle of the list

def scrollwheel():
    global scroll
    global running
    try:
        print(packagelist[scroll-2][0])
        print(packagelist[scroll-1][0])
        print(packagelist[scroll][0])
        print(packagelist[scroll+1][0])
        print(packagelist[scroll+2][0])
    except IndexError:
        pass
    a = m.getch()
    if (a == b'H'):
        scroll -= 1
    if (a == b'P'):
        scroll += 1
    if (a == b'\x1b'):
        running = False

global running
running = True
while running:
    os.system("cls")
    scrollwheel()