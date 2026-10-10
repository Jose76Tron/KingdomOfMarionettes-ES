# Estado de la traducción (v0.1)

| Fichero | Líneas | Cadenas | Estado |
|---|---|---|---|
| `game/character.rpy` | 204 | ~40 | ✅ Traducido y revisado a mano |
| `game/tl/spanish/screens.rpy` | — | 35 | ✅ Revisado a mano |
| `game/tl/spanish/common.rpy` | — | 35 | ✅ Revisado a mano |
| `game/Animation.rpy` | 951 | 0 | ✅ Sin texto (copia directa) |
| `game/script.rpy` | 1043 | 373 | ✅ Base MT + repaso manual de apertura |
| `game/choice chapter 1.rpy` | 1703 | 602 | ✅ Base MT + micro-repaso |
| `game/day2 choice.rpy` | 3480 | 1547 | ✅ Base MT + corrección `[title]` |
| `game/script day2.rpy` | 4451 | 1917 | ✅ Base MT + micro-repaso |
| `options.rpy / gui.rpy / screens.rpy` | — | — | ⏭️ No se tocan (solo config; la UI va por `tl/spanish`) |

Verificación automática (`tools/comprobar.py` + `check_qa.py`): ✅
nombres propios intactos al 100% (Jestyn 290/290, Knighter 111/111…),
placeholders `[player_call]/[title]/[poss]/[subj]` y `{tags}` íntegros,
cero líneas con comillas rotas.

## v0.2 — opciones de menú
Auditoría completa de todos los `menu:` (`tools/dev/audit_menu.py`,
`tools/dev/dump_choices.py`): 19 opciones cortas que el traductor automático
había omitido (`Yes`, `Again`, `Agree`, `Eat`, `Left`, `Sit`…) traducidas a
mano con contexto, y 21 malas traducciones corregidas
(`Marque la marioneta Jester` → `Revisar la marioneta bufón`,
`Golpéalo de nuevo` → `Tocarle la mejilla otra vez`,
`Mejor para` → `Mejor parar`, minúsculas iniciales, etc.).
Ver `tools/dev/fix_choices.py`.

## v0.3 — revisión exhaustiva manual (sin MT)

Metodología: barrido programático local (`tools/dev/revision_qa.py`: restos de
inglés, ratios, duplicados, tags, inconsistencias) + revisión semántica
humana línea a línea con 6 revisores en paralelo sobre los 4 guiones
completos (~4400 cadenas), verificando cada cambio contra el original.

- 62 correcciones lote 1 (`tools/dev/fix_revision1.py`): líneas sin traducir
  (`[poss] majesty is super-duper cute too...`, `{color}Here{/color}`,
  `Now...`), roles en inglés (King/Wizard/Knight/Priest Puppet, placas
  Jester/Knight), `cama tamaño king` → `king size`, `date` → `cita`,
  SFX (`SLAP` → `¡ZAS!`), concordancias (`ruidosa`, `[gend] mío`).
- ~200 correcciones lote 2 (`tools/dev/fix_revision2.py`): tuteo sistemático
  (usted → tú en Jestyn, Wizzy, Maidy, Prieston...), género (Maidy/Maidra/
  Maidelyn en femenino, jugador con formas neutras: `superadorable`,
  `a solas`, `sin moverme`), falsos amigos (`Easy now` → `Tranquilo`,
  `mudarse` → `moverse`, `feast` → `banquete`, `collar` → collar/collar
  de camisa según contexto, `brat taming` → `doma del malcriado`,
  `yap` → `parlotear`, `will` → `voluntad`), nombres con tilde
  fantasma (`JESTÍN` → `JESTYN`, 11×), `WARNING`/`Jumpscare`/`Delay`/
  `Run`/`Correct`/`However`/`Trade`/`Brat`/`Done` sin traducir,
  título `REINO DE LAS MARIONETTES` → `KINGDOM OF MARIONETTES`.
- Lote 3: restos menores + 4 comillas de cierre que faltaban (habrían
  roto el juego).
- Verificación final: nombres 100% (única diferencia: un "Butley"
  duplicado eliminado a posta), tags íntegros, 0 comillas rotas,
  `tools/comprobar.py` limpio.

## v0.4 — interfaz completa, menús y crédito

- `tl/spanish/screens.rpy` ampliado de 53 a 148 cadenas: preferencias
  (pantalla, volúmenes, transiciones...), ayuda de teclado/ratón/mando,
  `Prefs`, `End Replay`, `Main Menu`, `Language`, `Upload/Download Sync`,
  `The dialogue history is empty.`, `Version`, `Made with Ren'Py...`,
  carga (`empty slot` → `hueco vacío`, formato de fecha español
  + días/meses traducidos) y `Calibrate/Menu/Y-Top Button` que faltaban.
  Cobertura verificada con `tools/dev/missing_ui.py` (84/84 en uso).
- Menús de elección re-auditados con volcado completo (`dump_choices.py`
  reescrito): 20 minúsculas/rarezas corregidas (`mira la televisión` →
  `Mirar la televisión`, `Déjalo deslizar` → `Déjalo pasar`,
  `Lo haré. duro` → `Lo haré. Duro.`, `Eso es suficiente`, `Tengo sueño...`,
  `rey títere` residual → `Rey Marioneta`) + chequeo permanente
  `tools/dev/check_caps.py`.
- `game/creditos_es.rpy`: la pantalla Acerca de muestra
  "Traducción fan al español: Jose76Tron".

## v0.5 — selector de idioma Español

- El juego ya traía selector English/Chinese en Ajustes > Idioma; el
  parche añade el botón **Español** (`game/screens.rpy`, 1 línea sobre
  el original) + arranque por defecto en español (`fijar_espanol.rpy`).
- Nota de diseño: la historia está traducida en los propios guiones,
  así que **Español = juego 100% en español**. English/Chinese cambian
  la interfaz pero la historia sigue en español (limitación conocida).

Leyenda: ✅ listo · 🔄 generado por MT con glosario, pendiente de repaso ·
⏭️ no aplica.

## Limitaciones conocidas de v0.1

- La base automática puede dejar algún artículo discordante junto a
  `[title]` («un [title]» donde debería ser «una» si eres reina). Los casos
  frecuentes están corregidos; si ves uno, repórtalo con captura.
- Tono general revisado en apertura y menús; el resto mantiene glosario de
  nombres y tags verificados por `tools/comprobar.py`.
- Las voces (audio inglés) no se redoblan; solo se traduce el texto.
