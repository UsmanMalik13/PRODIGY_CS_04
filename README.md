# PRODIGY_CS_04
## Python Keylogger with Hourly Timestamps

### Overview

This project is a simple keylogger written in Python using the `pynput` library. It listens for keyboard input and logs all keypresses to a text file (`keyfile.txt`). The logger captures both character and special keys, and it appends an hourly timestamp to the log to track the passage of time during keylogging activities.

### Features

- **Logs All Keypresses**: Captures all alphanumeric characters and special keys (e.g., Enter, Shift, Backspace).
- **Hourly Timestamps**: Automatically inserts a timestamp into the log once every hour to track when the keypresses occurred.
- **Special Key Logging**: Non-character keys are logged with their respective names (e.g., `[Key.enter]`, `[Key.shift]`).
- **Persistent Logging**: Logs are continuously saved in `keyfile.txt` as keypresses are detected.

### How It Works

- The keylogger starts listening as soon as the script is executed.
- Every keypress is recorded, and special keys are noted using a bracketed notation (e.g., `[Key.enter]`).
- Once an hour has passed since the last log entry, a timestamp is added to the log file to mark the time.

### Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/keylogger-timestamp
   cd keylogger-timestamp

