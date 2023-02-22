---
title: Python Installation
author:
- Daniel Wesloh
keywords: [python, installation]
abstract: |
  Discussion of how to install python for use
...

# No Installation

## Jupyter Project

- <https://jupyter.org/try>
- In-browser notebook
- Hosted/run by the Jupyter project

## Google Colab

- <https://colab.research.google.com/>
- In-browser notebook
- Run by Google

# Minimal Installation

## Python.org

- <https://www.python.org/downloads/>
- Just python and standard library, no other packages

## Miniconda

- <https://docs.conda.io/en/latest/miniconda.html>
- Just python, standard library, and package manager, no other
  packages
- Follow conda instructions for installing more

## Mamba

- <https://github.com/conda-forge/miniforge#mambaforge>
- Package manager, no other packages
- Follow conda instructions for installing more packages, replacing
  `conda` with `mamba`

# Full Installation

## Anaconda

- <https://docs.anaconda.com/anaconda/install/index.html>
- Package manager, python, standard library, many other data-science
  packages

# Installing additional packages

## conda

```bash
conda install netCDF4
conda install -c conda-forge pint-xarray
```

- Recommended method: will install non-python dependencies if needed

## pip

```bash
pip install netCDF4
python -m pip install pint-xarray
```

- Has access to more packages, but will not install non-python
  dependencies
- may require compilers to install packages

# Creating Environments

## conda

At environment creation time:
```bash
conda create -n my-python numpy metpy cartopy netCDF4
```
when you want to use the environment (every time):
```bash
source activate -n my-python
```

- Useful if someone else installed conda without the packages you want

## venv

At environment creation time:
```bash
python -m venv /path/to/new/venv
source /path/to/new/venv/bin/activate
python -m pip install numpy metpy cartopy[plotting] netCDF4
```
when you want to use the environment (every time):
```bash
source /path/to/new/venv/bin/activate
```

- Useful if someone else installed python without the python packages
  you want

## pipenv

At environment creation time:
```bash
python -m pip install pipenv
cd /path/to/project/directory
pipenv install numpy metpy cartopy[plotting] netCDF4
```
when you want to use the environment (every time):
```bash
cd /path/to/project/directory
pipenv shell
```

- Has problems with compiled dependencies (NumPy, SciPy, netCDF4,
  Cartopy)

# Useful packages to install

## Read/Write files

