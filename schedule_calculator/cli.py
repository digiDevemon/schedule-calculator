import argparse
import os
import platform
from importlib.metadata import version

import yaml

from schedule_calculator.schedule_journal import ScheduleJournal
from schedule_calculator.time_assembler import TimeFormatter
from schedule_calculator.workday_calculator import WorkDayCalculator


def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version=version("schedule-calculator"))
    subparsers = parser.add_subparsers()

    _parse_calculate_command(subparsers)
    _parse_journal_command(subparsers)
    return parser


def _parse_calculate_command(parser):
    subparsers = parser.add_parser("calculate",
                                   help="Calculates a schedule") \
        .add_subparsers()

    __calculate_work_time_today_parser(subparsers)
    __calculate_worked_time_until_now_parser(subparsers)


def __calculate_work_time_today_parser(subparsers):
    worked_time_today_parser = subparsers.add_parser('worked-time-today',
                                                     help='It return a worked time of current day')
    worked_time_today_parser.add_argument('--config', type=str, required=False,
                                          help='Config file path')
    worked_time_today_parser.add_argument('--start-hour', '-start', type=str, required=True,
                                          help='Config file path')
    worked_time_today_parser.add_argument('--end-hour', '-end', type=str, required=True,
                                          help='Config file path')
    worked_time_today_parser.set_defaults(func=__calculate_worked_day)


def __calculate_worked_time_until_now_parser(subparsers):
    worked_time_until_now_parser = subparsers.add_parser('worked-time-until-now',
                                                         help='It return a worked time of current day')
    worked_time_until_now_parser.add_argument('--config', type=str, required=False,
                                              help='Config file path')
    worked_time_until_now_parser.add_argument('--start-hour', '-start', type=str, required=True,
                                              help='Config file path')
    worked_time_until_now_parser.set_defaults(func=__calculate_time_until_now)


def __calculate_worked_day(_args: argparse.Namespace):
    configuration = __load_configuration(_args.config)

    time_formatter = TimeFormatter()
    delta_schedule_standard = time_formatter.get_delta_from_str(configuration["schedule"]["standard"])
    delta_schedule_short = time_formatter.get_delta_from_str(configuration["schedule"]["short"])
    delta_launch = time_formatter.get_delta_from_str(configuration["schedule"]["launch"])
    short_day = configuration["schedule"]["short_day"]

    print(WorkDayCalculator(delta_schedule_standard, delta_schedule_short, delta_launch, short_day)
          .calculate_worked_time(_args.start_hour, _args.end_hour)[0])


def __calculate_time_until_now(_args: argparse.Namespace):
    configuration = __load_configuration(_args.config)

    time_formatter = TimeFormatter()
    delta_schedule_standard = time_formatter.get_delta_from_str(configuration["schedule"]["standard"])
    delta_schedule_short = time_formatter.get_delta_from_str(configuration["schedule"]["short"])
    delta_launch = time_formatter.get_delta_from_str(configuration["schedule"]["launch"])
    short_day = configuration["schedule"]["short_day"]

    worked_hours, expected_hours = (
        WorkDayCalculator(delta_schedule_standard, delta_schedule_short, delta_launch, short_day)

        .calculate_worked_time(_args.start_hour))

    print(f"You have worked {worked_hours}. Today you have to work {expected_hours}.")


def _parse_journal_command(parser):
    subparsers = parser.add_parser("journal",
                                   help="Time tracker") \
        .add_subparsers()

    __journal_init_parser(subparsers)


def __journal_init_parser(subparsers):
    worked_time_until_now_parser = subparsers.add_parser('init', help='It return a worked time of current day')
    worked_time_until_now_parser.add_argument('--config', type=str, required=False,
                                              help='Config file path')
    worked_time_until_now_parser.set_defaults(func=__init_journal)


def __init_journal(_args: argparse.Namespace):
    configuration = __load_configuration(_args.config)
    ScheduleJournal(configuration).init()


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
