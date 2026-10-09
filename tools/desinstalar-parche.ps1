param([Parameter(Mandatory=$true)][string]$Juego)
$ErrorActionPreference = "Stop"
$destino = Join-Path $Juego "game"
$backup = Join-Path $Juego "game.bak-pre-es"
# El parche solo añade .rpy sueltos + tl/spanish; para desinstalar basta borrarlos.
$sueltos = @("script.rpy","script day2.rpy","choice chapter 1.rpy","day2 choice.rpy","character.rpy","Animation.rpy","screens.rpy","fijar_espanol.rpy","creditos_es.rpy")
foreach ($f in $sueltos) {
  $p = Join-Path $destino $f
  if (Test-Path $p) { Remove-Item $p -Force; Write-Host "Quitado $f" }
}
$tl = Join-Path $destino "tl\spanish"
if (Test-Path $tl) { Remove-Item $tl -Recurse -Force; Write-Host "Quitado tl/spanish" }
Write-Host "OK. Juego restaurado al inglés. (Copia completa en $backup si la necesitas.)"
