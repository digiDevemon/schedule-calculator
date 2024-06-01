

pushd $PSScriptRoot\..\..
    python -m pytest -v --cache-clear --durations=0
popd