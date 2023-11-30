#!/bin/bash
# take an url and get the size
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
