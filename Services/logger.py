from time import time_ns
import json
import os
import tkinter as tk


def start(encoding: str, data_meaning: str, log_id: int, flight_id: int, data_dump: any):
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


def configure():
    # allow the user to change the save directory and other log attributes
    window = tk.Tk()
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    # TODO: Figure out how to make window and element dynamically sized
    default_xpad = 5
    default_ypad = 5

    header = tk.Frame(master=window)
    header.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    content = tk.Frame(master=window)
    content.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)

    header_msg = """Configure the logger"""
    header_lb = tk.Label(text=header_msg, master=header)
    header_lb.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)

