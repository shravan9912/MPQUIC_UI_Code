#!/bin/sh
go version
export PATH=$PATH:/usr/local/go/bin
go version
go run stream_sender.go 192.168.0.102

