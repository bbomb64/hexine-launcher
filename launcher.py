import subprocess
import os
import shutil

class Launcher():
    def __init__(self):
        self.defaultServer = "localhost"
        self.defualtPort = 53640

        self.appDataPath = os.getenv('LOCALAPPDATA')
        self.version = self.getVersions()[0]

        self.username = ""

        self.header = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\HexineLauncher.exe"
        self.content = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\content\\"
        self.tempPlace = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\content\\temp.rbxl"

    def getVersions(self):
        vers = []
        for ver in os.listdir(f"{self.appDataPath}\\Hexine\\Versions"):
            if ver.startswith("version"):
                vers.append(ver)
        return vers
        
    def setVersion(self, ver):
        self.version = ver
        self.header = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\HexineLauncher.exe"
        self.content = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\content\\"
        self.tempPlace = f"{self.appDataPath}\\Hexine\\Versions\\{self.version}\\content\\temp.rbxl"

    def setPort(self, port):
        self.defualtPort = port

    def setPlace(self, placePath):
        newPath = shutil.copy(placePath, self.tempPlace)

    def setUsername(self, username):
        self.username = username

    def play(self, ip, port):
        if self.version == None:
            return

        url = f'"http://hexine.tk/game/join.ashx?UserName={self.username}&server={ip}&serverPort={port}"'
        auth = '"http://hexine.tk/Login/Negotiate.ashx"'
        unknown = "0"
        print(subprocess.list2cmdline([self.header, "-play", url, auth, unknown]))
        subprocess.call([self.header, "-play", url, auth, unknown], shell=True)

    def host(self, rblx, placeName, port, public):
        if self.version == None:
            return

        placeType = 0
        if public == True: 
            placeType = 1
        else: 
            placeType = 0
        
        url = f'"http://hexine.tk/game/gameserver.ashx?placeId=0&serverPort={port}&publicPlace={placeType}&UserName={self.username}&placeName={placeName}&PS=0"'
        auth = '"http://hexine.tk/Login/Negotiate.ashx"'
        unknown = "0"
        print(subprocess.list2cmdline([self.header, "-play", url, auth, unknown]))
        subprocess.call([self.header, "-play", url, auth, unknown], shell=True)


