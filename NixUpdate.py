import os
from sys import platform

if platform == "darwin":
  input("Error: System not supported!")
if platform == "win32":
  input("Error: System not supported!")

def clear():
  os.system("clear")
    
def nixupdate():
  clear()
  print("███╗░░██╗██╗██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗")
  print("████╗░██║██║╚██╗██╔╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝")
  print("██╔██╗██║██║░╚███╔╝░██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░")
  print("██║╚████║██║░██╔██╗░██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░")
  print("██║░╚███║██║██╔╝╚██╗╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗")
  print("╚═╝░░╚══╝╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝")
  category_of_update = input("\nUpdate 'packages' or 'channels' (1, 2)? ")
  if category_of_update == "packages" or category_of_update == "package" or category_of_update == "1":
    os.system("nix-env -u")
  elif category_of_update == "channels" or category_of_update == "channel" or category_of_update == "2":
    os.system("nix-channel --update")
  else:
    input("Error: Command not found!")

while True:
  nixupdate()
