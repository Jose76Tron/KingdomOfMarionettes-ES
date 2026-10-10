# Kingdom of Marionettes 2.0 — Parche fan al español 🇪🇸

[![Release](https://img.shields.io/github/v/release/Jose76Tron/KingdomOfMarionettes-ES)](../../releases)
[![Lint](https://img.shields.io/github/actions/workflow/status/Jose76Tron/KingdomOfMarionettes-ES/lint.yml?label=checks)](../../actions)
[![Versión del juego](https://img.shields.io/badge/juego-2.0-blue)](https://github.com/Jose76Tron/KingdomOfMarionettes-ES)

Traducción no oficial de **Kingdom of Marionettes (v2.0)** al español,
manteniendo la esencia de cada personaje y los **nombres propios intactos**.
Traducido por **Jose76Tron**.

> Necesitas una copia legal del juego. Este repositorio solo contiene la
> traducción, nunca el juego completo ni sus imágenes/audio.

## 📥 Instalación

1. Descarga `KingdomOfMarionettes-ES-vX.Y.zip` de
   [**Releases**](../../releases) y descomprímelo.
2. Copia la carpeta `game` del parche **dentro** de la carpeta del juego
   (fusiona con la `game` existente). No borres `archive.rpa`.
3. Arranca `KingdomOfMarionettes.exe` → Ajustes > Idioma > **Español**.

<details>
<summary>Instalación con PowerShell (hace copia de seguridad)</summary>

```powershell
powershell -ExecutionPolicy Bypass -File tools\instalar-parche.ps1 -Juego "C:\ruta\KingdomOfMarionettes-2.0-pc"
```

Para quitarlo:

```powershell
powershell -ExecutionPolicy Bypass -File tools\desinstalar-parche.ps1 -Juego "C:\ruta\KingdomOfMarionettes-2.0-pc"
```

</details>

## 📁 Contenido

| Carpeta | Qué es |
|---|---|
| `game/` | **El parche**: guiones traducidos + `tl/spanish` + créditos + idioma. Se copia tal cual dentro del `game` del juego |
| `docs/` | `GLOSARIO.md` (nombres, tonos, reglas) y `ESTADO.md` (avance y metodología) |
| `tools/` | Instalador, desinstalador, verificación y generador de releases |
| `tools/dev/` | Utilidades puntuales de desarrollo (auditorías, repasos aplicados) |
| `.github/` | Plantillas de issue/PR y automatización (checks + releases) |

La carpeta se llama `game` a propósito: su contenido se fusiona con la
carpeta `game` del juego. Los `.rpy` sueltos tienen prioridad sobre el
`archive.rpa`, así que no hay que tocar nada más. Las voces siguen en
inglés (solo se traduce texto).

## 🌐 Nota sobre idiomas

La historia está traducida de base: **Español = juego 100% en español**.
English/Chinese cambian la interfaz, pero los diálogos siguen en español.

## 🤝 Contribuir

¿Viste una frase rara o mal traducida? Abre un issue con la plantilla de
**error de traducción** (versión, frase exacta o captura). Si quieres
proponer cambios, lee [CONTRIBUTING.md](CONTRIBUTING.md) y abre una PR —
hay checks automáticos y una checklist.

## ⚖️ Aviso legal

Parche de fans sin ánimo de lucro. Todos los derechos del juego pertenecen a
sus autores. Si eres autor y quieres retirar o adoptar esta traducción,
contacta y la retiramos o la cedemos.
