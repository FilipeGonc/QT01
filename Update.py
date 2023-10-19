from mysql.connector import cursor
from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def update(id,desc,dataIni,dataFim,resp,tipo,obs):
    conexao,cursor = conectar()
    try:
        sql = f"update tb_tarefas set descricao='{desc}', data_ini='{dataIni}', data_fim='{dataFim}', responsaveis='{resp}', tipo='{tipo}',obs='{obs}' where id_tarefa ='{id}'"
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizado","Atualizado com sucesso")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha","Falha ao atualizar" +str(falha))
        return False
    finally:
        cursor.close
        conexao.close
        