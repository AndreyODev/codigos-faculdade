import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# Conectando ao banco
DB_CONFIG = {
    "host": "localhost",
    "database": "biblioteca_db",
    "user": "postgres", 
    "password": "@Sedutornato2" 
}

ADMIN_USER = "postgres"

def conectar():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao conectar no banco:\n{e}")

def carregar_view():
    """Carrega os dados da view vw_detalhada na Treeview."""

    for item in tree.get_children():
        tree.delete(item)

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT nome, titulo, data_emprestimo, data_devolucao, status FROM vw_detalhada")
        registros = cur.fetchall()
        conn.close()

        for linha in registros:
            tree.insert("", "end", values=linha)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar view:\n{e}")

def inserir_emprestimo():

    if DB_CONFIG["user"] != ADMIN_USER:
        return messagebox.showwarning("Acesso negado", "Apenas o administrador pode inserir.")

    usuario_id = entry_usuario.get()
    livro_id = entry_livro.get()
    status = entry_status.get()

    if not usuario_id or not livro_id or not status:
        return messagebox.showwarning("Aviso", "Preencha todos os campos!")

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO emprestimos (id_usuario, id_livro, status)
            VALUES (%s, %s, %s)
        """, (usuario_id, livro_id, status))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Empréstimo inserido!")
        carregar_view()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao inserir empréstimo:\n{e}")

def atualizar_emprestimo():

    if DB_CONFIG["user"] != ADMIN_USER:
        return messagebox.showwarning("Acesso negado", "Apenas o administrador pode atualizar.")

    selecionado = tree.focus()
    if not selecionado:
        return messagebox.showwarning("Aviso", "Selecione um registro!")

    valores = tree.item(selecionado, "values")
    nome_usuario = valores[0]
    titulo_livro = valores[1]

    novo_status = entry_status.get()
    if not novo_status:
        return messagebox.showwarning("Aviso", "Informe o novo status!")

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
          UPDATE emprestimos
          SET status = %s, data_devolucao = NOW()
          WHERE id_usuario = (SELECT id FROM usuarios WHERE nome = %s)
          AND id_livro = (SELECT id FROM livros WHERE titulo = %s)
        """, (novo_status, nome_usuario, titulo_livro))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Empréstimo atualizado!")
        carregar_view()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar:\n{e}")

def excluir_emprestimo():

    if DB_CONFIG["user"] != ADMIN_USER:
        return messagebox.showwarning("Acesso negado", "Apenas administrador pode excluir.")

    selecionado = tree.focus()
    if not selecionado:
        return messagebox.showwarning("Aviso", "Selecione algo para excluir!")

    valores = tree.item(selecionado, "values")
    nome_usuario = valores[0]
    titulo_livro = valores[1]

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
          DELETE FROM emprestimos
          WHERE id_usuario = (SELECT id FROM usuarios WHERE nome = %s)
          AND id_livro = (SELECT id FROM livros WHERE titulo = %s)
        """, (nome_usuario, titulo_livro))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Registro excluído!")
        carregar_view()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir:\n{e}")

# INTERFACE TKINTER
root = tk.Tk()
root.title("Sistema Biblioteca")
root.geometry("900x600")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="ID Usuário:").grid(row=0, column=0)
entry_usuario = tk.Entry(frame_inputs)
entry_usuario.grid(row=0, column=1)

tk.Label(frame_inputs, text="ID Livro:").grid(row=0, column=2)
entry_livro = tk.Entry(frame_inputs)
entry_livro.grid(row=0, column=3)

tk.Label(frame_inputs, text="Status:").grid(row=1, column=0)
entry_status = tk.Entry(frame_inputs)
entry_status.grid(row=1, column=1)

frame_btns = tk.Frame(root)
frame_btns.pack(pady=10)

tk.Button(frame_btns, text="Inserir", width=12, command=inserir_emprestimo).grid(row=0, column=0, padx=5)
tk.Button(frame_btns, text="Atualizar", width=12, command=atualizar_emprestimo).grid(row=0, column=1, padx=5)
tk.Button(frame_btns, text="Excluir", width=12, command=excluir_emprestimo).grid(row=0, column=2, padx=5)
tk.Button(frame_btns, text="Recarregar", width=12, command=carregar_view).grid(row=0, column=3, padx=5)

colunas = ["Usuário", "Livro", "Data Emp.", "Data Dev.", "Status"]
tree = ttk.Treeview(root, columns=colunas, show="headings", height=20)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True, pady=10)

carregar_view()
root.mainloop()
