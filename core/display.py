import json, os, sys, ctypes, shutil
from pystyle import Colorate, Colors



# color function ------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_config():
    path = os.path.join(BASE_DIR, "..", "core", "config.json")
    with open(path, "r") as f:
        return json.load(f)

def save_config(data):
    path = os.path.join(BASE_DIR, "..", "core", "config.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

cfg = get_config()

SCHEMES = {
    "none": None,
    "red_to_white": Colors.red_to_white,
    "green_to_white": Colors.green_to_white,
    "blue_to_white": Colors.blue_to_white,   


    "purple_to_red": Colors.purple_to_red,

    "rainbow": Colors.rainbow,

    "red_to_yellow": Colors.red_to_yellow,
    "blue_to_cyan": Colors.blue_to_cyan,

    "purple_to_blue": Colors.purple_to_blue,

    "green_to_cyan": Colors.green_to_cyan,
    "red_to_black": Colors.red_to_black,
}

def get_scheme():
    try:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "core", "config.json")
        with open(path, "r") as f:
            cfg = json.load(f)
        scheme_key = cfg.get("color_scheme", "red_to_white")
        return SCHEMES.get(scheme_key, Colors.red_to_white)
    except:
        return Colors.red_to_white

def csh(text):
    scheme = get_scheme()
    if scheme is None:
        return text

    return Colorate.Horizontal(get_scheme(), text)


# cursor hide ------------------------------------

def hide_cursor():
    ci = ctypes.Structure.__new__(type('CONSOLE_CURSOR_INFO', (ctypes.Structure,), {
        '_fields_': [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_int)]
    }))
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.bVisible = 0
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

def show_cursor():
    ci = ctypes.Structure.__new__(type('CONSOLE_CURSOR_INFO', (ctypes.Structure,), {
        '_fields_': [("dwSize", ctypes.c_int), ("bVisible", ctypes.c_int)]
    }))
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.bVisible = 1
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))



# clear func ------------------------------------
def clear_all():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")















# print banners ------------------------------------



def print_banner2(color="\033[1;31m"):
    banner = [
        "▄▄▄   ▄▄▄            ",
        "███   ███            ",
        "█████████ ▄█▀█▄ ██ ██",
        "███▀▀▀███ ██▄█▀  ███ ",
        "███   ███ ▀█▄▄▄ ██ ██",
    ]
    width = os.get_terminal_size().columns
    for line in banner:
        sys.stdout.write(color + line.center(width) + "\033[0m\n")
    sys.stdout.flush()


def print_banner():
    banner = [
        "▄▄▄   ▄▄▄            ",
        "███   ███            ",
        "█████████ ▄█▀█▄ ██ ██",
        "███▀▀▀███ ██▄█▀  ███ ",
        "███   ███ ▀█▄▄▄ ██ ██",
    ]
    width = os.get_terminal_size().columns
    for line in banner:
        print(csh(line.center(width)))
    sys.stdout.flush()








