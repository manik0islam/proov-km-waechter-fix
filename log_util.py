# log_util.py
# Eigener Logger. Das logging-Modul war uns 2013 "zu viel Magie".
# (A homemade logger. The logging module felt like "too much magic" in 2013.)

import time

LOG_LINES: list[str] = []
DEBUG = False


def log(message: str) -> None:
    """Print a timestamped message and buffer it for flush_log."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def debug(message: str) -> None:
    """Print a debug message only when DEBUG is True."""
    if DEBUG:
        log(f"DEBUG: {message}")


def flush_log(path: str) -> None:
    """Append buffered log lines to the file at *path* and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
