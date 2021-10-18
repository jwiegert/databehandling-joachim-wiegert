
# 2021-10-11

- Kursen börjar 2021-10-18.
- Arbetsförmedlingen kommer, filmar och intervjuar några.

# 2021-10-18 : lect01 i code along

### Setup och påminnelser

- skapa ny repo:

> github: create repository
> git clone http....

(Inte tvärtom, inte skapa katalogen först, jag kan inte ha en katalog med samma namn redan :P )

- skapa ny pip-environment

> pipenv shell

- installera paketen där i

> pipenv install numpy pandas seaborn matplotlib

### Pandas Intro

- Pandas Series:

En pd.Serie är ett objekt i pandasklassen. Den innehåller en massa inbyggda funktioner som gör att den är båda snabbare och enklare att jobba med än t.ex. dict och list. Med dict och list måste man t.ex. loopa och annat för att lösa sina problem men pandas har verktygen inbyggda.

- Pandas DataFrame:

Ytterligare ett sätt att jobba med serier. En dataframe är som en mångdimensionell (2d endast?). Vissa fördelar med både serier och dataframes är att det går att skriva ut det snyggt som tabeller. Men andra fördelar är då igen alla inbyggda verktyg och operatorer. Pandas overloadar väldigt många operatorer och gör det mycket effektivare att gräva fram t.ex. vissa keys, vissa, data, byta ut data mellan olika typer, byta namn på keys, ta ut data som är större än/mindre än/lika med etc.

Kokchun: "När man tänker att man ska loopa [igenom en dataframe], då ska man tänka om."

#```py
#```