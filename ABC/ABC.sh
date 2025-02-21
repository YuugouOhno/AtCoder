#!/bin/bash
mkdir -p ABC$1 && cd ABC$1

if [ -n "$2" ]; then
    for ((i=0;i<${#2};i++)); do
        CHAR="${2:i:1}"
        touch "$CHAR.cpp"
        code "$CHAR.cpp"
    done
else
    touch A.cpp
    code A.cpp
fi





