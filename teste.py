from selenium import webdriver
import json
from bs4 import BeautifulSoup
import pandas as pd
import time

class queryState:
    def __init__ (self,uf):
        #1- USANDO O SELENIUM PARA FAZER O REQUEST
        self.uf=uf
        self.url='http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'    
        try:
            self.page = webdriver.Chrome('./chromedriver') #abre no linux
        except:
            self.page = webdriver.Chrome('./chromedriver.exe') #abre no windows
        self.page.get(self.url)

        #Iniciando algumas variáveis de controle
        self.loop=True
        self.control=0 
        self.columns_relaptions={'Localidade':'Localidade',
                            'Faixa de CEP':'Faixa de CEP',
                            'Situação':'Situação',
                            'Tipo de Faixa':'Tipo de Faixa'}

    def getData(self):    
        #2- BOTS REALIZANDO O ENVIO DO FORMULARIO
        self.page.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div/div/span[2]/label/select').send_keys(self.uf)
        self.page.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div/div/div[4]/input').click()

        #3- RECEBENDO O HTML
        self.element=self.page.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]")
        self.html=self.element.get_attribute('outerHTML')

        #4- A PRIMEIRA PÁGINA HTML COM AS TABELAS 0-49
        self.df_body=pd.read_html(str(self.html))[1]
    
        #5- AS PROXIMAS FAIXAS DAS TABELAS ATÉ O FIM.
        while self.loop:
            try:
                self.page.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a').click()
            
            except Exception as error: 
                self.loop=False
                time.sleep(1)
                self.page.quit()

            else:
                self.element=self.page.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]")
                self.html=self.element.get_attribute('outerHTML')
                self.df_prox=pd.read_html(str(self.html))[0]

            finally:
                if self.control == 0:
                    try:
                        self.df_full=pd.concat([self.df_body, self.df_prox.rename(columns=self.columns_relaptions)])
                    except:
                        self.df_full=self.df_body
                        self.control=self.control+1

                else:
                    self.df_full=pd.concat([self.df_full, self.df_prox.rename(columns=self.columns_relaptions)]) 

        #6- CRIANDO O CAMPO 'ID' E REALIZANDO A RASPAGEM DOS DADOS      
        self.df_full['Id']=[row for row in range(len(self.df_full))]
        self.df=self.df_full[['Id','Localidade','Faixa de CEP']]

    def getJson(self):  
        with open('./data/estado_'+self.uf+'.json', 'w') as stream:
            stream.write(self.df.to_json(orient='records', indent=4))
       
if __name__ == '__main__':
    uf='AC'
    obj=queryState(uf)
    obj.getData()
    obj.getJson()