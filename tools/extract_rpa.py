"""Extrae los .rpy originales desde game/archive.rpa (Ren'Py 8 / RPA-3.0).
Uso:
  python tools/extract_rpa.py "C:\\ruta\\KingdomOfMarionettes-2.0-pc" [--solo-rpy]
Genera: original/<ficheros.rpy> (solo referencia, no se distribuye).
"""
import os, sys, zlib, pickle

def read_index(rpa_path):
    with open(rpa_path, "rb") as f:
        header = f.read(40)
        offset = int(header[8:24], 16)
        key = int(header[25:33], 16)
        f.seek(offset)
        index = pickle.loads(zlib.decompress(f.read()))
    return index, key

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\songo\Downloads\KingdomOfMarionettes-2.0-pc"
    rpa = os.path.join(base, "game", "archive.rpa")
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "original")
    os.makedirs(out, exist_ok=True)
    index, key = read_index(rpa)
    n = 0
    with open(rpa, "rb") as f:
        for name in sorted(index.keys()):
            if not name.endswith(".rpy"):
                continue
            entry = index[name][0]
            off, leng = entry[0] ^ key, entry[1] ^ key
            prefix = b""
            if len(entry) == 3 and entry[2]:
                s = entry[2]
                prefix = s.encode("latin-1") if isinstance(s, str) else s
            f.seek(off)
            data = prefix + f.read(leng)
            dest = os.path.join(out, name)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as o:
                o.write(data)
            n += 1
            print(f"{name} ({len(data)} bytes)")
    print(f"OK: {n} ficheros .rpy en {out}")

if __name__ == "__main__":
    main()
