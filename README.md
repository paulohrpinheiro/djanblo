# djanblo

Welcome to the djanblo! This is a simple blog engine writen in Python, using the Django Framework.

![djanblo blog](djanblo.png)
> Logo by [RoboHash](https://robohash.org/)

## Spec

Develop a blog system using Python and Django.

- [x] The system must have a home page that shows the posts, from the most recent to the oldest, paginated, 10 posts per page.
- [ ] There must be a login system so that administrators can register new posts.
- [x] Should use the bootstrap framework for page layout.
- [ ] There must be an API where the database posts can be obtained through GET.
- [x] The code must be published in github, in a public account.

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

## Usage

To run in your machine:

    cd djanblo
    ./manage.py runserver

## Automated Tests and Converage Report

    cd /tmp/djanblo
    pip install -r requirements.txt
    ./manage.py test

## License

This is a [MIT licensed](LICENSE) project.