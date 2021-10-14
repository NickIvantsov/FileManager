from configparser import ConfigParser

from app.util.constants import PATH_TO_LOCALE_FILE, LOCAL_FILE_NAME, LOCALE_FILE


class ConfigParserManager:

    def __init__(self):
        self._config_parser = ConfigParser()
        self._config_parser.read(PATH_TO_LOCALE_FILE)
        language = self._config_parser.get("LOCALE", LOCAL_FILE_NAME)
        self._section = language.upper()
        self._local_file = "{}.ini".format(language)
        path_to_file = LOCALE_FILE + self._local_file
        self._config_parser.read(path_to_file)
        pass

    @property
    def config_parser(self) -> ConfigParser:
        return self._config_parser

    @property
    def section(self) -> str:
        return self._section
