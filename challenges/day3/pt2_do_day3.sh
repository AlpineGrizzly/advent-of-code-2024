#!/bin/bash
# Sorry but im dumb and this will be an overconvoluted solution using only grep lmao

function mul() { 
	echo $(($1 * $2))
}

# Disable monitor mode to use lastpipe to retain loop variables
set +m
shopt -s lastpipe

## Calculate all sums within a don't --> do boundary
sum_dont=0
sum=0

grep -oP "(?<=don't\(\))(.+?)(?=\s*do\(\))" input.txt | grep -oP 'mul\([0-9]+,[0-9]+\)' | while IFS= read eq; do
	call_func="${eq//[(,)]/ }"
	value=$(eval $call_func)
	sum_dont=$(($sum_dont + $value))
done;
echo "dont is sum $sum_dont"

## Calculate total summation
grep -oP 'mul\([0-9]+,[0-9]+\)' input.txt | while read eq; do
	call_func="${eq//[(,)]/ }"
	value=$(eval $call_func)
	sum=$(($sum + $value))
done;
echo "sum is sum $sum"

## Subtract don't boundary from all to get total
echo "Pt 2 sum is $(($sum-$sum_dont))"