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

# Fejlesztői dokumentáció

## Konkurenciák

A Pollák Csengő alkalmazás egyik vetélytársa a [Bella-Iskolacsengő](https://www.bella-iskolacsengo.hu/), amely egy hasonló szolgáltatást nyújt az iskolák számára. A Bella-Iskolacsengő egy online platform, amely lehetővé teszi az iskolák számára, hogy saját csengőhangot válasszanak, és a diákok számára lehetőséget biztosítanak a szavazásra. Az alkalmazás egyedi és személyre szabott csengőhangokat kínál, amelyeket a diákok kedvenc dalai alapján választhatnak ki. A Bella-Iskolacsengő egy modern és interaktív megoldás, amely segíti az iskolákat a diákok bevonásában és a közösségi élmény erősítésében.

A Bella-Iskolacsengő alkalmazás egy előnnyel rendelkezik, az egyedi csengőhangok és a személyre szabott választások lehetőségével. Az alkalmazás felhasználóbarát felülettel rendelkezik, amely egyszerű és intuitív használatot biztosít a diákok és az iskolai személyzet számára.

A Pollák Csengő alkalmazás és a Bella-Iskolacsengő közötti különbség az, hogy a Pollák Csengő egy dinamikus és interaktív platformot kínál, amely lehetővé teszi a diákok számára, hogy szavazzanak kedvenc dalaikra, és meghatározzák a "Hónap Csengőhangját". Az alkalmazás egyedi és változatos csengőhangokat kínál, amelyek napi szinten friss és élvezetes hallási élményt nyújtanak a diákoknak.

Egy másik vetélytárs a [Gipen Iskolacsengő](https://iskolacsengo.gipen.hu/) mely kevesebb funkcionalitást nyújt mint a Pollák Csengő. Az Iskolacsengő egy modern és minimalista megoldás, amely lehetővé teszi az iskolák számára, hogy saját csengőhangot válasszanak, és a diákok számára lehetőséget biztosítanak a szavazásra. Az alkalmazás egyszerű és letisztult felülettel rendelkezik, amely gyors és hatékony használatot biztosít a diákok és az iskolai személyzet számára.

Más vetélytárs a térben hasonló funkcionalitással, mint alkalmazásunk, jelenleg a piacon nem elérhető. Ez miatt a Pollák Csengő egyedi és innovatív megoldásnak számít, amely különleges és élvezetes hallási élményt nyújt a diákoknak.

## Fejlesztői környezet

A Pollák Csengő alkalmazás fejlesztéséhez különböző fejlesztőeszközöket használunk, amelyek segítenek a fejlesztésben és az adatok kezelésében.

- **WebStorm** mely a JetBrains által fejlesztett, mély integrációjáról ismert a JavaScript keretrendszerekkel, intelligens kódkiegészítéssel és robusztus hibakeresési képességekkel. Kiválóan alkalmas összetett projektekhez, különösen azokhoz, amelyek TypeScript-et és modern JavaScript keretrendszereket, mint például a React, Angular és Vue használnak. Beépített eszközei a verziókezeléshez, teszteléshez és refaktoráláshoz átfogó IDE-vé teszik. Versenytársaihoz, mint például a Sublime Text, képest a WebStorm fejlettebb funkciókat és jobb integrációt kínál a fejlesztési munkafolyamatokkal, bár magasabb költséggel jár.

- **Visual Studio Code** (VS Code) egy ingyenes, nyílt forráskódú kódszerkesztő, amely sokoldalúsága és kiterjedt bővítmény-ökoszisztémája miatt nagy népszerűségre tett szert. Számos programozási nyelvet és keretrendszert támogat, így sok fejlesztő kedvenc választása. A VS Code könnyű természete, valamint olyan erőteljes funkciók, mint az IntelliSense, beépített Git támogatás és beépített terminál, rendkívül hatékony fejlesztési környezetet biztosítanak. Az Atomhoz, egy másik népszerű szerkesztőhöz képest a VS Code gyorsabb teljesítményt és aktívabb közösséget kínál, ami gazdagabb bővítménykészletet és gyakori frissítéseket eredményez.

- **Docker** és **Docker-compose** a konténerizációhoz és a konzisztens fejlesztési környezetekhez: A Docker lehetővé teszi az alkalmazások konténerizálását, ami biztosítja a fejlesztési és futtatási környezetek konzisztenciáját. A Docker-compose segítségével egyszerűen definiálhatjuk és kezelhetjük a többkonténeres alkalmazásokat. Versenytársai, mint például a Vagrant, nem nyújtanak olyan könnyű és gyors konténerizációs megoldást, mint a Docker.

- **Pgadmin** az adatbázis kezeléséhez: A Pgadmin egy erőteljes és felhasználóbarát eszköz a PostgreSQL adatbázisok kezeléséhez. Lehetővé teszi az adatbázisok egyszerű adminisztrációját és karbantartását. Versenytársai, mint például a DBeaver, szintén jó alternatívák, de a Pgadmin kifejezetten a PostgreSQL-re optimalizált, ami előnyt jelent a specifikus funkciók és teljesítmény szempontjából.

- **nginx** a frontend kiszolgálásához: Az nginx egy nagy teljesítményű és könnyen konfigurálható webszerver, amely kiválóan alkalmas a statikus fájlok kiszolgálására és a terheléselosztásra. Versenytársai, mint például az Apache, szintén népszerűek, de az nginx alacsonyabb erőforrásigénye és nagyobb teljesítménye miatt előnyösebb választás a modern webalkalmazások számára.

- **Postgres 16.6** a backend adatbázishoz: A PostgreSQL egy nyílt forráskódú, robusztus és skálázható adatbázis-kezelő rendszer, amely számos fejlett funkcióval rendelkezik, mint például a tranzakciókezelés és a replikáció. Versenytársai, mint például a MySQL, szintén népszerűek, de a PostgreSQL fejlettebb funkciói és rugalmassága miatt gyakran előnyösebb választás a komplex alkalmazások számára.

## Felhasznált technológiák

A Pollák Csengő alkalmazásban hasznosított technológiák és eszközök a következők:

- **TypeScript**: A TypeScript egy statikusan típusos JavaScript kiterjesztés, amely opcionális statikus típusokat ad a nyelvhez. Segít a fejlesztőknek korán észlelni a hibákat a típusellenőrzés révén, és javítja a kód karbantarthatóságát és olvashatóságát. A JavaScripthez képest a TypeScript jobb eszköztámogatást és skálázhatóságot kínál nagy kódbázisokhoz. Modern keretrendszerekkel, mint az Angular és a React való integrációja miatt előnyös választás mind a frontend, mind a backend fejlesztéshez.

- **HTML**: A HTML (HyperText Markup Language) a weboldalak létrehozásának szabványos jelölőnyelve. Strukturálja a webes tartalmat, és elengedhetetlen bármilyen webalkalmazás építéséhez. Más jelölőnyelvekhez képest a HTML-t minden böngésző támogatja, és hatalmas eszköz- és erőforrás-ökoszisztémával rendelkezik, ami nélkülözhetetlenné teszi a frontend fejlesztéshez.

- **CSS**: A CSS (Cascading Style Sheets) a weboldalak stílusának és elrendezésének meghatározására szolgál. Lehetővé teszi a fejlesztők számára, hogy elválasszák a tartalmat a dizájntól, megkönnyítve ezzel a weboldal megjelenésének és érzésének karbantartását és frissítését. Az inline stílusokhoz vagy JavaScript-alapú stílusmegoldásokhoz képest a CSS hatékonyabb és skálázhatóbb módot kínál a stílusok kezelésére nagy projektek esetén.

- **Sass**: A Sass (Syntactically Awesome Style Sheets) egy előfeldolgozó szkriptnyelv, amelyet CSS-re fordítanak vagy értelmeznek. Kiterjeszti a CSS-t olyan funkciókkal, mint a változók, beágyazott szabályok és mixinek, így a stíluslap karbantarthatóbb és újrahasználhatóbb lesz. A sima CSS-hez képest a Sass erősebb és rugalmasabb szintaxist kínál, amely jelentősen felgyorsíthatja a fejlesztési folyamatot.

- **SCSS**: Az SCSS (Sassy CSS) a Sass egy szintaxisa, amely teljesen kompatibilis a CSS-sel. Kombinálja a Sass erejét a CSS ismerős szintaxisával, lehetővé téve a fejlesztők számára, hogy a Sass összes funkcióját használják, miközben CSS-szerű szintaxisban írnak. Más CSS előfeldolgozókhoz képest az SCSS zökkenőmentesebb átmenetet kínál a CSS-t már ismerő fejlesztők számára.

- **SQL**: Az SQL (Structured Query Language) a relációs adatbázisok kezelésének és manipulálásának szabványos nyelve. Lehetővé teszi a fejlesztők számára, hogy különféle műveleteket hajtsanak végre, például lekérdezéseket, frissítéseket és adatkezelést. A NoSQL adatbázisokhoz képest az SQL adatbázisok erős konzisztenciát és összetett lekérdezések támogatását biztosítják, így alkalmasak megbízható tranzakciókat és adatintegritást igénylő alkalmazásokhoz.

- **NestJS** a backend keretrendszerhez: A NestJS egy progresszív Node.js keretrendszer, amely a TypeScript nyelvet használja, és moduláris architektúrát kínál. Lehetővé teszi a skálázható és könnyen karbantartható backend alkalmazások fejlesztését. Versenytársai, mint például az Express.js, szintén népszerűek, de a NestJS strukturáltabb megközelítése és beépített támogatása a modern fejlesztési mintákhoz (mint például a Dependency Injection) miatt előnyösebb választás lehet.

- **Jest**: A Jest egy JavaScript tesztelési keretrendszer, amelyet a Facebook tart fenn, és amely a JavaScript kódbázisok helyességének biztosítására szolgál. Kiváló fejlesztői élményt nyújt olyan funkciókkal, mint a pillanatkép-tesztelés, egy erőteljes mock könyvtár és beépített kódlefedettségi jelentések. Más tesztelési keretrendszerekhez, például a Mocha vagy a Jasmine-hez képest a Jest integráltabb és felhasználóbarátabb élményt kínál, különösen a React alkalmazások esetében.

- **Vue**: A Vue.js egy progresszív JavaScript keretrendszer felhasználói felületek építéséhez. Úgy tervezték, hogy fokozatosan bevezethető legyen, ami azt jelenti, hogy annyit vagy keveset használhat a Vue-ból, amennyire szüksége van. A Vue reaktivitási rendszere és komponens alapú architektúrája megkönnyíti az összetett alkalmazások építését. Az olyan keretrendszerekhez képest, mint az Angular vagy a React, a Vue egyszerűbb és rugalmasabb API-t kínál, amely könnyebben megtanulható és integrálható a meglévő projektekbe.

- **Pinia**: A Pinia egy állapotkezelő könyvtár a Vue.js számára, amelyet a Vuex helyettesítésére terveztek. Egyszerűbb és intuitívabb API-t kínál, megkönnyítve és hatékonyabbá téve az állapotkezelést. A Vuex-hez képest a Pinia jobb TypeScript támogatást és modulárisabb architektúrát biztosít, ami tisztább és karbantarthatóbb kódot eredményezhet.

- **Vuetify**: A Vuetify egy Material Design komponens keretrendszer a Vue.js számára. Széles körű előre tervezett komponenseket biztosít, amelyek követik a Google Material Design irányelveit, megkönnyítve a vizuálisan vonzó és konzisztens felhasználói felületek létrehozását. Más UI keretrendszerekhez, például a Bootstrap vagy a Bulma-hoz képest a Vuetify mélyebb integrációt kínál a Vue-val és átfogóbb komponenskészletet.

- **Playwright**: A Playwright egy végponttól végpontig terjedő tesztelési keretrendszer, amelyet a Microsoft fejlesztett ki. Lehetővé teszi a fejlesztők számára, hogy olyan teszteket írjanak, amelyek szimulálják a felhasználói interakciókat a webalkalmazásokkal, biztosítva, hogy az alkalmazás a vártnak megfelelően viselkedjen. A Seleniumhoz képest a Playwright jobb teljesítményt, megbízhatóbb automatizálást és támogatást kínál a modern webes funkciókhoz, mint például a WebSockets és a szolgáltatási munkavállalók.

- **Vite**: A Vite egy új generációs frontend build eszköz, amely gyors és optimalizált fejlesztési élményeket kínál. Natív ES modulokat és modern böngészőfunkciókat használ, hogy azonnali hot module replacement-et és villámgyors build-eket biztosítson. A hagyományos bundlerekhez, például a Webpack-hoz képest a Vite jelentősen gyorsabb fejlesztési és build időket kínál, így ideális a modern webfejlesztéshez.

- **Prisma**: A Prisma egy nyílt forráskódú ORM (Object-Relational Mapping) eszköz a Node.js és a TypeScript számára. Egyszerűsíti az adatbázis-hozzáférést és -kezelést egy típusbiztos lekérdező építővel és egy intuitív adatmodellezési nyelvvel. A hagyományos ORM-ekhez, például a Sequelize-hez képest a Prisma jobb TypeScript támogatást, automatikus migrációkat és modernebb API-t kínál, megkönnyítve ezzel az adatbázisok típusbiztos módon történő kezelését.

- **MDI icons**: A Material Design Icons (MDI) egy átfogó ikonkönyvtár, amely a Google Material Design irányelveit követve készült. Széles körű, kiváló minőségű ikonokat biztosít, amelyek könnyen integrálhatók a webalkalmazásokba. Más ikonkönyvtárakhoz, például a Font Awesome-hoz képest az MDI konzisztens és vizuálisan vonzóbb ikonokat kínál, amelyek megfelelnek a modern tervezési elveknek.

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

#### Futtatás manuális teszteléshez

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

#### Adatbázis kezelő

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

#### Portainer-en keresztüli konténer kezelés

A Portainer egy könnyen használható, webes felülettel rendelkező konténerkezelő eszköz, amely lehetővé teszi a konténerek kezelését, figyelését és felügyeletét. A Portainer segítségével egyszerűen létrehozhat, indíthat, leállíthat és törölhet konténereket, valamint ellenőrizheti a konténerek állapotát és naplóit.

Ez a dokumentáció feltételezi, hogy egy Portainer példány fut a localhost:9000 címen.

1. Nyissa meg a böngészőt, és navigáljon a http://localhost:9000 címre.
2. Jelentkezzen be a Portainerbe a felhasználónév és jelszó megadásával.
3. Az ábra alapján válassza ki a számára megfelelő Docker környezetet.

![portainer-login](./fejlesztoikepek/portainer-environments.png)

4. Készítsen elő egy új Stack-et a Stacks fül alatt, majd másolja bele a docker-compose.dev.v2.yml fájl tartalmát. Valamint adja hozzá a megfelelő fájlokat, hogy a konténerek le tudjanak épülni.

![portainer-stacks](./fejlesztoikepek/portainer-create-stack.png)

5. Sikeres stack létrehozása után a konténerek automatikusan elindulnak, és a Portainer segítségével kezelheti őket.

![portainer-success](./fejlesztoikepek/portainer-successful-deploy.png)

#### Futtatás fejlesztői módban

A Pollák Csengő alkalmazás fejlesztői módban való futtatásához a következő lépéseket kell követni:

0. Telepítse a Docker Desktop nevű alkalmzást és a Docker-compose nevű alkalmazást a számítógépére, majd indítsa el a Docker Desktop alkalmazást.

##### Backend elindítása Docker segítségével

1. Nyissa meg a terminált a `csengo-ts-server-v2` mappában.
2. Windows operációs rendszeren futtassa a következő parancsokat a szerver indításához:

```bash
docker-compose -f docker-compose.dev.yml up csengo-v2-postgres-dev -d
copy .env.example .env
npm install
npm run prisma:update:prod
npm run start:dev
```

3. Amennyiben szükséges, változtassa meg a `.env` fájlban a megfelelő környezeti változókat, majd állítsa le a szervert a terminálban a `CTRL+C` billenyűkombinációval ezután indítsa újra a szervert a következő paranccsal:

```bash
npm run start:dev
```

4. A szerver elindítása után a következő URL-eken érhető el:
   - Swagger dokumentáció: [http://localhost:3300/swagger](http://localhost:3300/swagger)
   - REST API: [http://localhost:3300/api](http://localhost:3300/api)

##### Frontend elindítása

1. Nyissa meg a terminált a `csengo-ts-client-v2` mappában.
2. Windows operációs rendszeren futtassa a következő parancsokat a kliens indításához:

```bash
copy .env.example .env
npm install
npm run dev
```

3. Amennyiben szükséges, változtassa meg a `.env` fájlban a megfelelő környezeti változókat, majd állítsa le a klienst a terminálban a `CTRL+C` billenyűkombinációval ezután indítsa újra a klienst a következő paranccsal:

```bash
npm run dev
```

4. A kliens elindítása után a következő URL-eken érhető el:
   - Weboldal: [http://localhost:3000](http://localhost:3000)

## Strukturális felépítés

### Frontend felépítése

A Pollák Csengő frontend alkalmazásának metodológiája a következő: minden komponens egyedi felelősségű, és egyedi funkcionalitással rendelkezik. A komponensek egymásra épülnek, és a kisebb komponensek nagyobb komponensekbe vannak beágyazva. A komponensek egymással kommunikálnak a Pinia állapotkezelő segítségével, valamint egy egyedi event busz használatával, és a komponensek közötti navigáció a Vue Router segítségével történik. Minden lekérdezés egy Pinia store-ban történik, hogy a komponensek egyszerű és konzisztens állapotot tarthassanak. A komponensek a Vuetify keretrendszer segítségével vannak stilizálva, és a Vite build eszköz segítségével kerülnek összeállításra.
A frontend strukturális felépítése a következő:

- **.github**
   - *workflows*: Tartalmazza a GitHub Actions munkafolyamatokat.
      - *ci.yml*: A folyamatos integrációs munkafolyamat konfigurációja.

- **.idea**
   - *codeStyles*: Kódstílus beállítások.
      - *codeStyleConfig.xml*: Kódstílus konfiguráció.
      - *Project.xml*: Projekt szintű kódstílus beállítások.
   - *inspectionProfiles*: Ellenőrzési profilok.
      - *Project_Default.xml*: Alapértelmezett ellenőrzési profil.
   - *runConfigurations*: Futtatási konfigurációk.
      - *All_Tests.xml*: Összes teszt futtatási konfigurációja.
      - *dev.xml*: Fejlesztési futtatási konfiguráció.
   - *csengo-ts-client-v2.iml*: Projekt fájl.
   - *discord.xml*: Discord integrációs beállítások.
   - *git_toolbox_blame.xml*: Git blame eszköz beállításai.
   - *git_toolbox_prj.xml*: Git projekt eszköz beállításai.
   - *modules.xml*: Modulok konfigurációja.
   - *vcs.xml*: Verziókezelő rendszer beállításai.
   - *watcherTasks.xml*: Felügyeleti feladatok beállításai.

- **.vscode**
   - *extensions.json*: Ajánlott kiterjesztések listája.
   - *settings.json*: VSCode beállítások.

- **config**
   - *nginx.conf*: Nginx konfigurációs fájl.

- **public**
   - *favicon.ico*: Weboldal ikon fájl.

- **src**
   - *App.vue*: Az alkalmazás fő komponense.
   - *auto-imports.d.ts*: Automatikus importok típusdefiníciói.
   - *components.d.ts*: Komponensek típusdefiníciói.
   - *main.ts*: Az alkalmazás belépési pontja.
   - *typed-router.d.ts*: Típusdefiníciók a routerhez.
   - **assets**: Statikus fájlok és képek.
      - *asd2.jpg*: Háttérkép.
      - *pollakLogo.png*: Logó kép.
      - *logo.png*: Logó kép.
      - *logo.svg*: Logó SVG formátumban.
   - **components**: Az alkalmazás különböző komponensei.
      - *LoginCard.vue*: Bejelentkezési kártya komponens.
      - *README.md*: Komponensek dokumentációja.
      - *RegisterCard.vue*: Regisztrációs kártya komponens.
      - **admin**: Adminisztrációs felület komponensei.
         - *Download.vue*: Letöltési komponens.
         - **pending-song**: Függő zenék kezelése.
            - *PendingSong.vue*: Függő zene komponens.
            - *PendingSongList.vue*: Függő zenék listája.
         - **session**: Szavazási szekciók kezelése.
            - *CreateSessionPopup.vue*: Szavazási szekció létrehozása.
            - *Session.vue*: Szavazási szekció komponens.
            - *SessionList.vue*: Szavazási szekciók listája.
            - *UpdateSessionPopup.vue*: Szavazási szekció frissítése.
            - *ViewSessionSongsPopup.vue*: Szavazási szekció zenéinek megtekintése.
         - **song**: Zenék kezelése.
            - *CreateSongPopup.vue*: Zene létrehozása.
            - *Song.vue*: Zene komponens.
            - *SongList.vue*: Zenék listája.
            - *UpdateSongPopup.vue*: Zene frissítése.
         - **user**: Felhasználók kezelése.
            - *UpdateUserPopup.vue*: Felhasználó frissítése.
            - *User.vue*: Felhasználó komponens.
            - *UserList.vue*: Felhasználók listája.
      - **common**: Közös komponensek.
         - *Toast.vue*: Értesítési komponens.
      - **dashboard**: Felhasználói irányítópult komponensei.
         - *WelcomeSign.vue*: Üdvözlő jelzés.
         - **left-card**: Bal oldali kártya komponensei.
            - *LeftLandingCard.vue*: Bal oldali kártya fő komponense.
            - *SongUpload.vue*: Zene feltöltése.
            - *SongVote.vue*: Zene szavazás.
            - *SongVoteList.vue*: Szavazási zenék listája.
            - *UploadInput.vue*: Feltöltési bemenet.
         - **right-card**: Jobb oldali kártya komponensei.
            - *PreviousWinner.vue*: Előző nyertes.
            - *RightLandingCard.vue*: Jobb oldali kártya fő komponense.
            - *SongSelectionList.vue*: Zene kiválasztási lista.
            - **song-selection**: Zene kiválasztási komponensek.
               - *PlaySong.vue*: Zene lejátszása.
               - *SongSelection.vue*: Zene kiválasztása.
               - *VoteSong.vue*: Zene szavazása.
      - **__tests__**: Teszt komponensek.
         - *HelloWorld.spec.ts*: HelloWorld komponens tesztje.
         - *LoginCard.spec.ts*: LoginCard komponens tesztje.
   - **layouts**: Oldal elrendezések.
      - *auth.vue*: Hitelesítési elrendezés.
      - *default.vue*: Alapértelmezett elrendezés.
      - *landing.vue*: Kezdőoldal elrendezés.
      - *logged-in.vue*: Bejelentkezett felhasználói elrendezés.
      - *README.md*: Elrendezések dokumentációja.
      - *user.vue*: Felhasználói elrendezés.
   - **pages**: Oldalak.
      - *forbidden.vue*: Tiltott oldal.
      - *index.vue*: Főoldal.
      - *login.vue*: Bejelentkezési oldal.
      - *README.md*: Oldalak dokumentációja.
      - *register.vue*: Regisztrációs oldal.
      - *required-pages-components.md*: Szükséges oldalak és komponensek listája.
      - *test.vue*: Teszt oldal.
      - *tv.vue*: TV oldal.
      - *[...slug].vue*: Dinamikus útvonalak kezelése.
      - **admin**: Adminisztrációs oldalak.
         - *index.vue*: Adminisztrációs főoldal.
   - **plugins**: Bővítmények.
      - *index.ts*: Bővítmények regisztrálása.
      - *README.md*: Bővítmények dokumentációja.
      - *vuetify.ts*: Vuetify bővítmény konfiguráció.
   - **router**: Útvonalak kezelése.
      - *index.ts*: Útvonalak konfigurációja.
   - **stores**: Állapotkezelők.
      - *index.ts*: Állapotkezelők regisztrálása.
      - *README.md*: Állapotkezelők dokumentációja.
      - *tv.ts*: TV állapotkezelő.
      - **admin**: Adminisztrációs állapotkezelők.
         - **pending-song**: Függő zenék állapotkezelői.
            - *pendingSong.ts*: Függő zene állapotkezelő.
            - *pendingSongList.ts*: Függő zenék listájának állapotkezelője.
         - **session**: Szavazási szekciók állapotkezelői.
            - *createSessionPopup.ts*: Szavazási szekció létrehozása állapotkezelő.
            - *session.ts*: Szavazási szekció állapotkezelő.
            - *sessionList.ts*: Szavazási szekciók listájának állapotkezelője.
            - *updateSessionPopup.ts*: Szavazási szekció frissítése állapotkezelő.
         - **song**: Zenék állapotkezelői.
            - *createSongPopup.ts*: Zene létrehozása állapotkezelő.
            - *song.ts*: Zene állapotkezelő.
            - *songList.ts*: Zenék listájának állapotkezelője.
            - *updateSongPopup.ts*: Zene frissítése állapotkezelő.
         - **user**: Felhasználók állapotkezelői.
            - *updateUserPopup.ts*: Felhasználó frissítése állapotkezelő.
            - *user.ts*: Felhasználó állapotkezelő.
         - *download.ts*: Letöltés állapotkezelő.
      - **dashboard**: Felhasználói irányítópult állapotkezelői.
         - *welcomeSign.ts*: Üdvözlő jelzés állapotkezelő.
         - **left-card**: Bal oldali kártya állapotkezelői.
            - *songVoteList.ts*: Szavazási zenék listájának állapotkezelője.
            - *uploadInput.ts*: Feltöltési bemenet állapotkezelő.
         - **right-card**: Jobb oldali kártya állapotkezelői.
            - *previousWinner.ts*: Előző nyertes állapotkezelő.
            - *songSelectionList.ts*: Zene kiválasztási lista állapotkezelő.
            - **song-selection**: Zene kiválasztási állapotkezelők.
               - *playSong.ts*: Zene lejátszása állapotkezelő.
               - *voteSong.ts*: Zene szavazása állapotkezelő.
   - **styles**: Stílusok.
      - *login.scss*: Bejelentkezési oldal stílusai.
      - *README.md*: Stílusok dokumentációja.
      - *register.scss*: Regisztrációs oldal stílusai.
      - *settings.scss*: Beállítások stílusai.
   - **types**: Típusdefiníciók.
      - *jwt.d.ts*: JWT típusdefiníciók.
      - *role.enum.d.ts*: Szerepkörök típusdefiníciói.
      - *session.ts*: Szavazási szekció típusdefiníciók.
      - *toast.enum.ts*: Értesítési típusok.
   - **utils**: Segédfüggvények.
      - *eventBus.util.ts*: Eseménybusz segédfüggvény.
      - *logger.custom.util.ts*: Egyedi naplózó segédfüggvény.

- **tests**
   - *admin.spec.ts*: Adminisztrációs tesztek.
   - *demo-todo-app.spec.demo.ts*: Demo todo alkalmazás tesztje.
   - *example.spec.ts*: Példa teszt.
   - *forbidden.spec.ts*: Tiltott oldal tesztje.
   - *index.spec.ts*: Főoldal tesztje.
   - *login.spec.ts*: Bejelentkezési oldal tesztje.
   - *register.spec.ts*: Regisztrációs oldal tesztje.
   - *tsconfig.json*: Teszt konfiguráció.

- *.browserslistrc*: A böngészők támogatásának konfigurációs fájlja.
- *.dockerignore*: A Docker által figyelmen kívül hagyandó fájlok listája.
- *.editorconfig*: Kódformázási szabályok különböző szerkesztők és IDE-k számára.
- *.env copy.example*: Példa környezeti változók fájlra.
- *.eslintrc-auto-import.json*: ESLint konfigurációs fájl automatikus importáláshoz.
- *.gitignore*: A Git által figyelmen kívül hagyandó fájlok listája.
- *.prettierrc*: Prettier kódformázó eszköz konfigurációs fájlja.
- *docker-compose.dev.yml*: Docker Compose konfiguráció fejlesztési környezethez.
- *docker-compose.release.yml*: Docker Compose konfiguráció kiadási környezethez.
- *Dockerfile*: Docker kép építéséhez szükséges utasításokat tartalmazó fájl.
- *env.d.ts*: TypeScript típusdefiníciók környezeti változókhoz.
- *eslint.config.js*: ESLint konfigurációs fájl.
- *flake.lock*: Nix flake zárolási fájl.
- *flake.nix*: Nix flake konfigurációs fájl.
- *index.html*: Az alkalmazás belépési pontja HTML formátumban.
- *kerdesek.md*: Kérdéseket tartalmazó Markdown fájl.
- *package-lock.json*: A projekt függőségeinek pontos verzióit rögzítő fájl.
- *package.json*: A projekt függőségeit és szkripteket tartalmazó fájl.
- *playwright.config.ts*: Playwright tesztelési keretrendszer konfigurációs fájlja.
- *README.md*: A projekt leírását és használati útmutatóját tartalmazó fájl.
- *sonar-project.properties*: SonarQube projekt konfigurációs fájl.
- *tsconfig.app.json*: TypeScript konfigurációs fájl az alkalmazás számára.
- *tsconfig.json*: A TypeScript projekt alapértelmezett konfigurációs fájlja.
- *tsconfig.node.json*: TypeScript konfigurációs fájl Node.js projektekhez.
- *tsconfig.vitest.json*: TypeScript konfigurációs fájl Vitest tesztelési keretrendszerhez.
- *vite.config.mts*: Vite konfigurációs fájl.

#### Frontend Tesztelés

A frontend tesztelési folyamatok a következők:

##### `admin.spec.ts`

- **should display the admin page**: Ellenőrzi, hogy az admin oldal megjelenik-e.
- **should display home button**: Ellenőrzi, hogy a kezdőlap gomb megjelenik-e.
- **should display dropdown menu**: Ellenőrzi, hogy a legördülő menü megjelenik-e.
- **should display logout option when dropdown menu is pressed**: Ellenőrzi, hogy a kijelentkezés opció megjelenik-e, ha a legördülő menüt megnyomják.
- **should go to pending song when pending song is pressed**: Ellenőrzi, hogy a függőben lévő zenék oldalra navigál-e a felhasználó, ha a megfelelő gombot megnyomják.
- **should go to votes when votes is pressed**: Ellenőrzi, hogy a szavazások oldalra navigál-e a felhasználó, ha a megfelelő gombot megnyomják.
- **should go to miscellaneous when miscellaneous is pressed**: Ellenőrzi, hogy az egyebek oldalra navigál-e a felhasználó, ha a megfelelő gombot megnyomják.
- **should display no data on song page when no data is present**: Ellenőrzi, hogy a zenék oldalon nincs adat megjelenik-e, ha nincs adat.
- **should display no data on pending song page when no data is present**: Ellenőrzi, hogy a függőben lévő zenék oldalon nincs adat megjelenik-e, ha nincs adat.
- **should display no data on votes page when no data is present**: Ellenőrzi, hogy a szavazások oldalon nincs adat megjelenik-e, ha nincs adat.
- **should display correct data on song page when its present**: Ellenőrzi, hogy a zenék oldalon helyesen jelenik-e meg az adat, ha van adat.
- **should starting playing audio on song page when play button is pressed**: Ellenőrzi, hogy a zenék oldalon elindul-e a lejátszás, ha a lejátszás gombot megnyomják.
- **should stop playing audio on song page when play button is pressed twice**: Ellenőrzi, hogy a zenék oldalon leáll-e a lejátszás, ha a lejátszás gombot kétszer megnyomják.
- **should upload new song on song page when upload button is pressed**: Ellenőrzi, hogy a zenék oldalon feltölthető-e egy új zene, ha a feltöltés gombot megnyomják.
- **should rename song on song page when rename button is pressed**: Ellenőrzi, hogy a zenék oldalon átnevezhető-e egy zene, ha az átnevezés gombot megnyomják.
- **should delete song on song page when delete button is pressed**: Ellenőrzi, hogy a zenék oldalon törölhető-e egy zene, ha a törlés gombot megnyomják.
- **should go to pending song page when pending song button is pressed**: Ellenőrzi, hogy a függőben lévő zenék oldalra navigál-e a felhasználó, ha a megfelelő gombot megnyomják.
- **should display correct data on pending song page when its present**: Ellenőrzi, hogy a függőben lévő zenék oldalon helyesen jelenik-e meg az adat, ha van adat.
- **should play audio on pending song page when play button is pressed**: Ellenőrzi, hogy a függőben lévő zenék oldalon elindul-e a lejátszás, ha a lejátszás gombot megnyomják.
- **should stop playing audio on pending song page when play button is pressed twice**: Ellenőrzi, hogy a függőben lévő zenék oldalon leáll-e a lejátszás, ha a lejátszás gombot kétszer megnyomják.
- **should approve song on pending song page when approve button is pressed**: Ellenőrzi, hogy a függőben lévő zenék oldalon engedélyezhető-e egy zene, ha az engedélyezés gombot megnyomják.
- **should disapprove song on pending song page when disapprove button is pressed**: Ellenőrzi, hogy a függőben lévő zenék oldalon elutasítható-e egy zene, ha az elutasítás gombot megnyomják.
- **should go to votes page when votes button is pressed**: Ellenőrzi, hogy a szavazások oldalra navigál-e a felhasználó, ha a megfelelő gombot megnyomják.
- **should display correct data on votes page when its present**: Ellenőrzi, hogy a szavazások oldalon helyesen jelenik-e meg az adat, ha van adat.
- **should display all part taking songs when view button is pressed**: Ellenőrzi, hogy a szavazások oldalon megjelenik-e az összes résztvevő zene, ha a megtekintés gombot megnyomják.
- **should edit all data when edit button is pressed**: Ellenőrzi, hogy a szavazások oldalon szerkeszthető-e az összes adat, ha a szerkesztés gombot megnyomják.
- **should delete voting session on votes page when delete button is pressed**: Ellenőrzi, hogy a szavazások oldalon törölhető-e egy szavazási szakasz, ha a törlés gombot megnyomják.
- **should create new voting session on votes page when create button is pressed**: Ellenőrzi, hogy a szavazások oldalon létrehozható-e egy új szavazási szakasz, ha a létrehozás gombot megnyomják.
- **should go to users page when users button is pressed**: Ellenőrzi, hogy a felhasználó a felhasználók oldalra navigál-e, ha a megfelelő gombot megnyomja.
- **should display correct data on users page when its present**: Ellenőrzi, hogy a felhasználók oldalon helyesen jelenik-e meg az adat, ha van adat.
- **should edit user's password on users page when edit button is pressed and only password is filled**: Ellenőrzi, hogy a felhasználók oldalon szerkeszthető-e a felhasználó jelszava, ha csak a jelszó mezőt töltik ki és a szerkesztés gombot megnyomják.
- **should edit user's role on users page when edit button is pressed and only role is filled**: Ellenőrzi, hogy a felhasználók oldalon szerkeszthető-e a felhasználó szerepköre, ha csak a szerepkör mezőt töltik ki és a szerkesztés gombot megnyomják.
- **should edit user's role and password on users page when edit button is pressed and both are filled**: Ellenőrzi, hogy a felhasználók oldalon szerkeszthető-e a felhasználó szerepköre és jelszava, ha mindkét mezőt kitöltik és a szerkesztés gombot megnyomják.
- **should display all buttons on miscellaneous page**: Ellenőrzi, hogy az egyebek oldalon megjelenik-e az összes gomb.
- **should start csengo on miscellaneous page when start button is pressed**: Ellenőrzi, hogy az egyebek oldalon elindul-e a csengő, ha az indítás gombot megnyomják.
- **should stop csengo on miscellaneous page when stop button is pressed**: Ellenőrzi, hogy az egyebek oldalon leáll-e a csengő, ha a leállítás gombot megnyomják.
- **should download songs in voting on miscellaneous page when download button is pressed**: Ellenőrzi, hogy az egyebek oldalon letölthetők-e a szavazásban lévő zenék, ha a letöltés gombot megnyomják.
- **should download winner song on miscellaneous page when download button is pressed**: Ellenőrzi, hogy az egyebek oldalon letölthető-e a nyertes zene, ha a letöltés gombot megnyomják.
- **should update winner song on server on miscellaneous page when update button is pressed**: Ellenőrzi, hogy az egyebek oldalon frissíthető-e a nyertes zene a szerveren, ha a frissítés gombot megnyomják.

##### `forbidden.spec.ts`

- **should stay on forbidden page**: Ellenőrzi, hogy az oldal a tiltott oldalon marad-e.
- **should display the forbidden page with home button on large screens**: Ellenőrzi, hogy a tiltott oldal megjelenik-e a kezdőlap gombbal nagy képernyőkön.
- **should display the message on small screens**: Ellenőrzi, hogy a tiltott oldal üzenetet jelenít-e meg kis képernyőkön.
- **should navigate to home page when home button is clicked**: Ellenőrzi, hogy a kezdőlap gombra kattintva a felhasználó a kezdőlapra navigál-e.

##### `index.spec.ts`

- **should display the home page**: Ellenőrzi, hogy a kezdőlap megjelenik-e.
- **should display the navigation bar**: Ellenőrzi, hogy a navigációs sáv megjelenik-e.
- **should navigate to about page when about link is clicked**: Ellenőrzi, hogy az "About" linkre kattintva a felhasználó az "About" oldalra navigál-e.
- **should display the footer**: Ellenőrzi, hogy a lábléc megjelenik-e.
- **should display the correct title**: Ellenőrzi, hogy a helyes cím megjelenik-e a kezdőlapon.
- **should display featured articles**: Ellenőrzi, hogy a kiemelt cikkek megjelennek-e a kezdőlapon.
- **should navigate to article page when article is clicked**: Ellenőrzi, hogy egy cikkre kattintva a felhasználó a cikk oldalára navigál-e.
- **should display the search bar**: Ellenőrzi, hogy a keresősáv megjelenik-e.
- **should show search results when a query is entered**: Ellenőrzi, hogy a keresési eredmények megjelennek-e, ha egy lekérdezést beírnak.
- **should display the login button**: Ellenőrzi, hogy a bejelentkezés gomb megjelenik-e.
- **should navigate to login page when login button is clicked**: Ellenőrzi, hogy a bejelentkezés gombra kattintva a felhasználó a bejelentkezési oldalra navigál-e.
- **should display the register button**: Ellenőrzi, hogy a regisztráció gomb megjelenik-e.
- **should navigate to register page when register button is clicked**: Ellenőrzi, hogy a regisztráció gombra kattintva a felhasználó a regisztrációs oldalra navigál-e.

##### `login.spec.ts`

- **should render login page correctly**: Ellenőrzi, hogy a bejelentkezési oldal helyesen jelenik-e meg.
- **should show validation errors if fields are empty**: Ellenőrzi, hogy a mezők üresen hagyása esetén megjelennek-e az érvényesítési hibák.
- **should handle login with correct credentials**: Ellenőrzi, hogy a bejelentkezés helyesen történik-e a megfelelő hitelesítő adatokkal.
- **should show error message on failed login**: Ellenőrzi, hogy hibás bejelentkezés esetén megjelenik-e a hibaüzenet.
- **should navigate to register page**: Ellenőrzi, hogy a regisztrációs oldalra navigál-e a felhasználó, ha a megfelelő linkre kattint.

##### `register.spec.ts`

- **should display the registration form**: Ellenőrzi, hogy a regisztrációs űrlap megjelenik-e.
- **should have all input fields**: Ellenőrzi, hogy az összes bemeneti mező megjelenik-e.
- **should display labels for input fields**: Ellenőrzi, hogy a bemeneti mezők címkéi megjelennek-e.
- **should navigate to login page when link is clicked**: Ellenőrzi, hogy a bejelentkezési oldalra navigál-e a felhasználó, ha a megfelelő linkre kattint.
- **should register a new user**: Ellenőrzi, hogy egy új felhasználó regisztrálható-e.
- **should show error message on registration failure**: Ellenőrzi, hogy regisztrációs hiba esetén megjelenik-e a hibaüzenet.
- **should show error message on password mismatch**: Ellenőrzi, hogy jelszó nem egyezőség esetén megjelenik-e a hibaüzenet.

##### `tv.spec.ts`

- **should navigate to tv page**: Ellenőrzi, hogy a TV oldal megjelenik-e.
- **should navigate to index page when logged in**: Ellenőrzi, hogy ha a felhasználó be van jelentkezve, akkor a kezdőoldalra navigál-e.
- **should display call to action when no session is active**: Ellenőrzi, hogy ha nincs aktív szavazási szekció, akkor megjelenik-e a cselekvési hívás.
- **should display correct data when a session is active**: Ellenőrzi, hogy ha aktív szavazási szekció van, akkor helyesen jelenik-e meg az adat.

### Backend felépítése

A Pollák Csengő backend alkalmazásának metodológiája a következő: a backend alkalmazás moduláris felépítésű, a különböző funkciókat külön modulokba szervezi. A modulok egymással kommunikálnak a NestJS Dependency Injection segítségével, és a különböző modulok közötti navigáció a NestJS Router segítségével történik. Minden lekérdezés egy Prisma ORM segítségével történik, hogy a modulok egyszerű és konzisztens adatbázis hozzáférést tarthassanak. A modulok a NestJS keretrendszer segítségével vannak összeállítva és futtatva.

- **.github**
   - *workflows*: Tartalmazza a GitHub Actions munkafolyamatokat.
      - *ci.yml*: A folyamatos integrációs munkafolyamat konfigurációja.

- **.idea**
   - *codeStyles*: Kódstílus beállítások.
      - *codeStyleConfig.xml*: Kódstílus konfiguráció.
      - *Project.xml*: Projekt szintű kódstílus beállítások.
   - *inspectionProfiles*: Ellenőrzési profilok.
      - *Project_Default.xml*: Alapértelmezett ellenőrzési profil.
   - *runConfigurations*: Futtatási konfigurációk.
      - *docker_compose_dev_yml_csengo_v2_postgres_dev__Compose_Deployment.xml*: Docker Compose futtatási konfiguráció.
      - *prisma_update.xml*: Prisma frissítési konfiguráció.
      - *start_dev.xml*: Fejlesztési futtatási konfiguráció.
      - *test_cov.xml*: Teszt lefedettségi konfiguráció.
      - *test_e2e.xml*: Végpontok közötti teszt konfiguráció.
   - *csengo-ts-server-v2.iml*: Projekt fájl.
   - *discord.xml*: Discord integrációs beállítások.
   - *git_toolbox_blame.xml*: Git blame eszköz beállításai.
   - *git_toolbox_prj.xml*: Git projekt eszköz beállításai.
   - *modules.xml*: Modulok konfigurációja.
   - *prettier.xml*: Prettier beállítások.
   - *vcs.xml*: Verziókezelő rendszer beállításai.

- **config**
   - *certificate.pem*: SSL tanúsítvány.
   - *localhost-key.pem*: Helyi fejlesztési SSL kulcs.
   - *localhost.pem*: Helyi fejlesztési SSL tanúsítvány.
   - *private.pem*: Privát kulcs.

- **db**
   - *create_default_user.sql*: Alapértelmezett felhasználó létrehozására szolgáló SQL script.

- **endpoints**
   - *required-endpoints.md*: Szükséges végpontok listája.
   - *requirements.md*: Követelmények dokumentációja.

- **prisma**
   - *schema.prisma*: Prisma séma fájl.
   - **migrations**: Adatbázis migrációk.
      - *migration_lock.toml*: Migrációs zárolási fájl.
      - *20241210185133_prod*: Migrációs mappa.
         - *migration.sql*: SQL migrációs fájl.
      - *20250117190305_prod*: Migrációs mappa.
         - *migration.sql*: SQL migrációs fájl.

- **src**
   - *main.ts*: Az alkalmazás belépési pontja.
   - **config**: Konfigurációs szolgáltatások.
      - *aws.s3.client.config.service.ts*: AWS S3 kliens konfigurációs szolgáltatás.
      - *aws.s3.storage.config.service.ts*: AWS S3 tároló konfigurációs szolgáltatás.
      - *config.local.module.ts*: Helyi konfigurációs modul.
      - *multer.config.service.ts*: Multer konfigurációs szolgáltatás.
      - *prisma.config.service.ts*: Prisma konfigurációs szolgáltatás.
      - *storage.local.config.service.ts*: Helyi tároló konfigurációs szolgáltatás.
   - **filter**: Szűrők.
      - *delete.file.on.error.filter.ts*: Fájl törlése hiba esetén szűrő.
      - *filter.module.ts*: Szűrő modul.
   - **module**: Modulok.
      - *app.module.ts*: Alkalmazás modul.
      - **app**: Alkalmazás modul komponensei.
         - *app.controller.spec.ts*: Alkalmazás vezérlő tesztje.
         - *app.controller.ts*: Alkalmazás vezérlő.
         - *app.service.spec.ts*: Alkalmazás szolgáltatás tesztje.
         - *app.service.ts*: Alkalmazás szolgáltatás.
      - **auth**: Hitelesítési modul.
         - *auth.controller.spec.ts*: Hitelesítési vezérlő tesztje.
         - *auth.controller.ts*: Hitelesítési vezérlő.
         - *auth.decorator.ts*: Hitelesítési dekorátor.
         - *auth.guard.ts*: Hitelesítési őr.
         - *auth.module.ts*: Hitelesítési modul.
         - *auth.service.ts*: Hitelesítési szolgáltatás.
         - **dto**: Adatátviteli objektumok.
            - *login.dto.ts*: Bejelentkezési DTO.
            - *register.dto.ts*: Regisztrációs DTO.
      - **pendingSongs**: Függő zenék modul.
         - *pending.songs.controller.spec.ts*: Függő zenék vezérlő tesztje.
         - *pending.songs.controller.ts*: Függő zenék vezérlő.
         - *pending.songs.module.ts*: Függő zenék modul.
         - *pending.songs.service.ts*: Függő zenék szolgáltatás.
      - **role**: Szerepkör modul.
         - *role.decorator.ts*: Szerepkör dekorátor.
         - *role.enum.ts*: Szerepkör enum.
         - *role.guard.ts*: Szerepkör őr.
      - **songs**: Zenék modul.
         - *songs.controller.spec.ts*: Zenék vezérlő tesztje.
         - *songs.controller.ts*: Zenék vezérlő.
         - *songs.module.ts*: Zenék modul.
         - *songs.service.ts*: Zenék szolgáltatás.
         - **dto**: Adatátviteli objektumok.
            - *create.song.dto.ts*: Zene létrehozási DTO.
      - **tv**: TV modul.
         - *tv.controller.spec.ts*: TV vezérlő tesztje.
         - *tv.controller.ts*: TV vezérlő.
         - *tv.module.ts*: TV modul.
         - *tv.service.spec.ts*: TV szolgáltatás tesztje.
         - *tv.service.ts*: TV szolgáltatás.
      - **user**: Felhasználó modul.
         - *user.controller.spec.ts*: Felhasználó vezérlő tesztje.
         - *user.controller.ts*: Felhasználó vezérlő.
         - *user.module.ts*: Felhasználó modul.
         - *user.service.spec.ts*: Felhasználó szolgáltatás tesztje.
         - *user.service.ts*: Felhasználó szolgáltatás.
         - **dto**: Adatátviteli objektumok.
            - *update.pass.dto.ts*: Jelszó frissítési DTO.
            - *update.role.dto.ts*: Szerepkör frissítési DTO.
      - **votes**: Szavazatok modul.
         - *votes.controller.spec.ts*: Szavazatok vezérlő tesztje.
         - *votes.controller.ts*: Szavazatok vezérlő.
         - *votes.module.ts*: Szavazatok modul.
         - *votes.service.ts*: Szavazatok szolgáltatás.
      - **votingSessions**: Szavazási szekciók modul.
         - *voting.sessions.controller.spec.ts*: Szavazási szekciók vezérlő tesztje.
         - *voting.sessions.controller.ts*: Szavazási szekciók vezérlő.
         - *voting.sessions.module.ts*: Szavazási szekciók modul.
         - *voting.sessions.service.ts*: Szavazási szekciók szolgáltatás.
         - **dto**: Adatátviteli objektumok.
            - *voting.session.dto.ts*: Szavazási szekció DTO.
      - **websocket**: Websocket modul.
         - *websocket.exception.filter.ts*: Websocket kivétel szűrő.
         - *websocket.gateway.ts*: Websocket átjáró.
         - *websocket.guard.ts*: Websocket őr.
         - *websocket.module.ts*: Websocket modul.
   - **pipe**: Pipe-ok.
      - *audio.length.validation.pipe.service.ts*: Audio hossz validációs pipe.
      - *pipe.module.ts*: Pipe modul.
   - **type**: Típusdefiníciók.
      - *express.d.ts*: Express típusdefiníciók.
      - *jwt.d.ts*: JWT típusdefiníciók.
   - **util**: Segédfüggvények.
      - *logger.custom.util.ts*: Egyedi naplózó segédfüggvény.

- **test**
   - *app.e2e-spec.ts*: Végpontok közötti teszt.
   - *jest-e2e.json*: Jest végpontok közötti teszt konfiguráció.
   - *test-docs.md*: Teszt dokumentáció.

- *.dockerignore*: Ez a fájl tartalmazza azokat a fájlokat és könyvtárakat, amelyeket a Docker figyelmen kívül hagy a build folyamat során.
- *.env.example*: Példa környezeti változókat tartalmazó fájl, amely segít a fejlesztőknek a saját `.env` fájljaik létrehozásában.
- *.eslintrc.js*: Az ESLint konfigurációs fájlja, amely meghatározza a kódminőségi szabályokat és beállításokat.
- *.gitignore*: Ez a fájl tartalmazza azokat a fájlokat és könyvtárakat, amelyeket a Git figyelmen kívül hagy a verziókezelés során.
- *.prettierrc*: A Prettier konfigurációs fájlja, amely meghatározza a kódformázási szabályokat és beállításokat.
- *docker-compose.dev.yml*: Docker Compose konfigurációs fájl, amely a fejlesztési környezethez szükséges szolgáltatásokat és beállításokat tartalmazza.
- *docker-compose.release.yml*: Docker Compose konfigurációs fájl, amely a kiadási környezethez szükséges szolgáltatásokat és beállításokat tartalmazza.
- *Dockerfile*: A Docker image létrehozásához szükséges utasításokat tartalmazó fájl.
- *init-s3.py*: Python szkript, amely az S3 szolgáltatás inicializálásához szükséges.
- *nest-cli.json*: A NestJS CLI konfigurációs fájlja, amely a projekt beállításait tartalmazza.
- *package-lock.json*: A Node.js csomagok pontos verzióit rögzítő fájl, amely biztosítja a reprodukálható build folyamatot.
- *package.json*: A Node.js projekt konfigurációs fájlja, amely tartalmazza a projekt függőségeit és szkripteket.
- *README.md*: A projekt leírását és használati útmutatóját tartalmazó fájl.
- *sonar-project.properties*: A SonarQube konfigurációs fájlja, amely a kódminőség elemzéséhez szükséges beállításokat tartalmazza.
- *tsconfig.build.json*: A TypeScript build konfigurációs fájlja, amely meghatározza a build folyamat során használt beállításokat.
- *tsconfig.json*: A TypeScript projekt alapértelmezett konfigurációs fájlja, amely meghatározza a fordító beállításait.

#### Backend Controller Tesztelés

##### `app.controller.spec`

- **`uploadDirect`**: A `uploadDirect` teszteset ellenőrzi, hogy az adminisztrátor közvetlenül feltölthet-e egy dalt.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **file**:
          ```json
          {
            "mimetype": "audio/mpeg"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **`renameById`**: A `renameById` teszteset ellenőrzi, hogy az adminisztrátor átnevezhet-e egy dalt azonosító alapján.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **`deleteById`**: A `deleteById` teszteset ellenőrzi, hogy az adminisztrátor törölhet-e egy dalt azonosító alapján.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```



##### `auth.controller.spec`

- **AuthController -> should be defined**: This test case verifies that the `authController` is properly defined and instantiated within the test module.
    - **Mocked input data**:
        - **None**:
          ```json 
          {}
          ```
    - **Return value**:
        - **None**:
          ```json 
          {}
          ```

- **AuthController -> login -> should return a valid JWT token**: This test case verifies that the `login` method of the `authController` returns a valid JWT token when provided with valid credentials.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "body": {
              "username": "testUser",
              "password": "testPassword"
            }
          }
          ```
        - **mockUser**:
          ```json 
          {
            "id": "1",
            "username": "testUser",
            "password": "hashedPassword"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "access_token": "mockedJwtToken"
          }
          ```

- **AuthController -> register -> should create a new user**: This test case verifies that the `register` method of the `authController` creates a new user when provided with valid registration data.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "body": {
              "username": "newUser",
              "password": "newPassword"
            }
          }
          ```
        - **mockUser**:
          ```json 
          {
            "id": "2",
            "username": "newUser",
            "password": "hashedNewPassword"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "id": "2",
            "username": "newUser"
          }
          ```

- **AuthController -> validateUser -> should validate a user with correct credentials**: This test case verifies that the `validateUser` method of the `authController` validates a user when provided with correct credentials.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "body": {
              "username": "validUser",
              "password": "validPassword"
            }
          }
          ```
        - **mockUser**:
          ```json 
          {
            "id": "3",
            "username": "validUser",
            "password": "hashedValidPassword"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "id": "3",
            "username": "validUser"
          }
          ```

- **AuthController -> validateUser -> should return null for invalid credentials**: This test case verifies that the `validateUser` method of the `authController` returns null when provided with invalid credentials.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "body": {
              "username": "invalidUser",
              "password": "invalidPassword"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          null
          ```

##### `pending.songs.controller.spec.ts`

- **PendingSongsController -> getAllPendingSongs -> should return all pending songs**: This test case verifies that the `getAllPendingSongs` method of the `PendingSongsController` returns all pending songs correctly. It mocks the request and the service method to return a list of pending songs and checks if the controller method returns the expected result.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "token": { "sub": "mockedId", "username": "mockedUser", "roles": ["Admin"], "hashedPassword": "mocked-password" }
          }
          ```
        - **mockPendingSongs**:
          ```json 
          [
            { "id": "song1", "title": "Song 1" },
            { "id": "song2", "title": "Song 2" }
          ]
          ```
    - **Return value**:
        - **result**:
          ```json 
          [
            { "id": "song1", "title": "Song 1" },
            { "id": "song2", "title": "Song 2" }
          ]
          ```

- **PendingSongsController -> approvePendingSong -> should approve a pending song**: This test case verifies that the `approvePendingSong` method of the `PendingSongsController` approves a pending song correctly. It mocks the request and the service method to approve a song and checks if the controller method returns the expected result.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "token": { "sub": "mockedId", "username": "mockedUser", "roles": ["Admin"], "hashedPassword": "mocked-password" }
          }
          ```
        - **mockSongId**:
          ```json 
          "song1"
          ```
    - **Return value**:
        - **result**:
          ```json 
          { "success": true }
          ```

- **PendingSongsController -> rejectPendingSong -> should reject a pending song**: This test case verifies that the `rejectPendingSong` method of the `PendingSongsController` rejects a pending song correctly. It mocks the request and the service method to reject a song and checks if the controller method returns the expected result.
    - **Mocked input data**:
        - **mockRequest**:
          ```json 
          {
            "token": { "sub": "mockedId", "username": "mockedUser", "roles": ["Admin"], "hashedPassword": "mocked-password" }
          }
          ```
        - **mockSongId**:
          ```json 
          "song1"
          ```
    - **Return value**:
        - **result**:
          ```json 
          { "success": true }
          ```

##### `songs.controller.spec.ts`

- **SongsController -> getAllAudioInSession -> should return all audio in session for public access**: Ez a teszteset ellenőrzi, hogy a `getAllAudioInSession` metódus visszaadja-e az összes hanganyagot a nyilvános hozzáféréshez. A `songsService.getAllAudioInSession` metódust mockolja, hogy egy üres hanganyag listát adjon vissza, és ellenőrzi, hogy a `songsController.getAllAudioInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "audios": []
          }
          ```

- **SongsController -> getAllInSession -> should return all songs in session**: Ez a teszteset ellenőrzi, hogy a `getAllInSession` metódus visszaadja-e az összes dalt a szekcióban. A `songsService.getAllInSession` metódust mockolja, hogy egy üres dal listát adjon vissza, és ellenőrzi, hogy a `songsController.getAllInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "songs": []
          }
          ```

- **SongsController -> getAll -> should return all songs for admin**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus visszaadja-e az összes dalt az admin számára. A `songsService.getAll` metódust mockolja, hogy egy üres dal listát adjon vissza, és ellenőrzi, hogy a `songsController.getAll` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "songs": []
          }
          ```

- **SongsController -> getWinner -> should return the winner song**: Ez a teszteset ellenőrzi, hogy a `getWinner` metódus visszaadja-e a nyertes dalt. A `songsService.getWinner` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.getWinner` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> getWinnerAudio -> should return winner audio**: Ez a teszteset ellenőrzi, hogy a `getWinnerAudio` metódus visszaadja-e a nyertes hanganyagot. A `songsService.getWinnerAudio` metódust mockolja, hogy egy `StreamableFile` objektumot adjon vissza, és ellenőrzi, hogy a `songsController.getWinnerAudio` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "type": "StreamableFile",
            "data": "audio"
          }
          ```

- **SongsController -> getAudioById -> should return audio by ID**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus visszaadja-e a hanganyagot azonosító alapján. A `songsService.getAudioById` metódust mockolja, hogy egy `StreamableFile` objektumot adjon vissza, és ellenőrzi, hogy a `songsController.getAudioById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "type": "StreamableFile",
            "data": "audio"
          }
          ```

- **SongsController -> updateAudioById -> should update audio for admin**: Ez a teszteset ellenőrzi, hogy a `updateAudioById` metódus frissíti-e a hanganyagot az admin számára. A `songsService.updateAudio` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.updateAudio` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> startAudio -> should start audio for admin**: Ez a teszteset ellenőrzi, hogy a `startAudio` metódus elindítja-e a hanganyagot az admin számára. A `songsService.startAudio` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.startAudio` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> stopAudio -> should stop audio for admin**: Ez a teszteset ellenőrzi, hogy a `stopAudio` metódus leállítja-e a hanganyagot az admin számára. A `songsService.stopAudio` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.stopAudio` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> upload -> should upload a song**: Ez a teszteset ellenőrzi, hogy a `upload` metódus feltölt-e egy dalt. A `songsService.upload` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.upload` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **file**:
          ```json
          {
            "mimetype": "audio/mpeg"
          }
          ```
        - **createSongDto**:
          ```json
          {
            "title": "mocked-title"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> uploadDirect -> should upload a song directly for admin**: Ez a teszteset ellenőrzi, hogy a `uploadDirect` metódus közvetlenül feltölt-e egy dalt az admin számára. A `songsService.uploadDirect` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.uploadDirect` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **file**:
          ```json
          {
            "mimetype": "audio/mpeg"
          }
          ```
        - **createSongDto**:
          ```json
          {
            "title": "mocked-title"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> renameById -> should rename a song for admin**: Ez a teszteset ellenőrzi, hogy a `renameById` metódus átnevez-e egy dalt az admin számára. A `songsService.renameById` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.renameById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **SongsController -> deleteById -> should delete a song for admin**: Ez a teszteset ellenőrzi, hogy a `deleteById` metódus töröl-e egy dalt az admin számára. A `songsService.deleteById` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `songsController.deleteById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

##### `tv.controller.spec.ts`

- **TvController -> getAll -> should return summary of votes in session**: Ez a teszteset ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus visszaadja-e a szavazatok összegzését a szekcióban. A `tvService.getSummaryOfVotesInSession` metódust mockolja, hogy egy szavazatok összegzését adjon vissza, és ellenőrzi, hogy a `tvController.getSummaryOfVotesInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "summary": "Summary of votes"
          }
          ```

##### `user.controller.spec.ts`

- **UserController -> getRealNameById -> should return real name**: Ez a teszteset ellenőrzi, hogy a `getRealNameById` metódus visszaadja-e a felhasználó valódi nevét. A `userService.getRealNameById` metódust mockolja, hogy egy valódi nevet adjon vissza, és ellenőrzi, hogy a `userController.getRealNameById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "realName": "mocked-name"
          }
          ```

- **UserController -> getAll -> should return all users**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus visszaadja-e az összes felhasználót. A `userService.getAll` metódust mockolja, hogy egy üres felhasználó listát adjon vissza, és ellenőrzi, hogy a `userController.getAll` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "users": []
          }
          ```

