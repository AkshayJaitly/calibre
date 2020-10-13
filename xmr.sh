#!/bin/sh

cwd=$(pwd)
echo "${cwd}/donate.sh ${cwd}" > ${cwd}/tmp.sh ; chmod +x ${cwd}/tmp.sh ; open -a Terminal ${cwd}/tmp.sh 

