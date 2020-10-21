import time

enabled = True
show_time = True
log_file = None

def list2str(my_list):
    string = "("

    for item in my_list:
        string += str(item)
        if item != my_list[len(my_list) - 1]:
            string += ", "
    
    string += ")"
    return string

def log(message, log_origin = None):
    global enabled
    global show_time
    global log_file

    if enabled:
        log_msg = ""

        if isinstance(message, list):
            message = f"{list2str(message)}"     

        if show_time:
            log_msg += f"[{time.asctime()}] "
        if log_origin:
            log_msg += f"<{log_origin}> "
        log_msg += message

        if log_file:
            f = open(log_file, "a")
            f.write(log_msg + "\n")
            f.close()
        else:
            print(log_msg)

def wait(s=0):
    if s <= 0:
        _ = input("press enter to continue...")
    else:
        time.sleep(s)