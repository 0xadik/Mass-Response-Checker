import requests
import time
print('''
========================================================================
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
========================================================================
           www.facebook.com/sadikul.official || Never Give UP 
========================================================================
''')
file = str(input("Enter Your File Name: ")).strip()
print("[=] Loading Please wait...")
print("\n")
with open(file , "r") as urls:
    for url in urls:
        print(url.strip())
        response = requests.get(url.strip())
        if response.status_code == 200:
            print("[=] Status 200 ==> OK")
            save = open("Live.txt" , "a").writelines(url)
            print("[=] Saved !!!")
            print("\n")
        else:
            print("False")
            print("\n")
input("[+] Press Enter To Exit")
