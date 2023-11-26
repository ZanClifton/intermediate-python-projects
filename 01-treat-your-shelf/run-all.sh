#!/bin/bash
for file in "./db"/*.sql; do
    psql -f "${file}" > ${file%.sql}.txt
done

# if this script does not run, use chmod +x run-all.sh to make it executable