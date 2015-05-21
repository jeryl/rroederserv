# rroederserv
blaze it

setup:

    virtualenv venv
    . venv/bin/activate
    easy_install "pyramid==1.5.7"
    python setup.py develop

run the service:

    . venv/bin/activate
    pserve development.ini