- [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
  CSV, Excel
- [pygrib](https://jswhit.github.io/pygrib/api.html#example-usage)
  GriB2
- [cfgrib](https://pypi.org/project/cfgrib/) GriB2 (through XArray)
- [netCDF4](https://unidata.github.io/netcdf4-python/#tutorial)
  netCDF4, netCDF3
- [h5netcdf](https://h5netcdf.org/) netCDF4

## Handle Array Data

- [NumPy](https://numpy.org/learn/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
  tabular data
- [XArray](https://docs.xarray.dev/en/stable/tutorials-and-videos.html)
  multi-dimensional data, model output
- [SciTools-Iris](https://scitools-iris.readthedocs.io/en/stable/userguide/index.html)
  multi-dimensional data, model output

## Meteorological data, calculations and plots

- [MetPy](https://unidata.github.io/MetPy/latest/tutorials/index.html)
  Thermodynamic calculations
- [Siphon](https://unidata.github.io/siphon/latest/examples/index.html)
  Weather data download
- [cdsapi](https://github.com/ecmwf/cdsapi)
  ERA5 data download


## Units

- [cf_units](https://github.com/SciTools/cf-units)
- [pint](https://pint.readthedocs.io/en/stable/getting/tutorial.html)
- [pint-pandas](https://pypi.org/project/Pint-Pandas/) Units for tabular data
- [MetPy](https://unidata.github.io/MetPy/latest/tutorials/unit_tutorial.html#sphx-glr-tutorials-unit-tutorial-py)
  Units for multi-dimensional data

## Speeding things up

- [Numexpr](https://pypi.org/project/numexpr/) Take advantage of how
  memory work to speed up complex expressions
- [bottleneck](https://bottleneck.readthedocs.io/en/latest/reference.html)
  Faster rolling mean and mean with missing data
- [Cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)
  Compile frequently-used functions
- [Pythran](https://pythran.readthedocs.io/en/latest/MANUAL.html#first-steps)
  Compile frequently-used functions
- [Numba](https://numba.readthedocs.io/en/stable/user/5minguide.html)
  Compile frequently-used functions
  
## Statistics

- [SciPy](https://docs.scipy.org/doc/scipy/reference/stats.html)
  Descriptinve statistics, regression
- [Statsmodels](https://www.statsmodels.org/stable/gettingstarted.html)
  Regression, descriptive statistics
- [Scikit-Learn](https://scikit-learn.org/stable/getting_started.html)
  Machine learning
  
<!--
- [Pingouin](https://pingouin-stats.org/build/html/index.html#minutes-to-pingouin)
  Descriptive statistics, regression
- [bambi](https://bambinos.github.io/bambi/notebooks/getting_started.html#Quickstart)
  Regression
- [eofs](https://ajdawson.github.io/eofs/latest/userguide/index.html) EOF analysis
-->

## Plotting

- [matplotlib](https://matplotlib.org/stable/users/getting_started/)
  General plots
- [seaborn](https://seaborn.pydata.org/tutorial.html) Statistical
  plots for tabular data
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/getting_started/index.html)
  Maps
- [Basemap](https://matplotlib.org/basemap/users/mapsetup.html) Maps
- [MetPy](https://unidata.github.io/MetPy/latest/tutorials/upperair_soundings.html#sphx-glr-tutorials-upperair-soundings-py)
  Skew-T plots
- [XArray](https://tutorial.xarray.dev/fundamentals/04.1_basic_plotting.html)
  Plotting for multi-dimensional data
- [windrose](https://python-windrose.github.io/windrose/usage-output.html) Wind roses

## Testing

- [pytest](https://docs.pytest.org/en/7.2.x/getting-started.html) 
  Make sure that your code does what you want
- [hypothesis](https://hypothesis.readthedocs.io/en/latest/quickstart.html)
  Check corner cases: ensure code gives plausible output on possible
  input

## Check code correctness

- [black](https://black.readthedocs.io/en/stable/getting_started.html)
  Format your code consistently, flag syntax errors
- [flake8](https://flake8.pycqa.org/en/latest/index.html#using-flake8)
  Catch some mistakes before you run your code
- [pylint](https://pylint.pycqa.org/en/latest/tutorial.html)
  Catch some mistakes before you run your code
- [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html),
  [pyright](https://github.com/microsoft/pyright/blob/main/docs/getting-started.md),
  or [pyre](https://pyre-check.org/docs/types-in-python/)
  (somewhat experimental) check types in function calls
  
## Documentation

- [pdoc](https://pdoc.dev/docs/pdoc.html)
  Simple, quick documentation
- [Sphinx](https://www.sphinx-doc.org/en/master/tutorial/index.html)
  More complex, configurable documentation
- [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html)
  Guidelines for function documentation to be readable from console or
  online

## Packaging your functions for others

- [setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
  *De facto* standard tool for the purpose
- [meson-python](https://meson-python.readthedocs.io/en/stable/usage/start.html)
  New packager used by SciPy
- [poetry](https://python-poetry.org/docs/basic-usage/)
  New-ish packager; also sets up project skeleton
- [hatch](https://hatch.pypa.io/latest/intro/)
  New packager; also sets up project skeleton
- [PyScaffold](https://pyscaffold.org/en/stable/usage.html#quickstart)
  Sets up project skeleton
  
## Version Control

- [git](https://git-scm.com/book/en/v2)
  Maintain backups of your code
  
## Publishing your project

- [Open-source guide](https://opensource.guide/)
  Tips on how to maintain a successful open-source project
- [Choose a license](https://choosealicense.com/)
  Summary of different licenses and their characteristics
- [Zenodo](https://about.zenodo.org/)
  Store a fixed version of your code with a DOI
- [Python Package Index](https://pypi.org/)
  Store a fixed version of your code for `pip` to find
