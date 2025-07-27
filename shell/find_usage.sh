#!/bin/bash

# set -Eeuo pipefail

find . -type f -ls | awk '{print $7}' | paste -sd+ - | bc
