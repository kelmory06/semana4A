#!/bin/bash
while true
do
	clear

	USER=$(curl http://127.0.0.1:5000/user)
	curl -H "Content-type: application/json" \
	-X POST http://projectredex.herokuapp.com/user/update -d "$USER"

	MEM=$(curl http://127.0.0.1:5000/mem)
	curl -H "Content-type: application/json" \
	-X POST http://projectredex.herokuapp.com/mem/update -d "$MEM"

	SWAP=$(curl http://127.0.0.1:5000/swap)
	curl -H "Content-type: application/json" \
	-X POST http://projectredex.herokuapp.com/swap/update -d "$SWAP"

	CPU=$(curl http://127.0.0.1:5000/cpu)
	curl -H "Content-type: application/json" \
	-X POST http://projectredex.herokuapp.com/cpu/update -d "$CPU"

	SO=$(curl http://127.0.0.1:5000/os)
	curl -H "Content-type: application/json" \
	-X POST http://projectredex.herokuapp.com/so/update -d "$SO"

	#DORMIR 5 SEGUNDOS
	sleep 5;
done
