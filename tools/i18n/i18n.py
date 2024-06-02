import json
import locale
import os

default_i18n_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "i18n/locale")


def load_language_list(language, locale_path=default_i18n_dir):
    with open(os.path.join(locale_path, f"{language}.json"), "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list

from src.common_config_manager import app_config

class I18nAuto:
    def __init__(self, language=None, locale_path=default_i18n_dir):
        if language in ["auto", None]:
            if app_config.locale in ["auto", None, ""]:
                language = locale.getdefaultlocale()[0]
            else:
                language = app_config.locale
        if not os.path.exists(os.path.join(locale_path, f"{language}.json")):
            language = "en_US"
        self.language = language
        self.language_map = load_language_list(language, locale_path)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
