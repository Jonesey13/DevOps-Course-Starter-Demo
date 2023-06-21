FROM python:3.11 as test

# INSTALL POETRY


ENTRYPOINT poetry run pytest