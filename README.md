# Schedule-calculator

This pet project is about calculating the amount of time that you have to work from the beginning of the day until the
end of your schedule.

The project is developed in TDD with micro-testing. In the tests we do not use mocks, and we follow Chicago system.
When is not possible to use Chicago system we use fakes instead.

## Workplace installation

- Install poetry first
- Execute: `poetry lock`
- Execute: `poetry install --sync`

## Workplace scripts commands

- Windows
  - To execute your tests: `.\scripts\windows\run-tests.ps1`
  - To execute check style: `.\scripts\windows\run-lint.ps1`

- Linux
  - To execute your tests: `.\scripts\linux\run-tests.sh`
  - To execute check style: `.\scripts\linux\run-lint.sh`

## CLI commands

- To initialize your schedule:  `python -m schedule_calculator journal init`
- To check the time:  `python -m schedule_calculator journal check`