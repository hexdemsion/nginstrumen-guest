import subprocess
import os
import time
from threading import Thread
import requests

from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello from agent server"



def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

def tasked():
    anu = subprocess.Popen(["C:\\Users\\IEUser\\Desktop\\nginstrumen-guest\\lihat.exe", "/AcceptEula", "/BackingFile", "C:\\Users\\IEUser\\Desktop\\nginstrumen-guest\\logbit.pml", "/LoadConfig", "C:\\Users\\IEUser\\Desktop\\nginstrumen-guest\\locknot.pmc", "/Quiet"] )
    print(anu)

    time.sleep(5)
    ransomed = subprocess.Popen(["C:\\Users\\IEUser\\Desktop\\nginstrumen-guest\\LOCKBITv2.exe"] )
    # ransomed = subprocess.Popen(["C:\\Windows\\System32\\notepad.exe"] )

    still_ransom = True
    while still_ransom:
        time.sleep(2)
        if process_exists("LOCKBITv2.exe"):
            print("The ransomware process is still running...")
        else:
            print("Ransomware process has been stopped. Terminating ProcMon now...")
            killed = subprocess.Popen(["C:\\Users\\IEUser\\Desktop\\nginstrumen-guest\\lihat.exe", "/Terminate"] )

            files = {'fileku': open('logbit.pml', 'rb'),}
            response = requests.post('http://192.168.56.1:9090/receive-file', files=files)

            still_ransom = False





@app.route('/run-procmon')
def run_procmon():
    t1 = Thread(target=tasked)
    t1.start()

    return "ProcMon & Malware will be started now..."






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

