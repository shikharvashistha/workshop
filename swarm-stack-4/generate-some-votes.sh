#!/bin/sh

# create POST data files with ab friendly formats
sudo apt update -y && sudo apt install apache2-utils -y

python3 make-data.py

# create 3000 votes
ab -n 1000 -c 50 -p posta -T "application/x-www-form-urlencoded" http://localhost:5000/vote/
ab -n 1000 -c 50 -p postb -T "application/x-www-form-urlencoded" http://localhost:5000/vote/
ab -n 1000 -c 50 -p posta -T "application/x-www-form-urlencoded" http://localhost:5000/vote/
