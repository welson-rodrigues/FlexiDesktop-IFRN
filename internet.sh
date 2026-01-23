#!/bin/bash

username=$1
password=$2

if [ -z "$username" ] || [ -z "$password" ]; then
    echo "Erro: Credenciais vazias."
    exit 1
fi

# Curl silencioso (-s) ignorando SSL (-k)
curl -k -s -d "escapeUser=$username&user=$username&passwd=$password&ok=Login" -X POST "https://autenticacao-cn.ifrn.local:6082/php/uid.php?vsys=1&rule=0" > /dev/null

# Teste de conexão
if ping -c 1 8.8.8.8 > /dev/null; then
    exit 0 # Sucesso
else
    exit 1 # Falha
fi
