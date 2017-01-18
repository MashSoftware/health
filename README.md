# Mash Health
[![Build Status](https://travis-ci.org/MashSoftware/health.svg?branch=master)](https://travis-ci.org/MashSoftware/health)
[![Requirements Status](https://requires.io/github/MashSoftware/health/requirements.svg?branch=master)](https://requires.io/github/MashSoftware/health/requirements/?branch=master)

## Getting Started
```
git clone git@github.com:MashSoftware/health.git
cd health
pip3 install -r requirements.txt
export SECRET_KEY=your_secret_key
export FLASK_APP=mash_health/__init__.py
export FLASK_DEBUG=1
```

## Testing
```
pip3 install -r requirements_test.txt
flake8 .
```

## Running
```
python3 -m flask run
```