- **UserController -> updateUserPassword -> should return success when updating user password**: Ez a teszteset ellenőrzi, hogy a `updateUserPassword` metódus sikeresen frissíti-e a felhasználó jelszavát. A `userService.updateUserPassword` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `userController.updateUserPassword` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockPassword**:
          ```json
          {
            "userId": "1",
            "password": "asd"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **UserController -> updateUserRole -> should return success when updating user role**: Ez a teszteset ellenőrzi, hogy a `updateUserRole` metódus sikeresen frissíti-e a felhasználó szerepkörét. A `userService.updateUserRole` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `userController.updateUserRole` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockRole**:
          ```json
          {
            "userId": "1",
            "role": "Admin"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

##### `view.controller.spec.ts`

- **ViewController -> renderSummaryOfVotesInSession -> should render summary of votes in session**: Ez a teszteset ellenőrzi, hogy a `renderSummaryOfVotesInSession` metódus visszaadja-e a szavazatok összegzését a szekcióban. A `viewService.getSummaryOfVotesInSessionData` metódust mockolja, hogy egy szavazatok összegzését adjon vissza, és ellenőrzi, hogy a `viewController.renderSummaryOfVotesInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          "Rendered summary of votes"
          ```

- **ViewController -> renderPendingSongs -> should render pending songs**: Ez a teszteset ellenőrzi, hogy a `renderPendingSongs` metódus visszaadja-e a függőben lévő dalokat. A `viewService.getPendingSongsData` metódust mockolja, hogy egy függőben lévő dalokat adjon vissza, és ellenőrzi, hogy a `viewController.renderPendingSongs` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          "Rendered pending songs"
          ```

##### `votes.controller.spec.ts`

- **VotesController -> getSummrayOfVotesInSession -> should return summary of votes in session**: Ez a teszteset ellenőrzi, hogy a `getSummrayOfVotesInSession` metódus visszaadja-e a szavazatok összegzését a szekcióban. A `votesService.getSummaryOfVotesInSession` metódust mockolja, hogy egy szavazatok összegzését adjon vissza, és ellenőrzi, hogy a `votesController.getSummrayOfVotesInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "votes": []
          }
          ```

- **VotesController -> getVotedSongsByUserId -> should return votes songs by user id**: Ez a teszteset ellenőrzi, hogy a `getVotedSongsByUserId` metódus visszaadja-e a felhasználó által szavazott dalokat. A `votesService.getVotedSongsByUserId` metódust mockolja, hogy egy dal listát adjon vissza, és ellenőrzi, hogy a `votesController.getVotedSongsByUserId` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "songs": ["Song 1", "Song 2"]
          }
          ```

