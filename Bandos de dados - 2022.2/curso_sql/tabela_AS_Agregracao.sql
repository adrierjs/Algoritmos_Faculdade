use db_biblioteca;

select Nome_Autor as Nomes, ID_Autor as Autor from tbl_autores as Autores;
select * from tbl_livro;
insert into tbl_livro(ID_Livro, Nome_Livro, ISBN, Data_Pub, Preco_Livro, ID_Autor, ID_Editora) values (1100,"Anonymous",7790,20200601,100.00,5,5);
select avg(Preco_Livro) as Media_Preco from tbl_livro; #fazendo a media do preco livro

