### Használt technológiák

A Pollák Csengő alkalmazás számos modern technológiát használ annak érdekében, hogy egy robusztus, skálázható és felhasználóbarát platformot biztosítson. Ezek a technológiák a következők:

- **WebStorm** és **Visual Studio Code** a fejlesztéshez.
- **Docker** és **Docker-compose** a konténerizációhoz és a konzisztens fejlesztési környezetekhez.
- **Pgadmin** az adatbázis kezeléséhez.
- **nginx** a frontend kiszolgálásához.
- **Postgres 16.6** a backend adatbázishoz.
- **NestJS** a backend keretrendszerhez.

### A szoftver célja

A Pollák Csengő egy úttörő megoldás, amely kifejezetten az oktatási környezet javítására készült, elősegítve a kényelmesebb és vonzóbb légkört a diákok számára. Ez az innovatív alkalmazás egy sokoldalú webes platformot kínál, amely elérhető mind mobil eszközökön, mind számítógépeken, biztosítva a széles körű használhatóságot.

A platform alapvető funkciója lehetővé teszi a diákok számára, hogy szavazzanak kedvenc dalaikra, végül meghatározva a "Hónap Csengőhangját". Ez a funkció dinamikus csengőhangok sorát vezeti be, amelyek az iskolai év során váltakoznak, napi szinten friss és élvezetes hallási élményt nyújtva a diákoknak.
    
A vidám és derűs légkör elősegítése mellett a Pollák Csengő egy könnyed és innovatív megközelítést kínál a diákok bevonására, pozitívan hozzájárulva általános jólétükhöz és napi iskolai életükhöz. Az alkalmazás zökkenőmentes integrációjával és felhasználóbarát felületével erősíti a közösségi érzést, miközben egy kis örömöt és újdonságot hoz az akadémiai környezetbe.

### Kinek és miért?

A Pollák Csengő alkalmazás elsősorban iskolák számára készült, különösen azoknak, akik szeretnék javítani diákjaik iskolai élményét egy pozitív és közösségközpontú légkör kialakításával. A rendszer lehetőséget biztosít a diákoknak, hogy aktívan részt vegyenek az iskola napi környezetének alakításában kedvenc dalaikra való szavazással, ami egy szórakoztató és interaktív elemet ad az iskolai naphoz.

### Kinek szól?

- **Iskolák**: Azoknak az iskoláknak, amelyek célja egy élénk és vonzó környezet előmozdítása, ahol a diákok jobban kapcsolódnak és részt vesznek az iskolai közösségben.
- **Diákok**: Hogy a diákoknak lehetőséget adjon az iskolai évük hangulatának meghatározására, napi rutinjuk élvezetesebbé tételére, és az iskola kultúrájában való részvétel és tulajdonérzet erősítésére.
- **Tanítók és személyzet**: Hogy dinamikusabb és vidámabb légkört teremtsenek az iskolában, hozzájárulva egy pozitív és támogató környezethez mind a tanulás, mind a társas interakciók terén.

### Fejlesztői környezet

A Pollák Csengő alkalmazás elkészítéséhez különböző fejlesztőeszközöket használunk, amelyek segítenek a fejlesztésben és az adatok kezelésében. A WebStorm és a Visual Studio Code könnyen használható kódszerkesztők, amelyek segítenek a weboldal kialakításában.

A Docker és a Docker-compose lehetővé teszik számunkra, hogy konténerizált környezetben fejlesszük és teszteljük weboldalunkat, így biztosítva a konzisztens fejlesztési és futtatási környezetet. Az nginx egy hatékony webszerver, amely a frontend kiszolgálására szolgál. A Pgadmin segítségével könnyedén kezelhetjük és karbantarthatjuk a PostgreSQL adatbázisunkat, amely a receptekhez, felhasználókhoz és egyéb adatokhoz kapcsolódó információkat tárolja és kezeli.

A Postgres 16.6 adatbázis-kezelő rendszer hatékonyan tárolja és kezeli a Pollák Csengő alkalmazás adatait, beleértve a szavazatokat, dalokat és felhasználói információkat. A NestJS keretrendszer segítségével pedig egy robusztus és skálázható backend rendszert építhetünk. Az npm-et használjuk a frontend és backend fejlesztés során a függőségek kezelésére.

A frontend fejlesztéséhez a Vue keretrendszert használjuk Vite-tal, amely gyors és hatékony fejlesztési élményt biztosít. A frontend stílusát HTML, CSS, Sass és Scss segítségével alakítjuk ki, biztosítva a modern és reszponzív dizájnt. A Jest és a Playwright segítségével teszteljük a frontend és backend rendszert, biztosítva az alkalmazás megbízhatóságát és hibamentességét.

Ezeket a fejlesztőeszközöket választottuk, mert tanultunk velük, és ismerjük őket. A széles körű elérhetőségük és az, hogy ingyenesen elérhetők, tovább erősíti döntésünket. Segítségükkel hatékonyan fejleszthetünk és tesztelhetünk weboldalunkat, és könnyedén kezelhetjük az adatbázisunkat, így biztosítva a Pollák Csengő alkalmazás zökkenőmentes működését és felhasználóbarát felületét.