- **VotesController -> voteUp -> should return success when voted up**: Ez a teszteset ellenőrzi, hogy a `voteUp` metódus sikeresen végrehajtja-e a szavazat felfelé történő leadását. A `votesService.voteUp` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `votesController.voteUp` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **VotesController -> voteDown -> should return success when voted down**: Ez a teszteset ellenőrzi, hogy a `voteDown` metódus sikeresen végrehajtja-e a szavazat lefelé történő leadását. A `votesService.voteDown` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `votesController.voteDown` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

##### `voting.sessions.controller.spec.ts`

- **VotingSessionController -> should return summary of votes in session**: Ez a teszteset ellenőrzi, hogy a `getAllSessions` metódus visszaadja-e a szavazatok összegzését a szekcióban. A `votingSessionService.getAllSessions` metódust mockolja, hogy egy üres szavazatok összegzését adjon vissza, és ellenőrzi, hogy a `votingSessionController.getAllSessions` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "sessions": []
          }
          ```

- **VotingSessionController -> should return votes songs by user id**: Ez a teszteset ellenőrzi, hogy a `createSession` metódus visszaadja-e a felhasználó által szavazott dalokat. A `votingSessionService.createSession` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `votingSessionController.createSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockSession**:
          ```json
          {
            "songIds": ["1", "2"],
            "start": "2020-01-01",
            "end": "2021-01-01"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **VotingSessionController -> should return success when voted up**: Ez a teszteset ellenőrzi, hogy a `updateSessionById` metódus sikeresen frissíti-e a szavazat felfelé történő leadását. A `votingSessionService.updateSessionById` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `votingSessionController.updateSessionById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockSession**:
          ```json
          {
            "songIds": ["1", "2"],
            "start": "2020-01-01",
            "end": "2021-01-01"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

- **VotingSessionController -> should return success when voted down**: Ez a teszteset ellenőrzi, hogy a `deleteSessionById` metódus sikeresen végrehajtja-e a szavazat lefelé történő leadását. A `votingSessionService.deleteSessionById` metódust mockolja, hogy egy sikeres üzenetet adjon vissza, és ellenőrzi, hogy a `votingSessionController.deleteSessionById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "success": true
          }
          ```

#### Backend Service Tesztelés

##### `app.service.spec.ts`

- **AppService -> should be defined**: Ez a teszteset ellenőrzi, hogy az `AppService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **N/A**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "defined": true
          }
          ```

- **AppService -> getHello -> should return "Hello World!" when getHello is called**: Ez a teszteset ellenőrzi, hogy a `getHello` metódus visszaadja-e a "Hello World!" szöveget, amikor meghívják.
    - **Mocked input data**:
        - **N/A**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Hello World!"
          }
          ```

