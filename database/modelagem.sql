create table times(
	codigo int identity(1,1) primary key,
	nome varchar(13) not null,
	divisao int,
	quantidadeTitulo int constraint DF_times_quantidadeTitulo default 0,
	quantidadeVitoria int constraint DF_times_quantidadeVitoria default 0,
	quantidadeDerrota int constraint DF_times_quantidadeDerrota default 0,
	quantidadeEmpate int constraint DF_times_quantidadeEmpate default 0,
	quantidadeGols int constraint DF_times_quantidadeGols default 0
);

create table campeonatos(
	codigo int identity(1,1) primary key,
	nome varchar(50) not null,
	divisao int not null,
	ano int not null,
	trimestre int not null,
	formato varchar(20) not null,
	codigoVencedor int,
	constraint FK_campeonatos_times_vencedor foreign key (codigoVencedor)
	references times(codigo)
);

create table parametros(
	codigo int identity(1,1) primary key,
	ano int,
	trimestre int,
	divisao int,
	codigoCampeonatoAtual int,
	rodadaAtual int,
	partidaAtual int,
	constraint FK_parametros_campeonatos foreign key (codigoCampeonatoAtual)
	references campeonatos(codigo),
);

create table partidas(
	codigo int identity(1,1) primary key,
	codigoCampeonato int not null,
	numeroRodada int not null,
	numeroPartida int not null,
	codigoTime1 int not null,
	golsTime1 int,
	codigoTime2 int not null,
	golsTime2 int,
	flagEmpate bit not null constraint DF_partidas_flagEmpate default 0,
	codigoTimeVitoria int,
	codigoTimeDerrota int,
	flagPenalti bit not null constraint DF_partidas_flagPenalti default 0,
	penaltisTime1 int,
	penaltisTime2 int,
	flagFinalizada bit not null constraint DF_partidas_flagFinalizada default 0,
	constraint FK_partidas_campeonatos foreign key (codigoCampeonato)
	references campeonatos(codigo),
	constraint FK_partidas_times_1 foreign key (codigoTime1)
	references times(codigo),
	constraint FK_partidas_times_2 foreign key (codigoTime2)
	references times(codigo),
	constraint FK_partidas_times_vitoria foreign key (codigoTimeVitoria)
	references times(codigo),
	constraint FK_partidas_times_derrota foreign key (codigoTimeDerrota)
	references times(codigo)
);

create table amistosos(
	codigo int identity(1,1) primary key,
	codigoTime1 int not null,
	golsTime1 int,
	codigoTime2 int not null,
	golsTime2 int,
	constraint FK_amistosos_times_1 foreign key (codigoTime1)
	references times(codigo),
	constraint FK_amistosos_times_2 foreign key (codigoTime2)
	references times(codigo)
);

create table pontuacao(
	codigo int identity(1,1) primary key,
	codigoTime int not null,
	pontos int not null constraint DF_pontuacao_pontos default 0,
	partidas int not null constraint DF_pontuacao_partidas default 0,
	vitorias int not null constraint DF_pontuacao_vitorias default 0,
	empates int not null constraint DF_pontuacao_empates default 0,
	derrotas int not null constraint DF_pontuacao_derrotas default 0,
	golsMarcados int not null constraint DF_pontuacao_golsMarcados default 0,
	golsSofridos int not null constraint DF_pontuacao_golsSofridos default 0,
	saldoGols int not null constraint DF_pontuacao_saldoGols default 0,
	constraint FK_pontuacao_times foreign key (codigoTime)
	references times(codigo)
);

create table pontuacao_grupos(
	codigo int identity(1,1) primary key,
	codigoTime int not null,
	grupo varchar(1) not null,
	pontos int not null constraint DF_pontuacao_grupos_pontos default 0,
	partidas int not null constraint DF_pontuacao_grupos_partidas default 0,
	vitorias int not null constraint DF_pontuacao_grupos_vitorias default 0,
	empates int not null constraint DF_pontuacao_grupos_empates default 0,
	derrotas int not null constraint DF_pontuacao_grupos_derrotas default 0,
	golsMarcados int not null constraint DF_pontuacao_grupos_golsMarcados default 0,
	golsSofridos int not null constraint DF_pontuacao_grupos_golsSofridos default 0,
	saldoGols int not null constraint DF_pontuacao_grupos_saldoGols default 0,
	constraint FK_pontuacao_grupos_times foreign key (codigoTime)
	references times(codigo)
);

-- Define os par�metros iniciais
insert into [dbo].[parametros] ([ano],[trimestre],[divisao])
	--values('1','4','1');
	values('1','1','1');

-- Define os 32 times
insert into [dbo].[times] ([nome],[divisao])
	values ('Fireball','1'),
		   ('Confidence','2'),
		   ('Fenix','1'),
		   ('CSA','1'),
		   ('Englands','1'),
		   ('Indiana','1'),
		   ('Mars','1'),
		   ('Loopers','2'),
		   ('Pallet','1'),
		   ('Boomers','2'),
		   ('Xiscake','1'),
		   ('Simosono','1'),
		   ('Gaveland','2'),
		   ('Barracuda','1'),
		   ('Riptide','2'),
		   ('Azul','1'),
		   ('Poopers','2'),
		   ('Dynamo','2'),
		   ('Exmachina','2'),
		   ('Jasperito','1'),
		   ('Histocrata','2'),
		   ('Deviante','2'),
		   ('Jagerhead','2'),
		   ('Limeira','2'),
		   ('Inter','1'),
		   ('Mississipi','2'),
		   ('Olinda','2'),
		   ('Tomater','1'),
		   ('Dinoco','2'),
		   ('Revaneio','1'),
		   ('Triceract','1'),
		   ('Starse','2');

/*
-- Drop das tabelas para Reset
drop table pontuacao_grupos;
drop table pontuacao;
drop table amistosos;
drop table partidas;
drop table parametros;
drop table campeonatos;
drop table times;

-- Define o primeiro campeonato
insert into [dbo].[campeonatos] ([nome],[ano],[trimestre],[formato])
     values ('Campeonato Pontual - 1º Trimestre','1','1','Ponto Corrido');
GO

-- Teste de INSERT de uma partida
insert into [dbo].[partidas] ([codigoCampeonato],[numeroRodada],[numeroPartida],[codigoTime1],[codigoTime2])
	values('1','1','1','1','2');

*/