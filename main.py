import os
import time

def restoreSystemFile():
    os.system("clear")
    bckup = open("95hdparm-apm", "r")
    if(bckup.mode == "r"):
        dump = bckup.read()
        SYS_File = open("/usr/lib/pm-utils/power.d/95hdparm-apm", "w")
        SYS_File.write(dump)
        SYS_File.close()
        print("Restore complete!")
        input("Press any key to continue...")
        os.system("clear")
        print("See you...")
    else:
        print("Error.\n95hdparm-apm not found!\nDo you have backup file? This file is created by the program, but maybe something has happened to it.")

def selectMainOperation():
    os.system("clear")
    print("Select your operation.\n1)Run fix code!\n2)Restore modded files.")
    usr=int(input("USER>> "))
    if(usr==1):
        checkSystemFileExist()
    elif(usr==2):
        restoreSystemFile()
    else:
        os.system("clear");
        print("Error while taking your number.")
        print("Possible reasons:\nLeaving a space at the beginning or end of the number.\nEntering a character other than the numbers in the option.")

def checkSystemFileExist():
    try:
        bckup = open("95hdparm-apm", "w")
        os.system("clear")
        print("Dumping file...")
        time.sleep(1.5)
        dump=os.popen("cat /usr/lib/pm-utils/sleep.d/95hdparm-apm").read()
        print(dump)
        time.sleep(1.0)
        os.system("clear")
        print("Dumping Successful.")
        print("Continues...")
        time.sleep(2.0)
        os.system("clear")

        if("loginctl terminate-user" in dump):
            print("Your system files allready modded. You can restore them.")
            exit()

        bckup.write(dump)
        bckup.close()
        print("Getting line number...")
        print("The line number is where the code will be inserted. The code that solves the problem will be added below this line.")
        line_number=0
        for line in dump.splitlines():
            line_number+=1
            if(line=="        resume_hdparm_spindown"):
                break
        print("Line number found: "+ str(line_number))
        print("Do you approve to continue?\n1)Yes\n2)No")
        usr=int(input("USER>>"))
        if(usr==1):
            os.system("clear")
            print("If you don't read this, your computer could be damaged!")
            print("Enter the username with which you are currently using the computer. Otherwise, you may have problems.")
            print("\nMY CURRENT USERNAME IS:")
            username=str(input("USER>>"))
            modded_dump=dump.replace("        resume_hdparm_spindown", "        resume_hdparm_spindown\n        loginctl terminate-user "+username)
            SYS_File = open("/usr/lib/pm-utils/power.d/95hdparm-apm", "w")
            SYS_File.write(modded_dump)
            SYS_File.close()
            os.system("clear")
            print("Your system has been successfully refreshed. The user will now exit from sleep mode so the computer will run smoothly as if it was temporarily restarted.")
            print("\n IF YOU WILL HAVE A ERROR then you can restore your modded system files back by backup file.")
            print("\n Follow me...\n")
            print("Twitter:0rbianta\nGitHub:0rbianta\nAnd nothing else to say.")
            input("Press any key to continue...")
            os.system("clear")
            print("Good bye!")

        elif(usr==2):
            os.system("clear")
            print("Exiting...")
        else:
            os.system("clear");
            print("Error while taking your number.")
            print("Possible reasons:\nLeaving a space at the beginning or end of the number.\nEntering a character other than the numbers in the option.")

    except:
        print("Error\n/usr/lib/pm-utils/power.d/95hdparm-apm not found!\nProgram can't continue.")

def main():

    user_profile=os.popen("whoami").read()
    if("root" in user_profile):
        os.system("clear")
    else:
        print("Please run as root.")
        exit()

    print(" m    m mmmm   mmmmmm ")
    print(" #  m\"  #   \"m #      ")
    print(" #m#    #    # #mmmmm ")
    print(" #  #m  #    # #      ")
    print(" #   \"m #mmm\"  #mmmmm ")

    print("\n")

    print(" mm   m m    m mmmmm  mmmm   mmmmm    mm  ")
    print(" #\"m  # \"m  m\"   #    #   \"m   #      ##  ")
    print(" # #m #  #  #    #    #    #   #     #  # ")
    print(" #  # #  \"mm\"    #    #    #   #     #mm# ")
    print(" #   ##   ##   mm#mm  #mmm\"  mm#mm  #    #")

    print("\n")

    print(" mmmmmm mmmmm  m    m")
    print(" #        #     #  # ")
    print(" #mmmmm   #      ##  ")
    print(" #        #     m\"\"m ")
    print(" #      mm#mm  m\"  \"m")

    time.sleep(1.0);
    os.system("clear");
    print("This software has not been tested on all computers and operating systems. If you will use this software, you accept the risk. This software replaces the system file starting with 95 located outside of power.d. It adds a code that solves the whole error. In this way, when we put the computer to sleep mode of NVIDIA, we will not encounter disgusting errors and broken graphics again. Before using the program, I remind you that all responsibility belongs to you. Data loss, Computer damage etc. I am not responsible for anything. If you agree to take responsibility, continue.\n")
    print("1)Accept\n2)Refuse\n")
    usr=int(input("USER>> "))
    if(usr==1):
        selectMainOperation()
    elif(usr==2):
        os.system("clear")
        print("Exiting...")
    else:
        os.system("clear");
        print("Error while taking your number.")
        print("Possible reasons:\nLeaving a space at the beginning or end of the number.\nEntering a character other than the numbers in the option.")

if __name__ == '__main__':
    main()
