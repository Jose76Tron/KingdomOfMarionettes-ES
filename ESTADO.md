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

Auditoría completa de todos los `menu:` (`tools/audit_menu.py`,
`tools/dump_choices.py`): 19 opciones cortas que el traductor automático
había omitido (`Yes`, `Again`, `Agree`, `Eat`, `Left`, `Sit`…) traducidas a
mano con contexto, y 21 malas traducciones corregidas
(`Marque la marioneta Jester` → `Revisar la marioneta bufón`,
`Golpéalo de nuevo` → `Tocarle la mejilla otra vez`,
`Mejor para` → `Mejor parar`, minúsculas iniciales, etc.).
Ver `tools/fix_choices.py`.

Leyenda: ✅ listo · 🔄 generado por MT con glosario, pendiente de repaso ·
⏭️ no aplica.

## Limitaciones conocidas de v0.1

- La base automática puede dejar algún artículo discordante junto a
  `[title]` («un [title]» donde debería ser «una» si eres reina). Los casos
  frecuentes están corregidos; si ves uno, repórtalo con captura.
- Tono general revisado en apertura y menús; el resto mantiene glosario de
  nombres y tags verificados por `tools/comprobar.py`.
- Las voces (audio inglés) no se redoblan; solo se traduce el texto.
