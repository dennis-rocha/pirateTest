# pirateTest
Teste realizado para Neoway. Segue o link do teste: &lt;https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md>
<h1>Introdução</h1>
Para realizar teste com o código, ultilizar o modulo "main.py". 
O modulo "teste.py" carrega toda a função para pegar as faixas de CEP de cada UF. É possivél de
criar uma tela para apresentar para o usuário com o "teste.py" (sem a necessidade de usar linha
de comando para executar o código).
<h1>Instrução</h1>
1- Execute o comando para iniciar o código.

No windows:
	#Abrir a pasta através do CMD.
	cd pirateTest
	#executar o programa
	..pirateTest: python main.py
No linux(Ubuntu):
	#Abrir a pasta através do terminal.
	cd pirateTest
	#executar o programa
	~/pirateTest$ python3 main.py
	
2- Selecione uma das opções que aparecerá:

Caso seja a opção 1:
	O programa vai gerar um estado aleátorio.
	
Caso seja a opção 2:
	O programa vai pedir para que o usuário entre com um  valor inteiro para
	pesquisar em uma lista aleatória a quantidade que o usuário solicitar.
	Exemplo: Se o usuário digitar 10, o programa irá executar 10 vezes o comando
	para pegar as faixas de CEP sem repetir UFs.

Caso seja a opção 3:
	O usuário terá a liberdade de escolher qual estado será efetuado a pesquisa
	e em quantos estados será pesquisados.
	Exemplo: Usuário escolhe 'SC', em seguida o programa pede para que o usuário
	entre com o numero '1' para prosseguir ou apertar qualquer valor para sair. Obs,
	caso o usuário continue, o estado que ele escolheu, será retirado da lista até que se escerre
	o programa.
	
Caso seja a opção 4:
	Caso o usuário não queira mais fazer pesquisa, o programa possui a opção 4 para encerrar o programa.

Obs: O programa foi programado para que funcione tanto no windows quanto no Linux.
Caso tenha problema para acessar o site <http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm>
Limpar os cookies e cache do browser. Se persistir no mesmo erro "err_too_many_redirects" tente acessar em outro PC ou esperar um pouco,
repetir o processo de limpeza de cache e cookies e tentar acessar novamente.
