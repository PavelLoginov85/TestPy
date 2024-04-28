import subprocess

def execute_command(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False