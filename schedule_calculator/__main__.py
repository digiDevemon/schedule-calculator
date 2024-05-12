from schedule_calculator import cli

if __name__ == "__main__":
    args_worked_time_today_parser = cli.build_cli().parse_args()
    args_worked_time_today_parser.func(args_worked_time_today_parser)
