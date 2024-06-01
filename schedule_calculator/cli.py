import argparse
import os
import platform
from importlib.metadata import version

import yaml

from schedule_calculator.schedule_journal import create_schedule_journal


def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=version("schedule-calculator"))
    subparsers = parser.add_subparsers()

    _parse_journal_command(subparsers)
    return parser


def _parse_journal_command(parser):
    subparsers = parser.add_parser("journal",
                                   help="Time tracker") \
        .add_subparsers()

    __journal_init_parser(subparsers)
    __journal_check_parser(subparsers)


def __journal_init_parser(subparsers):
    worked_time_until_now_parser = subparsers.add_parser('init', help='It return a worked time of current day')
    worked_time_until_now_parser.add_argument('--config', type=str, required=False,
                                              help='Config file path')
    worked_time_until_now_parser.set_defaults(func=__init_journal)


def __init_journal(_args: argparse.Namespace):
    configuration = __load_configuration(_args.config)
    schedule_journal = create_schedule_journal(configuration)
    schedule_journal.init()


def __journal_check_parser(subparsers):
    worked_time_until_now_parser = subparsers.add_parser('check', help='It return a worked time of current day')
    worked_time_until_now_parser.add_argument('--config', type=str, required=False,
                                              help='Config file path')
    worked_time_until_now_parser.set_defaults(func=__check_journal)


def __check_journal(_args: argparse.Namespace):
    configuration = __load_configuration(_args.config)
    schedule_journal = create_schedule_journal(configuration)
    schedule_journal.check()


def __get_default_config_file_path():
    if platform.system() == "Windows":
        return f"{os.path.dirname(os.path.realpath(__file__))}\\configuration\\conf.yml"
    return f"{os.path.dirname(os.path.realpath(__file__))}/configuration/conf.yml"


def __load_configuration(config_path: str) -> dict:
    if not config_path:
        config_path = __get_default_config_file_path()

    with open(config_path, 'r', encoding="utf-8") as file:
        configuration = yaml.safe_load(file)
    return configuration
