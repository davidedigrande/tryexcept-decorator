python setup.py sdist
twine upload dist/*
rm -r tryexcept_decorator.egg-info
rm -r dist