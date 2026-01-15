#!/bin/bash
############################################################
#  Script de Autenticação Palo Alto (IFRN)  		   #
#  Autor: CTI do campus São Gonçalo do Amarante            #
#  Modificado para Automação (TCC TV Box)                  # 
############################################################

# Recebe usuário e senha vindos da interface Python
username=$1
password=$2

# Verifica se os dados chegaram
if [ -z "$username" ] || [ -z "$password" ]; then
    echo "Erro: Credenciais não fornecidas."
    exit 1
fi

echo "Tentando autenticar usuário $username no Firewall..."

# Requisição POST para o gateway do IFRN (Simula o login via navegador)
# A flag -k ignora erros de certificado SSL (comum na rede interna)
curl -k -d "escapeUser=$username&user=$username&passwd=$password&ok=Login" -X POST "https://autenticacao-cn.ifrn.local:6082/php/uid.php?vsys=1&rule=0"

# Verifica se liberou a internet pingando o Google
if ping -c 1 8.8.8.8 > /dev/null; then
    echo "SUCESSO: Internet Liberada! Fábio não conseguiu nos parar."
    exit 0
else
    echo "FALHA: Sem conexão. Verifique a senha ou o cabo de rede."
    exit 1
fi
