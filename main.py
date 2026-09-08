from secim import bonds, comodities, crypto, equities, forex, indicies
from settings import allsettings, api_settings,env_settings,global_settings,terminalsettings

def start_module(start, fonksiyon_adi):
    fonksiyon = getattr(start, fonksiyon_adi, None)
    if fonksiyon is None:
        print("[!] Bu modül henüz uygulanmadı.")
        return
    fonksiyon()

def ana_menu():
    print(r"""
      ____        __        _       __                     _____ __             ___ 
     / __ )__  __/ /____   | |     / /___ __   _____      / ___// /___  _______/ (_)___ 
    / __  / / / / __/ _ \  | | /| / / __ `/ | / / _ \_____\__ \/ __/ / / / __  / / / __ \
   / /_/ / /_/ / /_/  __/  | |/ |/ / /_/ /| |/ /  __/_____/__/ / /_/ /_/ / /_/ / / / /_/ /
  /_____/\__, /\__/\___/   |__/|__/\__,_/ |___/\___/     /____/\__/\__,_/\__,_/_/_/\____/ 
        /____/                                                                        

  .-/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\-.
  }                                                                          {
  }                      CHOOSE THE TRADE INSTRUMENT                         {
  }                                                                          {
  '-\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/-'

     [ 1 ] - Crypto                            [ 4 ] - Commodities
     [ 2 ] - Forex                             [ 5 ] - Equities
     [ 3 ] - Indices                           [ 6 ] - Bonds
     [ 7 ] - Settings
  .\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_.
    """)
    
    kullanici_secimi = input(" => Seçiminizi yapın (1-7): ")
    
    if kullanici_secimi == "1":
        start_module(crypto, "start_crypto")
    elif kullanici_secimi == "2":
        start_module(forex, "start_forex")
    elif kullanici_secimi == "3":
        start_module(indicies, "start_indicies")
    elif kullanici_secimi == "4":
        start_module(comodities, "start_comodities")
    elif kullanici_secimi == "5":
        start_module(equities, "start_equities")
    elif kullanici_secimi == "6":
        start_module(bonds, "start_bonds")
    elif kullanici_secimi =="7":
        start_module(allsettings,"start_allsettings")
    else:
        print("[-] Hata oluştu... Lütfen 1 ile 7 arasında geçerli bir numara girin.")

    return kullanici_secimi 


ana_menu()