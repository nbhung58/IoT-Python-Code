#!/bin/bash

while [ : ]
do
	sleep 2 
	git add .
	sleep 5
	git commit -m 'update'
	sleep 5
	git push
	sleep 13m
done

