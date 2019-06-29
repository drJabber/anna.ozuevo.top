#!/bin/sh

git push origin `git subtree split --prefix output 2> /dev/null` :gh-pages --force