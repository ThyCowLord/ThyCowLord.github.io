import os

import sys
if os.geteuid() != 0:
    exit("\033[1;31;40m Run again as root, using sudo python3 willow.py \n")
try:
    print("Welcome to Willow! ")
    print("")
    option = input("Please enter the corresponding number to the option you would like. Would you like to clone(1), wipe(2) or burn an image(3) to a drive? \n") 
    print("List of current drives below: \n")
    os.system("sudo fdisk -l")
    if option == "1":
        option2 = input("Which drive would you like clone? (e.g sda1, sda2 etc)")
        option3 = input("What drive would you like ", option2, "to be cloned to?")
        com2 = "sudo umount /dev/"+option2
        os.system(com2)
        com = "sudo dd if=/dev/"+option2+" of=/dev/"+option3+" bs=64K conv=noerror, sync"
        os.system(com)
        if option == "2":
            option2 = input("Which drive would you like to wipe? (e.g sda1, sda2 etc.")
            com = "sudo rm -rf /dev/"+option2
            if option == "3":
                option2 = input("Which drive would you like to burn an image to? (e.g sda1, sda2 etc")
                option3 = input("Enter the path to the OS image: (e.g /home/users/example/Desktop/ubuntu.iso) ")
                com2 = "sudo umount /dev/"+option2
                os.system(com2)
                com = "sudo dd if="+option3+" of=/dev/"+option2+" bs=4M conv=fdatasync"
                os.system(com)
                if option != [1, 2, 3]:
                    print("Invalid I.D.")
    
except KeyboardInterrupt as e:
    print("")
    print("Thanks for using Willow! ")
                    
