#!/bin/bash

if [[ -z "${REPO_URL_PREFIX}" ]]; then REPO_URL_PREFIX="git@github.com:ipshruti"; fi
if [[ -z "${REPO_NAME}" ]]; then REPO_NAME="viewing_product"; fi
if [[ -z "${S3_UPLOAD_PATH}" ]]; then S3_UPLOAD_PATH="s3://data_product_artefact/viewing_product/"; fi
if [[ -z "${RUN_TEST_COMMAND}" ]]; then RUN_TEST_COMMAND="python -m unittest discover test/"; fi


log () {
  echo "====================================="
  echo "$1"
  echo "====================================="
}

clone_repo () {
  REPO_URL=$REPO_URL_PREFIX/"$REPO_NAME".git
  log "Cloning repository: $REPO_URL"
  git clone $REPO_URL
  pushd "$REPO_NAME" || exit
}

run_python_tests () {
  log "Install requirements if it exists"
  pip install -r requirements.txt || true
  log "Running Python Tests"
  $RUN_TEST_COMMAND
}

zip_and_upload_to_s3 () {
  log "Zipping the repository"
  pushd ../
  zip -r "$REPO_NAME".zip "$REPO_NAME"/
  log "Copying repository files to s3"
  aws s3 cp "$REPO_NAME".zip "$S3_UPLOAD_PATH"
}

clone_repo
run_python_tests
zip_and_upload_to_s3
log "Done!"
