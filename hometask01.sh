#! /bin/bash
#Variables
py2='2.7.18'
py3='3.8.4'
#Install via python by pyenv
pyenv install $py2 && pyenv install $py3

#Clone virtualenv
git clone http://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

#Create python2env
pyenv virtualenv $py2 python2env

#Create python3env
pyenv virtualenv $py3 python3env
