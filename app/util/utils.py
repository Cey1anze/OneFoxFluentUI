import os
import subprocess

from app.common.config import cfg
from app.common.setting import defaultJava8Path, defaultJava11Path, defaultPythonPath


def run_command(command: str, runtime_type: str = None, java_version: int = None):
    isCustomJava = cfg.get(cfg.isCustomJava)
    isCustomPython = cfg.get(cfg.isCustomPython)
    customJavaPath = cfg.get(cfg.customJavaPath)
    customPythonPath = cfg.get(cfg.customPythonPath)

    command_to_run = []
    executable_path = os.path.dirname(command)

    try:
        if runtime_type == 'java':
            # 根据是否使用自定义 Java 路径
            if isCustomJava:
                command_to_run = ['cd', executable_path, '&&', customJavaPath, '-jar', command]
            else:
                # 根据 Java 版本选择路径
                java_paths = {8: defaultJava8Path, 11: defaultJava11Path}
                java_path = java_paths.get(java_version)
                if not java_path:
                    return f"Error: Unsupported Java version {java_version}"
                command_to_run = ['cd', executable_path, '&&', java_path, '-jar', command]

        elif runtime_type == 'python':
            command_to_run = [customPythonPath if isCustomPython else defaultPythonPath, command]

        elif runtime_type is None:
            command_to_run = ['cd', executable_path, '&&', command]

        result = subprocess.Popen(command_to_run, shell=True)
        return result.stdout

    except subprocess.CalledProcessError as e:
        return f"Command '{' '.join(command_to_run)}' failed with error: {e.stderr}"