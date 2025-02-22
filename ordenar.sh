#!/bin/bash

for i in {1..50} ;do
	for a in {a..z} ;do
		touch script$i.$a
		echo "Se creo " script$i.$a
	done
done

