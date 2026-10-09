# Kingdom of Marionettes 2.0 — Parche fan al español (ES)

Traducción no oficial del juego **Kingdom of Marionettes (v2.0)** al español,
manteniendo la esencia de cada personaje y **sin cambiar ningún nombre propio**.

> Necesitas una copia legal del juego. Este repositorio solo contiene la
> traducción (scripts `.rpy` traducidos + `tl/spanish`), nunca el juego completo
> ni sus imágenes/audio.

## Contenido

```
KOM-ES/
  README.md            este archivo
  GLOSARIO.md          nombres protegidos y tono por personaje
  ESTADO.md            avance de la traduccion por fichero
  game/                PARCHE (listo para copiar dentro de la carpeta del juego)
    script.rpy
    script day2.rpy
    choice chapter 1.rpy
    day2 choice.rpy
    character.rpy
    Animation.rpy
    tl/spanish/
      screens.rpy      menus e interfaz
      common.rpy       dialogos del motor (confirmaciones)
  tools/
    extract_rpa.py     extrae .rpy originales desde game/archive.rpa (referencia)
    translate_rpy.py   traductor EN->ES con glosario (motor GTX + cache)
    comprobar.py       verifica placeholders y sintaxis del parche
    instalar-parche.ps1
    desinstalar-parche.ps1
```

## Instalación rápida (Windows)

1. Localiza tu juego, p. ej. `C:\Users\songo\Downloads\KingdomOfMarionettes-2.0-pc`.
2. Copia la carpeta `game` de este repo **dentro** de la carpeta del juego
   (fusiona con la carpeta `game` existente). No borres `archive.rpa`.
   Los `.rpy` sueltos tienen prioridad sobre el `.rpa` y el juego pasará a
   mostrarse en español.
3. O usa el instalador (recomendado, hace copia de seguridad):

```powershell
powershell -ExecutionPolicy Bypass -File tools\instalar-parche.ps1 -Juego "C:\Users\songo\Downloads\KingdomOfMarionettes-2.0-pc"
```

4. Arranca `KingdomOfMarionettes.exe`. Si ves algún texto aún en inglés,
   abre un issue con captura y el nombre del fichero/label.

Para desinstalar (restaura la copia de seguridad):

```powershell
powershell -ExecutionPolicy Bypass -File tools\desinstalar-parche.ps1 -Juego "C:\Users\songo\Downloads\KingdomOfMarionettes-2.0-pc"
```

## Reglas de traducción

Ver `GLOSARIO.md`. Resumen:

- Nombres intactos: Jestyn, Knighter, Wizzy, Prieston, Crownus, Butley,
  Maidy, Maidra, Maidelyn, Sweetyn, Stubbornelle, Seven… y el título
  *Kingdom of Marionettes*.
- Se traducen diálogos, narración, menús y avisos. No se tocan voces,
  ficheros (`*.mp3/*.ogg/*.png`), ni `{tags}` / `[variables]`.
- Tono por personaje (Jestyn teatral y coqueto, Knighter hosco y seco,
  Wizzy nervioso y dulce, Prieston amable y sereno, Crownus inquietante).
- Español neutro con tuteo.

## Cómo se generó

1. `tools/extract_rpa.py` extrae los `.rpy` de `game/archive.rpa` (RPA-3.0).
2. `tools/translate_rpy.py` traduce con glosario de nombres + protección de
   `{tags}`/`[vars]`, con revisión humana de `character.rpy`, menús y
   primeras escenas.
3. `tools/comprobar.py` verifica que no se rompiera ningún placeholder.

## Estado

Ver `ESTADO.md`.

## Aviso legal

Parche de fans sin ánimo de lucro. Todos los derechos del juego pertenecen a
sus autores. Si eres autor y quieres retirar o adoptar esta traducción,
contacta y la retiramos o la cedemos.
