#!/bin/sh

sudo docker build -t "thread" . && sudo docker run -d -p "0.0.0.0:1339:1337" --cap-add=SYS_PTRACE --security-opt seccomp=unconfined thread
