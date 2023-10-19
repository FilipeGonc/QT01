from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def cadastrar(desc,dataIni,dataFim,resp,tipo,obs):
    conexao, cursor = conectar()
    try:
        sql = f"insert into tb_tarefas(descricao,data_ini,data_fim,responsaveis,tipo,obs) VALUES ('{desc}','{dataIni}','{dataFim}','{resp}','{tipo}','{obs}')"
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao cadastrar" +str(falha))
        return False
    finally:
        cursor.close
        conexao.close

