import wmi

f = wmi.WMI()

for process in f.Win32_Process():
    print(f"{process.processId:<10} {process.Name}" )   