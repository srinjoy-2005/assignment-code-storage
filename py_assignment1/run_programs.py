import subprocess

for i in range(22,31):
    subprocess.Popen(f'python .\{i}.py',shell=True)