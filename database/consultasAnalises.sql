/*
-- Selecionar o total de gols dos times ordenado pelo maior

select nome,
	   sum(gols) as gols
from(
	select t1.nome as nome,
		   sum(p.golsTime1) as gols
		from partidas p
			inner join times t1
				on t1.codigo = p.codigoTime1
		where p.golsTime1 is not null
		group by t1.nome
	union all
	select t2.nome as nome,
		   sum(p.golsTime2) as gols
		from partidas p
			inner join times t2
				on t2.codigo = p.codigoTime2
		where p.golsTime2 is not null
		group by t2.nome
		) aux
	group by nome
	order by gols desc

-- Selecionar a quantidade de vitórias e empates do time
select nome,
	   sum(vitorias) as vitorias,
	   sum(empates) as empates
from(
	select t.nome,
	       count(p.codigoTimeVitoria) vitorias,
		   0 as empates
	from partidas p
		inner join times t
			on t.codigo = p.codigoTimeVitoria
	where p.codigoCampeonato = 1
	group by t.nome
	union all
	select t1.nome as nome,
		   0 as vitorias,
		   count(p.codigo) as empates
		from partidas p
			inner join times t1
				on t1.codigo = p.codigoTime1
		where p.golsTime1 is not null
			  and p.flagEmpate = 1
			  and p.codigoCampeonato = 1
		group by t1.nome
	union all
	select t2.nome as nome,
		   0 as vitorias,
		   count(p.codigo) as empates
		from partidas p
			inner join times t2
				on t2.codigo = p.codigoTime2
		where p.golsTime2 is not null
			  and p.flagEmpate = 1
			  and p.codigoCampeonato = 1
		group by t2.nome
		) aux
	group by nome
	order by vitorias desc, empates desc
*/

select t.codigo, t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos
from pontuacao_grupos p inner join times t on t.codigo = p.codigoTime
where p.grupo = 'A'
order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos;

select t.codigo, t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos
from pontuacao_grupos p inner join times t on t.codigo = p.codigoTime
where p.grupo = 'B'
order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos;

select t.codigo, t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos
from pontuacao_grupos p inner join times t on t.codigo = p.codigoTime
where p.grupo = 'C'
order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos;

select t.codigo, t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos
from pontuacao_grupos p inner join times t on t.codigo = p.codigoTime
where p.grupo = 'D'
order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos;
	