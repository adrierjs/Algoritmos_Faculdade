drop table if exists AtividadesProjetos;
drop table if exists Projetos;
alter table if exists Funcionarios
   drop constraint FkDepto;
drop table if exists Departamentos;
drop table if exists Funcionarios;
drop table if exists Atividades;

Create Table Atividades (
   id Int Primary Key,
   descricao Varchar(30) Not Null
);

Create Table Funcionarios (
   id Int Primary Key,
   nome Varchar(30) Not Null,
   sexo Char(1) Not Null Check (Sexo IN ('F','M')),
   salario Numeric(8,2) Not Null,
   departamento_id Int
);

Create Table Departamentos (
   id Int Primary Key,
   descricao Varchar(30) Not Null,
   funcionario_gerente_id Int
);

Alter Table Funcionarios Add Constraint FkDepto Foreign Key (departamento_id)
   References departamentos (id) On Delete Set Null;

Alter Table Departamentos Add Constraint FkFuncionario Foreign Key (funcionario_gerente_id)
   References Funcionarios (id) On Delete Set Null;

Create Table Projetos (
   id Int Primary Key,
   descricao Varchar(30) Not Null,
   departamento_id Int References Departamentos (id) On Delete Set Null,
   funcionario_responsavel_id Int References Funcionarios (id) On Delete Set Null
);

Create Table AtividadesProjetos (
   projeto_id Int Not Null References Projetos (id),
   atividade_id Int Not Null References Atividades (id),
   data_inicio Date,
   data_fim Date,
   Constraint PkAtividadesProjetos Primary Key (projeto_id, atividade_id)
);

insert into departamentos
values (1,'Informatica',null);

insert into departamentos
values (2,'Materiais',null);

insert into departamentos
values (3,'Pessoal',null);

insert into Funcionarios
values (1,'Marsell','M',3000,1);

insert into Funcionarios
values (2,'Cleber','M',3500,1);

insert into Funcionarios
values (3,'Charles','M',2500,2);

insert into Funcionarios
values (4,'Paula','F',3000,3);

insert into Funcionarios
values (5,'Gutemberg','M',4000,2);

insert into Funcionarios
values (6,'Felipe','M',2000,3);

insert into Funcionarios
values (7,'Fernando','M',2500,3);

update departamentos
set funcionario_gerente_id = 1
where id = 1;

update departamentos
set funcionario_gerente_id = 5
where id = 2;

update departamentos
set funcionario_gerente_id = 4
where id = 3;

insert into Projetos
values (1,'Alfa',1,2);

insert into Projetos
values (2,'Beta',1,null);

insert into Projetos
values (3,'Gama',3,7);

insert into Atividades
values (1,'Projeto Arquitetural');

insert into Atividades
values (2,'Desenvolvimento de codigo');

insert into Atividades
values (3,'Testes de unidade');

insert into Atividades
values (4,'Testes de usabilidade');

insert into Atividades
values (5,'Contratacao de funcionarios');

insert into Atividades
values (6,'Compra de material');

insert into Atividades
values (7,'Implantacao do produto');

insert into Atividades
values (8,'Busca por recursos');

insert into AtividadesProjetos
values (1, 1, null, null);

insert into AtividadesProjetos
values (1, 2, null, null);

insert into AtividadesProjetos
values (1, 3, null, null);

insert into AtividadesProjetos
values (2, 1, null, null);

insert into AtividadesProjetos
values (2, 2, null, null);

insert into AtividadesProjetos
values (2, 3, null, null);

insert into AtividadesProjetos
values (2, 4, null, null);

insert into AtividadesProjetos
values (2, 7, null, null);

insert into AtividadesProjetos
values (3, 8, null, null);

insert into AtividadesProjetos
values (3, 5, null, null);