from dataclasses import dataclass

from settings.env_settings import (
	ACTIVE_PLATFORM,
	get_platform_config,
	require_platform_config,
)


ACTIVE_EXCHANGE = ACTIVE_PLATFORM


@dataclass(frozen=True)
class ExchangeCredentials:
	api_key: str
	api_secret: str


def get_exchange_credentials(exchange):
	config = get_platform_config(exchange)
	return ExchangeCredentials(
		api_key=config.get("API_KEY", ""),
		api_secret=config.get("API_SECRET", ""),
	)


def require_exchange_credentials(exchange=ACTIVE_EXCHANGE):
	config = require_platform_config(exchange)
	return ExchangeCredentials(
		api_key=config.get("API_KEY", ""),
		api_secret=config.get("API_SECRET", ""),
	)
