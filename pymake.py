import os
import subprocess
import sys  

quit = ['q', 'quit']
run = ['r', 'run']

if len(sys.argv) == 2:
    if any(sys.argv[1] == r for r in run):
        subprocess.run('start powershell "python server.py"', shell=True)

    elif any(sys.argv[1] == q for q in quit):
        subprocess.run("powershell.exe -command Stop-Process -Name 'python'", shell=True)