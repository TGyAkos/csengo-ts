# Felhasználói
## Rövid bemutatás

Üdvözöllek!

A Pollák Csengő webalapú alkalmazást tartja a kezében, amely lehetőséget biztosít az iskolák számára online szavazások lebonyolítására. A diákok ezen szavazások segítségével hozzájárulhatnak egy kényelmesebb és vonzóbb iskola környezet kialakításához, folyamatosan változó csengőhangok választásával. 

A szoftver alapvető funkciói között szerepel a belépés és regisztráció lehetősége. Ha még nem regisztrált, egyszerűen létrehozhatja a fiókját, majd bejelentkezhet az oldalra, hogy hozzáférést kapjon a funkciókhoz.

A weboldalon történő belépést követően lehetősége van kedvenc zenéinek feltöltésére, amelyeket a weboldal kezelője bírál el, és szükség esetén bevon a szavazásba. Ezen kívül megtekintheti az előző szavazás nyertes zenéjét, valamint amennyiben aktív szavazás folyik, lehetősége van a zenéket egyesével meghallgatni, és szavazni az Ön által kedvelt darabokra.

Amennyiben Admin jogosultsággal rendelkező fiókkal rendelkezik, a felhasználói ikonra kattintva megjelenik az „Admin” gomb, amely segítségével elérheti a kezelőpanelt. A kezelőpanel oldalán lehetősége nyílik az összes elfogadott zene megtekintésére és meghallgatására, valamint az elfogadásra váró zenék megtekintésére és meghallgatására. Ezen kívül lehetősége van a szavazások és a felhasználók kezelésére is.

Köszönjük, hogy a Pollák Csengőt választotta! Élvezze a zenét és a szavazásokat, és hozza létre együtt a tökéletes iskola hangulatot!

Üdvözlettel,
Pollák Csengő csapata

## Harver szükséglet átlagos felhasználónak

A Pollák Csengő webalkamazás viszonylag mérsékelt hardverigényekkel rendelkezik amely hasonló a napjainkba használt modern oldalkhoz mint például a Facebook, de a jobb felhasználói élmény érdekében az alábbi minimum és ajánlott konfigurációk figyelembevételével kell biztosítani a megfelelő eszközöket:

**Processzor (CPU):**

- Minimum: 1.6 GHz-es kétmagos processzor (Intel Core i3, AMD Ryzen 3) 
- Ajánlott: 2.5 GHz vagy gyorsabb négymagos processzor (Intel Core i5 / i7, AMD Ryzen 5)

**Memória (RAM):**

- Minimum: 4 GB RAM 
- Ajánlott: 8 GB RAM vagy több

**Videokártya (GPU):**
 
- Minimum: Integrált videokártya (Intel HD Graphics, AMD Vega) 
- Ajánlott: Dedikált videokártya (NVIDIA GeForce GTX Széria, AMD Radeon RX Széria)

**Tárhely:**

- Minimum: 20 GB szabad hely a rendszer és az alkalmazások számára 
- Ajánlott: SSD meghajtó, 256 GB vagy több

**Képernyőfelbontás:**

- Minimum: 600x600 
- Ajánlott: 1920x1080 (Full HD) vagy magasabb

## Szoftver szükséglet átlagos felhasználónak

A Pollák Csengő webalkalmazás optimális működéséhez a következő szoftverek és technológiai környezetek szükségesek:

**Webböngészők és Verziók:**

- Google Chrome: Minimum 85-ös verzió, ajánlott 110+ verzió
- Mozilla Firefox: Minimum 80+ verzió, ajánlott 100+ verzió
- Microsoft Edge: Minimum 85-ös verzió, ajánlott 110+ verzió
- Safari: Minimum 13-as verzió, ajánlott 14+ verzió
- A böngészők legfrissebb verzióinak használatát javasoljuk, mivel azok biztosítják a legújabb biztonsági frissítéseket és a legjobb teljesítményt.

**Operációs rendszerek:**

