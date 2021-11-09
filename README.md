
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

> pipenv install numpy pandas seaborn matplotlib openpyxl ipykernel plotly plotly-express

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

# 2021-11-04 : lect06

Anonymiseringar och genomgång av grupparbete.

## Hash function: S -h-> h(S)

Vi har ett "meddelande", S, skickas till en sida, ger h(S) = hash value. S -h-> h(S)

Har vissa krav:

- Deterministiskt, samma meddelande ska ge samma hast value h(S)

- Snabbt att beräkna

- S -h-> h(S) ska vara enkelriktat. h(S) -h-> ger inte tillbaka S. (Hackers löser det genom brute force istället.)

- Två olika strängar, S1 =/= S2, ger olika hash values, h(S1) =/= h(S2).

- S + epsilon -> h(S+epsilon) - h(S) >> 1. Alltså, S plus en liiten skillnad (epsilon) ger extremt olika hash values.

För att göra brute'forceing snabbare så brukar hackers börja med vanliga ord och vanliga lösenord. Därför är det faktiskt nytta att använda ovanliga ord i sina koder, men också bra att ha lååånga lösenord för det blir extra långsamt att bruteforce'a.

Fråga: Många ber om speciella tecken i sina lösenord. Det är väl för att ge ovanliga ord som är svåra att gissa, men om alla har specialtecken i sina lösenord blir de ju inte svåra att gissa på längre?

## Projekt

Görs i en gemensam github-repo

- New repository

- Settings i repo'n -> manage access -> logga in -> add people -> skriv deras github-email.

