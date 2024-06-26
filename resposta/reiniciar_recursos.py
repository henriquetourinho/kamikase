#!/bin/bash

SERVICOS=("apache2" "mysql")

for SERVICO in "${SERVICOS[@]}"
do
    if ! systemctl is-active --quiet $SERVICO; then
        systemctl restart $SERVICO
        echo "Serviço $SERVICO reiniciado."
    fi
done