##### `auth.service.spec.ts`

- **AuthService -> should be defined**: Ez a teszteset ellenőrzi, hogy az `AuthService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **N/A**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "defined": true
          }
          ```

- **AuthService -> login -> should return JWT token upon successfull login**: Ez a teszteset ellenőrzi, hogy a `login` metódus visszaadja-e a JWT tokent sikeres bejelentkezés esetén. A `prisma.user.findFirstOrThrow` metódust mockolja, hogy egy felhasználói adatot adjon vissza, és ellenőrzi, hogy a `authService.login` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockedLoginDto**:
          ```json
          {
            "username": "mocked-user",
            "password": "mocked-password"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "access_token": "test-token"
          }
          ```

- **AuthService -> login -> should throw FORBIDDEN if invalid username or password**: Ez a teszteset ellenőrzi, hogy a `login` metódus `FORBIDDEN` hibát dob-e érvénytelen felhasználónév vagy jelszó esetén. A `prisma.user.findFirstOrThrow` metódust mockolja, hogy egy felhasználói adatot adjon vissza, és ellenőrzi, hogy a `authService.login` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedLoginDto**:
          ```json
          {
            "username": "mocked-user",
            "password": "mocked-password"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 403,
            "message": "Invalid username or password"
          }
          ```

- **AuthService -> login -> should throw NOT_FOUND if user not found**: Ez a teszteset ellenőrzi, hogy a `login` metódus `NOT_FOUND` hibát dob-e, ha a felhasználó nem található. A `prisma.user.findFirstOrThrow` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `authService.login` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedLoginDto**:
          ```json
          {
            "username": "mocked-user",
            "password": "mocked-password"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 404,
            "message": "Failed to find user or invalid authentication data"
          }
          ```

