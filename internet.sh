#!/bin/bash

username=$1
password=$2

if [ -z "$username" ] || [ -z "$password" ]; then
    echo "Erro: Credenciais vazias."
    exit 1
fi

curl -k -s -d "escapeUser=$username&user=$username&passwd=$password&ok=Login" -X POST "https://autenticacao-cn.ifrn.local:6082/php/uid.php?vsys=1&rule=0" > /dev/null

if ping -c 1 8.8.8.8 > /dev/null; then
    exit 0 
else
    exit 1 
fi
