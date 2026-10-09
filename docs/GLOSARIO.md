# Glosario y guía de estilo — Kingdom of Marionettes ES

## 1. Nombres: NO se traducen jamás

| Original | ES | Notas |
|---|---|---|
| Jestyn | Jestyn | protagonista marioneta bufón. No "Burlón". |
| Knighter | Knighter | No "Caballero". Hosco, cortante. |
| Wizzy | Wizzy | Mago real. No "Maguito". |
| Prieston | Prieston | No "Cura/Sacerdote". Amable y sereno. |
| Crownus | Crownus | Entidad inquietante. Mantener mayúsculas/tono. |
| Butley | Butley | Mayordomo. No "Mayordomo". |
| Maidy, Maidra, Maidelyn, The Maids | igual | Doncellas. "The Maids" → "Las Doncellas" solo como etiqueta genérica si habla el grupo; nombres propios intactos. |
| You (u/mc) | Tú | El jugador. `player_call` por defecto `Seven`. |
| Seven | Seven | Nombre por defecto del jugador. No "Siete". |
| Sweetyn | Sweetyn | Apodo que Jestyn da si te llamas Jestyn. No traducir. |
| Stubbornelle / Stubornelle | igual (respetar la grafía original del fichero) | Apodo-castigo. No "Testaruda". |
| Kingdom of Marionettes | igual | Título del teatro/juego. |
| Farmer, Debt collector, Narrator, Puppet | Granjero, Cobrador, Narrador, Marioneta | Son roles genéricos, SÍ se traducen. |
| Puppet 1..4, Butler Puppet, Jester puppet, Knight puppet | Marioneta 1..4, Marioneta mayordomo, Marioneta bufón, Marioneta caballero | Roles, se traducen. |
| Jestyn & Knighter, Everyone | Jestyn y Knighter, Todos | Mantener nombres dentro. |

Si el motor de traducción automática propone "Caballero" para Knighter o
"Bufón" para Jestyn como nombre, se rechaza: son nombres propios.

## 2. Tono por personaje (esencia)

- **Jestyn**: teatral, juguetón, coqueto y posesivo. Tutea, usa diminutivos
  oscuros ("dulzura", "cielito"), ríe en escena. En ES mantiene muletillas
  como "Oh", "Mmm", "Tatatatá~". Nunca suena neutro ni formal.
- **Knighter**: seco, hosco, gruñón con fondo protector. Frases cortas.
  No usa exclamaciones alegres.
- **Wizzy**: nervioso, dulce, tartamudea un poco cuando se asusta.
  Interjecciones suaves.
- **Prieston**: sereno, amable, hospitalario. Habla pausado.
- **Crownus**: inquietante, susurrante. Frases fragmentadas, elipsis.
- **Narrador / Tú (monólogo)**: coloquial, joven, con humor cansado.
  Tuteo y español neutro (sin modismos regionales fuertes).

## 3. Tratamiento

- Tuteo general (tú). Nada de "vos" ni "usted" salvo que Prieston marque
  distancia en una escena concreta.
- Género del jugador: el juego usa `subj/obj/poss/refl/title/gend`
  (she/he/they). En ES se mantiene el sistema con pronombres
  ella/él/elle y títulos reina/rey/gobernante. Ver `character.rpy`.

## 4. Formato Ren'Py: intocable

- `{size=..}`, `{color=..}`, `{cps=..}`, `{b}`, `{i}`, `{/...}`, `\n`,
  `[player_call]`, `[subj]`, `[title]`… se conservan tal cual.
- `voice "..."`, `play music/sound "..."` y rutas de imagen nunca se traducen.
- `menu:` — se traduce el texto visible, nunca el `jump`/`label`.
- Comentarios de código en inglés/indonesio se dejan como están.

## 5. Palabras recurrentes

| EN | ES |
|---|---|
| security guard | guardia de seguridad |
| stage | escenario |
| storage room | almacén |
| corridor | pasillo |
| puppet | marioneta / títere (preferir **marioneta**) |
| master | amo (solo si es rol, nunca como nombre) |
| save / load | guardar / cargar |
| preferences | ajustes |
| quit | salir |
| back | atrás |
| skip | saltar |
| auto | auto |
| history | historial |
| Are you sure? | ¿Seguro? |
