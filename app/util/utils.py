import os
import subprocess
import psutil

from app.common.config import cfg
from app.common.setting import defaultJava8Path, defaultJava11Path, defaultPythonPath


def is_process_running(process_name, pid=None):
    """Checks if a process with the specified name is running"""
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                if pid is None or proc.pid == pid:
                    return proc.pid

            if process_name.endswith('.jar'):
                if any(arg.endswith(process_name) for arg in proc.cmdline()):
                    return proc.pid

            elif process_name.endswith('.py'):
                if any(arg.endswith(process_name) for arg in proc.cmdline()):
                    return proc.pid

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None


def run_command(command: str, shell=False, runtime_type: str = None, java_version: int = None, *args):
    isCustomJava = cfg.get(cfg.isCustomJava)
    isCustomPython = cfg.get(cfg.isCustomPython)
    customJavaPath = cfg.get(cfg.customJavaPath)
    customPythonPath = cfg.get(cfg.customPythonPath)

    command_to_run = []
    executable_path = os.path.dirname(command)
    process_name = os.path.basename(command)

    existing_pid = is_process_running(process_name)
    if existing_pid:
        return f"Process {process_name} is already running with PID: {existing_pid}."

    try:
        if runtime_type == 'java':
            if isCustomJava:
                command_to_run = [customJavaPath, '-jar', command]
            else:
                java_paths = {8: defaultJava8Path, 11: defaultJava11Path}
                java_path = java_paths.get(java_version)
                if not java_path:
                    return f"Error: Unsupported Java version {java_version}"
                command_to_run = [java_path, '-jar', command]

        elif runtime_type == 'python':
            command_to_run = [customPythonPath if isCustomPython else defaultPythonPath, command]

        elif runtime_type is None:
            command_to_run = [command]

        command_to_run.extend(args)

        process = subprocess.Popen(command_to_run, cwd=executable_path, shell=shell)

        return process

    except Exception as e:
        return f"An error occurred: {str(e)}"
