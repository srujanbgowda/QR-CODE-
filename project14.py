
import qrcode 
from PIL import Image 

def generate_wifi_qr(ssid,password,security = 'WPA'):
    wifi_format = f"WIFI:T:{security}:S:{ssid}_;P:{password};;"
    qr= qrcode.make(wifi_format)
    qr.save(f"{ssid}_wifi_qr.png")
    qr.show()

generate_wifi_qr("Mywifi","mypassword143") 



