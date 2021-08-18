from IPython.display import Math
from IPython.display import Markdown
import tensorflow as tf
import torch
import numpy as np

def sm_md(inmat):
    md = ""
    md += "\\begin{bmatrix}"
    tmp_rows = list()
    mat = inmat
    # Pythonify the TensorFlow
    if isinstance(inmat,tf.Variable):
        mat = inmat.numpy().tolist()
    # Pythonify the Numpy and PyTorch
    if isinstance(inmat,(torch.Tensor,np.ndarray)):
        mat = inmat.tolist()
    for rr in range(len(mat)):
        tmp_rows.append(" & ".join([(f'{item:.2f}').rstrip('0').rstrip('.') for item in mat[rr]]))
    md += "\\\\".join(tmp_rows)
    md += "\\end{bmatrix}"
    return display(Markdown(md))
