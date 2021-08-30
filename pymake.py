import os
import subprocess
import sys  

quit = ['q', 'quit']
run = ['r', 'run']
server = ['s', 'server']
client = ['c', 'client']

if len(sys.argv) == 2:
    if any(sys.argv[1] == r for r in run):
        subprocess.run('start powershell "python server.py"', shell=True)
        subprocess.run('start powershell "python client.py"', shell=True)

    elif any(sys.argv[1] == q for q in quit):
        subprocess.run("powershell.exe -command Stop-Process -Name 'python'", shell=True)

elif len(sys.argv) == 3:
    if any(sys.argv[1] == r for r in run) and any(sys.argv[2] == s for s in server):
        subprocess.run('start powershell "python server.py"', shell=True)
    elif any(sys.argv[1] == r for r in run) and any(sys.argv[2] == c for c in client):
        subprocess.run('start powershell "python client.py"', shell=True)   
