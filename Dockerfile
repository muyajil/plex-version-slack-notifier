FROM python:3.9-rc-alpine

RUN pip3 install retry requests

COPY plex_version_monitor.py /plex_version_monitor.py

ENTRYPOINT [ "python3", "/plex_version_monitor.py" ]