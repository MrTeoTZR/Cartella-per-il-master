# Progetto n° 1: analisi del dataset di Fifa 2021

## Overview
Il progetto permette l'analisi di un dataset di calciatori di Fifa 2021. 
Il file è già preimpostato per scaricare in autonomia il suddetto dataset senza quindi richiedere all'utente di procurarselo prima del run del Docker.

Lo script Python è stato pensato per essere eseguito tramite un container Docker. 
Il Dockerfile, infatti, fornisce le istruzioni necessarie per la creazione della macchina virtuale che poi sarà in grado di sfruttare il file Python per eseguire, con facilità, 14 analisi diverse fra loro.

L'output dell'analisi scelta viene anche salvato nella cartella locale dell'utente, all'indirizzo prefissato nel file (cioè nella cartella *materiale/results*).

## Prerequisiti
Prima di tutto, sarà indispensabile scaricare l'applicazione Docker Desktop nella propria macchina fisica, assieme ad un Kernel Linux.
La procedura è molto semplice ed è descritta all'interno dei link sottostanti:


- Link Docker --> https://www.docker.com/products/docker-desktop

- Link Kernel --> https://aka.ms/wsl2kernel


Poi, prima di passare alla fase di build e run del Docker, sarà necessario entrare nel prompt dei comandi e posizionarsi sulla cartella di progetto.


Comando per il posizionamento --> cd percorso

## Build del container
AL fine di effettuare la build del Docker, bisogna inserire il seguente comando nel prompt dei comandi. Questo servirà per creare un container chiamato "cloud_fifa", che verrà costruito a partire dalle istruzioni contenute all'interno del dockerfile.


Comando **build** Docker --> docker build -t cloud_fifa:latest .


Inserendo questo comando, verrà creato un container a partire dall'immagine "slim-buster". All'interno del container, il Docker installa autonomamente le librerie Python necessarie per l'esecuzione dello script. Queste librerie sono contenute nel file requirements.txt.
Sempre autonomamente, il Docker creerà al suo interno la cartella "materiale/results", a cui vengono assegnati i permessi di lettura, scrittura ed esecuzione.
Nella fase di build, viene indicato (nell'entry point) il file Python che il Docker dovrà eseguire durante la fase di run.

## Run del container
Per il run del Docker, bisognerà digitare il seguente comando nel prompt dei comandi, a seconda del sistema operativo utilizzato nel proprio pc.


Comando **run** del Docker in **Windows CMD**        --> docker run --rm -v "%cd%:/home" cloud_fifa *PARAMETRO*

Comando **run** del Docker in **Windows Powershell** --> docker run --rm -v "${PWD}:/home" cloud_fifa *PARAMETRO*

Comando **run** del Docker in **Linux**             ---> docker run --rm -v "$(PWD):/home" cloud_fifa *PARAMETRO*


Al posto della parola *PARAMETRO*, l'utente potrà scegliere di scrivere una delle seguenti 16 opzioni, a seconda dell'output che vuole ottenere.

- opzioni	=> L'utente vuole vedere **tutte le opzioni disponibili**             
- gn			  => L'utente vuole vedere i **giocatori divisi per nazione**        
- ng			  => L'utente vuole vedere l'**età dei giocatori**                   
- sp			  => L'utente vuole vedere le **squadre di club più popolari**       
- gg  		  => L'utente vuole vedere i **giocatori più giovani**               
- gv  		  => L'utente vuole vedere i **giocatori più vecchi**                
- sg    		=> L'utente vuole vedere le **squadre mediamente più giovani**     
- sv 		  => L'utente vuole vedere le **squadre mediamente più vecchie**     
- gt			  => L'utente vuole vedere i **giocatori più forti**                 
- di 		  => L'utente vuole vedere i **difensori centrali più forti**       
- at 	  	=> L'utente vuole vedere gli **attaccanti più forti**             
- ce 		  => L'utente vuole vedere i **centravanti più forti**              
- as 		  => L'utente vuole vedere le **ali sinistre più forti**            
- ad 		  => L'utente vuole vedere le **ali destre più forti**            
- po 	  	=> L'utente vuole vedere i **portieri più forti**                 
- all 	  	=> L'utente vuole vedere l'**output di tutte le analisi**  
