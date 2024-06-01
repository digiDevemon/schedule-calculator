
pushd $PSScriptRoot\..\..
    python -m pylint schedule_calculator --disable=C0114 --disable=C0115 --disable=C0116
    python -m mypy schedule_calculator
popd