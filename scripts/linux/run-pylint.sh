CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd "${CURRENT_PATH}"/../..
    python -m pylint schedule_calculator --disable=C0114 --disable=C0115 --disable=C0116
popd