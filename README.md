
# 2021-10-11

- Kursen börjar 2021-10-18.
- Arbetsförmedlingen kommer, filmar och intervjuar några.

# 2021-10-18 : lect00

### Setup och påminnelser

- skapa ny repo:

> github: create repository

> git clone http....

(Inte tvärtom, inte skapa katalogen först, jag kan inte ha en katalog med samma namn redan :P )

- skapa ny pip-environment

> pipenv shell

- installera paketen där i

> pipenv install numpy pandas seaborn matplotlib openpyxl ipykernel

 - numpy: vanliga numeriska paketet

 - pandas: datahanteringspaket

 - seaborn: plot-tools

 - matplotlib: plot-paketet

 - openpyxl: öppna excelfiler i python

 - ipykernel: för att köra jupyter notebook

### Pandas Intro

- Pandas Series:

En pd.Serie är ett objekt i pandasklassen. Den innehåller en massa inbyggda funktioner som gör att den är båda snabbare och enklare att jobba med än t.ex. dict och list. Med dict och list måste man t.ex. loopa och annat för att lösa sina problem men pandas har verktygen inbyggda.

- Pandas DataFrame:

Ytterligare ett sätt att jobba med serier. En dataframe är som en mångdimensionell (2d endast?). Vissa fördelar med både serier och dataframes är att det går att skriva ut det snyggt som tabeller. Men andra fördelar är då igen alla inbyggda verktyg och operatorer. Pandas overloadar väldigt många operatorer och gör det mycket effektivare att gräva fram t.ex. vissa keys, vissa, data, byta ut data mellan olika typer, byta namn på keys, ta ut data som är större än/mindre än/lika med etc.

Kokchun: "När man tänker att man ska loopa [igenom en dataframe], då ska man tänka om."

Olika arbetssätt vi använt: 

selections, filtering, masking, rename, sort_values

info(), describe(), unique(), head(), tail()

Dessutom, finns flera sätt att skapa DataFrames på. Vi har sett ett par nu. Nyttja dokumentationen!

- Pandas Index object

Vänstra kolumnen i dataframes är ett eget objekt med index, en kolumn med siffror vanligtvis. Inget vi gått igenom.

- Seaborn

Inte en del av pandas. Ett praktiskt verktyg för att snabbt plotta data från dataframes och lite mer avancerade figurer än vad matplotlib gör som default (utan att ha femtioelva rader kod). Är kompatibelt med matplotlib (bygger på det?) men innehåller färdiga metoder för att göra t.ex. barplots, pie charts och annat, samt skriva ut vad som står på axlarnarna från key values från dataframes.

# 2021-10-19 : lect01

### Saknade data och störande felaktiga data

"Shit in gives shit out"

DataFrame kan hantera alla möjliga sorters listor och array'er, bara att lägga in.

Finns olika sätt som saknade data syns, NaN, Na, Null, etc. Finns olika sätt att hantera detta.

- isnull() : returns True if null
- notnull() : returns True if number
- dropna() : drops an axis with nulls, default removes rows (change with axis=).
- fillna() : fills Null values with certain value.

Går också att ta ut medelvärden och lägga in istället. Hur man gör beror på vad det är för data. Prata med den som kan situationen de kommer ifrån.

* Strategier

Vilken strategi man kör med beror på:

- Data set size: små dataset kan varje värde vara extra viktigt och det går inte att bara drop'a NaN. I stora dataset kan det vara så att de inte spelar nån roll, då kan man ta bort rader/kolumner med Nan. Hanteras varsamt.
- Viktig info: vissa kolumner/rader kan vara väldigt viktiga och kan inte drop'as.
- Sakkunskap: du har inte expertis i området data är från. Fråga en expert hur man bör göra.

Saknade data kan signifikant påverka:

- Visualiseringen.
- Beräkningar.
- Statistik.
- Maskininlärningsalgoritmer
- etc

