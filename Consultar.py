from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def consultar():
    conexao,cursor = conectar()
    try:
        sql = "select * from tb_tarefas"
        cursor.execute(sql)
        messagebox.showinfo("Consultado","Dados consultados")
        resultado = cursor.fetchall()
        return resultado
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao consultar" +str(falha))
        return None
    finally:
        cursor.close
        conexao.close