Så 4st uppgifter plus uppvärmning. Lägg ihop allt i en dashboard som vi sen använder i presentationen, 5-15min per grupp. Sen ska vi också göra en video med [OBS](https://obsproject.com/sv) individuellt där jag går igenom vad koderna gör.

För VG krävs välstruktuerad kod m.h.a. funktioner eller klasser. Effektiv enkel kod och användarvänlig dashboard.


# 2021-11-08 :  GDPR

### Myndigheter

- Sverige: 

Riksdagsutskott, departement, integritetesskyddsmyndighet (fd datainspektionen, bytte namn i januari 2021).

- EU: 

EU council (EU-kommissionen), Coreper - committee of the parmanent representatives of the goverments of the member states of the european union.

EDPB: European data protection board - europeiska dataskyddsstyrelsen.


## Lite begrepp

- Data controller: Ingen aktör som faller under GDPR-lagstiftningen får vara anonyma. De måste ha någon person utåt, en "controller". Verksamheter, offentliga och privata företag, som hanterar personuppgifter är de som faller under GDPR.

- Profiling: Kallas det när man automatiskt går igenom och analyserar personuppgifter.


## Syfte

Alla aktörer måste hantera en del data.

- Legal plikt, t.ex. skickar skatteuppgifter till myndigheter.

- Förmåner till anställda, t.ex. låna företagsbil.

- Kunduppgifter eller liknande, t.ex. inför kampanjer och rea måste kunder som skriver upp sig få veta vilka data som behövs för att de ska kunna vara med på kampanjen.

All datainsamling handlar alltså inte om att aktören måste göra det p.g.a. lagstiftning. Då kan det vara så att de har legitima skäl till att samla in data. GDPR innebär då att de individer som samlas in data om måste få veta vad och varför som samlas in om dem, och såklart att man har möjligheten att inte delta. Individens rättigheter väger tungt, som att man får hämta ut de data som samlats in om en och har rätt att flytta dem från en annan aktör till en annan. Till exempel från en telefonoperatör till en annan.

Tvärtom däremot, att aktörer skickar persondata mellan olika aktörer får INTE hända. Inte utan personernas godkännande.


### Minimering av data

Aktörer är då också skyldiga att inte samla in mer data än de faktiskt behöva och syftet som gör det legitimt att samla in data är aldrig för evigt. Dock så är syftestiden lätt att sätta till något långt. Exempel, garanti på produkter, eller att spara data så länge någon är en kund.

I vissa specialfall finns det lagstiftning som går över GDPR. Exempel är att skolor kan spara på betygsuppgifter om elever som inte går på skolan längre, eller vaccinationsregistret i Sverige, eller andra journaler inom sjukvården.

Olika sätt finns för att avpersonifiera persondata. Ta som exempel födelsedatum, det exakta datumet, eller exakta året behövs sällan. Det räcker att samla in till exempel 5-10 årsspann av födelsedatum på personer när man behöver studera åldersmässiga effekter inom något.

Exempel till data science, här är det kanske svårt att legitimera datainsamlingen med att man har krav på dig att samla dem. Här är det viktigt att minimera insamling av onödiga data, data som är svårt att visa hur de är legitima. Som exempel, göra data inexaktare för att ta bort personifieringen, ta bort det som faktiskt inte behövs.

- Ta bort personlig data - går det? : Pseudoanonymisering

Om inte, går det att ta bort direkt personifieringen i datan? Namn, adress, IDnummer, födelsedatum, bilder, intern kommunikation (E-mail, jobbchat etc). Igen, födelsedatum går att ändra till t.ex. "född mellan 1980 och 1989". Alternativa lagar gäller i vissa fall, t.ex. patientdatalagen gäller hälsodata.

- Aktuella data - Data åldras

Finns det anledning till att spara t.ex. någons adress i 60 år för pensionssyfte? Nej, och dessutom lär inte adressen vara korrekt om ett par decennier i allafall.


### Dataprofilering

Exempel, företag hämtar ut inkomstnivåer beroende på postadresser. Sedan anpassar de t.ex. nivåer på rea till postadresser eller olika premier på bilförsäkringar beroende på var man bor.

I vissa fall faller det inte in i GDPR utan snarare inom lagstiftning kring förtryck (vad heter det?).

### DPA : Data processing agreements

- Alla företag som sparar data är data controllers.

- Data controllers är anvsariga att hantera data inom GDPR.

- Leverantörer som hanterar data blir själva data controllers.

- Alla kontrakt med nya samarbetspartners innehåller DPA'er.

- Företag bör kunna se till att deras leverantörer hanterar deta på korrekta vis.

- När ett företag byter leverantör måste den gamla leverantören kunna lämna över alla data och ta bort dem från sina egna förvaringar.

Exempel, molntjänster. När ett litet företag nyttjar t.ex. OneDrive för sina data så blir Microsoft en leverantör och då får företaget acceptera Microsofts DPA. Kan vara värt att se till att ens servrar - ens molntjänstleverantör - faktiskt finns inom EU i sådana fall.


## Kryptering vs anonymisering

Helt olika syfte bakom dessa två. Krypterade data går fortfarande att identifiera personer. Anonymisering är att faktiskt ta bort data och göra den omöjlig att återskapa från befintliga data. Båda har delar inom GDPR. Kryptering är till för att skydda persondata från yttre (otillåtna) aktörer.

- (Artikel 32) Data controller har ansvar att ta till tillräckligt åtgärder för att minimera identifiering såsom pseudoanonymisering och kryptering.


### Koppla olika dataset till personer

- Linkability

Att kunna koppla samman minst 2 data om samma individ, eller samma grupp människor etc. En yttre aktör, t.ex. en hacker ska inte kunna koppla samman två skilda uppsättningar data till samma individer. 

- Inference

Möjligheten att utröna med hög sannolikhet värden hos olika attribut från data inom andra attribut. Handlar inte om att ha tillgång till data, utan nyttja en delmängd av data som finns tillgängliga för att ta reda på något annat som man inte ska veta. 

I båda fall, om det går att identifiera personer har inte anonymiseringen och krypteringen gjorts tillräckligt bra. Bristen och ansvaret ligger då hos aktören som inte har hanterat sina insamlade data tillräckligt korrekt.

- Exempel: Lönedata

Dataset med löner för avdelning X. Dessa innehåller också kön och födelsedatum. Det går att se att det finns t.ex. två kvinnor på X. Kolla adressboken hos företaget, vilka personer har kvinnliga namn? Det går också att söka efter födelsedatum externt och så identifiera vilka löner dessa kvinnor har.

- Smart querying

Ett sätt att motverka linkability and inference är att hålla koll på vilka frågor som ställs inom databaserna. (Simulera data-mining?) Kolla vad för resultat som dyker upp. Försöker någon extern nyttja databasen för att få ut individdata?


### Internationella avtal

Samarbeten med aktörer utanför EU kräver att antingen har landet lagstiftning motsvarande GDPR eller att det går att avtala om dataskydd. Finns domslut inom Europeiska dataskyddsdomstolen. Uppmaningen är att aktörer ser till att ha koll på hur deras data överförs och hanteras av deras leverantörer. "Know your transfers".

- Länder med adekvat skyddsnivå : från integritetsskyddsmyndigheten

Länder som har tillräckliga dataskydd utanför EU:

Andorra, Argentina, Bailiwick of Guernsey, Färööarna, Isle of Man, Israel, Japan, Jersey, Nya Zeeland, Schweiz, Storbritannien, Uruguay.

Dock inte USA, Australien, Kina, Ryssland, etc.

Norge är med i GDPR via EEA.


## Rekommendationer

- Första-koll, är datan tillräckligt okänsliga?

- Var öppen och tydlig med varför data ska samlas in. Gör det inte bara för att du kan.

- Nyttja jurister på din arbetsplats, kolla vad du kan och inte kan göra. Se till att det finns DPA'er.

- Juristerna kan också se över att datan som sparas är tillräcklgit anonymiserade och krypterade. De vet också när och hur man ska kontakta personer som har data sparade.

- Om det inte finns jurister, nyttja myndigheter och andra nätverk. De ska inte bara se till att lagen följs utan hjälpa aktörer att följa lagen. Svenskt näringsliv, handelskammaren, etc.


# 2021-11-09 : lect05-2 : Fortsättning på stock-dashboard

Vad ska man tänka på när man gör en dashboard? Bra att ha en plan från början. En grundläggande design. UX-studenterna använder sig av [figma.com](figma.com). Men det går också bra med t.ex. paintbrush eller annat enkelt ritprogram.

> Ja den är ful. Det spelar inte så stor roll här.

Vanligtvis designar man först alla interaktiva saker. Vilka saker vill vi ha på dashboarden, vilka knappar, menyer, barer, figurer ska vi ha? Sedan designar vi om den så att den ska se snygg ut.

> dash-bootstrap-components

[dash-boostrap](http://dash-bootstrap-components.opensource.faculty.ai/)

För att göra stil och annat på ens dashboard. Går att välja en massa olika teman.

[bootstrap styles](https://hackerthemes.com/bootstrap-cheatsheet/)





#```py
#```
