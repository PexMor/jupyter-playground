from IPython.display import Math
from IPython.display import Markdown
import tensorflow as tf
import torch
import numpy as np

def to_list(inmat):
    mat = inmat
    # Pythonify the TensorFlow
    if isinstance(inmat,tf.Variable):
        mat = inmat.numpy().tolist()
    # Pythonify the Numpy and PyTorch
    if isinstance(inmat,(torch.Tensor,np.ndarray)):
        mat = inmat.tolist()
    return mat

def sm_md(inmat):
    md = ""
    md += "\\begin{bmatrix}"
    tmp_rows = list()
    mat = to_list(inmat)
    for rr in range(len(mat)):
        tmp_rows.append(" & ".join([(f'{item:.2f}').rstrip('0').rstrip('.') for item in mat[rr]]))
    md += "\\\\".join(tmp_rows)
    md += "\\end{bmatrix}"
    return display(Markdown(md))

# from IPython.display import Latex

def sm(inmat,mname="A"):
    latex = ""
    latex += "\\renewcommand{\\vec}[1]{\\boldsymbol{#1}}\n"
    latex += "\\renewcommand{\\matrix}[1]{\\boldsymbol{\\mathrm{#1}}}\n"
    latex += "\\newcommand{\\tensor}[1]{\\boldsymbol{\mathrm{#1}}}\n"
    latex += "\\boldsymbol{\\mathrm{"+mname+"}}"
    latex += " = \\begin{bmatrix}"
    mat = to_list(inmat)
    tmp_rows = list()
    for rr in range(len(mat)):
        tmp_rows.append(" & ".join([(f'{item:.2f}').rstrip('0').rstrip('.') for item in mat[rr]]))
    latex += "\\\\".join(tmp_rows)
    latex += "\\end{bmatrix}"
    return display(Math(latex))

# call as sm([[1,2,3],[4,5,6]],mname="V")