Byta ut NaN mot annan statistik, går att nyttja en massa inbyggda verktyg.

- .median()
- .mean()
- .max()
- .min()

# 2021-10-21 : lect02

### Boktips

- Python for Data Analysis - Wes McKinney

Wes McKinney är förörigt skaparen av Pandas. 2nd Edition ska vara senast vid skrivande stund.

### Plotly express

- Utvecklades för forskare (som inte kan java vanligtvis) för att plotta interaktiva plots.

- Finns både en opensource och en kommersiell variant. Den kommersiella kostar typ 50k$ per år och 5 användare...

Gör om ex00 och ex01 men med plotly express istället. Det går rätt enkelt att plotta dem så.

FYI man kan inte göra subplots med plotly-express. För det får man använda seaborn eller matplotlib.

# 2021-10-25 : lect03

### Slå ihop data-set: merge, join, concat, append

Se [Pandas dokumentation om merge](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)

- how/join: inner, right, left, outer

inner: tar bara det som är gemensamt för alla dataframes.

outer: tar allt från alla dataframes och slår ihop.

right: tar allt från "höger" dataframe och det som är gemensamt från båda.

left: tar allt från "vänster" dataframe och det som är gemensamt från båda.

- pd.concat([dataframe1,dataframe2, ... dataframeN])

Slår ihop dataframes, antingen som nya rader eller nya kolumner. Nya rader, axis=0/"rows" är default. Använder "set logic" med "join="outer"/"inner"", alltså slår ihop alla data (default, outer) i alla dataframes eller bara det som är gemensamt för alla dataframes (inner).

- pd.merge


"Då kan man få program som är användvänliga och det vore dåligt." (Erik, kursare)

### Parse HTML -> pandas dataframe

(TBD)

# 2021-10-26 : Intro till Lab1

Dataanalys av FHM:s statistik över C-19 i Sverige. Laddade hem filerna 2021-10-26. När du studerar antal barn i Sverige, kolla först om det finns några data på <16-åringar. Det ska inte finnas några men kan ha dykt upp senare.

- Jupyter notebook med Markdown-anteckningar som rapport. Spara bilderna.

- En py-fil med funktioner som jag återanvänder.

Uppgift 4: Egenhändigt studerande av internationella data. Se [FHM:s sida med länkar](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/antal-fall-globalt/).

Graferna ska vara designade så att de är enkla, pedagogiska och inte lurar folk. Inte kapa axlarna!

# 2021-10-28 : Gästföreläsning, KPI:er

Key Perfomance Indicator: att mäta effektivitet hos nånting m.h.a. av div. faktorer - ger indikatorer. Går egentligen att använda i nästan vad som helst som är resultatbaserat, att mäta om man är på väg åt rätt håll.

Exempel

- Försäljningssiffror - nöjda kunder, volumer, nya kunder.

- Produktion - Att rätt mängd produceras inom rätt tid.

- Samhälleliga frågor - Nollvisionen, Covid-19, mäta antal döda och skadade.

- Skolor - Mäta resultatet, antal examina, LiA (YH)

Behöver vara något

- mätbart.

- faktorer som är viktiga för framgångar i organisationen.

- kopplat till något mål.

- begränsas gärna till 5-8 mätvärden (blir det inte risk för att man sätter upp en för enkel modell då?)

- applicerbar för hela organisationen, den ska inte vara för "långt bort" och "stor" utan vara något alla relaterar till.

Som man frågar får man svar. KPI:en måste designas med omsorg för annars kan mätningen ge konstiga resultat som inte funkar.

Används för att

- identifiera trender - ger signaler på om något är fel.

- göra beslut, se hur man ska prioritera verksamheten.

Skapas från att

- kolla på övergripande mål.

- hur ser processen ut?

Man vill få till en både meningsfull och mätbar KPI. Så har man också ett "mätdatum" som behöver sättas på ett vettigt sätt (t.ex. så att det inte skapar onödig stress).

