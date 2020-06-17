#!/bin/bash

set -e

echo "REPO: $GITHUB_REPOSITORY"
echo "ACTOR: $GITHUB_ACTOR"
echo "INSTALOADER: $INPUT_INSTALOADER; $INPUT_INSTALOADER_OPTS; data dir: $INPUT_INSTAGRAM_DATA_DIR "

echo '=================== Install Requirements ==================='
pip install -r requirements.txt
echo '=================== Build site ==================='
${INPUT_INSTALOADER} ${INPUT_INSTAGRAM_PROFILE} ${INPUT_INSTALOADER_OPTS} --dirname-pattern ${INPUT_INSTAGRAM_DATA_DIR}
pelican ${INPUT_PELICAN_INPUT_DIR} -o ${INPUT_PELICAN_OUTPUT_DIR} -s ${INPUT_PELICAN_CONFIG_FILE:=publishconf.py} ${INPUT_PELICAN_OPTS}
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