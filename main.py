import teste
import random

#2- GERAR OBJETO PARA CONECTAR COM O TESTE E OBTER O ARQUIVO JSON
def generator_files(uf): #Funcao para não repetir código a cada opção
    obj=teste.queryState(uf)
    obj.getData()
    obj.getJson()

#3- INICIANDO AS OPÇÕES
def option1(list_uf): #Funcao que recebe um estado aleatorio
    random.shuffle(list_uf)
    random.shuffle(list_uf)
    uf=list_uf.pop(0)
    print(f"Aguarde... Pegando dados do seguinte {uf}...")
    try:
        generator_files(uf)
    except Exception as error:
        print(f"\nErro inesperado!\nErro: {error}")
    else:
        print("Arquivo .JSON gerado com sucesso!")

def option2(list_uf): #Funcao que recebe uma quantidade de estados para pesquisar aleatoriamente
    control_option=True
    random.shuffle(list_uf)
    random.shuffle(list_uf)
    while control_option:
        try:
            number_states=int(input("""
 ___________________________________
|           MENU OPÇÃO2             |
+-----------------------------------+
| Digite uma quantidade de estados: |
+-----------------------------------+
|>"""))

        except Exception as error:
            print("Digite um numero inteiro valido")
        else:
            if number_states <=0 or number_states > len(list_uf):
                print(f"Selecione um valor valido de 1 a {len(list_uf)}")
            else:
                for gen_file in range(0,number_states):
                    print(f"Pegando dados do seguinte estado {list_uf[gen_file]}")
                    try:
                        generator_files(list_uf[gen_file])
                    except Exception as error:
                        print(f"Erro inesperado ou muitas tentativas\nErro: {error}")
                    else:
                        print(f"Dados do seguinte estado {list_uf[gen_file]} pego com sucesso!\n")
                print("Finalizado com sucesso!")
                control_option=False

def option3(list_uf): #Funcao que o usuario seleciona o estado e quantos estados quer
    uf_selected=[]
    control_option=True
    while control_option:
        print("""
 ___________________________________
|           MENU OPÇÃO3             |
+-----------------------------------+
| Selecione um dos estados abaixo:  |
+-----------------------------------+
""")
        for row in range(len(list_uf)):
            print(f"{row+1}-{list_uf[row]}")
        try:
            number_uf=int(input("Digite o UF desejado: "))
        except Exception as error:
            print ("Digite um valor inteiro valido!")
        else:
            if number_uf <= 0 or number_uf > len(list_uf):
                print (f"\nUF:{number_uf} não existe!\nSelecione um valor valido!\n")
            else:
                print (f"Você selecionou {number_uf}-{list_uf[number_uf-1]}")
                uf_selected.append(list_uf.pop(number_uf-1))
            
            try:
                option_exit=int(input("Digite qualquer tecla para sair ou digite '1' para continuar\n>"))
            except:
                control_option=False
            else:
                if option_exit != 1:
                    control_option=False

    try:
        for gen_file in range(0,len(uf_selected)):
            print(f"Pegando dados do seguinte estado {list_uf[gen_file]}")
            generator_files(list_uf[gen_file])
            print("Finalizado com sucesso!")
    except Exception as error:
        print(f"Erro inesperado:\nErro: {error}")

#1- MENU INICIAL
if __name__ == '__main__': #Iniciando aqui
    list_uf=['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PL','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
    menu_control = True
    while menu_control:
        print("""
 ___________________________________
|          MENU PRINCIPAL           |
+-----------------------------------+
|1- Selecione apenas 1 UF aleatório |
|2- Selecione 'x' UFs aleatórios    |
|3- Selecione o UF que desejar      |
+-----------------------------------+
|4- Finalizar programa              |
+-----------------------------------+
""")
        try:
            menu_option = int(input(">"))
        except Exception as error:
            print(f"Você digitou um valor invalido! Tente novamente!\nErro: {error}")
        else:
            if menu_option == 4:
                print("Obrigado por usar o programa!")
                menu_control=False
            if menu_option > 4 or menu_option <= 0:
                print("Você digitou um valor invalido! Tente novamente!")
            if menu_option == 1:
                option1(list_uf)
            if menu_option == 2:
                option2(list_uf)
            if menu_option == 3:
                option3(list_uf)