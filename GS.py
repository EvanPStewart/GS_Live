import tkinter as tk
from tkinter import ttk


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
            port_box.insert(0, "900")
            port_box.config(state="disabled")
        else:
            port_box.config(state="normal")

    default_port_status = tk.IntVar()

    # ----------
    # Frames
    # ----------
    header_frame = tk.Frame(master=window)
    header_frame.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    # header_frame.rowconfigure(0, weight=1, pad=5)
    # header_frame.columnconfigure(0, weight=1, pad=5)
    content_frame = tk.Frame(master=window)
    content_frame.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)
    # content_frame.rowconfigure(1, weight=1, pad=5)
    # content_frame.columnconfigure(0, weight=1, pad=5)
    service_frame = tk.Frame(master=content_frame)
    service_frame.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    # service_frame.rowconfigure(0, weight=1, pad=5)
    # service_frame.columnconfigure(0, weight=1, pad=5)
    network_frame = tk.Frame(master=content_frame)
    network_frame.grid(row=0, column=1, padx=default_xpad, pady=default_ypad)
    # network_frame.rowconfigure(0, weight=1, pad=5)
    # network_frame.columnconfigure(1, weight=1, pad=5)

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
    services = ["test1", "test2"]
    service_ddl_label = tk.Label(text="Select a service:", master=service_frame)
    service_ddl_label.grid(row=0, column=0, padx=default_xpad, pady=default_ypad)
    service_ddl = ttk.Combobox(master=service_frame, values=services)
    service_ddl.set("Pick an Option")
    service_ddl.grid(row=1, column=0, padx=default_xpad, pady=default_ypad)
    configure_service = tk.Button(text="Configure Service", master=service_frame)
    configure_service.grid(row=2, column=0, padx=default_xpad, pady=default_ypad)
    start_service = tk.Button(text="Start Service", master=service_frame)
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


if __name__ == "__main__":
    main()