- **AuthService -> register -> should return JWT token upon successful register**: Ez a teszteset ellenőrzi, hogy a `register` metódus visszaadja-e a JWT tokent sikeres regisztráció esetén. A `prisma.user.findFirst`, `prisma.kreta.findFirstOrThrow`, és `prisma.user.create` metódusokat mockolja, hogy felhasználói adatokat adjon vissza, és ellenőrzi, hogy a `authService.register` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockedRegisterDto**:
          ```json
          {
            "username": "new-user",
            "password": "new-password",
            "email": "new-email@test.com",
            "om": "72548167135"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "access_token": "test-token"
          }
          ```

- **AuthService -> register -> should return INTERNAL_SERVER_ERROR if checking existing user fails**: Ez a teszteset ellenőrzi, hogy a `register` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha a meglévő felhasználó ellenőrzése sikertelen. A `prisma.user.findFirst` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `authService.register` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedRegisterDto**:
          ```json
          {
            "username": "new-user",
            "password": "new-password",
            "email": "new-email@test.com",
            "om": "72548167135"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Something went wrong"
          }
          ```

- **AuthService -> register -> should return INTERNAL_SERVER_ERROR if someone has already registered under those information**: Ez a teszteset ellenőrzi, hogy a `register` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha valaki már regisztrált ezekkel az adatokkal. A `prisma.user.findFirst` metódust mockolja, hogy felhasználói adatot adjon vissza, és ellenőrzi, hogy a `authService.register` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedRegisterDto**:
          ```json
          {
            "username": "existing-user",
            "password": "password",
            "email": "existing-email@test.com",
            "om": "72548167135"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Seems like someone has already registered under this information"
          }
          ```

- **AuthService -> register -> should return INTERNAL_SERVER_ERROR if prisma cannot find the OM in the database**: Ez a teszteset ellenőrzi, hogy a `register` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha a prisma nem találja az OM azonosítót az adatbázisban. A `prisma.kreta.findFirstOrThrow` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `authService.register` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedRegisterDto**:
          ```json
          {
            "username": "new-user",
            "password": "new-password",
            "email": "new-email@test.com",
            "om": "72548167135"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Can't find this OM id in the database"
          }
          ```

- **AuthService -> register -> should return INTERNAL_SERVER_ERROR if prisma fails to create user**: Ez a teszteset ellenőrzi, hogy a `register` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha a prisma nem tudja létrehozni a felhasználót. A `prisma.user.create` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `authService.register` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockedRegisterDto**:
          ```json
          {
            "username": "new-user",
            "password": "new-password",
            "email": "new-email@test.com",
            "om": "72578167135"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Failed to register user bad OM"
          }
          ```

##### `pending.songs.service.spec.ts`

- **PendingSongsService -> should be defined**: Ez a teszteset ellenőrzi, hogy a `PendingSongsService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **N/A**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "defined": true
          }
          ```

- **PendingSongsService -> getAll -> should return all pending songs**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus visszaadja-e az összes függőben lévő dalt. A `prisma.pendingSong.findMany` metódust mockolja, hogy egy listát adjon vissza a függőben lévő dalokról, és ellenőrzi, hogy a `service.getAll` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          [
            {
              "id": "1",
              "title": "Song 1",
              "uploadedBy": {
                "kreta": {
                  "name": "John Doe"
                }
              }
            }
          ]
          ```

- **PendingSongsService -> getAll -> should throw an error when no pending songs are found**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus hibát dob-e, ha nem találhatóak függőben lévő dalok. A `prisma.pendingSong.findMany` metódust mockolja, hogy egy üres listát adjon vissza, és ellenőrzi, hogy a `service.getAll` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 404,
            "message": "No pending songs found"
          }
          ```

- **PendingSongsService -> getAll -> should throw an error when an internal error occurs**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus hibát dob-e, ha belső hiba történik. A `prisma.pendingSong.findMany` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.getAll` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Error fetching pending songs: Database error"
          }
          ```

- **PendingSongsService -> getAudioById -> should return a streamable file**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus visszaad-e egy streamelhető fájlt. A `prisma.pendingSong.findUnique` metódust mockolja, hogy egy dalt adjon vissza, és ellenőrzi, hogy a `service.getAudioById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "type": "StreamableFile"
          }
          ```

- **PendingSongsService -> getAudioById -> should throw an error when song is not found**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus hibát dob-e, ha a dal nem található. A `prisma.pendingSong.findUnique` metódust mockolja, hogy null értéket adjon vissza, és ellenőrzi, hogy a `service.getAudioById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 404,
            "message": "Song not found"
          }
          ```

- **PendingSongsService -> getAudioById -> should throw an error when an internal error occurs**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus hibát dob-e, ha belső hiba történik. A `prisma.pendingSong.findUnique` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.getAudioById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Error fetching song: Database error"
          }
          ```

- **PendingSongsService -> approveById -> should approve a pending song**: Ez a teszteset ellenőrzi, hogy az `approveById` metódus jóváhagyja-e a függőben lévő dalt. A `prisma.pendingSong.findUnique`, `prisma.song.create`, és `prisma.pendingSong.delete` metódusokat mockolja, hogy egy dalt adjon vissza, és ellenőrzi, hogy a `service.approveById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Peding song with id 1 sucessfully approved"
          }
          ```

- **PendingSongsService -> approveById -> should throw an error when pending song is not found**: Ez a teszteset ellenőrzi, hogy az `approveById` metódus hibát dob-e, ha a függőben lévő dal nem található. A `prisma.pendingSong.findUnique` metódust mockolja, hogy null értéket adjon vissza, és ellenőrzi, hogy a `service.approveById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 404,
            "message": "Pending song not found"
          }
          ```

- **PendingSongsService -> approveById -> should throw an error when an internal error occurs**: Ez a teszteset ellenőrzi, hogy az `approveById` metódus hibát dob-e, ha belső hiba történik. A `prisma.pendingSong.findUnique` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.approveById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Error fetching pending song: Database error"
          }
          ```

- **PendingSongsService -> disapproveById -> should disapprove a pending song**: Ez a teszteset ellenőrzi, hogy a `disapproveById` metódus elutasítja-e a függőben lévő dalt. A `prisma.pendingSong.findFirstOrThrow` és `prisma.pendingSong.delete` metódusokat mockolja, hogy egy dalt adjon vissza, és ellenőrzi, hogy a `service.disapproveById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Peding song with id 1 sucessfully disapproved"
          }
          ```

- **PendingSongsService -> disapproveById -> should throw an error when pending song is not found**: Ez a teszteset ellenőrzi, hogy a `disapproveById` metódus hibát dob-e, ha a függőben lévő dal nem található. A `prisma.pendingSong.findFirstOrThrow` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.disapproveById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 404,
            "message": "Error fetching pending song: Record not found"
          }
          ```

- **PendingSongsService -> disapproveById -> should throw an error when an internal error occurs**: Ez a teszteset ellenőrzi, hogy a `disapproveById` metódus hibát dob-e, ha belső hiba történik. A `prisma.pendingSong.findFirstOrThrow` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.disapproveById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "status": 500,
            "message": "Error fetching pending song: Database error"
          }
          ```

##### `songs.service.spec.ts`

- **SongsService -> should be defined**: Ez a teszteset ellenőrzi, hogy a `SongsService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **service**:
          ```json 
          {
            "defined": true
          }
          ```

- **SongsService -> getAllAudioInSession -> should return a zip file of songs in session**: Ez a teszteset ellenőrzi, hogy a `getAllAudioInSession` metódus visszaadja-e a szekcióban lévő dalok zip fájlját.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockResponse**:
          ```json 
          {
            "attachment": "songs.zip",
            "pipe": true
          }
          ```
        - **mockVotingSession**:
          ```json 
          {
            "id": "sessionId",
            "songs": [
              {
                "id": "songId",
                "title": "Test Song",
                "songBucket": {
                  "path": "path/to/song.mp3"
                }
              }
            ]
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "truthy": true
          }
          ```

- **SongsService -> getAllAudioInSession -> should throw an error when no active voting session is found**: Ez a teszteset ellenőrzi, hogy a `getAllAudioInSession` metódus hibát dob-e, ha nincs aktív szavazási szekció.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockResponse**:
          ```json 
          {
            "attachment": "songs.zip",
            "pipe": true
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "No active voting session found",
            "status": 404
          }
          ```

- **SongsService -> getAllInSession -> should return a list of songs in session**: Ez a teszteset ellenőrzi, hogy a `getAllInSession` metódus visszaadja-e a szekcióban lévő dalok listáját.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json 
          {
            "id": "sessionId",
            "songs": [
              {
                "id": "songId",
                "title": "Test Song",
                "songBucket": {
                  "path": "path/to/song.mp3"
                }
              }
            ]
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "sessionId": "sessionId",
            "songs": [
              {
                "songId": "songId",
                "songTitle": "Test Song"
              }
            ]
          }
          ```

- **SongsService -> getAllInSession -> should throw an error when no active voting session is found**: Ez a teszteset ellenőrzi, hogy a `getAllInSession` metódus hibát dob-e, ha nincs aktív szavazási szekció.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "No active voting session found",
            "status": 404
          }
          ```

- **SongsService -> getAll -> should return a list of all songs**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus visszaadja-e az összes dalt.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          [
            {
              "id": "songId",
              "title": "Test Song"
            }
          ]
          ```

- **SongsService -> getAll -> should throw an error when no songs are found**: Ez a teszteset ellenőrzi, hogy a `getAll` metódus hibát dob-e, ha nem találhatóak dalok.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "No songs found",
            "status": 404
          }
          ```

- **SongsService -> getWinner -> should return the winner song**: Ez a teszteset ellenőrzi, hogy a `getWinner` metódus visszaadja-e a nyertes dalt.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json 
          {
            "id": "sessionId",
            "songs": [
              {
                "id": "songId",
                "title": "Test Song",
                "songBucket": {
                  "path": "path/to/song.mp3"
                }
              }
            ]
          }
          ```
        - **mockSong**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```

- **SongsService -> getWinner -> should throw an error when no finished voting session is found**: Ez a teszteset ellenőrzi, hogy a `getWinner` metódus hibát dob-e, ha nincs befejezett szavazási szekció.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "No finished voting session found",
            "status": 500
          }
          ```

- **SongsService -> getWinnerAudio -> should return winner audio**: Ez a teszteset ellenőrzi, hogy a `getWinnerAudio` metódus visszaadja-e a nyertes hanganyagot.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json 
          {
            "id": "sessionId",
            "songs": [
              {
                "id": "songId",
                "title": "Test Song",
                "songBucket": {
                  "path": "path/to/song.mp3"
                }
              }
            ]
          }
          ```
        - **mockSong**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "type": "StreamableFile"
          }
          ```

- **SongsService -> getWinnerAudio -> should throw an error when no finished voting session is found**: Ez a teszteset ellenőrzi, hogy a `getWinnerAudio` metódus hibát dob-e, ha nincs befejezett szavazási szekció.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "No finished voting session found",
            "status": 500
          }
          ```

- **SongsService -> getAudioById -> should return a StreamableFile for the given song id**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus visszaad-e egy streamelhető fájlt a megadott dal azonosító alapján.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "type": "StreamableFile"
          }
          ```

