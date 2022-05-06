from enum import Enum

class AppMode(Enum):
    WEB = "WEB"
    LOCAL = "LOCAL"
    DEV = "DEV"

_resources = {
    AppMode.WEB: '/home/cappy/pla-multi-checker-web/',
    AppMode.LOCAL: './static/',
    AppMode.DEV: './static/'
}

_config = {
    AppMode.WEB: '/home/cappy/???/',
    AppMode.LOCAL: './',
    AppMode.DEV: './'
}

APP_MODE = AppMode.LOCAL
RESOURCE_PATH = _resources[APP_MODE]
CONFIG_PATH = _config[APP_MODE]