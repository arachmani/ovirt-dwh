#!/bin/sh

. "$(dirname "$(readlink -f "$0")")"/dwh-prolog.sh
. "$(dirname "$(readlink -f "$0")")"/generate-pgpass.sh

usage() {
    cat << __EOF__
Usage $0:

    -a          - run analyze, update optimizer statistics
    -A          - run analyze only, only update optimizer stats, no vacuum
    -f          - do full vacuum. DWH service should not be running when doing full vacuum
    -t          - vacuum specific table
    -v          - verbose output

    -h --help   - this help message
__EOF__
}

MIXED_PARAMS_ERR="Can not mix -A and -f, use only one of them"

while getopts ":aAft:v" opt; do
    case $opt in
        a) ANALYZE=1
        ;;
        A) ANALYZE=
           ANALYZE_ONLY=1
            [[ -n $FULL ]] && die "$MIXED_PARAMS_ERR"
        ;;
        f) FULL=1
            [[ -n $ANALYZE_ONLY ]] && die "$MIXED_PARAMS_ERR"
        ;;
        t) TABLES="${TABLES} -t $OPTARG"
        ;;
        v) VERBOSE=1
        ;;
        \?) usage && exit
        ;;
        :) die "-$OPTARG requires an argument"
        ;;
    esac
done

if ! [ -z "$sclenv" ]; then
        . scl_source enable ${sclenv}
fi

# setups with 'trust' may have empty passwords
[[ -n $DWH_DB_PASSWORD ]] && generatePgPass

vacuumdb \
${ANALYZE+-z} \
${ANALYZE_ONLY+-Z} \
${FULL+-f} \
${VERBOSE+-v -e} \
${TABLES+$TABLES} \
-h $DWH_DB_HOST \
-p $DWH_DB_PORT \
-U $DWH_DB_USER \
-d $DWH_DB_DATABASE \
-w
