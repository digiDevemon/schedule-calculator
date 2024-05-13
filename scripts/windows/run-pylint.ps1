
pushd $PSScriptRoot\..\..
    pylint schedule_calculator --disable=C0114 --disable=C0115 --disable=C0116
popd