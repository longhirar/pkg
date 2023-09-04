import os
import sys
import csv

PKGLIST_URL = "https://pkg.longhi.me/packagelist"

print("Baixando Lista de Pacotes...")
os.system(f"mkdir C:\\Users\\{os.getlogin()}\\longhipkg")
if (os.system(f"powershell.exe Invoke-WebRequest -Uri {PKGLIST_URL} -OutFile C:\\Users\\{os.getlogin()}\\longhipkg\\packagelist.csv")) != 0:
    print("===================================")
    print("Falha ao atualizar lista de pacotes")
    print("===================================")
    sys.exit(1)


with open(f"C:\\Users\\{os.getlogin()}\\longhipkg\\packagelist.csv", "r") as packagelistfile:
    packagelist = csv.reader(packagelistfile, delimiter=";")
    for package in packagelist:
        print(package)