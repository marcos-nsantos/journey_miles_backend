#!/bin/sh

make migrate

# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
    exit 1
fi

make run-server