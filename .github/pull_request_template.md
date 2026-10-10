## Qué corrige esta PR

<!-- Enlaza el issue: Closes #NN -->

## Checklist del traductor

- [ ] Nombres propios intactos (Jestyn, Knighter, Wizzy, Prieston, Crownus, Butley, maids, título del juego)
- [ ] Roles traducidos donde toca (bufón, caballero, mago, sacerdote, doncella, Rey Marioneta)
- [ ] Tuteo coherente; sin adjetivos generizados para el jugador
- [ ] `{tags}` y `[variables]` intactos; sin tocar voces, rutas ni `jump`/`label`
- [ ] Probado en juego (escena afectada jugada)
- [ ] Checks en verde (pega la salida):
  - `python tools/comprobar.py`
  - `python tools/dev/check_caps.py`
  - `python tools/dev/missing_ui.py`

## Capturas (si aplica)

<!-- Antes / después -->
