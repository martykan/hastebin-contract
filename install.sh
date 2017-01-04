#!/bin/bash
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root." 1>&2
else
    cp -r TransfershContract /usr/share/
    mv /usr/share/TransfershContract/transfersh.contract /usr/share/contractor/
    chmod 755 /usr/share/TransfershContract/transfersh.py
    chmod 644 /usr/share/contractor/transfersh.contract
fi

