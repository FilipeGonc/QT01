from mysql.connector import cursor
from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def deletar(id):
    conexao,cursor = conectar()
    try: 
        sql = f"delete from tb_tarefas where id_tarefa ='{id}'"
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Deletado","Deletado com sucesso")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao deletar" + str(falha))
        return False
    finally:
        cursor.close
        conexao.close