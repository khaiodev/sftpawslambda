#!/bin/bash

#instalando pacotes
apt install s3fs sshfs parallel rclone sshpass unrar unzip rsync -y

#Criando os diretorios para montar
mkdir /gcoresftp-mount
mkdir /s3bucket-mount

#Montando S3
s3fs NOMEDOBUCKETS3 /s3bucket-mount -o passwd_file=~/.passwd-s3fs -o use_path_request_style -o umask=0002 -o allow_other

#Montando SFTP
sshfs -p2200 storage@storage.com:htdocs /gcoresftp-mount
