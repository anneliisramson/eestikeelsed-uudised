# Eestikeelsete uudiste kogumine veebist, meelsus, klassifitseerimine, väär ja tõene info

11.12.20

Kasutusjuhend skriptide jooksutamiseks Jupyter Notebookis:
1. Installida Anaconda (https://docs.anaconda.com/anaconda/install/)
2. Installida EstNLTK käsuga:
conda install -c estnltk -c conda-forge estnltk=1.6.7b
3. Installida EstNLTK-d sisaldavas virtuaalkeskkonnas Jupyter Notebook käsuga:
conda install jupyter
3. Installida vajalikud teegid:

conda install scikit-learn

conda install tqdm

conda install -c conda-forge scrapy

conda install bs4

kas veel mõni?

Projekti etapid, sisendid ja väljundid

01 Veebiämblikud veebilehelt linkide "kraapimiseks"

    Delfi newsbot.py
    Telegram telebot.py
    Uued Uudised uueduudised.py
    
    sisend: Delfi, Telegrami või Uued Uudised veebilehe aadress
    väljundfail: veebilehtedelt leitud uudiste html-lingikogud csv-formaadis

02 Andmekorje lingikogude linkidelt

    02 delfi_andmetekorje.ipynb
    02 telegram_andmekorje_rubriigid.ipynb
    02 uueduudised_andmekorje_rubriigid.ipynb
    
    sisendfail: html-lingikogu;  
    väljund ekraanile: andmetabel, mis sisaldab iga uudise kohta title, text, subject, date, url
                       sõnapilv (saab muuta stoppsõnu, sõnapilves kasutatavaid sõnaliike)
    väljundfailid: uudisteandmed csv-formaadis (title, text, subject, date, url)
                   sõnapilv png-formaadis
                   
03 Andmete liitmine

    03 andmete_liitmine.ipynb
    
    sisendfailid: uudisteandmed (data_delfi.csv; data_telegram_csv; data_uueduudised.csv);
    väljund ekraanile: uudisartiklite jaotus väljaannete kaupa;
                       sõnapilv (saab muuta stoppsõnu, sõnapilves kasutatavaid sõnaliike)
    väljundfail: ühendatud uudisteandmed csv-formaadis (title, text, subject, date, url)
   
04 Andmete tekstide meelsus, tonaalsus, polaarsus: väljund csv-fail (meelsuse karakteristikutega tabel)

    04 Meelsus.ipynb
    
    sisendfailid: ühendatud uudisteandmed; estonian-emotion-lexicon.csv
    väljund ekraanile: artiklite meelsusega tabel (tabelis on uudise kohta arvutatud karakteristikud)
    väljundfail: artiklite meelsusega tabel csv-formaadis
    
05 Andmete tekstide klasterdamine

    05 Klasterdamine.ipynb
    sisendfail: ühendatud uudisteandmed;
    väljund ekraanile: KMeans klasterdus ja visualiseering (saab muuta klastrite arvu, stoppsõnu, 
                                                            kasutada kaht meetodit teksti sõnestamiseks lemmatize_with_estnltk või tokenize_with_estnltk)
                       hierarhiline klasterdus ja visualiseering

06 Väärinfo ja tõese info eristamine ning uurimine

    06 Väärinfo_ja_tõese_info_uurimine.ipynb
    
    sisendfailid: fake.csv; true.csv
    väljund ekraanile: väärinfo ja tõese info sõnapilved; sagedate sõnade jaotus, sõnade sarnasus Wordnetis, sõnade sarnasused Word2Vec mudeli abil)
    
    
07 Mudelid: logistiline regressioon, otsustuspuu, juhuslik mets, passiivne agressiivne klassifitseerija

    07 Väärinfo_mudelid.ipynb
    sisendfailid: fake.csv; true.csv
    väljund: mudeli täpsus ja segadusmaatriks (saab muuta mudelite parameetreid, stoppsõnu, 
                                               kasutada kaht meetodit teksti sõnestamiseks lemmatize_with_estnltk või tokenize_with_estnltk)
