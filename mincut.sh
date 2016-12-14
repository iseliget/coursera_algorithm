#!/bin/bash

output=1000
for i in {1..600}
do
  #echo "Iteration $i"
  temp=$(python mingraph.py)
  if [ $temp -lt $output ]; then
  	output=$temp
  fi
done
echo $output
