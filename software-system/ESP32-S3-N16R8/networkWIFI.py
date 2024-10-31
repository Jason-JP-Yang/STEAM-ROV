import network
from time import sleep

class APmode():
    def __init__(self) -> None:
        self.ap = network.WLAN(network.AP_IF) ##创建热点对象

    def createAP(self, ESSID: str="ESP32"):
        """
        可以自定义热点名称ESSID 字符串形式 默认="ESP32"
        ESP32-S3内置Wi-Fi 4 802.11n
        """
        self.ap.config(essid=ESSID) ## 配置热点对象
        self.ap.active(True) ## 启动热点对象
        print(f"HotSpot has been started!\nHotSpot Name: {ESSID}")
    
    def disactivateAP(self):
        self.ap.active(False) ## 关闭热点对象
        print(f"HotSpot has been Deactivated!")

class WIFImode():
    def __init__(self) -> None:
        self.wlan = network.WLAN(network.STA_IF) ##创建WIFI对象
        self.wlan.active(True)

    def connectWIFI(self, SSID: str, PASSWARD: str):
        self.wlan.disconnect()
        print("Connecting the WIFI now: ", end="")
        self.wlan.connect(SSID, PASSWARD)
        connectIndex = 0
        while not self.wlan.isconnected() and connectIndex<40:
            print(".", end="")
            sleep(0.5)
            connectIndex += 1
        if self.wlan.isconnected(): print("\nWIFI CONNECTED!")
        else: print("\nERROR: Connecting WIFI out of time")

    def checkIPCONFIG(self):
        if self.wlan.isconnected():
            self.ip, self.subnet, self.gateway, self.dns = self.wlan.ifconfig()
            print("WIFI-IPCONFIG:")
            print(f"IP ADRESS: {self.ip}\nSubnet ADRESS: {self.subnet}")
            print(f"Gateway ADRESS: {self.gateway}\nDNS ADRESS: {self.dns}")
        else: print("ERROR: You have not connected to an available WIFI.")
