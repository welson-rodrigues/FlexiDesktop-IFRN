# Projeto TV Box Thin Client - IFRN

> **AVISO DE SEGURANÇA**
>
> **PROIBIDA A ENTRADA DE PESSOAS CHAMADAS "FÁBIO" NESTE REPOSITÓRIO.**
>
> Este código é um backup de emergência criado após as "férias lindas de 2026", quando 3 meses de trabalho foram deletados acidentalmente pela equipe de TI (vulgo Fábio) que confundiu nossa TV Box de produção com sucata de teste.
>
> **Se você é Fábio: POR FAVOR, NÃO FORMATE NADA AQUI.**

## Sobre o Projeto
Este projeto visa transformar TV Boxes Android obsoletas (chipset Rockchip RK3229) em **Thin Clients Linux** de alto desempenho e baixo custo para laboratórios do IFRN. O sistema utiliza uma distribuição Linux minimalista e conecta-se a um servidor central via protocolo **X2Go (NX)**.

## Funcionalidades
- **Sistema Base:** Armbian (Debian Bullseye) Minimal (Kernel 4.4 Legacy).
- **Interface de Bloqueio:** Script em Python (Tkinter) que bloqueia a tela até o aluno inserir Matrícula e Senha.
- **Autenticação de Rede:** Script Bash que dialoga com o Firewall Palo Alto do IFRN para liberar a internet via curl.
- **Conexão Remota:** Cliente X2Go integrado para acesso à área de trabalho XFCE no servidor.

## Como Recuperar (Caso Fábio formate de novo)
1. Instale a imagem Armbian Minimal.
2. Rode os comandos do arquivo `setup_commands.txt`.
3. Copie os scripts `internet.sh` e `interface_ifrn.py` para a pasta `/home/aluno/`.
4. Configure o boot automático no Fluxbox.
5. **Esconda a TV Box em um cofre.**