- Windows: Minimum 10-es verzió, ajánlott 11-es verzió
- macOS: Minimum Mojave (10.14), ajánlott Monterey (12.0) vagy újabb
- Linux: Ubuntu 20.04 vagy újabb verzió
- Mobil eszközök: iOS 14 vagy Android 10 és újabb verziók

**JavaScript, TypeScript és HTML5 Támogatás:**

A Pollák Csengő alkalmazás a Vue.js, JavaScript/TypeScript és HTML5 technológiákat használ a dinamikus funkciók és interaktív elemek biztosításához. A böngészőknek támogatniuk kell a JavaScript/TypeScript futtatását, valamint az HTML5 szabványokat a helyes működéshez.

**Multimédia Támogatás:**

A webalkalmazás zenék feltöltésére, meghallgatására és szavazásra is lehetőséget biztosít. Az alábbi multimédia formátumok és technológiák szükségesek:

- HTML5 Audio: Az alkalmazás audio fájlokat használ a zenék lejátszásához, így a böngészőnek támogatnia kell az HTML5 Audio API-t.
- MP3: Az elfogadott zenei formátumok közé tartozik az MP3.
  
**Biztonság és Adatvédelem:**

A Pollák Csengő alkalmazás biztonságos használata érdekében javasoljuk a következő biztonsági intézkedések betartását:

- HTTPS: Az alkalmazás minden adatátvitele titkosított HTTPS kapcsolaton keresztül történik. Győződjön meg arról, hogy böngészője támogatja az SSL/TLS titkosítást.
- Cookie-k: Az alkalmazás használatának részeként a böngészőnek támogatnia kell a cookie-kat, hogy a felhasználói élmény zökkenőmentes legyen (pl. a bejelentkezett állapot tárolása).

## Hardver szükséglet a futtatáshoz

GYULA

## Szoftver szükséglet a futtatáshoz

GYULA

## Letöltés, Telepítés és Elindítás

GYULA

## Ismertetés

A webalkalmazás lebontása:
- Toast [Értesítési ablak]
- Regisztráció [Oldal]
- Bejelentkezés [Oldal]
- Kezdőlap [Oldal]
- Admin [Oldal]
 - - Zenék [Menűpont]
 - - Elfogadásra váró zenék [Menűpont]
 - - Felhasználók [Menűpont]
 - - Sessions [Menűpont]
 - - Egyebek [Menűpont]

### Toast értesítési ablak

A Toast menü biztosítja a felhasználó étesültségét a háttérben történő dolgokrol. Minden esetben a kijelző jobb alsó sakéban ugrik fel. Ha siekres akkor zöld, ha csak figyelmeztetés akkor sárga és ha pobléma tötént akkor prios szinben jelenik meg. Minden esteben tartalmazza a pontos üzenetet arról, hogy mi történt.

### Regisztrációs oldal

A regisztrációs oldal biztosítja a gyors és egyszerű regisztrációs folyamatot. Az oldal a következő útvonalon érhető el: [/register].

Az oldal megnyitásakor a felhasználók egy központi elrendezésű felületet látnak, amely 4 beviteli mezőt és 1 gombot tartalmaz. A beviteli mezők a következő adatokat és kikötéseket kérik a felhasználótól:

- **Felhasználónév**
- - Nem lehet üres
- - Minimum 5 karakter hosszú
- - Maximum 30 karakter hosszú
  
- **Email cím**
- - Nem lehet üres
- - Csak érvényes email cím lehet
  
- **OM azonosító**
- - Nem lehet üres
- - Csak szám lehet
- - Csak érvényes, adatbázisban feljegyett azonosító lehet
  
- **Jelszó**
- - Nem lehet üres
- - Minimum 6 karakter hosszú
- - Maximum 20 karakter hosszú 

Minden mező felett látható a szükséges adat megnevezése.

A regisztrációs űrlap kitöltését követően, ha a felhasználó rákattint a Regisztráció gombra, sikeres regisztráció esetén a felhasználó átirányításra kerül a főoldalra. Ha a regisztráció nem sikerül, egy hibaüzenet jelenik meg egy toast értesítés formájában a képernyő jobb alsó sarkában, amely tartalmazza a hiba okát.
   
