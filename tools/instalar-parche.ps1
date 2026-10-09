# Instala el parche ES. Funciona desde el repo (tools/) o desde el zip
# de release (junto a la carpeta game): detecta solo la ubicación.
param([Parameter(Mandatory=$true)][string]$Juego)
$ErrorActionPreference = "Stop"
$candidatos = @(
  (Join-Path $PSScriptRoot "..\game"),
  (Join-Path $PSScriptRoot "game")
)
$origen = $candidatos | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $origen) { throw "No encuentro la carpeta 'game' del parche junto al instalador." }
$destino = Join-Path $Juego "game"
$backup = Join-Path $Juego "game.bak-pre-es"
if (!(Test-Path $destino)) { throw "No existe $destino. Revisa la ruta -Juego." }
if (!(Test-Path $backup)) {
  Write-Host "Creando copia de seguridad en $backup ..."
  Copy-Item $destino $backup -Recurse
} else { Write-Host "Ya existe copia de seguridad, no se duplica." }
$ver = Get-Content (Join-Path $origen "..\..\VERSION") -ErrorAction SilentlyContinue
if (-not $ver) { $ver = Get-Content (Join-Path $PSScriptRoot "..\VERSION") -ErrorAction SilentlyContinue }
Write-Host "Instalando parche ES v$ver ..."
Copy-Item (Join-Path $origen "*") $destino -Recurse -Force
Write-Host "OK. Arranca KingdomOfMarionettes.exe (Ajustes > Idioma > Español)."
