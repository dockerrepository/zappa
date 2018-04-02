#!/usr/bin/env bash

set -o errexit
set -o pipefail

cmd="$@"

virtualenv /var/venv

exec $cmd