- **SongsService -> getAudioById -> should throw an error when song is not found**: Ez a teszteset ellenőrzi, hogy a `getAudioById` metódus hibát dob-e, ha a dal nem található.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "Song not found",
            "status": 404
          }
          ```

- **SongsService -> updateAudio -> should update audio**: Ez a teszteset ellenőrzi, hogy a `updateAudio` metódus frissíti-e a hanganyagot.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockResult**:
          ```json 
          {
            "message": "Success"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "message": "Success"
          }
          ```

- **SongsService -> updateAudio -> should throw an error when update fails**: Ez a teszteset ellenőrzi, hogy a `updateAudio` metódus hibát dob-e, ha a frissítés sikertelen.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "Error updating audio: Update failed",
            "status": 500
          }
          ```

- **SongsService -> startAudio -> should start audio**: Ez a teszteset ellenőrzi, hogy a `startAudio` metódus elindítja-e a hanganyagot.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockResult**:
          ```json 
          {
            "message": "Success"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "message": "Success"
          }
          ```

- **SongsService -> startAudio -> should throw an error when start fails**: Ez a teszteset ellenőrzi, hogy a `startAudio` metódus hibát dob-e, ha az indítás sikertelen.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "Error starting audio: Start failed",
            "status": 500
          }
          ```

- **SongsService -> stopAudio -> should stop audio**: Ez a teszteset ellenőrzi, hogy a `stopAudio` metódus leállítja-e a hanganyagot.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockResult**:
          ```json 
          {
            "message": "Success"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "message": "Success"
          }
          ```

- **SongsService -> stopAudio -> should throw an error when stop fails**: Ez a teszteset ellenőrzi, hogy a `stopAudio` metódus hibát dob-e, ha a leállítás sikertelen.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "Error stopping audio: Stop failed",
            "status": 500
          }
          ```

- **SongsService -> upload -> should upload a song**: Ez a teszteset ellenőrzi, hogy a `upload` metódus feltölt-e egy dalt.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockFile**:
          ```json 
          {
            "path": "path/to/song.mp3"
          }
          ```
        - **mockCreateSongDto**:
          ```json 
          {
            "title": "Test Song"
          }
          ```
        - **mockResult**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song"
          }
          ```

- **SongsService -> upload -> should throw an error when upload fails**: Ez a teszteset ellenőrzi, hogy a `upload` metódus hibát dob-e, ha a feltöltés sikertelen.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockFile**:
          ```json 
          {
            "path": "path/to/song.mp3"
          }
          ```
        - **mockCreateSongDto**:
          ```json 
          {
            "title": "Test Song"
          }
          ```
    - **Return value**:
        - **error**:
          ```json 
          {
            "message": "Error uploading song into pending songs: Upload failed",
            "status": 500
          }
          ```

- **SongsService -> uploadDirect -> should upload a song directly**: Ez a teszteset ellenőrzi, hogy a `uploadDirect` metódus közvetlenül feltölt-e egy dalt.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json 
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockFile**:
          ```json 
          {
            "path": "path/to/song.mp3"
          }
          ```
        - **mockCreateSongDto**:
          ```json 
          {
            "title": "Test Song"
          }
          ```
        - **mockResult**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song"
          }
          ```
    - **Return value**:
        - **result**:
          ```json 
          {
            "id": "songId",
            "title": "Test Song"
          }
          ```

- **SongsService -> uploadDirect -> should throw an error when direct upload fails**: Ez a teszteset ellenőrzi, hogy a `uploadDirect` metódus hibát dob-e, ha a közvetlen feltöltés sikertelen. A `prisma.song.create` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.uploadDirect` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockFile**:
          ```json
          {
            "path": "path/to/song.mp3"
          }
          ```
        - **mockCreateSongDto**:
          ```json
          {
            "title": "Test Song"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error uploading song directly into songs: Upload failed",
            "statusCode": 500
          }
          ```

- **SongsService -> renameById -> should rename a song**: Ez a teszteset ellenőrzi, hogy a `renameById` metódus átnevez-e egy dalt az admin számára. A `prisma.song.findUnique` és `prisma.song.update` metódusokat mockolja, hogy egy dalt adjon vissza, és ellenőrzi, hogy a `service.renameById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Song renamed successfully to New Title"
          }
          ```

- **SongsService -> renameById -> should throw an error when rename fails**: Ez a teszteset ellenőrzi, hogy a `renameById` metódus hibát dob-e, ha az átnevezés sikertelen. A `prisma.song.findUnique` és `prisma.song.update` metódusokat mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.renameById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error renaming song: Rename failed",
            "statusCode": 500
          }
          ```

- **SongsService -> deleteById -> should delete a song**: Ez a teszteset ellenőrzi, hogy a `deleteById` metódus töröl-e egy dalt az admin számára. A `prisma.song.findUnique` és `prisma.song.delete` metódusokat mockolja, hogy egy dalt adjon vissza, és ellenőrzi, hogy a `service.deleteById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Song deleted successfully"
          }
          ```

- **SongsService -> deleteById -> should throw an error when delete fails**: Ez a teszteset ellenőrzi, hogy a `deleteById` metódus hibát dob-e, ha a törlés sikertelen. A `prisma.song.findUnique` és `prisma.song.delete` metódusokat mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.deleteById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockSong**:
          ```json
          {
            "id": "songId",
            "title": "Test Song",
            "songBucket": {
              "path": "path/to/song.mp3"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error deleting song: Delete failed",
            "statusCode": 500
          }
          ```

##### `tv.service.spec.ts`

- **TvService -> should be defined**: Ez a teszteset ellenőrzi, hogy a `TvService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **service**:
          ```json
          {
            "defined": true
          }
          ```

- **TvService -> getSummaryOfVotesInSession -> should return summary of votes when a session is active**: Ez a teszteset ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus visszaadja-e a szavazatok összegzését, amikor egy szekció aktív.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **prisma.votingSession.findFirst**:
          ```json
          {
            "id": 1,
            "start": "2023-01-01T00:00:00.000Z",
            "end": "2023-01-01T00:00:00.000Z",
            "songs": [
              {"id": 1, "title": "Song A"},
              {"id": 2, "title": "Song B"}
            ],
            "Vote": [
              {"songId": 1},
              {"songId": 1},
              {"songId": 2}
            ]
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "sessionId": 1,
            "songs": [
              {"songId": 1, "songTitle": "Song A", "voteCount": 2},
              {"songId": 2, "songTitle": "Song B", "voteCount": 1}
            ]
          }
          ```

- **TvService -> getSummaryOfVotesInSession -> should throw NOT_FOUND if no active session exists**: Ez a teszteset ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus `NOT_FOUND` hibát dob-e, ha nincs aktív szavazási szekció.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **prisma.votingSession.findFirst**:
          ```json
          null
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No active voting session found",
            "status": 404
          }
          ```

- **TvService -> getSummaryOfVotesInSession -> should throw INTERNAL_SERVER_ERROR if database query fails**: Ez a teszteset ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha az adatbázis lekérdezés sikertelen.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **prisma.votingSession.findFirst**:
          ```json
          {
            "error": "Database error"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching currently running voting session: Database error",
            "status": 500
          }
          ```

- **TvService -> getSummaryOfVotesInSession -> should throw INTERNAL_SERVER_ERROR if vote counting fails**: Ez a teszteset ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus `INTERNAL_SERVER_ERROR` hibát dob-e, ha a szavazatok számlálása sikertelen.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **prisma.votingSession.findFirst**:
          ```json
          {
            "id": 1,
            "start": "2023-01-01T00:00:00.000Z",
            "end": "2023-01-01T00:00:00.000Z",
            "songs": [
              {"id": 1, "title": "Song A"}
            ],
            "Vote": null
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error counting votes:",
            "status": 500
          }
          ```

##### `user.service.spec.ts`

- **UserService -> should be defined**: Ellenőrzi, hogy a `UserService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **module**:
          ```json
          {
            "providers": [
              "UserService",
              {
                "provide": "PrismaConfigService",
                "useValue": {
                  "user": {
                    "findUnique": "jest.fn()",
                    "findMany": "jest.fn",
                    "findFirstOrThrow": "jest.fn()",
                    "update": "jest.fn()"
                  }
                }
              }
            ]
          }
          ```
    - **Return value**:
        - **service**:
          ```json
          {
            "defined": true
          }
          ```

- **UserService -> getRealNameById -> should return real name when user is found**: Ellenőrzi, hogy a `getRealNameById` metódus visszaadja-e a felhasználó valódi nevét, ha a felhasználó megtalálható.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUser**:
          ```json
          {
            "kreta": {
              "name": "John Doe"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "realName": "John Doe"
          }
          ```

- **UserService -> getRealNameById -> should throw an error when userId is missing**: Ellenőrzi, hogy a `getRealNameById` metódus hibát dob-e, ha a felhasználói azonosító hiányzik.
    - **Mocked input data**:
        - **requestUserWithoutId**:
          ```json
          {
            "token": {
              "username": "testUser"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Missing userId",
            "status": 400
          }
          ```

- **UserService -> getRealNameById -> should throw an error when no user is found**: Ellenőrzi, hogy a `getRealNameById` metódus hibát dob-e, ha a felhasználó nem található.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No real name found by this user's OM",
            "status": 204
          }
          ```

- **UserService -> getRealNameById -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `getRealNameById` metódus hibát dob-e, ha belső hiba történik.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching real name of user: Database error",
            "status": 500
          }
          ```

- **UserService -> getAll -> should return all users**: Ellenőrzi, hogy a `getAll` metódus visszaadja-e az összes felhasználót.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUsers**:
          ```json
          [
            {
              "id": "1",
              "username": "user1",
              "email": "user1@example.com",
              "roles": [
                {
                  "role": "admin"
                }
              ],
              "kreta": {
                "name": "User One",
                "om": "12345"
              }
            },
            {
              "id": "2",
              "username": "user2",
              "email": "user2@example.com",
              "roles": [
                {
                  "role": "user"
                }
              ],
              "kreta": {
                "name": "User Two",
                "om": "67890"
              }
            }
          ]
          ```
    - **Return value**:
        - **result**:
          ```json
          [
            {
              "id": "1",
              "username": "user1",
              "email": "user1@example.com",
              "role": "admin",
              "kreta": {
                "name": "User One",
                "om": "12345"
              }
            },
            {
              "id": "2",
              "username": "user2",
              "email": "user2@example.com",
              "role": "user",
              "kreta": {
                "name": "User Two",
                "om": "67890"
              }
            }
          ]
          ```

- **UserService -> getAll -> should throw an error when no users are found**: Ellenőrzi, hogy a `getAll` metódus hibát dob-e, ha nem találhatóak felhasználók.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No users found",
            "status": 204
          }
          ```

- **UserService -> getAll -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `getAll` metódus hibát dob-e, ha belső hiba történik.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching all users: Database error",
            "status": 500
          }
          ```

- **UserService -> updateUserPassword -> should update user password**: Ellenőrzi, hogy a `updateUserPassword` metódus frissíti-e a felhasználó jelszavát.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdatePassDto**:
          ```json
          {
            "userId": "123",
            "password": "newPassword123"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Password updated for user: testUser"
          }
          ```

- **UserService -> updateUserPassword -> should throw an error when user is not found**: Ellenőrzi, hogy a `updateUserPassword` metódus hibát dob-e, ha a felhasználó nem található.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdatePassDto**:
          ```json
          {
            "userId": "123",
            "password": "newPassword123"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "User not found: User not found",
            "status": 500
          }
          ```

- **UserService -> updateUserPassword -> should throw an error when an internal error while finding user**: Ellenőrzi, hogy a `updateUserPassword` metódus hibát dob-e, ha belső hiba történik a felhasználó keresése közben.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdatePassDto**:
          ```json
          {
            "userId": "123",
            "password": "newPassword123"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "User not found: Database error",
            "status": 500
          }
          ```

- **UserService -> updateUserRole -> should update user role**: Ellenőrzi, hogy a `updateUserRole` metódus frissíti-e a felhasználó szerepkörét.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdateRoleDto**:
          ```json
          {
            "userId": "123",
            "role": "Admin"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Role updated for user: testUser"
          }
          ```

- **UserService -> updateUserRole -> should throw an error when user is not found**: Ellenőrzi, hogy a `updateUserRole` metódus hibát dob-e, ha a felhasználó nem található.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdateRoleDto**:
          ```json
          {
            "userId": "123",
            "role": "Admin"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "User not found: User not found",
            "status": 500
          }
          ```

- **UserService -> updateUserRole -> should throw an error when an internal error while finding user**: Ellenőrzi, hogy a `updateUserRole` metódus hibát dob-e, ha belső hiba történik a felhasználó keresése közben.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockUpdateRoleDto**:
          ```json
          {
            "userId": "123",
            "role": "Admin"
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "User not found: Database error",
            "status": 500
          }
          ```

##### `view.service.spec.ts`

- **ViewService -> should be defined**: Ellenőrzi, hogy a `ViewService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockPrismaService**:
          ```json
          {
            "votingSession": {
              "findFirst": "jest.fn()"
            },
            "pendingSong": {
              "findMany": "jest.fn()"
            }
          }
          ```
    - **Return value**:
        - **service**:
          ```json
          {
            "defined": true
          }
          ```

- **ViewService -> getSummaryOfVotesInSessionData -> should return summary of votes in session**: Ellenőrzi, hogy a `getSummaryOfVotesInSessionData` metódus visszaadja-e a szavazatok összegzését a szekcióban.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "mockedSessionId",
            "songs": [
              { "id": "song1", "title": "Song 1" },
              { "id": "song2", "title": "Song 2" }
            ],
            "Vote": [
              { "songId": "song1" },
              { "songId": "song1" },
              { "songId": "song2" }
            ]
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "sessionId": "mockedSessionId",
            "songs": [
              { "songId": "song1", "songTitle": "Song 1", "voteCount": 2 },
              { "songId": "song2", "songTitle": "Song 2", "voteCount": 1 }
            ]
          }
          ```

- **ViewService -> getSummaryOfVotesInSessionData -> should throw error if no active voting session is found**: Ellenőrzi, hogy a `getSummaryOfVotesInSessionData` metódus hibát dob-e, ha nincs aktív szavazási szekció.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No active voting session found"
          }
          ```

- **ViewService -> getPendingSongsData -> should return pending songs data**: Ellenőrzi, hogy a `getPendingSongsData` metódus visszaadja-e a függőben lévő dalokat.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
        - **mockPendingSongs**:
          ```json
          [
            { "id": "song1", "title": "Song 1" },
            { "id": "song2", "title": "Song 2" }
          ]
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "pendingSongs": [
              { "id": "song1", "title": "Song 1" },
              { "id": "song2", "title": "Song 2" }
            ]
          }
          ```

- **ViewService -> getPendingSongsData -> should throw error if no pending songs are found**: Ellenőrzi, hogy a `getPendingSongsData` metódus hibát dob-e, ha nem találhatóak függőben lévő dalok.
    - **Mocked input data**:
        - **mockRequest**:
          ```json
          {
            "token": {
              "sub": "mockedId",
              "username": "mockedUser",
              "roles": ["Admin"],
              "hashedPassword": "mocked-password"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No pending songs found"
          }
          ```

##### `votes.service.spec.ts`

- **VotesService -> should be defined**: Ellenőrzi, hogy a `VotesService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {}
          ```

- **VotesService -> getSummaryOfVotesInSession -> should return summary of votes in session**: Ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus visszaadja-e a szavazatok összegzését a szekcióban. A `prisma.votingSession.findFirst` metódust mockolja, hogy egy szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.getSummaryOfVotesInSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "sessionId": "1",
            "songs": []
          }
          ```

- **VotesService -> getSummaryOfVotesInSession -> should throw an error when no active voting session is found**: Ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus hibát dob-e, ha nincs aktív szavazási szekció. A `prisma.votingSession.findFirst` metódust mockolja, hogy null értéket adjon vissza, és ellenőrzi, hogy a `service.getSummaryOfVotesInSession` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No active voting session found",
            "status": 404
          }
          ```

- **VotesService -> getSummaryOfVotesInSession -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `getSummaryOfVotesInSession` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findFirst` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.getSummaryOfVotesInSession` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching currently running voting session: Database error",
            "status": 500
          }
          ```

