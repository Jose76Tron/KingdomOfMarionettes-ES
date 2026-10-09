# Kingdom of Marionettes 2.0 — Parche fan al español

Traducción no oficial al español, con la esencia de cada personaje y
**nombres propios intactos** (Jestyn, Knighter, Wizzy, Prieston, Crownus...).
Traducido por **Jose76Tron**.

> Necesitas una copia legal del juego. Este parche solo contiene la
> traducción, nunca el juego completo ni sus imágenes/audio.

## Instalación en 1 minuto

1. Descarga `KingdomOfMarionettes-ES-vX.Y.zip` de la sección
   [Releases](../../releases) y descomprímelo.
2. Copia la carpeta `game` del parche **dentro** de la carpeta del juego
   (fusiona con la `game` que ya existe). No borres `archive.rpa`.
3. Arranca `KingdomOfMarionettes.exe`. En Ajustes > Idioma puedes elegir
   entre English, Chinese y **Español** (el juego arranca en español).

O con instalador (hace copia de seguridad en `game.bak-pre-es`):

```powershell
powershell -ExecutionPolicy Bypass -File tools\instalar-parche.ps1 -Juego "C:\ruta\KingdomOfMarionettes-2.0-pc"
```

Para quitarlo:

```powershell
powershell -ExecutionPolicy Bypass -File tools\desinstalar-parche.ps1 -Juego "C:\ruta\KingdomOfMarionettes-2.0-pc"
```

## Contenido del repositorio

```
KOM-ES/
  README.md / CHANGELOG.md / VERSION   portada, historial y versión
  game/          PARCHE (réplica exacta de la carpeta game del juego:
                 guiones traducidos + tl/spanish + créditos + idioma)
  docs/          GLOSARIO.md (nombres y tonos) y ESTADO.md (avance)
  tools/         instalador, desinstalador y herramientas de desarrollo
  .github/       publicación automática de releases
```

La carpeta se llama `game` a propósito: su contenido se copia tal cual
dentro de la carpeta `game` del juego. Los `.rpy` sueltos tienen prioridad
sobre el `archive.rpa`, así que el juego muestra el español sin tocar nada
más. Las voces siguen en inglés (solo se traduce texto).

## Nota sobre idiomas

La historia está traducida de base: **Español = juego 100% en español**.
English/Chinese cambian la interfaz pero los diálogos siguen en español.

## Desarrollo

Ver `docs/ESTADO.md` (metodología y avance) y `docs/GLOSARIO.md` (reglas).
Para generar el zip publicable:

```powershell
python tools\build_release.py
```

## Aviso legal

Parche de fans sin ánimo de lucro. Todos los derechos del juego pertenecen a
sus autores. Si eres autor y quieres retirar o adoptar esta traducción,
contacta y la retiramos o la cedemos.
