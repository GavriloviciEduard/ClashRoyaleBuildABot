import multiprocessing
import subprocess
import os
import signal


def start_process(process_path: str, args: str = ""):
    """Start process.

    Args:
        process_path (str): Path to process to start.
        args (str, optional): Arguments for process. Defaults to "".
    """

    return subprocess.Popen([process_path, args])


def stop_process(pid: int):
    """Stop process.

    Args:
        pid (int): process id of process to stop.
    """

    os.kill(pid, signal.SIGTERM)
