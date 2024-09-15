# Automatizovaný osobní asistent pro sledování počasí a plánování úkolů


### Cíl projektu:
Vytvořit automatizovaný systém, který:

- Každý den získá aktuální předpověď počasí z API.
- Na základě předpovědi počasí pošle do kalendáře nebo to-do aplikace doporučení, jaké úkoly v ten den plnit.
- Pošle denní souhrn do e-mailu nebo na mobil.


### Kroky k realizaci:
1. #### Získání dat o počasí:
- API: Použij OpenWeatherMap API (nebo jiné API pro počasí), které poskytuje aktuální předpověď. ✅
- Skript: Napiš Python skript, který se připojí k API, získá předpověď na následující den (např. teplotu, srážky) a uloží ji do proměnné nebo databáze. ✅

2. #### Plánování úkolů na základě počasí
- Podmínky: Definuj pravidla, která se budou rozhodovat podle počasí. Například:
    - Pokud bude hezké počasí, doporučí se venkovní aktivity.
    - Pokud bude pršet, doporučí se domácí úkoly nebo práce, které se dají dělat uvnitř.
- Automatizace úkolů: Vytvoř skript, který tyto podmínky zpracuje a na jejich základě vytvoří úkoly pro daný den. Můžeš použít Google Calendar API nebo Todoist API k automatickému přidání úkolů. ✅ - pomocí AI_API dotazu

3. #### Odesílání denního souhrnu
- E-mailový klient: Použij SMTP protokol nebo službu jako SendGrid pro automatické odeslání e-mailu s denním souhrnem. ✅ API Mailgun (nějaká omezení)
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


## Future:

- předělat API mailgun na google gmail ofiko (težší registrace....)
- změnit (doplnit) průměrnou teplotu za MIN a MAX v daný den.
- Web App ?
- ukládání do dbs ? 
  - jak AI doporučení (pro případ výpadku)
  - tak teploty, pro uchování historie

### Poznamky:

Když se změní nastavení Dockerfile / docker-compose.yml nebo soubory, které se kopírují do kontejneru, nutné rebuild image! ``` docker-compose up --build ```

```
# DOCKER-COMPOSE (do budoucna i s dbs)

version: '3'
services:
  app:
    build:
    context: .
    dockerfile: Dockerfile
    container_name: weather_app
    depends_on:
      - db
    environment:
      - POSTGRES_HOST=db
      - POSTGRES_PORT=5432
      - POSTGRES_DB=weather_db
      - POSTGRES_USER=your_user
      - POSTGRES_PASSWORD=your_password
      - WEATHER_API_KEY=${WEATHER_API_KEY}
      - AI_API_KEY=${AI_API_KEY}
      - DOMAIN=${DOMAIN}
      - MAIL_API_KEY=${MAIL_API_KEY}
      - MAIL_TO=${MAIL_TO}
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
    networks:
      - weather_network

  db:
    image: postgres:latest
    container_name: postgres_db
    environment:
      POSTGRES_DB: weather_db
      POSTGRES_USER: your_user
      POSTGRES_PASSWORD: your_password
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - weather_network
    ports:
      - "5432:5432"

volumes:
  pgdata:

networks:
  weather_network:

```
