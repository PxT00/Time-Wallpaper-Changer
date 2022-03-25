import ctypes 

from datetime import datetime
from time import sleep

manha_path = "C:/Users/gabri/Documents/Wallpaper images/manha.jpg"
tarde_path = "C:/Users/gabri/Documents/Wallpaper images/tarde.jpg"
noite_path = "C:/Users/gabri/Documents/Wallpaper images/noite.jpg"

def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

def check_system_hour():
    now = datetime.now()
    hour = now.hour
    if hour >= 6 and hour <= 12:
        print("Hora é de manhã")
        return "manhã"
    elif hour >= 13 and hour <= 18:
        print("Hora é de tarde")
        return "tarde"
    elif hour >= 19 and hour <= 23:
        print("Hora é de noite")
        return "noite"
    elif hour >= 0 and hour <= 5:
        print("Hora é de madrugada")
        return "madrugada"

while True:
    print("Verificando hora...")
    if check_system_hour() == "manhã":
        set_wallpaper(manha_path)
        print("Wallpaper set to manhã")
    elif check_system_hour() == "tarde":
        set_wallpaper(tarde_path)
        print("Wallpaper set to tarde")
    elif check_system_hour() == "noite":
        set_wallpaper(noite_path)
        print("Wallpaper set to noite")
    elif check_system_hour() == "madrugada":
        print("Wallpaper set to madrugada")
        set_wallpaper(noite_path)
    sleep(5)
