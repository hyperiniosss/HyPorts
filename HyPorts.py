print('''  _    _       _____           _    _____ 
 | |  | |     |  __ \         | |  / ____|
 | |__| |_   _| |__) |__  _ __| |_| (___  
 |  __  | | | |  ___/ _ \| '__| __|\___ \ 
 | |  | | |_| | |  | (_) | |  | |_ ____) |
 |_|  |_|\__, |_|   \___/|_|   \__|_____/ 
          __/ |                           ''')




print('''    _________________,
 ___\_____________, /  _((
 `\__........... / ,.-' c`--,
     \_    .' .'/_/  ,------
       \_.'  .' __  /
         \__.' | |,===;   /|
            \_. \ \ \     ||
              \_ \ \ \___//
                `/  `----'
                 `''')




print(''' \ \      /   _)  |   _)                 _ )          |  |                      _)       _)            
  \ \ \  /  _| |   _|  |    \    _` |    _ \  |  |    __ |  |  |  _ \   -_)   _| |    \   |   _ \ (_-< 
   \_/\_/ _|  _| \__| _| _| _| \__, |   ___/ \_, |   _| _| \_, | .__/ \___| _|  _| _| _| _| \___/ ___/ 
                               ____/         ___/          ___/ _|                                     ''')

import socket

def port_tarama(hedef_ip, baslangic_portu, bitis_portu):
    for port in range(baslangic_portu, bitis_portu+1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(5)
        result = soket.connect_ex((hedef_ip, port))
        if result == 0:
            print(f"Port {port} açık.")
        soket.close()

hedef_ip = input("Hedef IP: ")
baslangic_portu = int(input("Başlangıç Portu: "))
bitis_portu = int(input("Bitiş Portu: "))

port_tarama(hedef_ip, baslangic_portu, bitis_portu)