# djanblo

Welcome to the djanblo! This is a simple blog engine writen in Python, using the Django Framework.

![djanblo blog](djanblo.png)
> Logo by [RoboHash](https://robohash.org/)

## Installation

Get the code:

    git clone https://github.com/paulohrpinheiro/djanblo /tmp/djanblo

Create a *virtualenv* using `virtualenvwrapper`:

    mkvirtualenv djanblo

or if using `pyvenv` only:

    python3 -m venv /tmp/djanblo-venv
    source /tmp/djanblo-venv/bin/activate

then install the dependencies:

    pip install -r requirements.txt

## Automated Tests

    cd /tmp/djanblo
    ./manage.py test

## Usage

To run in your machine:

    cd djanblo
    ./manage.py runserver

## License

This is a [MIT licensed](LICENSE) project.