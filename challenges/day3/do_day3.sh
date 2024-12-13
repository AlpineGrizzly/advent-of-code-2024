#!/bin/bash

function mul() { 
	echo $(($1 * $2))
}

grep -oP 'mul\([0-9]+,[0-9]+\)' input.txt | while read eq; do
	call_func="${eq//[(,)]/ }"
	value=$(eval $call_func)
	sum=$(($sum + $value))

	echo "Evaluated: $call_func = $value"

	echo "Running sum $sum"
done;


