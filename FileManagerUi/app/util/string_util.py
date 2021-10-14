from configparser import ConfigParser


def get_str_res(config_parser: ConfigParser, section, res_id):
    return config_parser.get(section, res_id)