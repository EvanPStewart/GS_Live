import os.path
import tkinter as tk
from tkinter import ttk
import Services as Sv


def main():
    # Main window
    window = tk.Tk()
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    # TODO: Figure out how to make window and element dynamically sized
    default_xpad = 5
    default_ypad = 5

    # Event callbacks
    def use_local_ip():
        if local_ip_status.get():
            ip_box.delete(0, tk.END)
            ip_box.insert(0, "127.0.0.1")
            ip_box.config(state="disabled")
        else:
            ip_box.config(state="normal")

    local_ip_status = tk.IntVar()

    def use_default_port():
        if default_port_status.get():
            port_box.delete(0, tk.END)
            port_box.insert(0, "1555")
            port_box.config(state="disabled")
        else:
            port_box.config(state="normal")

    default_port_status = tk.IntVar()

    def ddl_config():
        services[service_ddl.get()].configure()

    def ddl_start():
        services[service_ddl.get()].start()

    services = {"test1": "test1v", "test2": "test2v", "logger": Sv.logger}

    # ----------
    # Frames
    # ----------
    header_frame = tk.Frame(master=window)
    header_frame.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    content_frame = tk.Frame(master=window)
    content_frame.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)
    service_frame = tk.Frame(master=content_frame)
    service_frame.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    network_frame = tk.Frame(master=content_frame)
    network_frame.grid(row=0, column=1, padx=default_xpad, pady=default_ypad)

    # ----------
    # Header frame
    # ----------

    greeting_msg = """Welcome to GS Live!
    For information on how to use the ground station, consult the README file.
    To submit a complaint, write the complaint to a plaintext file and save in /dev/null/
    """
    greeting = tk.Label(text=greeting_msg, master=header_frame)
    greeting.grid(row=0, column=0, padx=5, pady=5)

    # ----------
    # Content frame
    # ----------

    # Service frame
    service_ddl_label = tk.Label(text="Select a service:", master=service_frame)
    service_ddl_label.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    service_ddl = ttk.Combobox(master=service_frame, values=list(services.keys()))
    service_ddl.set("Pick an Option")
    service_ddl.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)
    configure_service = tk.Button(text="Configure Service", master=service_frame, command=ddl_config)
    configure_service.grid(row=2, column=0, padx=default_xpad, pady=default_ypad)
    start_service = tk.Button(text="Start Service", master=service_frame, command=ddl_start)
    start_service.grid(row=3, column=0, padx=default_xpad, pady=default_ypad)

    # Network frame
    ip_box_lb = tk.Label(text="Enter an IP address:", master=network_frame)
    ip_box_lb.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    ip_box = tk.Entry(master=network_frame)
    ip_box.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)
    local_ip_select = tk.Checkbutton(text="Use localhost", master=network_frame, variable=local_ip_status, onvalue=1,
                                     offvalue=0, command=use_local_ip)
    local_ip_select.grid(row=1, column=1, padx=default_xpad, pady=default_ypad)

    port_box_lb = tk.Label(text="Enter a port:", master=network_frame)
    port_box_lb.grid(row=2, column=0, padx=default_xpad, pady=default_ypad)
    port_box = tk.Entry(master=network_frame)
    port_box.grid(row=3, column=0, padx=default_xpad, pady=default_ypad)
    default_port_select = tk.Checkbutton(text="Use default port", master=network_frame, variable=default_port_status,
                                         onvalue=1, offvalue=0, command=use_default_port)
    default_port_select.grid(row=3, column=1, padx=default_xpad, pady=default_ypad)

    window.mainloop()


def cleanup(tmp_dir):
    print("Cleaning up...")
    for tmp_file in os.listdir(tmp_dir):
        os.remove(os.path.join(tmp_path, file))
    os.rmdir(tmp_path)
    print("Done!")


if __name__ == "__main__":
    # creating a temp folder to store runtime information
    tmp_path = os.path.join(os.path.abspath(os.curdir), "temp")
    if not os.path.isdir(tmp_path):
        os.mkdir(tmp_path)
    else:
        print("previous runtime environment detected! Deleting temporary files...")
        for file in os.listdir(tmp_path):
            os.remove(os.path.join(tmp_path, file))
    # Main GUI
    main()
    # Cleaning up runtime environment
    cleanup(tmp_path)
