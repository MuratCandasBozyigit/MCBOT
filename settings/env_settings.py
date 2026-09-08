import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


def _load_env_file(path):
	if not path.exists():
		return

	for line in path.read_text(encoding="utf-8").splitlines():
		line = line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue

		key, value = line.split("=", 1)
		os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


_load_env_file(ENV_FILE)


# Add a provider here when it needs fields beyond the generic API pair.
PLATFORM_REQUIRED_FIELDS = {
	"mexc": ("API_KEY", "API_SECRET"),
	"binance": ("API_KEY", "API_SECRET"),
	"xm": ("LOGIN", "PASSWORD", "SERVER"),
	"exness": ("LOGIN", "PASSWORD", "SERVER"),
}

ACTIVE_PLATFORM = os.getenv("ACTIVE_PLATFORM", "mexc").lower()


def get_platform_config(platform=ACTIVE_PLATFORM):
	prefix = platform.upper() + "_"
	return {
		key[len(prefix):]: value
		for key, value in os.environ.items()
		if key.startswith(prefix) and value
	}


def require_platform_config(platform=ACTIVE_PLATFORM):
	platform = platform.lower()
	config = get_platform_config(platform)
	required_fields = PLATFORM_REQUIRED_FIELDS.get(
		platform, ("API_KEY", "API_SECRET")
	)
	missing = [
		f"{platform.upper()}_{field}"
		for field in required_fields
		if not config.get(field)
	]

	if missing:
		raise RuntimeError(
			"Eksik platform ayarı: " + ", ".join(missing) + ". .env dosyasını doldurun."
		)

	return config
