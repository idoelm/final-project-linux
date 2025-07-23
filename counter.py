import subprocess
import json
def run_local_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), result.stderr.strip()

    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr.strip()}")
        return None, e.stderr.strip()

def checkResult(count):
    if count[0] is not None and count[0].isdigit():
        return True
    return False


def main():
    data = [None] * 4
    count = run_local_command("date +%s")
    if checkResult(count):
        data[0] = int(count[0])
    else:
        data[0] = 0

    count = run_local_command("grep -c INFO /var/log/syslog")
    if checkResult(count):
        data[1] = int(count[0])
    else:
        data[1] = 0

    count = run_local_command("grep -c WARN /var/log/syslog")
    if checkResult(count):
        data[2] = int(count[0])
    else:
        data[2] = 0 


    count = run_local_command("grep -c ERROR /var/log/syslog")
    if checkResult(count):
        data[3] = int(count[0])
    else:
        data[3] = 0
    print(json.dumps(data))
if __name__ == "__main__":
    main()