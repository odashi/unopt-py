#!/bin/bash
set -eoux pipefail

python -m pytest src -vv
python -m black --check src
python -m flake8p src
python -m isort --check src
python -m mypy src
