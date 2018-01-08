
# Data Processing jupyter notebook
=========================================

    python, mongo engine, api rest autheticator, spark, etc...

## I tested it on Debian 8.

    docker-compose build && up

## Try out this view with the following curl command:

    http://34.239.113.110:8000/api/bairro-mongo/?format=json


curl -X POST http://34.239.113.110:8000/api/bairro-mongo/bulk_upload/ \
        -d "codigo,nome,municipio,uf,area
            355620110,Observatório,Valinhos,SP,68.0009
            3519071024,Rp 6-24,Hortolândia,SP,0.981768
            3536505002,Jardim De Itapoan,Paulínia,SP,0.808537" \
        -H "Content-type: text/csv" \
        -H "Accept: text/csv"


## Create a docker machine
➜  ~ docker-machine create --driver amazonec2 --amazonec2-region us-west-1 \
                           --amazonec2-zone a --amazonec2-vpc-id vpc-32c73756 \
                           --amazonec2-subnet-id subnet-16c84872 \
                           --amazonec2-ami ami-1b17257b \
                           --amazonec2-access-key $AWS_ACCESS_KEY_ID \
                           --amazonec2-secret-key $AWS_SECRET_ACCESS_KEY aws-swarm-manager


Running pre-create checks...
Creating machine...
(aws-swarm-manager) Launching instance...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with ubuntu(upstart)...
Installing Docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!

## To see how to connect your Docker Client to the Docker Engine running on this virtual machine, 

run: docker-machine env aws-swarm-manager

➜  ~ docker-machine ls
NAME                ACTIVE   DRIVER      STATE     URL                         SWARM   DOCKER    ERRORS
aws-swarm-manager   -        amazonec2   Running   tcp://54.183.145.111:2376           v17.10.0-ce
➜  ~


# Jupyter Notebook

[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/notebook.svg?branch=master)](https://travis-ci.org/jupyter/notebook)
[![Documentation Status](https://readthedocs.org/projects/jupyter-notebook/badge/?version=latest)](http://jupyter-notebook.readthedocs.io/en/latest/?badge=latest)
                

The Jupyter notebook is a web-based notebook environment for interactive
computing.

![Jupyter notebook example](docs/resources/running_code_med.png "Jupyter notebook example")

### Jupyter notebook, the language-agnostic evolution of IPython notebook
Jupyter notebook is a language-agnostic HTML notebook application for
Project Jupyter. In 2015, Jupyter notebook was released as a part of
The Big Split™ of the IPython codebase. IPython 3 was the last major monolithic
release containing both language-agnostic code, such as the *IPython notebook*,
and language specific code, such as the *IPython kernel for Python*. As
computing spans across many languages, Project Jupyter will continue to develop the
language-agnostic **Jupyter notebook** in this repo and with the help of the
community develop language specific kernels which are found in their own
discrete repos.
[[The Big Split™ announcement](https://blog.jupyter.org/the-big-split-9d7b88a031a7)]
[[Jupyter Ascending blog post](https://blog.jupyter.org/jupyter-ascending-1bf5b362d97e)]

## Installation
You can find the installation documentation for the
[Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html).
The documentation for advanced usage of Jupyter notebook can be found
[here](https://jupyter-notebook.readthedocs.io/en/latest/).

For a local installation, make sure you have
[pip installed](https://pip.readthedocs.io/en/stable/installing/) and run:

    $ pip install notebook

## Usage - Running Jupyter notebook

### Running in a local installation

Launch with:

    $ jupyter notebook

## Development Installation

See [`CONTRIBUTING.rst`](CONTRIBUTING.rst) for how to set up a local development installation.

## Contributing

If you are interested in contributing to the project, see [`CONTRIBUTING.rst`](CONTRIBUTING.rst).

## Resources
- [Project Jupyter website](https://jupyter.org)
- [Online Demo at try.jupyter.org](https://try.jupyter.org)
- [Documentation for Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/latest/) [[PDF](https://media.readthedocs.org/pdf/jupyter-notebook/latest/jupyter-notebook.pdf)]
- [Korean Version of Installation](https://github.com/ChungJooHo/Jupyter_Kor_doc/)
- [Documentation for Project Jupyter](https://jupyter.readthedocs.io/en/latest/index.html) [[PDF](https://media.readthedocs.org/pdf/jupyter/latest/jupyter.pdf)]
- [Issues](https://github.com/jupyter/notebook/issues)
- [Technical support - Jupyter Google Group](https://groups.google.com/forum/#!forum/jupyter)