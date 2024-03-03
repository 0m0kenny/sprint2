# Installation

Below are the steps to install the package on Linux OS.

## Download the source code

Download the git repo
```bash
$ git clone https://github.com/0m0kenny/sprint2
$ cd variant_annotation/
```

## Create a virtual environment and install dependencies

Create environment using conda
```bash
$ conda env create -f environment.yml
$ conda activate SPRINT2
```

Once the virtual environment is activated, install dependencies
```bash
$ pip install -r requirements.txt
```
## Install the Software
```bash
$ pip install .
```


For any other systems, or if you cannot install the databases, we recommend installing via [docker](https://github.com/0m0kenny/sprint2/blob/main/Dockerfile)

## Installing via Docker

Build Image
```bash
$ docker build .
```
Run docker
```bash
$ docker run -it <IMAGE> /bin/bash
```

Once container is running
```bash docker
root@container:/app#  cd variant_annotator/
root@containerID:/app/variant_annotator#  python __main__.py
```


Please refer to [Manual](https://github.com/0m0kenny/sprint2/blob/main/docs/MANUAL.md) for how to use and interact with the software.
