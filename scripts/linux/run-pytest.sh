CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd "${CURRENT_PATH}"/../..
    pytest -v --cache-clear --durations=0
popd