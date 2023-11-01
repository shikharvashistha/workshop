#!/bin/bash

docker build -t stream1new .

docker run --rm --name stream1new --cpuset-cpus 1 -m 2048m stream1new
