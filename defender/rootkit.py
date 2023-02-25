import subprocess

def detect_rootkits():
    cmd = 'chkrootkit'
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        if b'not infected' not in output:
            print('WARNING: Rootkit detected!')
    except:
        pass

detect_rootkits()