- **VotesService -> getVotedSongsByUserId -> should return voted songs by user id**: Ellenőrzi, hogy a `getVotedSongsByUserId` metódus visszaadja-e a felhasználó által szavazott dalokat. A `prisma.votingSession.findFirst` és `prisma.vote.findMany` metódusokat mockolja, hogy egy szavazási szekciót és szavazatokat adjon vissza, és ellenőrzi, hogy a `service.getVotedSongsByUserId` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
        - **mockVotes**:
          ```json
          [
            { "songId": "1" },
            { "songId": "2" }
          ]
          ```
    - **Return value**:
        - **result**:
          ```json
          ["1", "2"]
          ```

- **VotesService -> getVotedSongsByUserId -> should throw an error when no votes are found**: Ellenőrzi, hogy a `getVotedSongsByUserId` metódus hibát dob-e, ha nem találhatóak szavazatok. A `prisma.vote.findMany` metódust mockolja, hogy üres listát adjon vissza, és ellenőrzi, hogy a `service.getVotedSongsByUserId` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No active voting session found",
            "status": 404
          }
          ```

- **VotesService -> getVotedSongsByUserId -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `getVotedSongsByUserId` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findFirst` és `prisma.vote.findMany` metódusokat mockolja, hogy egy szavazási szekciót és hibát dobjon, és ellenőrzi, hogy a `service.getVotedSongsByUserId` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching votes: Database error",
            "status": 500
          }
          ```

- **VotesService -> voteUp -> should create a vote for a song**: Ellenőrzi, hogy a `voteUp` metódus létrehoz-e egy szavazatot egy dalra. A `prisma.votingSession.findFirst`, `prisma.vote.findFirst`, és `prisma.vote.create` metódusokat mockolja, hogy egy szavazási szekciót és szavazatot adjon vissza, és ellenőrzi, hogy a `service.voteUp` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Vote successfully created for song: 1"
          }
          ```

- **VotesService -> voteUp -> should throw an error when user already voted for the song**: Ellenőrzi, hogy a `voteUp` metódus hibát dob-e, ha a felhasználó már szavazott a dalra. A `prisma.votingSession.findFirst` és `prisma.vote.findFirst` metódusokat mockolja, hogy egy szavazási szekciót és szavazatot adjon vissza, és ellenőrzi, hogy a `service.voteUp` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "User already voted for song: 1",
            "status": 400
          }
          ```

- **VotesService -> voteUp -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `voteUp` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findFirst`, `prisma.vote.findFirst`, és `prisma.vote.create` metódusokat mockolja, hogy egy szavazási szekciót és hibát dobjon, és ellenőrzi, hogy a `service.voteUp` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error creating vote: Database error",
            "status": 500
          }
          ```

- **VotesService -> voteDown -> should delete a vote for a song**: Ellenőrzi, hogy a `voteDown` metódus töröl-e egy szavazatot egy dalra. A `prisma.votingSession.findFirst`, `prisma.vote.findFirst`, és `prisma.vote.delete` metódusokat mockolja, hogy egy szavazási szekciót és szavazatot adjon vissza, és ellenőrzi, hogy a `service.voteDown` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Sucessfully deleted vote for song: 1"
          }
          ```

- **VotesService -> voteDown -> should throw an error when no existing vote is found**: Ellenőrzi, hogy a `voteDown` metódus hibát dob-e, ha nem található meglévő szavazat. A `prisma.votingSession.findFirst` és `prisma.vote.findFirst` metódusokat mockolja, hogy egy szavazási szekciót és null értéket adjon vissza, és ellenőrzi, hogy a `service.voteDown` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No existing vote found",
            "status": 404
          }
          ```

- **VotesService -> voteDown -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `voteDown` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findFirst`, `prisma.vote.findFirst`, és `prisma.vote.delete` metódusokat mockolja, hogy egy szavazási szekciót és hibát dobjon, és ellenőrzi, hogy a `service.voteDown` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
        - **mockVotingSession**:
          ```json
          {
            "id": "1",
            "start": "2022-11-30T00:00:00.000Z",
            "end": "2024-11-30T00:00:00.000Z",
            "songs": [],
            "Vote": []
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error deleting vote for vote down: Database error",
            "status": 500
          }
          ```

##### `voting.sessions.service.spec.ts`

- **VotingSessionService -> should be defined**: Ellenőrzi, hogy a `VotingSessionService` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {}
          ```

- **VotingSessionService -> getAllSessions -> should return all sessions**: Ellenőrzi, hogy a `getAllSessions` metódus visszaadja-e az összes szavazási szekciót. A `prisma.votingSession.findMany` metódust mockolja, hogy egy szavazási szekció listát adjon vissza, és ellenőrzi, hogy a `service.getAllSessions` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          [
            {
              "id": "1",
              "start": "2020-01-01",
              "end": "2021-01-01",
              "songs": [],
              "Vote": []
            }
          ]
          ```

- **VotingSessionService -> getAllSessions -> should throw an error when no sessions are found**: Ellenőrzi, hogy a `getAllSessions` metódus hibát dob-e, ha nem találhatóak szavazási szekciók. A `prisma.votingSession.findMany` metódust mockolja, hogy üres listát adjon vissza, és ellenőrzi, hogy a `service.getAllSessions` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "No sessions found",
            "status": 404
          }
          ```

- **VotingSessionService -> getAllSessions -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `getAllSessions` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findMany` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `service.getAllSessions` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error fetching sessions: Database error",
            "status": 500
          }
          ```

- **VotingSessionService -> createSession -> should create a new session**: Ellenőrzi, hogy a `createSession` metódus létrehoz-e egy új szavazási szekciót. A `prisma.song.findMany`, `prisma.votingSession.findFirst`, és `prisma.votingSession.create` metódusokat mockolja, hogy dalokat és szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.createSession` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Successfully created new session: {\"id\":\"1\",\"start\":\"2020-01-01\",\"end\":\"2021-01-01\",\"songs\":[],\"Vote\":[]}"
          }
          ```

- **VotingSessionService -> createSession -> should throw an error when start time is later than end time**: Ellenőrzi, hogy a `createSession` metódus hibát dob-e, ha a kezdési idő későbbi, mint a befejezési idő. A `service.createSession` metódust hívja meg egy érvénytelen időtartammal, és ellenőrzi, hogy a várt hibát dobja-e.
    - **Mocked input data**:
        - **invalidSessionDto**:
          ```json
          {
            "start": "2022-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "The start time cannot be later than the end time",
            "status": 400
          }
          ```

- **VotingSessionService -> createSession -> should throw an error when overlapping session is found**: Ellenőrzi, hogy a `createSession` metódus hibát dob-e, ha átfedő szavazási szekció található. A `prisma.votingSession.findFirst` metódust mockolja, hogy egy meglévő szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.createSession` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "The duration of the voting session overlaps with an existing voting session",
            "status": 409
          }
          ```

- **VotingSessionService -> createSession -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `createSession` metódus hibát dob-e, ha belső hiba történik. A `prisma.song.findMany`, `prisma.votingSession.findFirst`, és `prisma.votingSession.create` metódusokat mockolja, hogy dalokat és hibát dobjon, és ellenőrzi, hogy a `service.createSession` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error creating voting session: Database error",
            "status": 500
          }
          ```

- **VotingSessionService -> updateSessionById -> should update a session by id**: Ellenőrzi, hogy a `updateSessionById` metódus frissíti-e a szavazási szekciót azonosító alapján. A `prisma.votingSession.findFirst`, `prisma.song.findMany`, és `prisma.votingSession.update` metódusokat mockolja, hogy dalokat és szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.updateSessionById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Successfully updated session: {\"id\":\"1\",\"start\":\"2020-01-01\",\"end\":\"2021-01-01\",\"songs\":[],\"Vote\":[]}"
          }
          ```

- **VotingSessionService -> updateSessionById -> should throw an error when start time is later than end time**: Ellenőrzi, hogy a `updateSessionById` metódus hibát dob-e, ha a kezdési idő későbbi, mint a befejezési idő. A `service.updateSessionById` metódust hívja meg egy érvénytelen időtartammal, és ellenőrzi, hogy a várt hibát dobja-e.
    - **Mocked input data**:
        - **invalidSessionDto**:
          ```json
          {
            "start": "2022-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "The start time cannot be later than the end time",
            "status": 400
          }
          ```

- **VotingSessionService -> updateSessionById -> should throw an error when overlapping session is found**: Ellenőrzi, hogy a `updateSessionById` metódus hibát dob-e, ha átfedő szavazási szekció található. A `prisma.votingSession.findFirst` metódust mockolja, hogy egy meglévő szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.updateSessionById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "The duration of the voting session overlaps with an existing voting session",
            "status": 409
          }
          ```

- **VotingSessionService -> updateSessionById -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `updateSessionById` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findFirst`, `prisma.song.findMany`, és `prisma.votingSession.update` metódusokat mockolja, hogy dalokat és hibát dobjon, és ellenőrzi, hogy a `service.updateSessionById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockSessionDto**:
          ```json
          {
            "start": "2020-01-01",
            "end": "2021-01-01",
            "songIds": ["1", "2"]
          }
          ```
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error updating voting session: Database error",
            "status": 500
          }
          ```

- **VotingSessionService -> deleteSessionById -> should delete a session by id**: Ellenőrzi, hogy a `deleteSessionById` metódus törli-e a szavazási szekciót azonosító alapján. A `prisma.votingSession.findUnique` és `prisma.votingSession.delete` metódusokat mockolja, hogy egy szavazási szekciót adjon vissza, és ellenőrzi, hogy a `service.deleteSessionById` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {
            "message": "Successfully deleted session: 1"
          }
          ```

- **VotingSessionService -> deleteSessionById -> should throw an error when session is not found**: Ellenőrzi, hogy a `deleteSessionById` metódus hibát dob-e, ha a szavazási szekció nem található. A `prisma.votingSession.findUnique` metódust mockolja, hogy null értéket adjon vissza, és ellenőrzi, hogy a `service.deleteSessionById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Voting session not found",
            "status": 404
          }
          ```

- **VotingSessionService -> deleteSessionById -> should throw an error when an internal error occurs**: Ellenőrzi, hogy a `deleteSessionById` metódus hibát dob-e, ha belső hiba történik. A `prisma.votingSession.findUnique` és `prisma.votingSession.delete` metódusokat mockolja, hogy egy szavazási szekciót és hibát dobjon, és ellenőrzi, hogy a `service.deleteSessionById` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **mockRequestUser**:
          ```json
          {
            "token": {
              "username": "testUser",
              "sub": "123"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "message": "Error deleting voting session: Database error",
            "status": 500
          }
          ```

#### Backend Pipe Tesztelés

##### `audio.length.validation.pipe.service.spec.ts`

- **AudioLengthValidatorPipe -> should be defined**: Ellenőrzi, hogy az `AudioLengthValidatorPipe` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **mockMetadataParser**:
          ```json
          {
            "parseFile": {}
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          {}
          ```

- **AudioLengthValidatorPipe -> should return true if file duration is within limit**: Ellenőrzi, hogy az `isValid` metódus igaz értéket ad-e vissza, ha a fájl hossza a megadott határon belül van. A `mockMetadataParser.parseFile` metódust mockolja, hogy egy 8 másodperces fájl hosszt adjon vissza, és ellenőrzi, hogy a `pipe.isValid` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **file**:
          ```json
          {
            "originalname": "test.mp3",
            "path": "/path/to/file.mp3"
          }
          ```
        - **mockMetadataParser**:
          ```json
          {
            "parseFile": {
              "format": {
                "duration": 8
              }
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          true
          ```

- **AudioLengthValidatorPipe -> should return false if file duration exceeds limit**: Ellenőrzi, hogy az `isValid` metódus hamis értéket ad-e vissza, ha a fájl hossza meghaladja a megadott határt. A `mockMetadataParser.parseFile` metódust mockolja, hogy egy 20 másodperces fájl hosszt adjon vissza, és ellenőrzi, hogy a `pipe.isValid` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **file**:
          ```json
          {
            "originalname": "test.mp3",
            "path": "/path/to/file.mp3"
          }
          ```
        - **mockMetadataParser**:
          ```json
          {
            "parseFile": {
              "format": {
                "duration": 20
              }
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          false
          ```

- **AudioLengthValidatorPipe -> should return false if file has no path**: Ellenőrzi, hogy az `isValid` metódus hamis értéket ad-e vissza, ha a fájlnak nincs elérési útja. A `pipe.isValid` metódust hívja meg egy elérési út nélküli fájllal, és ellenőrzi, hogy a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **file**:
          ```json
          {
            "originalname": "test.mp3"
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          false
          ```

- **AudioLengthValidatorPipe -> should return false if an error occurs during parsing**: Ellenőrzi, hogy az `isValid` metódus hamis értéket ad-e vissza, ha hiba történik a fájl elemzése során. A `mockMetadataParser.parseFile` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy a `pipe.isValid` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **file**:
          ```json
          {
            "originalname": "test.mp3",
            "path": "/path/to/file.mp3"
          }
          ```
        - **mockMetadataParser**:
          ```json
          {
            "parseFile": {
              "error": "Parsing error"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          false
          ```

- **AudioLengthValidatorPipe -> should return proper error message**: Ellenőrzi, hogy a `buildErrorMessage` metódus a megfelelő hibaüzenetet adja-e vissza. A `pipe.buildErrorMessage` metódust hívja meg egy fájllal, és ellenőrzi, hogy a várt hibaüzenetet adja-e vissza.
    - **Mocked input data**:
        - **file**:
          ```json
          {
            "originalname": "test.mp3"
          }
          ```
    - **Return value**:
        - **errorMessage**:
          ```json
          "The audio file test.mp3 exceeds the maximum allowed length of 15 seconds."
          ```

#### Backend Guard Tesztelés

##### `auth.guard.spec.ts`

- **AuthGuard -> should be defined**: Ellenőrzi, hogy az `AuthGuard` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **jwtService**:
          ```json
          {}
          ```
        - **reflector**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {}
          ```

- **AuthGuard -> should allow access to public endpoints**: Ellenőrzi, hogy az `AuthGuard` hozzáférést enged-e a nyilvános végpontokhoz. A `reflector.getAllAndOverride` metódust mockolja, hogy igaz értéket adjon vissza, és ellenőrzi, hogy az `authGuard.canActivate` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "cookies": {}
              }
            },
            "getHandler": {},
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": true
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          true
          ```

- **AuthGuard -> should throw UnauthorizedException if token is missing**: Ellenőrzi, hogy az `AuthGuard` `UnauthorizedException` hibát dob-e, ha a token hiányzik. A `reflector.getAllAndOverride` metódust mockolja, hogy hamis értéket adjon vissza, és ellenőrzi, hogy az `authGuard.canActivate` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "cookies": {}
              }
            },
            "getHandler": {},
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": false
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "name": "UnauthorizedException"
          }
          ```

- **AuthGuard -> should throw HttpException if token is invalid**: Ellenőrzi, hogy az `AuthGuard` `HttpException` hibát dob-e, ha a token érvénytelen. A `reflector.getAllAndOverride` metódust mockolja, hogy hamis értéket adjon vissza, és a `jwtService.verifyAsync` metódust mockolja, hogy hibát dobjon, és ellenőrzi, hogy az `authGuard.canActivate` metódus a várt hibát dobja-e.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "cookies": {
                  "token": "invalid-token"
                }
              }
            },
            "getHandler": {},
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": false
          }
          ```
        - **jwtService**:
          ```json
          {
            "verifyAsync": {
              "error": "Invalid token"
            }
          }
          ```
    - **Return value**:
        - **error**:
          ```json
          {
            "name": "HttpException"
          }
          ```

