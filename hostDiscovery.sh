#!/bin/bash

for i in $(seq 1 254);do
    timeout 1 bash -c"ping -c 1 10.10.10.$i > /dev/null 2>&i" && echo "host 10.10.10.$i -ACTIVE" &
done; wait