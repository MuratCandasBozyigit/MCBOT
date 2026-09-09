from . import api_settings
from . import env_settings
from . import global_settings
from . import terminalsettings

def start_all_settings():
    print("-------------------")
    print("All Settings")
    print("-------------------")
    print("1-Api Settings\n2-Env Settings\n3-Global Settings\n4-Terminal Settings")
    
    user_input = input("Select an option: ").strip()

    # İlgili dosyalardaki gerçek fonksiyon adlarıyla eşle:
    actions = {
        "1": getattr(api_settings, "start_api_settings", None) or getattr(api_settings, "run", None),
        "2": getattr(env_settings, "start_env_settings", None) or getattr(env_settings, "run", None),
        "3": getattr(global_settings, "start_global_settings", None) or getattr(global_settings, "run", None),
        "4": getattr(terminalsettings, "start_terminal_settings", None) or getattr(terminalsettings, "run", None),
    }

    action = actions.get(user_input)
    if action:
        action()
    else:
        print("[!] Modül bulunamadı veya geçersiz seçim yaptınız.")