

pushd $PSScriptRoot\..\..
    pytest -v --cache-clear --durations=0
popd