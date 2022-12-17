use db_biblioteca;
select * from tbl_autores;
select ID_Autor, Nome_Autor, Sobrenome_Autor from tbl_autores where ID_Autor between 1 and 4;
select * from tbl_autores where Nome_Autor like 'D%' or Nome_Autor like 'A%';
select * from tbl_autores where Nome_Autor like '_d%' or Nome_Autor like '_D%';