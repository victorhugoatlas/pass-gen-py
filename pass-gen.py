import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

class PassGen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Senhas | Pass Gen | V 0.4")
        self.root.geometry("450x420")
        self.root.configure(bg="black")

        self.total_chars_var = tk.StringVar(value="10")
        self.include_symbols_var = tk.BooleanVar(value=False)
        self.current_password = ""
        self.filename_var = tk.StringVar(value="minha_senha.txt")
        self.username_var = tk.StringVar(value="")

        f = tk.Frame(self.root, bg="black")
        f.pack(pady=10)

        tk.Label(f, text="Quantidade de caracteres:", bg="black", fg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        ttk.Combobox(f, textvariable=self.total_chars_var, values=list(range(1, 31)), state="readonly", width=5).grid(row=0, column=1, sticky="w", padx=5, pady=2)

        tk.Checkbutton(f, text="Incluir Símbolos", variable=self.include_symbols_var, bg="black", fg="white", selectcolor="black", font=("Arial", 10)).grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        tk.Label(f, text="Usuário:", bg="black", fg="white", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=2)
        tk.Entry(f, textvariable=self.username_var, width=30).grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(f, text="Nome do arquivo:", bg="black", fg="white", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=5, pady=2)
        tk.Entry(f, textvariable=self.filename_var, width=30).grid(row=3, column=1, sticky="ew", padx=5, pady=2)

        self.output_display = tk.Text(self.root, height=5, width=35, bg="white", fg="black", font=("Arial", 10))
        self.output_display.pack(pady=10)

        tk.Button(self.root, text="Gerar Senha", command=self.gerar_senha_gui, bg="gray", fg="white", font=("Arial", 12, "bold"), width=15).pack(pady=5)
        tk.Button(self.root, text="Salvar Senha", command=self.salvar_senha, bg="darkgreen", fg="white", font=("Arial", 10), width=15).pack(pady=5)

        tk.Label(self.root, text="by Victor Hugo", bg="black", fg="gray", font=("Arial", 8)).pack(side="bottom", pady=5)

    def gerar_senha_gui(self):
        try:
            num_chars = int(self.total_chars_var.get())
            if num_chars <= 0:
                raise ValueError()

            chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            symbols = list('@#$Çç!?')
            pw_list = []

            if self.include_symbols_var.get():
                chars.extend(symbols)
                pw_list.append(random.choice(symbols))
                num_chars -= 1

            pw_list.extend(random.choices(chars, k=num_chars))
            random.shuffle(pw_list)
            self.current_password = ''.join(pw_list)

            self.output_display.delete(1.0, tk.END)
            self.output_display.insert(tk.END, f"Senha Gerada: {self.current_password}\n")
        except Exception as e:
            self.output_display.delete(1.0, tk.END)
            self.output_display.insert(tk.END, f"Por favor, insira um valor válido.")
            self.current_password = ""

    def salvar_senha(self):
        if not self.current_password:
            messagebox.showwarning("Aviso", "Nenhuma senha para salvar!")
            return

        fname = self.filename_var.get().strip()
        if not fname:
            messagebox.showwarning("Aviso", "Insira um nome para o arquivo.")
            return

        if not fname.lower().endswith(".txt"):
            fname += ".txt"

        path = os.path.join(os.path.expanduser("~"), "Desktop", fname)
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(f"Usuário: {self.username_var.get().strip() or 'N/A'}\nSenha: {self.current_password}\n" + "-" * 30 + "\n\n")
            messagebox.showinfo("Sucesso", f"Salvo em:\n{path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    def Iniciar(self):
        self.root.mainloop()

if __name__ == '__main__':
    PassGen().Iniciar()