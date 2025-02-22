#!/bin/bash

top -b -n 1 
echo "-----------------------------------------------------------------------------------------------------------------"
sleep 1

read -p "Ingrese el PID: " pid 

if ! ps -p "$pid" > /dev/null 2>&1; then
    echo "Error: No existe un proceso con PID $pid."
    exit 1
fi

echo "Total en K:"
sleep 1
pmap "$pid" | awk 'END {print $2}'

echo "Total en MB:"
sleep 1
pmap "$pid" | awk 'END {print $2 / 1024}'
