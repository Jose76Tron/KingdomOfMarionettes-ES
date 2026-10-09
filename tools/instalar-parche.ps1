# Requiere -Juego con la ruta del juego instalado.
param([Parameter(Mandatory=$true)][string]$Juego)
$ErrorActionPreference = "Stop"
$origen = Join-Path $PSScriptRoot "..\game"
$destino = Join-Path $Juego "game"
$backup = Join-Path $Juego "game.bak-pre-es"
if (!(Test-Path $destino)) { throw "No existe $destino. Revisa la ruta -Juego." }
if (!(Test-Path $backup)) {
  Write-Host "Creando copia de seguridad en $backup ..."
  Copy-Item $destino $backup -Recurse
} else { Write-Host "Ya existe copia de seguridad, no se duplica." }
Write-Host "Instalando parche ES ..."
Copy-Item (Join-Path $origen "*") $destino -Recurse -Force
Write-Host "OK. Arranca KingdomOfMarionettes.exe para jugar en español."
Write-Host "Si algo falla, restaura con desinstalar-parche.ps1 o borrando los .rpy sueltos."
