FROM python:3.10-slim

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY pythonfiles/* .

RUN pip install numpy

USER app_user

CMD ["bash"]