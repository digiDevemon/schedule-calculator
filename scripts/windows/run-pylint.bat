set CURRENT_PATH=%0

pushd %CURRENT_PATH%\..\..
    pylint schedule_calculator --disable=C0114 --disable=C0115 --disable=C0116

popd