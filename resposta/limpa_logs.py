#!/bin/bash

LOGS=("/var/log/syslog" "/var/log/auth.log")

for LOG in "${LOGS[@]}"
do
    > $LOG
    echo "Log $LOG limpo."
done