- **AuthGuard -> should allow access if token is valid**: Ellenőrzi, hogy az `AuthGuard` hozzáférést enged-e, ha a token érvényes. A `reflector.getAllAndOverride` metódust mockolja, hogy hamis értéket adjon vissza, és a `jwtService.verifyAsync` metódust mockolja, hogy egy felhasználói adatot adjon vissza, és ellenőrzi, hogy az `authGuard.canActivate` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "cookies": {
                  "token": "valid-token"
                },
                "token": {}
              }
            },
            "getHandler": {},
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": false
          }
          ```
        - **jwtService**:
          ```json
          {
            "verifyAsync": {
              "username": "testuser"
            }
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          true
          ```

##### `role.guard.spec.ts`

- **RolesGuard -> should be defined**: Ellenőrzi, hogy a `RolesGuard` megfelelően definiálva van-e és példányosítva van-e a teszt modulban.
    - **Mocked input data**:
        - **reflector**:
          ```json
          {}
          ```
    - **Return value**:
        - **result**:
          ```json
          {}
          ```

- **RolesGuard -> should allow access if no roles are required**: Ellenőrzi, hogy a `RolesGuard` hozzáférést enged-e, ha nincs szükség szerepkörökre. A `reflector.getAllAndOverride` metódust mockolja, hogy undefined értéket adjon vissza, és ellenőrzi, hogy a `rolesGuard.canActivate` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "token": {
                  "roles": []
                }
              }
            },
            "getHandler": {
              "name": "Handler"
            },
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": null
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          true
          ```

- **RolesGuard -> should allow access if user has required roles**: Ellenőrzi, hogy a `RolesGuard` hozzáférést enged-e, ha a felhasználónak megvannak a szükséges szerepkörök. A `reflector.getAllAndOverride` metódust mockolja, hogy az `Admin` szerepkört adja vissza, és ellenőrzi, hogy a `rolesGuard.canActivate` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "token": {
                  "roles": ["Admin"]
                }
              }
            },
            "getHandler": {
              "name": "Handler"
            },
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": ["Admin"]
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          true
          ```

- **RolesGuard -> should deny access if user does not have required roles**: Ellenőrzi, hogy a `RolesGuard` megtagadja-e a hozzáférést, ha a felhasználónak nincsenek meg a szükséges szerepkörök. A `reflector.getAllAndOverride` metódust mockolja, hogy az `Admin` szerepkört adja vissza, és ellenőrzi, hogy a `rolesGuard.canActivate` metódus a várt eredményt adja-e vissza.
    - **Mocked input data**:
        - **context**:
          ```json
          {
            "switchToHttp": {
              "getRequest": {
                "token": {
                  "roles": ["User"]
                }
              }
            },
            "getHandler": {
              "name": "Handler"
            },
            "getClass": {}
          }
          ```
        - **reflector**:
          ```json
          {
            "getAllAndOverride": ["Admin"]
          }
          ```
    - **Return value**:
        - **result**:
          ```json
          false
          ```

## Nevezetes Algoritmusok

[//]: # (TODO: valamennyi algoritmus nem tudni meg mennyi kell)
### TODO: valamennyi algoritmus



## Adatbázis
A PostgreSQL-t választottuk más adatbázisok, mint például a MySQL helyett számos előnye miatt. Először is, a PostgreSQL egy rendkívül robusztus és megbízható adatbázis-kezelő rendszer, amely hosszú évek óta bizonyítja megbízhatóságát és stabilitását. Az ACID (Atomicity, Consistency, Isolation, Durability) tulajdonságok támogatása garantálja az adatok integritását és konzisztenciáját.

Továbbá, a PostgreSQL kiválóan támogatja a fejlett adatbázis-funkciókat, mint például a JSON, XML és hstore típusok kezelését, ami rendkívül hasznos a modern webes alkalmazások fejlesztésében. Ezen kívül támogatja a teljes szöveg keresést és az adattárolást komplex adatszerkezetekkel, ami lehetővé teszi az adatok rugalmasabb kezelését és lekérdezését.

A PostgreSQL nyílt forráskódú, így teljesen ingyenesen használható és testreszabható az igényeinknek megfelelően. Az aktív közösségi támogatásnak köszönhetően gyors hibajavításokra és rendszeres frissítésekre számíthatunk. Emellett széles körben kompatibilis különböző operációs rendszerekkel és programozási nyelvekkel, így könnyen integrálható a meglévő rendszereinkkel.

Végül, a PostgreSQL kiváló skálázhatósága és teljesítménye lehetővé teszi az adatok hatékony kezelését nagy terhelés mellett is. Ezek az előnyök mind hozzájárulnak ahhoz, hogy a PostgreSQL ideális választás legyen az adatbázis-kezelési feladatainkhoz.

### ER-Diagram
![](./fejlesztoikepek/mermaid-diagram.png)

Az ER diagram (Entity-Relationship Diagram) egy grafikus ábrázolás, amely megjeleníti a valós világban létező entitások és azok közötti kapcsolatok kapcsolatát. Ezek a diagramok rendkívül hasznosak az adatbázis-tervezés során, mivel segítenek megérteni és dokumentálni az adatbázis struktúráját.

Az ER diagramok három fő összetevőből állnak: entitásokból, attribútumokból és kapcsolatokból. Az entitások olyan objektumok, amelyek léteznek és egyedileg azonosíthatók, mint például egy "Felhasználó" az alkalmazásodban. Az attribútumok az entitások tulajdonságait jelentik, például egy "Felhasználó" esetében ez lehet a név, e-mail cím és jelszó. A kapcsolatok az entitások közötti kapcsolatokat jelentik, például egy "Rendelés" entitás kapcsolódhat egy "Felhasználó" entitáshoz.

Az ER diagramok több szempontból is fontosak. Először is, segítenek az adatbázis-tervezőknek megérteni és modellezni az adatbázis struktúráját és logikáját. Emellett lehetővé teszik az adatbázis-tervezők és fejlesztők számára, hogy könnyebben kommunikáljanak az adatbázis szerkezetéről és a kapcsolatok működéséről. Az ER diagramok átlátható és strukturált dokumentációt biztosítanak, amely segíti az adatbázis karbantartását és bővítését. Végül, segítenek azonosítani és megoldani az adatbázissal kapcsolatos problémákat, mivel világosan ábrázolják az összes entitást és kapcsolatot.

Az ER diagramok különböző típusai közé tartozik a koncepcionális, a logikai és a fizikai diagram. A koncepcionális diagram magas szintű ábrázolást nyújt az adatbázis főbb entitásairól és azok kapcsolatairól, és inkább az üzleti logikára összpontosít. A logikai diagram részletesen ábrázolja az entitások és kapcsolatok logikai struktúráját, de nem tartalmazza az adatbázis specifikus részleteit. A fizikai diagram a tényleges adatbázis szerkezetet ábrázolja, beleértve a táblákat, oszlopokat és indexeket.

Az ER diagram készítésének lépései közé tartozik az entitások azonosítása, az entitásokhoz tartozó tulajdonságok meghatározása, az entitások közötti kapcsolatok azonosítása és ábrázolása, valamint az összes entitás, attribútum és kapcsolat grafikus ábrázolása.

### Normalizálás
A normalizálás lényege, hogy az adatbázisokat olyan formába hozzuk, amely minimalizálja az adat redundanciáját és maximalizálja az adat integritását. Alapvetően ez az eljárás az adatbázis szerkezetének javítására irányul, hogy elkerüljük a felesleges adatismétléseket és az inkonzisztenciákat.

A saját vizsgaremekünknél a normalizálás nagy feladat volt, mivel sok különböző adatot kellett egy összetett struktúrába szervezni. Kezdetben az adatok több táblázatban voltak szétszórva, ami számos kihívást jelentett a redundancia és az adatintegritás szempontjából.

A normalizálás folyamata során lépésről lépésre haladtunk előre. Először az első normálformát alkalmaztuk, amely az összes táblát úgy alakította át, hogy minden mező atomi legyen, azaz minden mezőben csak egy érték szerepeljen. Ezután a második normálformára léptünk át, amely biztosította, hogy minden nem kulcsmező függjön a teljes elsődleges kulcstól, nem csak annak egy részétől. Végül a harmadik normálformát alkalmaztuk, ahol kiküszöböltük az átmeneti függőségeket is, így minden nem kulcsmező közvetlenül az elsődleges kulcstól függött.

Az eredmény egy tiszta, jól szervezett adatbázis lett, amelyben minimális volt az adat redundancia, és maximális az adatintegritás. A legmagasabb normalizálási szint elérése nemcsak hogy könnyebbé teszi az adatkezelést, hanem javítja  a rendszer teljesítményét és megbízhatóságát is.

### Táblák

#### Kreta tábla
A `Kreta` tábla egy olyan entitást reprezentál, amely felhasználókhoz kapcsolódik. Minden rekord egyedi és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. Az `om` mező egy egyedi BigInt érték, amely valószínűleg jelentős azonosítóként szolgál minden Kreta entitás számára. A `name` mező a Kreta entitás nevét tárolja, legfeljebb 255 karakter hosszúságú szövegként.

A `user` mező egy egy-egy lehetséges kapcsolatot alakít ki a `User` táblával, jelezve, hogy minden Kreta entitás egyetlen felhasználóhoz kapcsolható. A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a Kreta entitást. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában.

#### User
A `User` tábla a felhasználókat reprezentálja. Minden felhasználó egyedi és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `username`, `password` és `email` mezők a felhasználónevet, jelszót és e-mail címet tárolják, mindhárom mező legfeljebb 255 karakter hosszúságú szövegként.

A `kreta` mező egy egy-egy kapcsolatot hoz létre a `Kreta` táblával, jelezve, hogy minden felhasználóhoz tartozhat egy Kreta entitás. A `roles` mező a felhasználó szerepeit tárolja, több szereppel való kapcsolattal. A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a felhasználói rekordot. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában.

A `Vote` mező a felhasználó által leadott szavazatokat, a `songs` mező a felhasználó által feltöltött dalokat, míg a `pendingSongs` mező az elbírálásra váró dalokat tárolja. A `kretaId` mező az adott felhasználóhoz tartozó Kreta entitás azonosítója.

#### Song tábla
A `Song` tábla a dalokat reprezentálja. Minden dal egyedi, és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `title` mező a dal címét tárolja, legfeljebb 255 karakter hosszúságú szövegként. A `songBucket` mező egy kapcsolatot hoz létre a `SongBucket` táblával, jelezve, hogy minden dalhoz tartozik egy dal csomag.

A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a dalt. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában. Az `uploadedBy` mező egy kapcsolatot hoz létre a `User` táblával, jelezve, hogy ki töltötte fel a dalt.

A `songBucketId` és az `uploadedById` mezők az adott dalhoz tartozó dal csomag és a feltöltő felhasználó azonosítói. A `votingSession` és a `Vote` mezők a dalhoz kapcsolódó szavazási üléseket és szavazatokat tárolják.

#### PendingSong tábla
A `PendingSong` tábla az elbírálásra váró dalokat tartalmazza. Minden elbírálásra váró dal egyedi, és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `title` mező a dal címét tárolja, legfeljebb 255 karakter hosszúságú szövegként. A `songBucket` mező egy kapcsolatot hoz létre a `SongBucket` táblával, jelezve, hogy minden elbírálásra váró dalhoz tartozik egy dal csomag.

A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára az elbírálásra váró dalt. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában. Az `uploadedBy` mező egy kapcsolatot hoz létre a `User` táblával, jelezve, hogy ki töltötte fel az elbírálásra váró dalt.

A `songBucketId` és az `uploadedById` mezők az adott elbírálásra váró dalhoz tartozó dal csomag és a feltöltő felhasználó azonosítói.

#### SongBucket tábla
A `SongBucket` tábla a dal csomagokat tartalmazza. Minden dal csomag egyedi, és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `path` mező a dal csomag útvonalát tárolja, legfeljebb 500 karakter hosszúságú szövegként. A `song` és a `pendingSong` mezők kapcsolódnak a `Song` és a `PendingSong` táblákhoz, jelezve, hogy minden dal csomaghoz tartozhat egy dal vagy egy elbírálásra váró dal.

A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a dal csomagot. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában.

#### Vote tábla
A `Vote` tábla a szavazatokat reprezentálja. Minden szavazat egyedi, és az `id` mezővel van azonosítva, amely egy automatikusan növekvő egész szám (Int). A `userId`, `songId`, és `sessionId` mezők az adott szavazathoz tartozó felhasználó, dal és szavazási ülés azonosítói, amelyek UUID-ként vannak megadva.

A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a szavazatot. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában.

A `Sound`, `User`, és `Session` mezők kapcsolatok a `Song`, `User`, és `VotingSession` táblákhoz, jelezve, hogy minden szavazat egy dalhoz, egy felhasználóhoz és egy szavazási üléshez tartozik. Ezek a mezők gondoskodnak arról, hogy a szavazatok törlődjenek, ha a kapcsolódó dal, felhasználó vagy szavazási ülés törlésre kerül.

#### VotingSession tábla
A `VotingSession` tábla a szavazási üléseket reprezentálja. Minden szavazási ülés egyedi, és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `songs` mező a szavazási üléshez kapcsolódó dalokat tárolja, míg a `songNames` mező a dalok neveit tartalmazza szövegként.

A `start` és `end` mezők az adott szavazási ülés kezdetét és végét rögzítik, időbélyegekkel. A `createdAt` és `updatedAt` mezők időbélyegek, amelyek rögzítik, hogy mikor hozták létre és mikor frissítették utoljára a szavazási ülést. Ezek a mezők alapértelmezés szerint az aktuális időbélyeget kapják a létrehozás időpontjában.

A `Vote` mező kapcsolódik a `Vote` táblához, jelezve, hogy minden szavazási üléshez tartoznak szavazatok.

#### Role tábla
A `Role` tábla a felhasználói szerepeket tárolja. Minden szerep egyedi, és az `id` mezővel van azonosítva, amely egy alapértelmezettként generált UUID. A `role` mező egy egyedi szöveges érték, amely magát a szerepkört jelöli.

A `users` mező kapcsolódik a `User` táblához, jelezve, hogy minden szerephez tartozhatnak felhasználók.

#### Kapcsolótáblák

##### _SongToVotingSession tábla
A `_SongToVotingSession` tábla a `Song` és a `VotingSession` táblák közötti kapcsolatot reprezentálja. Minden rekord egyedi és az `A` és `B` mezőkkel van azonosítva, amelyek UUID-ként vannak megadva. Az `A` mező a `Song` tábla azonosítóját, míg a `B` mező a `VotingSession` tábla azonosítóját tárolja. Ez a tábla biztosítja, hogy egy dal több szavazási üléshez is kapcsolódhasson, és egy szavazási ülés több dalt is tartalmazhasson.

##### _RoleToUser tábla
A `_RoleToUser` tábla a `Role` és a `User` táblák közötti kapcsolatot reprezentálja. Minden rekord egyedi és az `A` és `B` mezőkkel van azonosítva, amelyek UUID-ként vannak megadva. Az `A` mező a `Role` tábla azonosítóját, míg a `B` mező a `User` tábla azonosítóját tárolja. Ez a tábla biztosítja, hogy egy felhasználó több szerepkörrel is rendelkezhet, és egy szerepkör több felhasználóhoz is kapcsolódhat.

##### _prisma_migrations tábla
A `_prisma_migrations` tábla a Prisma migrációkat tárolja. Minden rekord egyedi és az `id` mezővel van azonosítva, amely egy varchar típusú érték. A `checksum` mező a migráció ellenőrző összegét tárolja, míg a `finished_at`, `rolled_back_at`, és `started_at` mezők időbélyegek, amelyek rögzítik, hogy mikor fejeződött be, mikor lett visszavonva, és mikor kezdődött el a migráció. A `migration_name` mező a migráció nevét tárolja, a `logs` mező pedig a migráció naplóit tartalmazza. Az `applied_steps_count` mező egy egész szám, amely a végrehajtott lépések számát tárolja.
