#!/bin/bash

set -e

echo "REPO: $GITHUB_REPOSITORY"
echo "ACTOR: $GITHUB_ACTOR"
echo "INSTALOADER: $INSTALOADER; $INSTALOADER_OPTS; data dir: $INSTAGRAM_DATA_DIR "

echo '=================== Install Requirements ==================='
pip install -r requirements.txt
echo '=================== Build site ==================='
${INSTALOADER} ${INSTAGRAM_PROFILE} ${INSTALOADER_OPTS} --dirname-pattern ${INSTAGRAM_DATA_DIR}
pelican ${PELICAN_INPUT_DIR} -o ${PELICAN_OUTPUT_DIR} -s ${PELICAN_CONFIG_FILE:=publishconf.py} ${PELICAN_OPTS}
echo '=================== Publish to GitHub Pages ==================='
cd output
# shellcheck disable=SC2012
remote_repo="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
remote_branch=${GH_PAGES_BRANCH:=gh-pages}
git init
git remote add deploy "$remote_repo"
git checkout $remote_branch || git checkout --orphan $remote_branch
git config user.name "${GITHUB_ACTOR}"
git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git add .
echo -n 'Files to Commit:' && ls -l | wc -l
timestamp=$(date +%s%3N)
git commit -m "[ci skip] Automated deployment to GitHub Pages on $timestamp"
git push deploy $remote_branch --force
rm -fr .git
cd ../
echo '=================== Done  ==================='