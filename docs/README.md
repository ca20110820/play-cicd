## Rules of Documentation
This repository is using Sphinx to automatically generate documentation fot `the_package` package.

## Initial Steps
The following procedure are the steps I used to generate the documentation:

1. Go to `docs/` and `sphinx-quickstart`
```bash
$ cd docs
$ sphinx-quickstart
```

2. Generate the Package .rst files
```bash
# Assume we are in docs/
$ sphinx-apidoc -o source ../the_package
```

3. (Optional) Edit or create new .rst files

4. Build
```bash
# Assume we are in docs/

# If you are using Windows:
$ make clean
$ make html

# If you are using Linux:
$ sphinx-build -E -v ./source ./build
```
