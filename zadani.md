# Automatizovaný osobní asistent pro sledování počasí a plánování úkolů


### Cíl projektu:
Vytvořit automatizovaný systém, který:

- Každý den získá aktuální předpověď počasí z API.
- Na základě předpovědi počasí pošle do kalendáře nebo to-do aplikace doporučení, jaké úkoly v ten den plnit.
- Pošle denní souhrn do e-mailu nebo na mobil.


### Kroky k realizaci:
1. #### Získání dat o počasí:
- API: Použij OpenWeatherMap API (nebo jiné API pro počasí), které poskytuje aktuální předpověď.
- Skript: Napiš Python skript, který se připojí k API, získá předpověď na následující den (např. teplotu, srážky) a uloží ji do proměnné nebo databáze.

2. #### Plánování úkolů na základě počasí
- Podmínky: Definuj pravidla, která se budou rozhodovat podle počasí. Například:
    - Pokud bude hezké počasí, doporučí se venkovní aktivity.
    - Pokud bude pršet, doporučí se domácí úkoly nebo práce, které se dají dělat uvnitř.
- Automatizace úkolů: Vytvoř skript, který tyto podmínky zpracuje a na jejich základě vytvoří úkoly pro daný den. Můžeš použít Google Calendar API nebo Todoist API k automatickému přidání úkolů.

3. #### Odesílání denního souhrnu
- E-mailový klient: Použij SMTP protokol nebo službu jako SendGrid pro automatické odeslání e-mailu s denním souhrnem.
- Mobilní notifikace: Alternativně můžeš nastavit notifikace na mobil (např. pomocí Twilio API pro SMS zprávy).

4. #### Automatizace skriptů
- Cron Job (Linux) nebo Task Scheduler (Windows): Nastav automatické spouštění tohoto skriptu každý den ráno, aby byl souhrn připraven ještě před tím, než začne tvůj den.

5. #### Bonus: Rozšíření projektu
- Grafická vizualizace: Přidej grafické zobrazení počasí nebo úkolů na svůj webový dashboard pomocí Flask nebo Django.
- Integrace s dalšími API: Přidej integraci s dalšími API, například pro získávání novinek, sledování dopravy nebo nákupních seznamů podle počasí.


### Technologie a nástroje:
- Programovací jazyk: Python
- Knihovny: 
    - Requests, 
    - smtplib (pro odesílání e-mailů), 
    - Flask/Django (webová aplikace), 
    - Celery (pokročilá automatizace úkolů)
- API: 
    - OpenWeatherMap API, 
    - Google Calendar API nebo Todoist API
- Nástroje: Cron Job (Linux) nebo Task Scheduler (Windows) pro plánování úloh


### Výsledky projektu:
Funkční automatizovaný systém, který každý den poskytne relevantní informace na základě počasí a pomůže lépe organizovat čas a úkoly. 




### Poznamky:


```
# DOCKER-COMPOSE

version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    command: python app.py

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:

```