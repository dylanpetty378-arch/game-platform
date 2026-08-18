"""L23 · the Channel table. Positions in hundredths; every row sums, in
absolute value, to exactly 100. Generated artefact — edit here, rebuild the
workbook and the docs from it."""
DIMS = [("temperature","physical","BIPOLAR"),("integrity","physical","signed"),
        ("substance","physical","signed"),("vitality","physical","signed"),
        ("vigor","physical","signed"),("mobility","physical","signed"),
        ("acuity","physical","signed"),("composure","mental","signed"),
        ("clarity","mental","signed"),("will","mental","signed"),
        ("regard","social","signed"),("standing","social","signed"),
        ("working","mystic","BIPOLAR"),("essence","mystic","signed")]
GROUPS = [
("FORCE & WEAPONS",[("impact",{"integrity":-100}),("pierce",{"integrity":-80,"vitality":-20}),
 ("rend",{"integrity":-60,"vitality":-40}),("bleed",{"vitality":-70,"integrity":-30}),
 ("crush",{"integrity":-70,"substance":-30}),("stagger",{"integrity":-50,"vigor":-50}),
 ("concussion",{"integrity":-50,"clarity":-50}),("knockdown",{"integrity":-40,"mobility":-60})]),
("ELEMENTS",[("fire",{"temperature":100}),("frost",{"temperature":-100}),
 ("lightning",{"temperature":30,"integrity":-70}),("blast",{"temperature":50,"integrity":-50}),
 ("shockwave",{"integrity":-60,"acuity":-40}),("acid",{"substance":-100}),
 ("molten",{"temperature":50,"substance":-50}),("scald",{"temperature":60,"vitality":-40}),
 ("frostbite",{"temperature":-50,"vitality":-50}),("exposure",{"temperature":-40,"vigor":-60}),
 ("flash",{"acuity":-70,"clarity":-30})]),
("AFFLICTION",[("venom",{"vitality":-70,"clarity":-30}),("blight",{"vitality":-50,"substance":-50}),
 ("agony",{"vitality":-50,"clarity":-50}),("fatigue",{"vigor":-70,"composure":-30}),
 ("wither",{"vitality":-60,"vigor":-40}),("rot",{"substance":-60,"vigor":-40}),
 ("numb",{"acuity":-60,"mobility":-40})]),
("BINDING & MOVEMENT",[("slow",{"mobility":-100}),("entangle",{"mobility":-70,"vigor":-30}),
 ("snare",{"mobility":-80,"vitality":-20}),("cripple",{"mobility":-60,"vitality":-40}),
 ("pin",{"mobility":-50,"integrity":-50}),("petrify",{"mobility":-60,"integrity":40})]),
("FEAR & MIND",[("dread",{"composure":-100}),("terror",{"composure":-70,"vigor":-30}),
 ("confusion",{"clarity":-100}),("panic",{"composure":-60,"clarity":-40}),
 ("charm",{"will":-70,"clarity":-30}),("domination",{"will":-100}),
 ("despair",{"composure":-50,"will":-50}),("compel",{"will":-60,"standing":-40}),
 ("daze",{"clarity":-60,"acuity":-40}),("madness",{"clarity":-50,"composure":-50}),
 ("transfix",{"composure":-50,"mobility":-50})]),
("STANDING",[("praise",{"regard":100}),("scorn",{"regard":-100}),("endorse",{"standing":100}),
 ("discredit",{"standing":-100}),("champion",{"regard":60,"standing":40}),
 ("slander",{"regard":-70,"standing":-30}),("denounce",{"regard":-20,"standing":-80}),
 ("humble",{"regard":50,"standing":-50}),("menace",{"regard":-50,"standing":50}),
 ("humiliate",{"standing":-50,"composure":-50}),("embolden",{"composure":60,"standing":40}),
 ("enthrall",{"will":-50,"regard":50})]),
("MYSTIC",[("enchant",{"working":100}),("dispel",{"working":-100}),("infuse",{"essence":100}),
 ("drain",{"essence":-100}),("ward",{"working":60,"essence":40}),
 ("siphon",{"working":-50,"essence":-50}),("bind",{"working":70,"essence":-30}),
 ("surge",{"working":-40,"essence":60}),("curse",{"working":40,"vitality":-30,"regard":-30}),
 ("blessing",{"working":40,"composure":30,"vitality":30}),("soulburn",{"essence":-60,"vitality":-40}),
 ("hallow",{"working":60,"composure":40})]),
("RESTORE & PROTECT",[("mend",{"vitality":100}),("rally",{"vigor":100}),("courage",{"composure":100}),
 ("lucidity",{"clarity":100}),("unbind",{"will":100}),("brace",{"integrity":100}),
 ("seal",{"substance":100}),("haste",{"mobility":100}),("keen",{"acuity":100}),
 ("regenerate",{"vitality":60,"vigor":40}),("fortify",{"integrity":60,"substance":40}),
 ("bolster",{"integrity":60,"vitality":40}),("preserve",{"substance":60,"vitality":40}),
 ("steady",{"composure":50,"clarity":50}),("soothe",{"composure":60,"vigor":40}),
 ("sharpen",{"clarity":60,"acuity":40}),("vigilance",{"acuity":60,"clarity":40}),
 ("quicken",{"mobility":60,"acuity":40}),("steel",{"will":50,"composure":50}),
 ("freedom",{"mobility":60,"will":40}),("cleanse",{"vitality":50,"working":-50})]),
]
CHANNELS = {n: d for _, rows in GROUPS for n, d in rows}
if __name__ == "__main__":
    bad = [n for n, d in CHANNELS.items() if sum(abs(v) for v in d.values()) != 100]
    seen, dup = {}, []
    for n, d in CHANNELS.items():
        k = tuple(sorted(d.items()))
        if k in seen: dup.append((n, seen[k]))
        seen[k] = n
    # Rule 17b, second half: every Dimension must be used on both signs, or the axis dies.
    dead = []
    for dim, _, _ in DIMS:
        signs = {(v > 0) for d in CHANNELS.values() for k, v in d.items() if k == dim}
        if signs != {True, False}: dead.append(dim)
    print(f"{len(CHANNELS)} Channels · sum≠100 {bad or 'none'} · duplicate positions {dup or 'none'}"
          f" · single-sign Dimensions {dead or 'none'}")
    if bad or dup or dead:
        raise SystemExit(1)
