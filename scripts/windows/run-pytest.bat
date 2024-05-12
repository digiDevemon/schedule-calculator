set CURRENT_PATH=%0

pushd %CURRENT_PATH%\..\..
    pytest -v --cache-clear --durations=0
popd