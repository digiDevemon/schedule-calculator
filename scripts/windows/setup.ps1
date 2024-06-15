
pushd $PSScriptRoot\..\..
    python -m pip install --upgrade poetry
    poetry config virtualenvs.create false --local
    poetry lock
    poetry install
popd