Möjlighet är att ha alternativ för att inte fastna i en för enkel och stringent modell som gör arbetsflödet oanpassningsbart och t.ex. stressigt. 

Allt detta behöver någon slags löpande datainsamling och arbete för att analysera data och ge resultat. 

## Nackdelar

- Ensidigt synsätt - stirrar sig blind på siffrorna, externa faktorer missar. T.ex.. man måste inte uppnå "målen" bara för målets skull.

- Data behöver mätas löpande eller frekvent. Läggs för mycket tid på att mäta och prata mätningar.

- Väldigt mycket risk för tillbakablick, stirrar sig blind bakåt och inte hanterar framtiden.

## KPI:er och AI

En löpande insamling data och dess analys kan hanteras automatiskt med AI.

Mätningar kan handla om

- Noggrannhet och absoluta fel.

- Antal frågor, problem, requests, och antal behandlade sådana.

- Meta: mäta volymer av analyserade mätdata...

Tillgång till data i allmänhet är extremt mycket större idag. Mer data än vad man kan hantera. Här kommer då AI in för att hantera och analysera och sålla bland alla data. Vad är faktiskt användbart? Kombinera det med KPI:er så kan man automatisera själva KPI-formulerandet. Andra exempel är t.ex. inom prissättning, att samla data på vad andra har för prissättningar, hur ska det påverka ens egna prissättning? (Låter farligt...)

## Övning: KPI:er och C19-vaccin

Möjliga KPI:er

- Antal givna doser, 1 och 2.

- Jämför med tidigare, tidsserier.

- Andel vaccinerade, i landet, i regioner, per åldergrupp.

- Hur många med C19 på sjukhus, hur utvecklar det sig, hur stor andel är ovaccinerade.

- Prognos framåt, kapacitet på sjukhus och antal vaccin.

- Typer av vaccin, hur många ges av vardera, allmänna resultat där.

## Frågor

Hur hantera chefer som stirrar sig blinda på KPI:er som är dåligt formulerade och missar andra viktiga detaljer? Bara för att det inte är mätbart betyder ju itne att det är oviktigt.

Svar: visa nyfikenhet istället för kritik i början. Fråga och undra vad man får ut av div. KPI:er och fråga om hur de hanterar andra faktorer.

# 2021-11-01 : Lecture04

## Git bash kommadon

> git status

Kollar info i den katalogen som är ditt git-repo. Listar om det finns något commit'at men icke-push'at.

> git pull

Hämtar hem allt som blivit push'at till repo'n sen sist. 

Här finns en massa kommandon som vi innan bara kört grafiskt i VSC. Som commit, push, etc.

## Datetime : lect04_dates

> from datetime import datetime

hämtar en klass som hanterar datum etc.

Exempel:

> datetime.now()

Ger datum och tid till nu.

> .strftime()

gör om object till sträng'ad tid

> .strptime()

gör om sträng'ad 


## Stock data och gömda filer

I .gitignore finns en lista över filnamn och filändelser som git ignorerar när man pushar filer till github. T.ex. kan man har en textfil med namnet

> .env

Det är en environmentfil där man kan lägga koder, lösenord, nycklar som man behöver men inte vill sprida på.

I .gitignore man kan också lägga in vad som helst som man nu inte vill dela på.

# 2021-11-02 : lect05

Mer om aktier och design'a dashboard. Se katalogen lect05_*

Vi skrev en modul, load_data som laddar in data från lokalt sparade csv-filer och sparar dem som object.

Vi designade ett enkelt API som körs i webläsarn med lite text och dropdown-meny där man väljer från de aktier vi har laddat ner. Den plottar kursen med plotlyexpress.

Sen la vi till en time-slider som använder relativedelta:

```py
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
yesterday = now.date() - relativedelta(days = 10)
print(yesterday)
```


#```py
#```