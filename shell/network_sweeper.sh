#!/bin/bash

if [[ "$#" -ne 3 ]]
then
    echo "$0 network lo hi"
    exit 1
fi

sweep-net () {
    network=$1
    lo=$2
    hi=$3
    out=$4
    while [[ ${lo} -le ${hi} ]]; do
        ip="${network}.${lo}"
        if ping -c 1 -W 1 "$ip" &> /dev/null; then
            echo "Host $ip is up"
        else
            echo "Host $ip is down"
        fi
        lo=$((lo+1))
    done > $out
}

sweep-net $1 $2 $3 /tmp/alpha
read -rsp $'Unplug device and press any key to continue...\n' -n1 key
sweep-net $1 $2 $3 /tmp/omega
diff /tmp/alpha /tmp/omega
