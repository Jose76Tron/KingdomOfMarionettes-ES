# Contribuir a la traducción ES

¡Gracias por ayudar! Lee esto antes de abrir una PR: el 90% de los errores
típicos se evitan con estas reglas.

## Reglas de oro (resumen de `docs/GLOSARIO.md`)

1. **Nombres propios JAMÁS se traducen**: Jestyn, Knighter, Wizzy,
   Prieston, Crownus, Butley, Maidy, Maidra, Maidelyn, Sweetyn,
   Stubbornelle, Seven, Kingdom of Marionettes.
2. **Roles SÍ se traducen**: marioneta bufón, títere caballero, mago,
   sacerdote, doncella, Rey Marioneta (el personaje), granjero...
3. **Tuteo** general (tú). Nada de usted/vos, salvo distancia deliberada.
4. **Jugador de género elegible**: evita adjetivos generizados para el
   protagonista (`cansado/a`, `solo/a`); reformula en neutro
   (`a solas`, `sin moverme`, `me daba vergüenza`).
5. **Intocable**: `{tags}`, `[variables]`, voces (`voice`, `play ...`),
   rutas de ficheros, `jump`/`label`, comentarios de código.

## Flujo de trabajo

1. Abre (o enlaza) un issue describiendo el problema.
2. Crea una rama `fix/descripcion-corta` desde `main`.
3. Edita solo los ficheros de `game/`. No toques `original/` (referencia).
4. Pasa las verificaciones y pega su salida en la PR:
   ```powershell
   python tools/comprobar.py
   python tools/dev/check_caps.py
   python tools/dev/missing_ui.py
   ```
5. Abre la PR contra `main` completando la plantilla.

## Probar en juego

Copia tu `game/` al juego (haz copia de seguridad primero) y juega la
escena afectada. Los `.rpyc` viejos de `tl/spanish` deben borrarse para
recompilar (el instalador ya lo hace).

## Dudas de tono

Jestyn es teatral y posesivo; Knighter, seco; Wizzy, nervioso y dulce;
Prieston, sereno. Ante la duda, abre un issue y lo decidimos ahí.
