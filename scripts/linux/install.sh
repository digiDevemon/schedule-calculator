CURRENT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd "${CURRENT_PATH}"/../..
      python -m pip install poetry
      poetry lock
      poetry install
popd