from SshToServer import SshToServer
import json
import csv
import os

def append_to_csv(data):
    file_path = r"C:\Users\idoel\linux\stat.csv"
    file_exists = os.path.isfile(file_path)
 
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        if not file_exists:
            writer.writerow(["Time", "INFO", "WARN", "ERROR"])
        writer.writerow(data)

def getDataFromLinux():
    my_linux = SshToServer(r"C:\Users\idoel\linux\my-key.pem", "13.60.171.183", "ubuntu")
    result = my_linux.runRemoteCommand("python3 counter.py")
    append_to_csv(json.loads(result[0]))
    print("end")

if __name__ == "__main__":
    getDataFromLinux()
