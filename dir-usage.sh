#!/usr/bin/env bash

function usage {
    echo
    echo "$0 </path/to/initial/dir> [<No of entries>]"
    echo
    echo "$0 uses du to summarize a given file tree disk usage and graphs percentages to cli."
    echo "No. of entries is optional, it displays the top N directories"
    echo "e.g $0 /home/retux 20"
    exit 0

}

function is_integer {
    if [[ ! $1 == ?(-)+([0-9]) ]]
    then
        echo "[error] ${1} is not an integer. See what you're doin' fella."
        exit 1
    fi
}

function main {
    if [[ -z ${1} ]]
        then
            usage
    fi
    if [[ -z ${2} ]]
	then
	    NENTRIES=20
	else
	    NENTRIES=${2}
            is_integer "${2}"
            NENTRIES=$((NENTRIES+2))
    fi
    du -kcad 1 "${1}" | sort -nr | head -n ${NENTRIES} | ./du-graph.py
}


main "$@"
