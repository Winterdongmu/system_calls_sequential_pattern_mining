import json
import datetime
import time

while True:
    path = "G:\project\lisa_data\\falco_logs\events_2.json"
    empty_data = []
    with open(path) as f:
        line = f.readline()
        while line:
            new_dict = json.loads(line)
            empty_data.append(new_dict)
            line = f.readline()

    start_mark = 0
    count_error = 0
    for i in empty_data:
        if i["rule"] == "Test open file" and (datetime.datetime.now()-datetime.datetime.fromisoformat(i["time"][:-4])).total_seconds() < 10  and start_mark == 0:
            start_mark = 1
            count_error += 1
            tmp_time = datetime.datetime.now()
        elif i["rule"] == "Test open file" and start_mark == 1 and count_error < 8 and (datetime.datetime.fromisoformat(i["time"][:-4]) - tmp_time).total_seconds() < 10:
            count_error += 1
        elif i["rule"] == "Test open file" and start_mark == 1 and count_error >= 8 and (datetime.datetime.fromisoformat(i["time"][:-4]) - tmp_time).total_seconds() < 10:
            print("Sensitive files that contain attributes of pod's CPU opened.")
            count_error = 0
            start_mark = 0

    time.sleep(2)
