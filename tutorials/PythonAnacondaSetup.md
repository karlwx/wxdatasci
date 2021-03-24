# Anaconda Python Setup
How to install and use your anaconda python environment on your personal computer.  
Conda cheat sheet (useful commands): https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf

Anaconda is a leading data science and package management platform

### Installation and usage 
Download the and install the latest version of Anaconda here:  
https://www.anaconda.com/products/individual

Verify that the installation has worked correctly by typing ```conda``` in your terminal (on Windows, you'll need to open the anaconda prompt).

Anaconda comes with several python libraries, but does not include everything we need for weather data science. You can install new libraries with ```conda install```. For example, if I want to install metpy, I see from https://anaconda.org/conda-forge/metpy that I need to type ```conda install -c conda-forge metpy``` (the c flag specifies the channel to download from - in this case it's conda forge). This installs metpy in your base user environment.

Sometimes, new versions of libraries can cause conflicts with other libraries you have installed when an upgrade occurs. Thus, it's often useful to create separate environments for different projects you're working on; that way if an error occurs, it won't mess up your base environment (and prevent you from working on other projects). Referring to the conda cheat sheet, you can create a new environment by typing ```conda env create --name <envname> python=<version>```. This will make sure you have the latest version of python. To create the environment I use for the club's training materials, I ran ```conda env create --name wxdatasci python=3.9```.

For simplicity, I maintain an environment file that lists all of the libraries installed in my wxdatasci environment. This makes it easy to clone this environemnt and ensure all of the code will work on your computer. Simply cd into the wxdatasci directory and type ```conda env create --file environment.yml```.

To activate the conda environment, type ```conda activate <envname>```. The conda environment must be activated in order for python to find the librairies installed there. If you're running a JupyterLab server, make sure to activate the environment before launcing JupyterLab.