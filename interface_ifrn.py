import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time

# CONECTAR
def conectar():
    matricula = entry_matricula.get()
    senha = entry_senha.get()
    
    if matricula and senha:
        label_status.config(text="Autenticando...", fg="blue")
        root.update()
        
        # Chama o script de internet
        resultado = subprocess.run(
            ["/home/aluno/internet.sh", matricula, senha], 
            capture_output=True, text=True
        )
        
        if resultado.returncode == 0:
            label_status.config(text="Sucesso! Entrando...", fg="green")
            root.update()
            time.sleep(1)
            # Fecha a janela e retorna código 0 (Sucesso) para o bash
            root.destroy()
            sys.exit(0) 
        else:
            label_status.config(text="Erro de Login ou Rede.", fg="red")
            entry_senha.delete(0, tk.END)
    else:
        label_status.config(text="Preencha tudo.", fg="orange")

# DESLIGAR
def desligar():
    if messagebox.askyesno("Desligar", "Desligar a TV Box?"):
        subprocess.run(["sudo", "/sbin/poweroff"])

# Interface Gráfica
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="#f5f5f5")

# Cabeçalho
tk.Label(root, text="Login IFRN", font=("Arial", 40, "bold"), bg="#f5f5f5", fg="#333").pack(pady=(60, 20))
tk.Label(root, text="Autenticação de Rede", font=("Arial", 16), bg="#f5f5f5", fg="#666").pack(pady=(0, 40))

# Campos
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack()

tk.Label(frame, text="Matrícula:", font=("Arial", 14), bg="#f5f5f5").pack(anchor="w")
entry_matricula = tk.Entry(frame, font=("Arial", 20), width=20, bd=2, relief="groove")
entry_matricula.pack(pady=(0, 20))

tk.Label(frame, text="Senha:", font=("Arial", 14), bg="#f5f5f5").pack(anchor="w")
entry_senha = tk.Entry(frame, font=("Arial", 20), width=20, bd=2, relief="groove", show="*")
entry_senha.pack(pady=(0, 30))

# Botões
tk.Button(root, text="CONECTAR", font=("Arial", 18, "bold"), bg="#2E7D32", fg="white", 
          command=conectar, height=2, width=15).pack(pady=10)

label_status = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5")
label_status.pack(pady=20)

tk.Button(root, text="DESLIGAR", font=("Arial", 12, "bold"), bg="#d32f2f", fg="white", 
          command=desligar).place(relx=0.95, rely=0.95, anchor="se")

root.mainloop()

# Se fechar com Alt+F4, retorna erro
sys.exit(1)
