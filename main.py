#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import pathlib 
import sys
import os
import logging
import seaborn as sns


# In[2]:


#Imposto directory di output, dove verranno salvati i risultati delle analisi
dir = str(pathlib.Path().parent.absolute())
dir_out = "{}/materiale/results/".format(dir)


# In[3]:


#controllo esistenza directory
def esistenza_directory(dir):
    if os.path.isdir(dir) == False:
        logging.warning("Directory di output: {}  non esistente".format(dir))
        try: 
            #Se non esiste la creo
            os.makedirs(dir)
            logging.info("Creazione directory: {} ".format(dir))
            
        except OSError as error:
            logging.error("Errore durante la creazione della directory: {}".format(dir))
    
    else:
        logging.info("Directory di output: {} esistente".format(dir))


# In[4]:


#Istanzio il logger
logging.basicConfig(handlers=[logging.FileHandler(filename='filelog.log', encoding='utf-8', mode='a+')],format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logging.info("RUN docker with parameter: {} ".format(sys.argv[1] if len(sys.argv)>1 else 'NULL' ))


#Controllo esistenza directory di output
esistenza_directory(dir_out)

#Scarico il Dataframe dal percorso remoto
percorso_remoto = 'https://github.com/MrTeoTZR/Cloud-project-Fifa/raw/master/FIFA2021.csv'
try:
    df = pd.read_csv(percorso_remoto, sep = ';')
    logger.info("Lettura dataset")
except Exception as e:
    logger.error("Non è stato è stato possibile leggere il file all'indirizzo: {}".format(percorso_remoto))


# In[5]:


#Funzioni richiamabili per l'Analisi del dataset
def giocatori_nazione(): 
    plt.figure(figsize = (20,7))
    df['nationality'].value_counts().head(10).plot.bar(color = sns.color_palette('viridis'))
    plt.title('Giocatori per nazione in FIFA')
    plt.xlabel('Nazionalità')
    plt.ylabel('Conteggio')
    filename = "{}.png".format('Giocatori per nazione in FIFA-2021')
    plt.savefig(dir_out+filename,bbox_inches='tight',dpi=500,transparent=True)
           
def numero_giocatori():
    age  = df.age
    plt.figure(figsize = (12,8))
    ax = sns.displot(age,bins = 60, kde = True, color = 'green')
    ax.set_axis_labels('Età','Numero di giocatori')
    ax.set_titles('Età dei giocatori in FIFA')
    filename = "{}.png".format('Età dei giocatori in FIFA')
    plt.savefig(dir_out+filename,bbox_inches='tight',dpi=500,transparent=True)
    
def squadre_popolari():
    plt.figure(figsize = (20,7))
    df['team'].value_counts().head(20).plot.bar(color = sns.color_palette('viridis'))
    plt.title('Squadre di club più popolari in FIFA')
    plt.xlabel('Nomi squadre')
    plt.ylabel('Numero giocatori')
    filename = "{}.png".format('Squadre di club più popolari in FIFA-2021')
    plt.savefig(dir_out+filename,bbox_inches='tight',dpi=500,transparent=True)

def giocatori_giovani():
    df_giovani = df.sort_values('age', ascending = True)[['name', 'age', 'team', 'nationality']].head(10) 
    filename = "{}.csv".format("Giocatori più giovani in FIFA")
    df_giovani.to_csv(dir_out+filename, index=False)

def giocatori_vecchi():
    df_vecchi = df.sort_values('age', ascending = False)[['name', 'age', 'team', 'nationality']].head(10) 
    filename = "{}.csv".format("Giocatori più vecchi in FIFA")
    df_vecchi.to_csv(dir_out+filename, index=False)
    
def squadre_giovani():   
    df_squadre_giovani = df.groupby(['team'])['age'].mean().sort_values(ascending = True).head(10).to_frame().reset_index() 
    filename = "{}.csv".format("Squadre mediamente più giovani in FIFA")
    df_squadre_giovani.to_csv(dir_out+filename, index=False)

def squadre_vecchie():
    df_squadre_vecchie = df.groupby(['team'])['age'].mean().sort_values(ascending = False).head(10).to_frame().reset_index() 
    filename = "{}.csv".format("Squadre mediamente più vecchie in FIFA")
    df_squadre_vecchie.to_csv(dir_out+filename, index=False)

def giocatori_top():  
    df_giocatori_top = df[['name', 'age', 'team', 'nationality', 'overall']].head(10) 
    filename = "{}.csv".format("Giocatori più forti in FIFA")
    df_giocatori_top.to_csv(dir_out+filename, index=False)

def difensori():
    df_difensori = df[df['position'] == 'CB'][['name', 'age', 'team', 'nationality', 'overall']].head(10) 
    filename = "{}.csv".format("Difensori centrali più forti in FIFA")
    df_difensori.to_csv(dir_out+filename, index=False)

def attaccanti():
    df_attaccanti = df[df['position'] == 'ST'][['name', 'age', 'team', 'nationality', 'overall']].head(10) 
    filename = "{}.csv".format("Attaccanti più forti in FIFA")
    df_attaccanti.to_csv(dir_out+filename, index=False)

def centravanti():
    df_centravanti = df[df['position'] == 'CF'][['name', 'age', 'team', 'nationality', 'overall']].head(10) 
    filename = "{}.csv".format("Centravanti più forti in FIFA")
    df_centravanti.to_csv(dir_out+filename, index=False)

def ala_sinistra():
    df_ala_sinistra = df[df['position'] == 'LW'][['name', 'age', 'team', 'nationality', 'overall']].head(10)
    filename = "{}.csv".format("Ali sinistre più forti in FIFA")
    df_ala_sinistra.to_csv(dir_out+filename, index=False)
    
def ala_destra():
    df_ala_destra = df[df['position'] == 'RW'][['name', 'age', 'team', 'nationality', 'overall']].head(10) 
    filename = "{}.csv".format("Ali destre più forti in FIFA")
    df_ala_destra.to_csv(dir_out+filename, index=False)
    
def df_portieri():
    df_portieri = df[df['position'] == 'GK'][['name', 'age', 'team', 'nationality', 'overall']].head(10)
    filename = "{}.csv".format("Portieri più forti in FIFA")
    df_portieri.to_csv(dir_out+filename, index=False)


# In[6]:


#A seconda degli argomenti passati in ingresso, restituisco una specifica analisi sui dati
opzioni=["-opzioni",
         "-gn",
         "-ng",
         "-sp",
         "-gg",  
         "-gv",   
         "-sg",    
         "-sv", 
         "-gt",
         "-di",
         "-at",
         "-ce",
         "-as",
         "-ad",
         "-po",     
         "-all"]
descr_opzioni=[ "Tutte le opzioni",
                "Giocatori per nazione in FIFA-2021",
                "Età dei giocatori in FIFA",
                "Squadre di club più popolari in FIFA-2021",
                "Giocatori più giovani in FIFA.png",
                "Giocatori più vecchi in FIFA.png",
                "Squadre mediamente più giovani in FIFA.png",
                "Squadre mediamente più vecchie in FIFA.png",
                "Giocatori più forti in FIFA.png",
                "Difensori centrali più forti in FIFA.png",
                "Attaccanti più forti in FIFA.png",
                "Centravanti più forti in FIFA.png",
                "Ali sinistre più forti in FIFA.png",
                "Ali sinistre più forti in FIFA.png",
                "Portieri più forti in FIFA.png",
                "Analizza tutto"]

for i in range(1,len(sys.argv)):
    argomento = sys.argv[i]
    if argomento == "-opzioni":
        for j, opzione in enumerate(opzioni):
            print("{}\n {}\n".format(opzione,descr_opzioni[j]))
        quit()
    if argomento == "-gn":
        logger.info("chiamata funzione giocatori_nazione")
        giocatori_nazione()
    if argomento == "-ng":
        logger.info("chiamata funzione numero_giocatori")
        numero_giocatori()
    if argomento == "-sp":
        logger.info("chiamata funzione squadre_popolari")
        squadre_popolari()
    if argomento == "-gg":
        logger.info("chiamata funzione giocatori_giovani")
        giocatori_giovani()   
    if argomento == "-gv":
        logger.info("chiamata funzione giocatori_vecchi")
        giocatori_vecchi()    
    if argomento == "-sg":
        logger.info("chiamata funzione squadre_giovani ") 
        squadre_giovani()    
    if argomento == "-sv":
        logger.info("chiamata funzione squadre_vecchie ")
        squadre_vecchie() 
    if argomento == "-gt":
        logger.info("chiamata funzione giocatori_top ")  
        giocatori_top()
    if argomento == "-di":
        logger.info("chiamata funzione difensori ") 
        difensori()
    if argomento == "-at":
        logger.info("chiamata funzione attaccanti ") 
        attaccanti()
    if argomento == "-ce":
        logger.info("chiamata funzione centravanti ") 
        centravanti()
    if argomento == "-as":
        logger.info("chiamata funzione ala_sinistra ") 
        ala_sinistra()
    if argomento == "-ad":
        logger.info("chiamata funzione ala_destra ")
        ala_destra()
    if argomento == "-po":
        logger.info("chiamata funzione df_portieri ")
        df_portieri()       
    if argomento == "-all":
        logger.info("chiamata all")
        giocatori_nazione()
        numero_giocatori()
        squadre_popolari()
        giocatori_giovani()
        giocatori_vecchi()
        squadre_giovani()
        squadre_vecchie()
        giocatori_top()
        difensori()
        attaccanti()
        centravanti()
        ala_sinistra()
        ala_destra()
        df_portieri()