### Docker Compose fájl dokumentáció

Ez a `docker-compose` fájl meghatározza a Pollák Csengő alkalmazás futtatásához szükséges szolgáltatásokat, hálózatokat és köteteket. Az alábbiakban részletes magyarázat található a fájl minden soráról.

#### Szolgáltatások

1. **csengo-v2-postgres**:
    - `container_name: csengo-v2-postgres`: Beállítja a konténer nevét `csengo-v2-postgres`-ra.
    - `image: postgres:16.6`: A PostgreSQL 16.6 verzióját használja.
    - `restart: always`: Biztosítja, hogy a konténer mindig újrainduljon, ha leáll.
    - `environment`: Környezeti változókat állít be a PostgreSQL konténerhez:
        - `POSTGRES_USER: csengo`: Beállítja a PostgreSQL felhasználót `csengo`-ra.
        - `POSTGRES_PASSWORD: csengo`: Beállítja a PostgreSQL jelszót `csengo`-ra.
        - `POSTGRES_DB: csengo`: Beállítja a PostgreSQL adatbázis nevét `csengo`-ra.
    - `volumes: - csengo-v2_db:/var/lib/postgresql/data`: Csatolja a `csengo-v2_db` kötetet a PostgreSQL adatainak megőrzéséhez.
    - `networks: - csengo-v2`: Csatlakoztatja a konténert a `csengo-v2` hálózathoz.

2. **csengo-ts-server-v2**:
    - `container_name: csengo-ts-server-v2`: Beállítja a konténer nevét `csengo-ts-server-v2`-ra.
    - `build`: A konténer felépítéséhez használt Dockerfile:
        - `context: ./csengo-ts-server-v2`: A build kontextus a `csengo-ts-server-v2` könyvtár.
        - `dockerfile: Dockerfile`: A Dockerfile elérési útja.
    - `image: csengo-ts-server-v2`: A konténer képének neve.
    - `restart: always`: Biztosítja, hogy a konténer mindig újrainduljon, ha leáll.
    - `volumes: - csengo-v2_sounds:/data`: Csatolja a `csengo-v2_sounds` kötetet a konténer `/data` könyvtárához.
    - `ports: - "3300:3300"`: A 3300-as portot a gazdagépen a 3300-as portra térképezi a konténerben.
    - `depends_on`: Meghatározza a szolgáltatás függőségeit:
        - `csengo-v2-postgres`
    - `networks: - csengo-v2`: Csatlakoztatja a konténert a `csengo-v2` hálózathoz.
    - `environment`: Környezeti változókat állít be a TypeScript szerverhez:
        - `PORT: 3300`: Beállítja a szerver portját 3300-ra.
        - `DATABASE_URL: "postgresql://csengo:csengo@csengo-v2-postgres:5432/csengo?schema=public"`: Beállítja az adatbázis kapcsolat URL-jét.
        - `UPLOAD_PATH: "./data/audio"`: Beállítja a hangfájlok feltöltési útvonalát.
        - `TOKEN_SECRET: "token-secret"`: Beállítja a token titkot az autentikációhoz.
        - `JWT_SECRET: "jwt-secret"`: Beállítja a JWT titkot az autentikációhoz.
        - `SESSION_STORE_PASSWORD: "session-store-password"`: Beállítja a jelszót a munkamenet tárolóhoz.
        - `SESSION_STORE_HOST: "csengo-v2-session-store"`: Beállítja a munkamenet tároló hosztját.
        - `SESSION_STORE_PORT: 6379`: Beállítja a munkamenet tároló portját.
        - `CORS_ORIGIN: "*"`: Beállítja a CORS eredetet.
        - `CORS_DOMAIN: "localhost"`: Beállítja a CORS domaint.
        - `DEV: true`: Beállítja a fejlesztési módot igazra.
        - `WS_API_KEY: "ws-api-key"`: Beállítja a WebSocket API kulcsot.

3. **csengo-ts-client-v2**:
    - `container_name: csengo-ts-client-v2`: Beállítja a konténer nevét `csengo-ts-client-v2`-ra.
    - `build`: A konténer felépítéséhez használt Dockerfile:
        - `context: ./csengo-ts-client-v2`: A build kontextus a `csengo-ts-client-v2` könyvtár.
        - `dockerfile: Dockerfile`: A Dockerfile elérési útja.
        - `target: prod`: A build célja a `prod`.
        - `args`: Build argumentumok:
            - `VITE_API_URL=http://localhost:3300`
            - `VITE_COOKIE_DOMAIN=localhost`
    - `image: csengo-ts-client-v2`: A konténer képének neve.
    - `ports: - "8080:80"`: A 8080-as portot a gazdagépen a 80-as portra térképezi a konténerben.
    - `networks: - csengo-v2`: Csatlakoztatja a konténert a `csengo-v2` hálózathoz.

