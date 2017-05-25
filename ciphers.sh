#!/bin/sh

export CIPHER=aes-256-cbc
alias enc_stream="gzip -f | openssl enc -${CIPHER} -a"
alias dec_stream="openssl enc -d -${CIPHER} -a | gunzip - "
