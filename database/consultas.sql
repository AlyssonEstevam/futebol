select * from times order by divisao;
select * from parametros;
select * from campeonatos;
select * from partidas where codigoCampeonato = 5 and flagFinalizada = 0;
select * from pontuacao;
select * from pontuacao_grupos;
select * from amistosos;

select len(nome)
	from times;

update partidas set flagFinalizada = 1;
update partidas set flagFinalizada = 0;
update partidas set flagFinalizada = 1 where codigo = 1;

update partidas set flagFinalizada = 'True';

EXEC sp_rename 'dbo.partidas.numeropartida', 'numeroPartida', 'COLUMN';

begin transaction

select * from partidas where codigo = 1;

update partidas set golsTime1 = '5', golsTime2 = '1', flagEmpate = 'False', codigoTimeVitoria = '1', codigoTimeDerrota = '2', flagFinalizada = 'True' where codigo = '1';

select * from partidas where codigo = 1;

rollback transaction

select * from times	
	order by quantidadeTitulo desc, quantidadeVitoria desc, quantidadeEmpate desc, 
	quantidadeDerrota, quantidadeGols desc;

/*
select top 1 * 
	from partidas 
	where codigoCampeonato = 1
		  and flagFinalizada = 0 
	order by codigo

begin transaction
select top 1 * 
	from partidas 
	where codigoCampeonato = 1
		  and flagFinalizada = 0 
	order by codigo;

update partidas
	set golsTime1 = 3, golsTime2 = 1, codigoTimeVitoria = 1, codigoTimeDerrota = 2, flagFinalizada = 1
	where codigo = 1;

select * from partidas where codigo = 1;

select top 1 * 
	from partidas 
	where codigoCampeonato = 1
		  and flagFinalizada = 0 
	order by codigo;

rollback transaction;
*/

select max(numeroPartida)
	from partidas
	where flagFinalizada = 0;