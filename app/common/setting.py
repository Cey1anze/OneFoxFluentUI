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
YUJIAN_PATH = resource_path('AppData\\gui_shouji\\yjdirscanv1.1\\御剑2.exe')
TIDE_PATH = resource_path('AppData\\gui_shouji\\tide\\TideFinger_Win.exe')
MULTIPLEPUPILS_PATH = resource_path('AppData\\gui_shouji\\fofaviewer\\MultiplePupils.exe')
ENSCAN_PATH = resource_path('AppData\\gui_shouji\\enscan\\enscan-0.0.15-windows-amd64.exe')


YEAR = 2024
AUTHOR = "Cey1anze"
VERSION = "v0.0.1"
HELP_URL = "https://github.com/Cey1anze/OneFoxFluentUI"
FEEDBACK_URL = "https://github.com/Cey1anze/OneFoxFluentUI/issues"

CONFIG_FOLDER = Path('AppData').absolute()
CONFIG_FILE = CONFIG_FOLDER / "config.json"