4. **csengo-v2-pgadmin**:
    - `container_name: csengo-v2-pgadmin`: Beállítja a konténer nevét `csengo-v2-pgadmin`-ra.
    - `image: dpage/pgadmin4`: A pgAdmin 4 képét használja.
    - `restart: always`: Biztosítja, hogy a konténer mindig újrainduljon, ha leáll.
    - `ports: - "8081:80"`: A 8081-es portot a gazdagépen a 80-as portra térképezi a konténerben.
    - `environment`: Környezeti változókat állít be a pgAdmin-hoz:
        - `PGADMIN_DEFAULT_EMAIL: csengo@csengo.dev`: Beállítja az alapértelmezett email címet a pgAdmin-hoz.
        - `PGADMIN_DEFAULT_USERNAME: admin`: Beállítja az alapértelmezett felhasználónevet a pgAdmin-hoz.
        - `PGADMIN_DEFAULT_PASSWORD: admin`: Beállítja az alapértelmezett jelszót a pgAdmin-hoz.
        - `PGADMIN_CONFIG_WTF_CSRF_ENABLED: "False"`: Letiltja a CSRF védelmet.
    - `volumes: - csengo-v2_pgadmin:/var/lib/pgadmin`: Csatolja a `csengo-v2_pgadmin` kötetet a pgAdmin adatainak megőrzéséhez.
    - `networks: - csengo-v2`: Csatlakoztatja a konténert a `csengo-v2` hálózathoz.

#### Hálózatok

- `csengo-v2`: Meghatároz egy egyedi hálózatot `csengo-v2` néven, amelyen a szolgáltatások kommunikálhatnak egymással.

#### Kötetek

- `csengo-v2_db`: Meghatároz egy kötetet `csengo-v2_db` néven a PostgreSQL adatok megőrzéséhez.
- `csengo-v2_sounds`: Meghatároz egy kötetet `csengo-v2_sounds` néven a hangadatok megőrzéséhez.
- `csengo-v2_pgadmin`: Meghatároz egy kötetet `csengo-v2_pgadmin` néven a pgAdmin adatok megőrzéséhez.

#### Futtatás

Windows-on, telepítse a `Docker-compose`-t és a `Docker Desktop` alkalmazást, majd indítsa el a `Docker Desktop` alkalmazást.

Linux-on és macOS-en, telepítse a `Docker`-t és a `Docker-compose`-t, majd nyissa meg a terminált a `docker-compose` fájl mappájában.

Nyisson meg egy parancssort git repository törzs mappájában, ahol a `docker-compose.dev.v2.yml` nevű fájl található.

A `docker-compose` fájlban meghatározott szolgáltatásokat, hálózatokat és köteteket a következő paranccsal futtathatjuk:

```bash
docker-compose -f docker-compose.dev.v2.yml up -d
```

Ez a parancs elindítja a Pollák Csengő alkalmazást a meghatározott szolgáltatásokkal, hálózatokkal és kötetekkel. A `-d` kapcsolóval a konténerek háttérben futnak, és a parancs végrehajtása után visszatér a parancssorhoz.

A Pollák Csengő alkalmazás futtatása után a következő URL-eken érhető el:
- pgAdmin adatbázis kezelő: `http://localhost:8081`
- Csengő szerver: `http://localhost:3300`
- Csengő weboldal: `http://localhost:8080`

Ezekkel a lépésekkel sikeresen futtathatja a Pollák Csengő alkalmazást a Docker segítségével, és hozzáférhet a szolgáltatásokhoz a megadott URL-eken.

### Adatbázis kezelő

Az adatbázis kezelőhöz bejelentkezéshez használja az alábbi adatokat:
- Email: `csengo@csengo.dev`
- Felhasználónév: `admin`
- Jelszó: `admin`

![pgadmin-login](./fejlesztoikepek/pgadmin-login.png)

Az pgAdmin adatbázis kezelőn belül a kövekező módon tudunk kapcsolódni az adatbázishoz:

![pgadmin-connection](./fejlesztoikepek/pgadmin-create-server-connection.png)

A következő adatokat kell megadni a kapcsolódás elnevezéséhez a következő módon:

- Name: `csengo-v2-postgres`

![pgadmin-connection-details](./fejlesztoikepek/pgadmin-create-server-connection-popup-name.png)

A következő adatokat kell megadni a kapcsolódáshoz a következő módon:

- Host name/address: `csengo-v2-postgres`
- Port: `5432`
- Maintenance database: `postgres`
- Username: `csengo`
- Password: `csengo`
- Save password: `True`

![pgadmin-connection-details](./fejlesztoikepek/pgadmin-create-server-connection-popup-connection.png)

A következő módon lehet az adatbázisban tárolt táblákat megtekinteni:

![pgadmin-tables](./fejlesztoikepek/pgadmin-list-tables.png)

