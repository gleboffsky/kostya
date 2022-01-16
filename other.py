import tkinter
from tkinter import filedialog
import serial
from datetime import datetime
import time as tme
data = input()
port,connection_speed,timeout, btn = data.split()

root = tkinter.Tk()
root.withdraw()
filepath = filedialog.asksaveasfilename(confirmoverwrite=False)
try:
    ser = serial.Serial(port=port, baudrate=connection_speed, timeout=int(timeout))

    while True:
        serialString = ser.readline()
        data_str = serialString.decode('UTF-8')
        now = str(datetime.now())
        if filepath[-4] != ".":
            if data_str != "":
                log_file = open(filepath + ".csv", 'a')
                log_file.write(str(now)[0:-7] + ' ' + str(data_str))
                log_file.close()
                print(filepath+ ".csv")
        else:
            if data_str != "":
                log_file = open(filepath, 'a')
                log_file.write(str(now)[0:-7] + ' ' + str(data_str))
                log_file.close()
                print(filepath)
        tme.sleep(0.1)

except:
    print("error")


