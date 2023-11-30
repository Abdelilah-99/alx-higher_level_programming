#!/bin/bash
# take an url and show all method tha server accepte
curl -sI "$1" | grep Allow | cut -d ":" -f 2
