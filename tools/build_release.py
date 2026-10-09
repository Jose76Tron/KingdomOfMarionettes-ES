"""Genera el zip publicable del parche (lo que se sube a GitHub Releases).
Uso:  python tools/build_release.py [--salida release]
Estructura del zip:
  KingdomOfMarionettes-ES-vX.Y/
    LEEME.txt            instrucciones + creditos + version
    game/                copia exacta de parche/game/
    instalar-parche.ps1
    desinstalar-parche.ps1
"""
import os, sys, zipfile, hashlib, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = open(os.path.join(BASE, "VERSION"), encoding="utf-8").read().strip()
NOMBRE = f"KingdomOfMarionettes-ES-v{VERSION}"

LEEME = """Kingdom of Marionettes 2.0 — Parche fan al español v{ver} ({fecha})
Traducido por Jose76Tron. Parche sin ánimo de lucro; necesitas el juego original.

INSTALACIÓN
1. Descomprime este zip donde quieras.
2. Copia la carpeta "game" DENTRO de la carpeta del juego
   (p. ej. KingdomOfMarionettes-2.0-pc), fusionando con la existente.
   No borres archive.rpa.
   (Alternativa: ejecuta instalar-parche.ps1 con clic derecho >
   "Ejecutar con PowerShell" teniéndolo junto a la carpeta game...
   lo más fiable es la copia manual o el instalador con -Juego.)
3. Arranca KingdomOfMarionettes.exe. Ajustes > Idioma > Español.

DESINSTALAR
- Borra de la carpeta game del juego los .rpy sueltos y tl/spanish,
  o ejecuta desinstalar-parche.ps1 -Juego "<ruta del juego>".

NOTA: la historia está traducida de base (Español = 100% español).
English/Chinese cambian la interfaz; los diálogos siguen en español.
""".format(ver=VERSION, fecha=datetime.date.today().isoformat())

def main():
    salida = sys.argv[sys.argv.index("--salida") + 1] if "--salida" in sys.argv else os.path.join(BASE, "release")
    os.makedirs(salida, exist_ok=True)
    zip_path = os.path.join(salida, NOMBRE + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(NOMBRE + "/LEEME.txt", LEEME.encode("utf-8"))
        for raiz, _, fichs in os.walk(os.path.join(BASE, "game")):
            for f in sorted(fichs):
                p = os.path.join(raiz, f)
                rel = os.path.relpath(p, BASE)
                z.write(p, NOMBRE + "/" + rel.replace(os.sep, "/"))
        for s in ["instalar-parche.ps1", "desinstalar-parche.ps1"]:
            z.write(os.path.join(BASE, "tools", s), NOMBRE + "/" + s)
    sha = hashlib.sha256(open(zip_path, "rb").read()).hexdigest()
    print("zip:", zip_path)
    print("sha256:", sha)
    print("ficheros:", len(zipfile.ZipFile(zip_path).namelist()))

if __name__ == "__main__":
    main()
