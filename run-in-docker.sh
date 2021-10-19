#!/bin/bash

# IMG=jupyter/minimal-notebook
IMG=jupyter/base-notebook

docker run -it --rm \
    -p 8888:8888 \
    -v $(pwd):/home/jovyan/work \
    jupyter/minimal-notebook
