FROM python:3.8

LABEL "com.github.actions.name"="Download instagram content and build Pelican static site action"
LABEL "com.github.actions.description"="Builds and deploys the Pelican project to GitHub Pages"

LABEL "Name"="Build pelican site"
LABEL "Version"="0.1.1"

ENV LC_ALL C.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]