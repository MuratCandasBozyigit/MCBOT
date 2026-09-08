from settings.env_settings import ACTIVE_PLATFORM, require_platform_config


def start_crypto():
    print(f"[+] Crypto modülü yükleniyor: {ACTIVE_PLATFORM.upper()}")
    try:
        require_platform_config()
    except RuntimeError as error:
        print(f"[!] {error}")
        return

    print("[+] API kimlik bilgileri hazır.")