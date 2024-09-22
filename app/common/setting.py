# coding: utf-8
from pathlib import Path

from app.common.utils import resource_path

# change DEBUG to False if you want to compile the code to exe
DEBUG = "__compiled__" not in globals()

defaultJava8Path = resource_path('app\\resource\\runtime\\Java_path\\Java_8_win\\bin\\java.exe')
defaultJava11Path = resource_path('app\\resource\\runtime\\Java_path\\Java_11_win\\bin\\java.exe')
defaultPythonPath = resource_path('app\\resource\\runtime\\Python_path\\python.exe')

BEHINDER_PATH = resource_path('Appdata\\gui_webshell\\Behinder4\\Behinder.jar')
GODZILLA_PATH = resource_path('AppData\\gui_webshell\\Godzilla\\godzilla.jar')
ANTSWORD_PATH = resource_path('AppData\\gui_webshell\\AntSword\\AntSword\\AntSword-Loader-v4.0.3-win32-x64\\AntSword.exe')
TIANXIE_PATH = resource_path('AppData\\gui_webshell\\TianXie\\天蝎权限管理工具.jar')
ALIEN_PATH = resource_path('AppData\\gui_webshell\\alien\\WebShell.exe')

SNOWSHADOW_PATH = resource_path('AppData\\gui_shouji\\leiying\\SnowShadow_v1.0\\SnowShadow.exe')
WEBFINDER_PATH = resource_path('AppData\\gui_shouji\\webfinder-next.jar')


YEAR = 2024
AUTHOR = "Cey1anze"
VERSION = "v0.0.1"
APP_NAME = "OFF"
HELP_URL = "https://qfluentwidgets.com"
REPO_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets"
FEEDBACK_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues"
DOC_URL = "https://qfluentwidgets.com/"

CONFIG_FOLDER = Path('AppData').absolute()
CONFIG_FILE = CONFIG_FOLDER / "config.json"
