CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd "${CURRENT_PATH}"/../..
    python -m pip install --upgrade poetry
    poetry config virtualenvs.create false --local
    poetry lock
    poetry install
popd