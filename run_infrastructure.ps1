# run_infrastructure.ps1
$root = (Get-Item .).FullName
$phpPath = "$root\server\php\php.exe"
$mysqlPath = "$root\server\mariadb\bin\mysqld.exe"
$wwwRoot = "$root\server\www"

Write-Host "Starting MariaDB..." -ForegroundColor Cyan
Start-Process -FilePath $mysqlPath -ArgumentList "--datadir=$root\server\mariadb\data --console" -WindowStyle Hidden -PassThru

Write-Host "Waiting for MariaDB to start..."
Start-Sleep -Seconds 5

Write-Host "Creating Joomla database..." -ForegroundColor Cyan
& "$root\server\mariadb\bin\mysql.exe" -u root -e "CREATE DATABASE IF NOT EXISTS joomla_db;"

Write-Host "Starting PHP server at http://localhost:8080..." -ForegroundColor Green
Start-Process -FilePath $phpPath -ArgumentList "-S localhost:8080 -t $wwwRoot" -WindowStyle Hidden

Write-Host "Ready! You can now access http://localhost:8080 to finish Joomla installation." -ForegroundColor Yellow
Write-Host "Database Name: joomla_db"
Write-Host "User: root"
Write-Host "Password: (empty)"
Write-Host "Host: localhost"
