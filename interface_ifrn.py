import tkinter as tk
import subprocess
import os

# Funções do Sistema
def conectar():
    matricula = entry_matricula.get()
    senha = entry_senha.get()
    
    if matricula and senha:
        label_status.config(text="Autenticando no Palo Alto...", fg="blue")
        root.update()
        
        # Chama o script internet.sh passando os dados
        resultado = subprocess.run(
            ["/home/aluno/internet.sh", matricula, senha], 
            capture_output=True, 
            text=True
        )
        
        if resultado.returncode == 0:
            label_status.config(text="Sucesso! Iniciando X2Go...", fg="green")
            root.update()
            # Abre o cliente remoto e libera o sistema
            subprocess.Popen(["x2goclient"])
        else:
            label_status.config(text="Erro de Login. Tente novamente.", fg="red")
            
    else:
        label_status.config(text="Preencha todos os campos!", fg="red")

def desligar():
    # Desliga a TV Box com segurança
    os.system("poweroff")

# Interface Gráfica (Tkinter)
root = tk.Tk()
root.attributes('-fullscreen', True) # Modo Kiosk (Tela Cheia)
root.configure(bg="#f0f0f0") 

# Cabeçalho
label_titulo = tk.Label(root, text="IFRN - Laboratório Thin Client", font=("Arial", 30, "bold"), bg="#f0f0f0", fg="#2E7D32")
label_titulo.pack(pady=(80, 20))

label_subtitulo = tk.Label(root, text="Projeto de Acesso Remoto Linux", font=("Arial", 12), bg="#f0f0f0", fg="#555")
label_subtitulo.pack(pady=(0, 40))

# Formulário
frame_form = tk.Frame(root, bg="#f0f0f0")
frame_form.pack()

tk.Label(frame_form, text="Matrícula:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w")
entry_matricula = tk.Entry(frame_form, font=("Arial", 18), width=25)
entry_matricula.pack(pady=5)

tk.Label(frame_form, text="Senha:", font=("Arial", 14), bg="#f0f0f0").pack(anchor="w", pady=(10, 0))
entry_senha = tk.Entry(frame_form, font=("Arial", 18), width=25, show="*")
entry_senha.pack(pady=5)

# Botões
btn_conectar = tk.Button(root, text="CONECTAR", font=("Arial", 16, "bold"), bg="#2E7D32", fg="white", command=conectar)
btn_conectar.pack(pady=40, ipadx=40, ipady=10)

btn_desligar = tk.Button(root, text="Desligar TV Box", font=("Arial", 12), bg="#c62828", fg="white", command=desligar)
btn_desligar.pack(side="bottom", pady=30)

# Mensagens de Erro/Status
label_status = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_status.pack(pady=10)

root.mainloop()
