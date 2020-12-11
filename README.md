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
    Scrapy juhend: https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

    Delfist linkide kogumiseks käsureale (vastava spidersi kaustas):
    scrapy crawl newsbot
    
    Telegram linkide kogumiseks käsureale (vastava spidersi kaustas):
    scrapy crawl telebot
    
    Uued Uudised linkide kogumiseks käsureale (vastava spidersi kaustas):
    scrapy crawl uueduudised
    
    failides newsbot.py, telebot.py või uueduudised.py määrab start_urls veebilehe, millelt alustatakse "kraapimist"
    Delfi puhul alustatakse kraapimist lehelt 'https://www.delfi.ee/archive/?tod=03.12.2020&fromd=01.01.2020&channel=1&category=13&query=']
    
    Telegrami puhul alustatakse kraapimist lehtedelt 'https://www.telegram.ee/arvamus', 'https://www.telegram.ee/eesti','https://www.telegram.ee/maailm',                   'https://www.telegram.ee/nwo', 'https://www.telegram.ee/teadus-ja-tulevik'
    
    Uued Uudised puhul alustatakse kraapimist lehtedelt 'https://uueduudised.ee/rubriik/arvamus/','https://uueduudised.ee/rubriik/uudis/eesti/', 'https://uueduudised.ee/rubriik/uudis/maailm/', 'https://uueduudised.ee/rubriik/majandus/'
    
    soovi korral saab start_urls muuta
   
    väljundfaili nimi määratakse  failides settings.py (näiteks FEED_URI = "uueduudised_rubriigid_arhiiv.csv")
    väljund: veebilehtedelt leitud uudiste html-lingikogud csv-formaadis (fail tekib vastava spidersi kausta)
    
02 Andmekorje lingikogude linkidelt
    Järgnevad failid käivitada Jupyter Notebookis
    
    02 delfi_andmetekorje.ipynb
    02 telegram_andmekorje_rubriigid.ipynb
    02 uueduudised_andmekorje_rubriigid.ipynb
    
    sisendfail: html-lingikogu;  
    NB! Eelmises punktis saadud html-lingikogus võib olla katkisi linke. Ma ei leidnud praegu muud lahendust kui katkiste linkide käsitsi eemaldamine.
    NB! Koodi töö õigeks jätkamiseks saab kasutada parandatud lingikogu_muudetud.csv
    väljund ekraanile: andmetabel, mis sisaldab iga uudise kohta title, text, subject, date, url
                       sõnapilv (saab muuta stoppsõnu, sõnapilves kasutatavaid sõnaliike)
    väljundfailid: uudisteandmed (data_delfi.csv; data_telegram_csv; data_uueduudised.csv), igale uudisele vastab title, text, subject, date, url
                   sõnapilv png-formaadis
                   
03 Andmete liitmine

    03 andmete_liitmine.ipynb
    
    sisendfailid: uudisteandmed (data_delfi.csv; data_telegram_csv; data_uueduudised.csv);
    väljund ekraanile: uudisartiklite jaotus väljaannete kaupa;
                       sõnapilv (saab muuta stoppsõnu, sõnapilves kasutatavaid sõnaliike)
                       
    sõnaliikide tähendused:
    https://github.com/estnltk/estnltk/blob/version_1.6/tutorials/nlp_pipeline/A_02_morphology_tables.ipynb
    väljundfail: ühendatud uudisteandmed data_uudised_koos.csv, igale uudisele vastav title, text, subject, date, url
   
04 Andmete tekstide meelsus, tonaalsus, polaarsus: väljund csv-fail (meelsuse karakteristikutega tabel)

    04 Meelsus.ipynb
    
    sisendfailid: ühendatud uudisteandmed data_uudised_koos.csv; Eesti keele instituudi koostatud: estonian-emotion-lexicon.csv
    kasutatud verbivormid
    https://github.com/estnltk/estnltk/blob/version_1.6/tutorials/nlp_pipeline/A_02_morphology_tables.ipynb
    väljund ekraanile: artiklite meelsusega tabel (tabelis on uudise kohta arvutatud karakteristikud)
    väljundfail: artiklite meelsusega tabel csv-formaadis
    
05 Andmete tekstide klasterdamine

    05 Klasterdamine.ipynb
    sisendfail: ühendatud uudisteandmed data_uudised_koos.csv;
    väljund ekraanile: KMeans klasterdus ja visualiseering (saab muuta klastrite arvu, stoppsõnu, 
                                                            kasutada kaht meetodit teksti sõnestamiseks lemmatize_with_estnltk või tokenize_with_estnltk)
                       hierarhiline klasterdus ja visualiseering

06 Väärinfo ja tõese info eristamine ning uurimine

    06 Väärinfo_ja_tõese_info_uurimine.ipynb
    
    sisendfailid: fake.csv; true.csv (enamus fake ja true uudiseid on valitud failist data_uudised_koos.csv, käsitsi märgendatud)
    väljund ekraanile: väärinfo ja tõese info sõnapilved; sagedaste sõnade jaotus, sõnade sarnasus Wordnetis, sõnade sarnasused Word2Vec mudeli abil)
    NB! Wordnet ja Word2Vec annab samade andmete korral aeg-ajalt veateateid, põhjust veel ei tea.
    
    
07 Mudelid: logistiline regressioon, otsustuspuu, juhuslik mets, passiivne agressiivne klassifitseerija

    07 Väärinfo_mudelid.ipynb
    sisendfailid: fake.csv; true.csv
    väljund: mudeli täpsus ja segadusmaatriks (saab muuta mudelite parameetreid, stoppsõnu, 
                                               kasutada kaht meetodit teksti sõnestamiseks lemmatize_with_estnltk või tokenize_with_estnltk)
    Näiteks:
    # teksti sõnestamiseks on kasutatud lemmasid ja stopsõnu
    pipe = Pipeline([('vect', CountVectorizer(tokenizer = lemmatize_with_estnltk, stop_words = stopsõnad_uus)),
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])
                 
    või
    # vaikimisi parameetrid
    pipe = Pipeline([('vect', CountVectorizer())
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])
                 
    või
    #teksti sõnestamiseks on kasutatud sõnasid ja stopsõnu
    pipe = Pipeline([('vect', CountVectorizer(tokenizer = tokenize_with_estnltk, stop_words = stopsõnad_uus)),
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])
    või
    teksti sõnestamiseks on kasutatud lemmasid
     pipe = Pipeline([('vect', CountVectorizer(tokenizer = lemmatize_with_estnltk),
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])
