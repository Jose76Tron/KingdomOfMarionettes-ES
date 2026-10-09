"""Repaso manual: aplica traducciones curadas (calidad humana) sobre la base MT.
Uso: python tools/repaso_manual.py
Lee tools/mt_cache.json para localizar el texto MT y sustituirlo por la
version curada. Idempotente: se puede ejecutar varias veces.
"""
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(BASE, "game")
CACHE = os.path.join(BASE, "tools", "mt_cache.json")

# EN original (clave tal cual aparece entre comillas en el .rpy) -> ES curado.
CURADAS = {
    "Who would've thought I'd end up trapped in a situation this strange?":
        "¿Quién iba a pensar que acabaría atrapado en una situación tan extraña?",
    "It all started because I was desperately looking for a job.":
        "Todo empezó porque buscaba trabajo a la desesperada.",
    "Of course I was desperate. My savings were running low, and I still had countless living expenses plus debt to pay.":
        "Y no era para menos. Mis ahorros se agotaban y aún tenía un montón de gastos y deudas por pagar.",
    "I applied to all kinds of places, but it felt like luck absolutely hated me":
        "Eché currículums en todas partes, pero parecía que la suerte me odiaba.",
    "In a situation like this, I no longer cared what kind of job it was, as long as it paid. Cleaning toilets, catching bears...I'd do anything.":
        "A esas alturas ya me daba igual el trabajo mientras pagaran. Limpiar baños, atrapar osos... haría lo que fuera.",
    "That's when I found this job online...":
        "Fue entonces cuando encontré este trabajo en internet...",
    "A security position at an abandoned theater. Seriously, why would a place that no longer operates even need a security guard?":
        "Vigilante en un teatro abandonado. En serio, ¿para qué querría un sitio cerrado un guardia de seguridad?",
    "Kingdom of Marionettes. I'd heard this place used to be famous for its puppet performances long ago.":
        "Kingdom of Marionettes. Había oído que este sitio fue famoso hace tiempo por sus espectáculos de marionetas.",
    "Oh. Only three duties. Duty number one: keep the theater safe from vandals. Hmm.... I could probably manage that.":
        "Oh. Solo tres tareas. Tarea uno: mantener el teatro a salvo de vándalos. Mmm... eso creo que puedo hacerlo.",
    "Duty number two: clean the theater. That's technically outside a security guard's job, but whatever as long as it pays.":
        "Tarea dos: limpiar el teatro. Eso no es muy de guardia de seguridad, pero bueno, mientras paguen...",
    "Duty number three: make sure none of the puppets are missing and walking around.":
        "Tarea tres: asegurarse de que no falte ninguna marioneta y de que no anden por ahí.",
    "Hmm. Maybe I'm so sleep-deprived that I misread it.":
        "Mmm. Será que he dormido tan poco que lo he leído mal.",
    "Make sure none of the puppets are missing...and walking around.":
        "Que no falte ninguna marioneta... y que no anden por ahí.",
    "W-wait. Walking around?? Make sure there are no puppets walking around?? What does that even mean?!":
        "E-espera. ¿Que anden por ahí? ¿¡Que me asegure de que no haya marionetas andando por ahí!? ¿¡Qué significa eso!?",
    "Hahaha... maybe they meant making sure no one steals the puppets. Yeah. That has to be it. Whoever wrote this must be joking.":
        "Jajaja... seguro que querían decir que no se las robe nadie. Sí. Tiene que ser eso. Quien lo escribió estaba de broma.",
    "Alright then. Let's do this.":
        "Vale. Vamos allá.",
    "Here it is.... After all this time, I finally got a job.":
        "Aquí está... Después de tanto tiempo, por fin tengo trabajo.",
    "Strangely enough, this job didn't require an interview.":
        "Lo raro es que este trabajo no pedía entrevista.",
    "When I contacted them yesterday, everything was settled almost immediately.":
        "Cuando contacté ayer, quedó todo apalabrado casi al momento.",
    "I almost thought this was a scam but thankfully, it wasn't.":
        "Casi pensé que era una estafa, pero por suerte no.",
    "Alright. I have three tasks. First, keep the place safe from vandals. Fortunately, there hasn't been any sign of trouble so far.":
        "Vale. Tengo tres tareas. Primero, proteger el sitio de vándalos. Por suerte, de momento ni rastro de problemas.",
    "That only leaves cleaning the theater and making sure all the puppets are accounted for.":
        "Solo quedan limpiar el teatro y comprobar que estén todas las marionetas.",
    "Cleaning up":
        "Limpiar",
    "Checking puppets":
        "Revisar las marionetas",
    "All done":
        "Todo listo",
    "I head straight back to my room and report to the boss.":
        "Vuelvo directo a mi cuarto e informo al jefe.",
    "All of my tasks are finished. Now all that's left is to stand guard.":
        "Tareas terminadas. Ahora solo queda hacer guardia.",
    "Being a security guard doesn't seem so bad. I get paid just for keeping watch.":
        "Ser guardia no está tan mal. Me pagan por vigilar.",
    "The pay isn't great, but better than nothing.":
        "La paga no es gran cosa, pero mejor que nada.",
    "What should I do while I'm on watch...?":
        "¿Qué hago mientras vigilo...?",
    "I'm so tired... but I can't afford to fall asleep.":
        "Estoy agotado... pero no puedo dormirme.",
    "I take out my phone and start browsing the internet.":
        "Saco el móvil y empiezo a navegar por internet.",
    "My knowledge about this theater is still pretty limited and my curiosity gets the better of me, so I decide to look up some information online.":
        "Sé más bien poco de este teatro y la curiosidad me puede, así que decido buscar información en internet.",
    "Kingdom of Marionettes. A puppet theater that tells the story of the everyday lives of puppets in a kingdom.":
        "Kingdom of Marionettes. Un teatro de marionetas que cuenta la vida cotidiana de las marionetas de un reino.",
    "No wonder the puppets I saw earlier were dressed in outfits from a royal era":
        "Con razón las marionetas que vi antes vestían trajes de época real.",
    "Kingdom of Marionettes was known for its amusing and mesmerizing performances, enhanced by the puppet's charming designs.":
        "Kingdom of Marionettes era conocido por sus espectáculos divertidos y fascinantes, con unos diseños de marionetas encantadores.",
    "Was this place really that famous back then? They even sold merchandise and all kinds of stuff.":
        "¿De verdad fue tan famoso? Hasta vendían merchandising y de todo.",
    "There was even a poll for favorite characters. That's kind of cute.":
        "Hasta había una votación del personaje favorito. Qué mono.",
    "First place went to the jester. People really do like odd characters, huh.":
        "El primer puesto fue para el bufón. A la gente le van los personajes raros, ¿eh?",
    "Second place was the knight, and third was the wizard.":
        "El segundo fue el caballero, y el tercero el mago.",
    "I end up getting completely absorbed in all this information about the theater, and before I realize it, I've been scrolling for half an hour.":
        "Me absorbe tanto la información del teatro que, cuando me doy cuenta, llevo media hora deslizando.",
    "Oh crap. I need to check the CCTV.":
        "Mierda. Tengo que mirar las cámaras.",
    "Check outer gate":
        "Mirar la entrada",
    "Check corridor 1":
        "Mirar el pasillo 1",
    "Check theater hall":
        "Mirar la sala del teatro",
    "Check storage":
        "Mirar el almacén",
    "Check stage":
        "Mirar el escenario",
}

def main():
    cache = {}
    if os.path.exists(CACHE):
        cache = json.load(open(CACHE, encoding="utf-8"))
    cambiados = 0
    for raiz, _, fichs in os.walk(GAME):
        for f in fichs:
            if not f.endswith(".rpy") or "spanish" in raiz:
                continue
            p = os.path.join(raiz, f)
            txt = open(p, encoding="utf-8").read()
            for en, es in CURADAS.items():
                # 1) si el original EN sigue presente, sustituir directo
                if f'"{en}"' in txt:
                    txt = txt.replace(f'"{en}"', '"' + es + '"')
                    cambiados += 1
                # 2) si está la versión MT (vía caché), sustituirla
                elif en in cache and cache[en] and cache[en] != es:
                    mt = cache[en].replace('"', '\\"')
                    if f'"{mt}"' in txt:
                        txt = txt.replace(f'"{mt}"', '"' + es.replace('"', '\\"') + '"')
                        cambiados += 1
            open(p, "w", encoding="utf-8").write(txt)
    print(f"Repaso aplicado: {cambiados} cadenas curadas.")

if __name__ == "__main__":
    main()
