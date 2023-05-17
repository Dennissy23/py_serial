import subprocess


subprocess.Popen(["python","get_IMU.py"])
subprocess.Popen(["python","get_RSSI.py"])
subprocess.Popen(["python","get_GNSS.py"])


