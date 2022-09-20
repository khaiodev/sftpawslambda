#!/bin/bash
run_rsync() {
    sshpass -p 'valuePASS' rsync -avzr --progress -e "ssh -p 2200" "$1" "storagesftp@storage.com:/dir/ftp/home/htdocs/${1#/s3bucket-mount/}"
}
export -f run_rsync
parallel -j10 run_rsync ::: /s3bucket-mount/*
