from time import time_ns
import json
import os


def mk_log(encoding: str, data_meaning: str, log_id: int, flight_id: int, data_dump: any):
    # Save directory for log files
    save_path = os.path.join(os.path.abspath(os.pardir), "Data_Logs")
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    # Data to dump to json file
    json_out = {"rec_time": time_ns(),
                "log_id": log_id,
                "flight_id": flight_id,
                "encoding": encoding,
                "data_meaning": data_meaning,
                "data": data_dump}

    with open(os.path.join(save_path, f"{json_out['rec_time']}")) as out_file:
        json.dump(json_out, out_file)



