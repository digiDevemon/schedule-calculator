import sys

from schedule_calculator import cli

if __name__ == "__main__":
    worked_time_today_parser = cli.build_cli()
    if len(sys.argv) <= 1:
        worked_time_today_parser.print_usage()
        sys.exit()
    args = worked_time_today_parser.parse_args()
    args.func(args)
