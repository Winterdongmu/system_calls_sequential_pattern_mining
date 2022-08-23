import json
import pandas as pd
data = json.load(open('G:\project\lisa_data\\falco_logs\events_2.json'))

df = pd.DataFrame(data["rule"])
for i in empty_data:
    if i["rule"] == "Test open file":
        tmp_time = datetime.datetime.now()
        tmp_time2 = datetime.datetime.now() + datetime.timedelta(seconds=10)
        tmp_time2 = tmp_time2
        print(tmp_time2-tmp_time)