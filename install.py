# check if selenium is available
# check if firefox is installed
# get user credentials from user

#checking for selenium
try:
    import selenium
except:
    print("selenium not installed.\nTry 'pip install selenium and try again'")
    sys.exit()
    
print('WARNING : Firefox must be installed.')

print("Enter Keka credentials.")
kname = input('Email Id : ')
kpass = input('Password : ')

print("Enter local login credentials.")
lname = input("Username : ")
lpass = input("Password : ")

file = open("credentials.txt","w")
file.write("#LocalLoginDetails\n")
file.write("Username: "+lname+"\n")
file.write("Password: "+lpass+"\n")
file.write("#KekaLoginDetails\n")
file.write("Username: "+kname+"\n")
file.write("Password: "+kpass+"\n\n")
file.write("#maintain the space\n#Eg : Username: walter")
file.close()

import os
pwd = os.getcwd()
file = open("loginAutomation.desktop","w")
file.write("[Desktop Entry]\n")
file.write("Encoding=UTF-8\n")
file.write("Name=loginAutomation\n")
file.write("Icon=gnome-info\n")
file.write("Exec=python3 "+pwd+"/loginAutomation.py\n")
file.write("Terminal=true\n")
file.write("Type=Application\n")
file.write("Categories=\n\n")
file.write("X-GNOME-Autostart-enabled=true\n")
file.write("X-GNOME-Autostart-Delay=5")
file.close()

print("creating autologin setting\n")
os.system("chmod u+x loginAutomation.desktop")
os.system("mv loginAutomation.desktop ~/.config/autostart")
