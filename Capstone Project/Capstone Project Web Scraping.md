# Capstone Project : 
 ### **Web Scraping using BeautifulSoup and Selenium : Extract Vehicule attributes based on VIN Number**
 
 ## 1-Prepare Project Environment :
 
 - Aller au terminal :



    - Créer un dossier "Capstone Project" :
   
   ```
      mkdir Capstone-Project
    ```
    - Aller au dossier créer :
    
     ```
     cd .\Capstone-Project\
     ```
     
     - Créer un environement virtuel env :
     
     ```
     python -m venv env
     ```
     
- Aller au Visual Studio Code :

![a](https://user-images.githubusercontent.com/78825764/211033999-c84e7804-98ae-426c-a97c-cdcf6f3834d8.jpg)

- Cliquer sur Open Folder et sélectionner votre dossier "Capstone-Project" :


![a](https://user-images.githubusercontent.com/78825764/211034951-b9599400-0e68-423b-8f80-654f72fd832b.jpg)

- Ajouter un nouveau fichier 'web-scraping.py' :

![a](https://user-images.githubusercontent.com/78825764/211036319-4cb239a8-50d8-448e-af25-1a7421028e84.jpg)

---

![a](https://user-images.githubusercontent.com/78825764/211036658-101b4283-58fc-4004-9429-a77ce207a153.jpg)

 ## 2-Install chrome driver :
 
 - Aller au : https://chromedriver.chromium.org/downloads

![image](https://user-images.githubusercontent.com/78825764/211037329-dc687474-c676-4383-bd26-965e0ed02799.png)

- Installer la version de chromedriver qui convient à la version de votre browser Google Chrome

![image](https://user-images.githubusercontent.com/78825764/211038543-65915fc6-19bb-4ead-b34c-45c8578eafa0.png)

- Décompresser le dossier 

 ## 3-Télécharger la Data de VIN :

- Aller au : https://raw.githubusercontent.com/zinebzannouti/Web-Scraping/main/Data/VIN_Numbers.csv

- Bouton Droit > Enregistrer-sous

## 4- web-scraping.py Scipt
 
 - Installer Selenium , BeautifullSoup et Pandas
  
   - Ouvrir le terminal de VS code : terminal > New Terminal

![image](https://user-images.githubusercontent.com/78825764/211042329-af82adff-9153-4380-87fe-b51ee4629cdb.png)

  ``` 
  python -m pip install --upgrade pip setuptools wheel
  pip install Selenium
  pip install bs4
  pip install pandas
  ```


 - importer les bibliothèques

```
from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
import json
import pandas as pd
```

 - Définir un dataframe pandas depuis le fichier csv de vin que vous avez déjà télécharger :

```
df_vin=pd.read_csv('path')
```
- Définir un tableau vin où on va stocker les données :
```
vin=[]
```
- On va scraper les données du site : https://www.autodna.com/

![image](https://user-images.githubusercontent.com/78825764/211046648-b77e542f-ed4d-4097-8aff-5f7ea2e69923.png)

- Pour savoir les champs que vous allez extraire avec la méthode find_element() vous devez inspecter la page (bouton droit > inspecter )

![image](https://user-images.githubusercontent.com/78825764/211047295-3a2b051b-003a-4367-9d0e-e3c7d03bf1d5.png)

- L'idée est de prendre les vin qu'on a dans VIN_Numbers.csv et les encoder de tel manière d'avoir des VIN de 17 caractères au lieu de 11 caractères on peut ajouter 6 chiffre aléatoire pour compléter le VIN afin qu'il soit déchifrer par le site.
- Ensuite on va utiliser Selenium pour extraire les données des vehicules des VIN (Va jouer le role d'un robot qui passe les caractères des vin au site et click sur la bouton check vin.

- En supposant que vous êtes sur la page que vous souhaitez parser, Selenium stocke le code HTML source dans l'attribut page_source du driver. Vous chargeriez ensuite le page_source dans BeautifulSoup avec la méthode soup()

- On va ensuite s'interesser juste au title du code HTML source et on va le diviser en sorte qu'on va avoir le model et le make avec la méthode split()
- par exemple (Vous pouvez voir que la marque et le modèle est spécifier dans le title ) :

![image](https://user-images.githubusercontent.com/78825764/211050409-9b1d6204-91c1-4684-857e-763c71601010.png)

- On va boucler pour tous l'ensemble de nos VIN avec une boucle for .
- et pour chaque vin on va avoir la marque et le modèle extrait dans une liste qu'on va ensuite les grouper tous dans notre tableau vin avec vin.append()
- Après , on va enregistrer nos données sous forme de JSON et csv

- Voici à quoi ressemble notre script :

```
from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
import json
import pandas as pd
df_vin=pd.read_csv(`path_to-vin')
vin=[]
def web_scrap():
    for i in df_vin['vin_11'][0:30]:
    
        driver = webdriver.Chrome(executable_path='chromedriver.exe_path')
        #get the website to our driver
        #Fill_HERE
        #trouver le champ où on doit coller les vin pour effectuer la recherche à l'aide de (bouton droit>inspecter)
        search= #Fill_HERE
        #Envoyer les clés du VIN encoder 
        search.#Fill_HERE
        #trouver la bouton de recherche et clicker 
        driver.#fill_HERE.Fill_HERE
        #Make it sleep fo 10 seconds
        #Fill_HERE
        #Use beautifulsoup method soup() to parse the html source page
        S = #Fill_HERE
        #Select the title of the html and split it to get the make and model properly
        t=str(#Fill_HERE).#Fill_HERE.#Fill_HERE.#Fill_HERE
        d={'vin_11':i,
                'Make':t[0],
                'Model':' '.join(t[1:])}
        print(d)
        #ajouter les listes d dans vin[]
        #Fill_HERE
        #quit the driver
        #Fill_HERE
    #Save the vin table in a json file    
    #Fill_HERE
    #Convert it to a csv file
    #Fill_HERE
if __name__ == "__main__":
    web_scrap()
```

- Une fois que vous avez terminer votre script , exécuter cette commande dans le terminal :

```
python web-scraping.py
```

- Voici ce que vous allez avoir :

![ezgif com-gif-maker](https://user-images.githubusercontent.com/78825764/211056541-fb5a4b72-9302-4df5-a6b3-519ec46d1786.gif)

