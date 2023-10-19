CREATE DATABASE bd_av1;
USE bd_av1;

CREATE TABLE tb_tarefas(
	id_tarefa int not null auto_increment primary key,
    descricao varchar(100) not null,
    data_ini date not null,
    data_fim date not null,
    responsaveis varchar(255) not null,
    tipo varchar(5) not null,
    obs varchar(255) not null
);