import io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.join(BASE, "../..", "game")
pats = [r"\bJester\b", r"\bKnight\b(?!er)", r"\bWizard\b", r"\bPriest\b(?!on)",
        r"\bKing Puppet\b", r"\bMaid Sisters\b", r"JEST.N\b", "MARIONETTES",
        "BOFETA", "SLAP", "OOF", "UGH", "WTF", "However", r"\bTrade\b",
        "Delay", "Se\xf1or Crownus", "Eduardo", "Bureado", "ABUCHEO",
        "Oopssy", "Ding, ding", "HUZZAA", "NOMBRE\\d", "NAME\\d"]
files = ["script.rpy", "script day2.rpy", "choice chapter 1.rpy", "day2 choice.rpy"]
n = 0
for f in files:
    for i, ln in enumerate(io.open(os.path.join(GAME, f), encoding="utf-8").read().splitlines(), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        for p in pats:
            if re.search(p, ln):
                print(f"{f}:{i}: [{p}] {ln.strip()[:130]}")
                n += 1
                break
print("TOTAL:", n)
