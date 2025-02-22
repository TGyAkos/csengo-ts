@echo off

echo Replacing /data/audio with the current working directory + /assets/audio in initdb_bat_local.sql...
set "current_dir=%cd%"
set "search=/data/audio/"
set "replace=%current_dir:/=\%\assets\audio\"
powershell -Command "(Get-Content assets\initdb_bat.sql) -replace [regex]::Escape('%search%'), '%replace%' | Set-Content assets\initdb_bat_local.sql"

set installer_url="https://sbp.enterprisedb.com/getfile.jsp?fileid=1259408"
set installer_path="./postgresql-16.8-1-windows-x64.exe"
set exe_name="postgresql-16.8-1-windows-x64.exe"

if not exist %installer_path% (
  echo Downloading postgres installer...
  curl -L -o %installer_path% %installer_url%
) else (
  echo Installer already exists.
)

echo Running the installer...
start /wait %installer_path% %exe_name%
echo Installation completed.

echo Setting up the database...
setlocal
set PATH=%PATH%;C:\Program Files\PostgreSQL\16\bin
set PGDATA=C:\Program Files\PostgreSQL\16\data
set PGDATABASE=postgres
set PGUSER=postgres
set PGPASSWORD=csengo
set PGPORT=5582

echo Replacing /data/audio with the current working directory + /assets/audio in initdb_bat_local.sql...
set "current_dir=%cd%"
set "search=/data/audio/"
set "replace=%current_dir:/=\%\assets\audio\"
powershell -Command "(Get-Content assets\initdb_bat.sql) -replace [regex]::Escape('%search%'), '%replace%' | Set-Content assets\initdb_bat_local.sql"

echo Connecting to the PostgreSQL database...
psql -U %PGUSER% -d %PGDATABASE% -f assets\initdb_bat_local.sql

echo Done setting up the database.
endlocal

:: echo Starting the server...
:: cd "./csengo-ts-server-v2"
:: echo Setting up .env file...
:: copy .env.example .env
:: echo Installing dependencies...
:: call npm install
:: echo Migrating prisma schema...
:: call npm run prisma:update:prod
:: echo Starting the server...
:: npm run start:dev

start cmd /k "echo Starting the server... & cd /d \"./csengo-ts-server-v2\" & echo Setting up .env file... & copy .env.example .env & echo Installing dependencies... & call npm install & echo Migrating prisma schema... & call npm run prisma:update:prod & echo Starting the server... & npm run start:dev"

:: echo Starting the client...
:: cd "../csengo-ts-client-v2"
:: echo Setting up .env file...
:: copy .env.example .env
:: echo Installing dependencies...
:: call npm install
:: echo Starting the client in dev mode...
:: npm run dev

start cmd /k "echo Starting the client... & cd /d \"../csengo-ts-client-v2\" & echo Setting up .env file... & copy .env.example .env & echo Installing dependencies... & call npm install & echo Starting the client in dev mode... & npm run dev"
