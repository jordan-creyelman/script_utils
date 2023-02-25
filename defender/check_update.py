import subprocess

def check_security_updates():
    cmd = 'apt-get update && apt-get -s upgrade'
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        if b'0 upgraded' not in output:
            print('WARNING: Security updates available!')
    except:
        pass

check_security_updates()