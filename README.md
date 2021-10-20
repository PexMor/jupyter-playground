# Jupyter playground (Python)

A place to share some Pythonish things wrapped into Jupyter

* [AspectRatio.ipynb](AspectRatio.ipynb) - reverting the aspect ratio for local vector to maintain visual acuracy
* [BetterTabs.ipynb](BetterTabs.ipynb) - improve visual appearance of column data while adding lines on the fly
* [PyXel.ipynb](PyXel.ipynb) - working with MS Excel in Python
* [ExponentialNumpy.ipynb](ExponentialNumpy.ipynb) - mix of experiments later spinned off into [AspectRatio.ipynb](AspectRatio.ipynb), [sm_md.py](sm_md.py) also some javascript and watermark stuff

## Matrix as MathJax

* [MathJax](https://www.mathjax.org/) - a javascript lib to display math ([input](http://docs.mathjax.org/en/latest/options/input/index.html): LaTeX, MathML, AsciiMath)
* [sm_md.py](sm_md.py) - test matrix display function
* [MatrixMathJax.ipynb](MatrixMathJax.ipynb) - Better display of matrices

Please note that the formating functions like `IPython.display.Markdown` or `IPython.display.Latex` might not be available on all instances of Jupyter.
As an example the `sm_md` worked on **Jupyter Hub** local install, plain **Jupyter** in virtualenv, also on [https://colab.research.google.com](https://colab.research.google.com), todo test on [https://mybinder.org/](https://mybinder.org/) as well.

## Other sources

* [regression-in-pytorch.ipynb](regression-in-pytorch.ipynb) - Jon Krohn notebook with some tweaks showing converging lines
* [Jupyter GIT](https://github.com/jupyterlab/jupyterlab-git) - installable extension

[run-in-docker.sh](run-in-docker.sh) - quick start for dockerized **Jupyter**
