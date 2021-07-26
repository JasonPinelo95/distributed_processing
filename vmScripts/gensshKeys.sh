#!/bin/bash

# This bash script automate the generation of ssh keypairs
# You should pass the name of the user you want as the first argument

USERNAME=$1

ssh-keygen -P "" -t rsa -f ~/.ssh/$USERNAME -C "$USERNAME"
