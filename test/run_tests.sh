set -e

cd ..

flake8 . --max-line-length=119 --exclude=env

nosetests