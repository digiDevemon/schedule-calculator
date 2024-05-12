import argparse
import os
import platform

import yaml

from schedule_calculator.workday_calculator import WorkDayCalculator


def build_cli():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    __calculate_work_time_today_parser(subparsers)
    __calculate_worked_time_until_now_parser(subparsers)

    return parser


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


def __calculate_worked_day(_args):
    configuration = __load_configuration(_args.config)
    print(WorkDayCalculator(configuration)
          .calculate_worked_time(_args.start_hour, _args.end_hour)[0])


def __calculate_time_until_now(_args):
    configuration = __load_configuration(_args.config)
    worked_hours, expected_hours = (WorkDayCalculator(configuration)
                                    .calculate_worked_time(_args.start_hour))
    print(f"You have worked {worked_hours}. Today you have to work {expected_hours}.")


def __get_default_config_file_path():
    if platform.system() == "Windows":
        return f"{os.path.dirname(os.path.realpath(__file__))}\\configuration\\conf.yml"
    return f"{os.path.dirname(os.path.realpath(__file__))}/configuration/conf.yml"


def __load_configuration(config_path):
    if not config_path:
        config_path = __get_default_config_file_path()

    with open(config_path, 'r', encoding="utf-8") as file:
        configuration = yaml.safe_load(file)
    return configuration
