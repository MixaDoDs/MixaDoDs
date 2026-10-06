#!/usr/bin/env python3
"""Pixel SVGs for the MixaDoDs profile README: header, project icons, fastfetch window."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
(OUT / "icons").mkdir(parents=True, exist_ok=True)

MONO = "'JetBrains Mono','Cascadia Mono','DejaVu Sans Mono',Consolas,Menlo,monospace"

FONT = {
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
}


def pixel_word(word, x0, y0, px):
    """Rects of a word in the 5x7 font; returns (svg, width)."""
    rects = []
    x = x0
    for ch in word:
        for r, row in enumerate(FONT[ch]):
            for c, bit in enumerate(row):
                if bit == "1":
                    rects.append(f'<rect x="{x + c * px}" y="{y0 + r * px}" width="{px}" height="{px}"/>')
        x += 6 * px
    return "".join(rects), x - x0 - px


def bitmap(rows, palette, px, x0=0, y0=0):
    out = []
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch in palette:
                out.append(f'<rect x="{x0 + c * px}" y="{y0 + r * px}" width="{px}" height="{px}" fill="{palette[ch]}"/>')
    return "".join(out)


HEART = [".KK...KK.", "KPPK.KPPK", "KPWPKPPPK", "KPPPPPPPK", ".KPPPPPK.", "..KPPPK..", "...KPK...", "....K...."]
SPARK = ["..W..", "..W..", "WWWWW", "..W..", "..W.."]

# ---------------------------------------------------------------- header
W, H = 960, 300
stars = [(70, 70, 0), (190, 220, 1.1), (180, 60, 2.3), (790, 60, .6), (770, 200, 1.7), (880, 100, 2.9),
         (120, 150, 3.4), (850, 230, .3), (600, 232, 2.0), (330, 236, 3.0)]
star_svg = "".join(
    f'<g class="tw" style="animation-delay:{d}s" transform="translate({x},{y})">{bitmap(SPARK, {"W": "#fff4fb"}, 3)}</g>'
    for x, y, d in stars)
hearts = [(36, 196, 0, 4), (896, 150, 1.5, 4), (250, 118, 2.6, 3), (700, 128, .9, 3)]
heart_svg = "".join(
    f'<g class="fl" style="animation-delay:{d}s"><g transform="translate({x},{y})">'
    f'{bitmap(HEART, {"K": "#3b1f4f", "P": "#ff5cad", "W": "#ffd6ec"}, s)}</g></g>'
    for x, y, d, s in hearts)
bands = "".join(f'<rect x="14" y="{y}" width="932" height="{h}" fill="#ffffff" opacity="{o}"/>'
                for y, h, o in [(170, 18, .025), (196, 26, .035), (230, 34, .05)])

px = 10
name_w = 6 * 7 * px - px
nx = (W - name_w) // 2
name_shadow, _ = pixel_word("MIXADOD", nx + 4, 74 + 4, px)
name, _ = pixel_word("MIXADOD", nx, 74, px)

tagline = "~ welcome back, internet angel ~"
tag_chars = len(tagline)
char_w = 10.8  # 18px monospace
tag_w = tag_chars * char_w
tag_x = (W - tag_w) / 2
type_vals = ";".join(f"{i * char_w:.1f}" for i in range(tag_chars + 1))
type_keys = ";".join(f"{i / tag_chars:.3f}" for i in range(tag_chars + 1))


def field(x, w, label):
    return (f'<rect x="{x}" y="266" width="{w}" height="20" fill="#1a0f26"/>'
            f'<path d="M{x} 286V266H{x + w}" stroke="#120a1c" fill="none"/>'
            f'<path d="M{x + w} 266V286H{x}" stroke="#7a4f99" fill="none"/>'
            f'<text x="{x + 8}" y="280" class="sb">{label}</text>')


status = (field(18, 150, "stress 0%") + field(172, 150, "love 100%") + field(326, 200, "loc: Bulgaria")
          + field(530, 412, "tg @psxgld ✧ github.com/MixaDoDs"))

header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="MixaDoD.exe — welcome back, internet angel">
<title>MixaDoD.exe — welcome back, internet angel</title>
<defs>
<linearGradient id="tb" x1="0" x2="1"><stop offset="0" stop-color="#ff5cad"/><stop offset=".55" stop-color="#b36bff"/><stop offset="1" stop-color="#4fe3ff"/></linearGradient>
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="{nx}" x2="{nx + name_w}" y1="74" y2="144"><stop offset="0" stop-color="#fff0f8"/><stop offset=".45" stop-color="#ffb3d9"/><stop offset="1" stop-color="#9fe8ff"/></linearGradient>
<linearGradient id="bg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#241432"/><stop offset="1" stop-color="#3d2257"/></linearGradient>
<clipPath id="type"><rect x="{tag_x:.1f}" y="158" height="30" width="0"><animate attributeName="width" begin=".4s" dur="2.6s" values="{type_vals}" keyTimes="{type_keys}" calcMode="discrete" fill="freeze"/></rect></clipPath>
</defs>
<style>
.t{{font:700 15px {MONO};fill:#fff}}
.tag{{font:18px {MONO};fill:#ffb3d9}}
.sb{{font:12px {MONO};fill:#e9d8ff}}
.live{{font:700 13px {MONO};fill:#ff6b8f}}
.tw{{animation:tw 3.2s steps(2) infinite}}
.fl{{animation:fl 4s ease-in-out infinite}}
.dot{{animation:bl 1.2s steps(1) infinite}}
.cur{{animation:bl 1s steps(1) infinite}}
@keyframes tw{{0%,100%{{opacity:1}}50%{{opacity:.15}}}}
@keyframes fl{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
@keyframes bl{{0%{{opacity:1}}50%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.tw,.fl,.dot,.cur{{animation:none}}}}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" fill="#2b1840" stroke="#120a1c" stroke-width="2"/>
<path d="M4 {H - 4}V4H{W - 4}" stroke="#ffb3d9" stroke-width="2" fill="none"/>
<path d="M{W - 4} 4V{H - 4}H4" stroke="#120a1c" stroke-width="2" fill="none"/>
<rect x="10" y="10" width="{W - 20}" height="28" fill="url(#tb)"/>
<g transform="translate(18,15)">{bitmap(HEART, {"K": "#3b1f4f", "P": "#fff", "W": "#ffd6ec"}, 2)}</g>
<text x="42" y="30" class="t">MixaDoD.exe</text>
<g font-family="{MONO}" font-size="14" font-weight="700" text-anchor="middle">
{"".join(f'<rect x="{x}" y="14" width="24" height="20" fill="#e9d8ff" stroke="#3b1f4f"/><text x="{x + 12}" y="29" fill="#3b1f4f">{g}</text>' for x, g in [(W - 96, "_"), (W - 68, "□"), (W - 40, "×")])}
</g>
<rect x="14" y="42" width="{W - 28}" height="218" fill="url(#bg)"/>
<g shape-rendering="crispEdges">{bands}{star_svg}{heart_svg}</g>
<g fill="#120a1c" shape-rendering="crispEdges">{name_shadow}</g>
<g fill="url(#nm)" shape-rendering="crispEdges">{name}</g>
<text x="{tag_x:.1f}" y="180" class="tag" clip-path="url(#type)">{tagline}</text>
<rect class="cur" x="{tag_x + tag_w + 4:.1f}" y="164" width="9" height="20" fill="#ffb3d9" opacity="0"><set attributeName="opacity" to="1" begin="3s" fill="freeze"/></rect>
<text x="480" y="226" class="sb" text-anchor="middle" opacity=".8">trying to be a programmer, idk ✧ making things by editing files</text>
<circle class="dot" cx="{W - 88}" cy="62" r="5" fill="#ff3d6e"/>
<text x="{W - 78}" y="67" class="live">LIVE</text>
{status}
</svg>
'''
(OUT / "angel-header.svg").write_text(header)

# ---------------------------------------------------------------- icons
K = "#3b1f4f"
ICONS = {
    "heart": (["..KK....KK..", ".KPPK..KPPK.", "KPWPPKKPPPPK", "KPPPPPPPPPPK", "KPPPPPPPPPPK", ".KPPPPPPPPK.",
               "..KPPPPPPK..", "...KPPPPK...", "....KPPK....", ".....KK....."],
              {"K": K, "P": "#ff5cad", "W": "#ffd6ec"}),
    "key": (["............", "..KKK.......", ".KYYYK......", "KYK.KYKKKKKK", "KYK.KYYYYYYK", "KYK.KYKKKYKY",
             ".KYYYK..KYKY", "..KKK....K.K", "............"],
            {"K": K, "Y": "#ffd36b"}),
    "cat": (["KK......KK", "KWK....KWK", "KWWKKKKWWK", "KWWWWWWWWK", "KWKWWWWKWK", "KWWWKKWWWK", "KPWWWWWWPK",
             "KWWWWWWWWK", ".KKKKKKKK."],
            {"K": K, "W": "#ffffff", "P": "#ffb3d9"}),
    "picture": (["KKKKKKKKKKKK", "KCCCCCCCCCCK", "KCCCCCCCYYCK", "KCCCCCCCYYCK", "KCCCKCCCCCCK", "KCCKGKCCCCCK",
                 "KCKGGGKCKCCK", "KKGGGGGKGKCK", "KGGGGGGGGGGK", "KKKKKKKKKKKK"],
                {"K": K, "C": "#9fe8ff", "Y": "#ffd36b", "G": "#b36bff"}),
    "mic": (["....KKKK....", "...KSSSSK...", "...KSKKSK...", "...KSSSSK...", "...KSKKSK...", "...KSSSSK...",
             ".K..KKKK..K.", ".KK......KK.", "..KK....KK..", "....KKKK....", ".....KK.....", "...KKKKKK..."],
            {"K": K, "S": "#c9b8e8"}),
    "film": (["KKKKKKKKKKKK", "KWKWKWKWKWKK", "KKKKKKKKKKKK", "KPPPPKCCCCCK", "KPPPPKCCCCCK", "KPPPPKCCCCCK",
              "KKKKKKKKKKKK", "KWKWKWKWKWKK", "KKKKKKKKKKKK"],
             {"K": K, "W": "#ffffff", "P": "#ff5cad", "C": "#9fe8ff"}),
}
for name_, (rows, pal) in ICONS.items():
    p = 4
    w, h = max(map(len, rows)) * p, len(rows) * p
    ox, oy = (48 - w) // 2, (48 - h) // 2
    (OUT / "icons" / f"{name_}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" shape-rendering="crispEdges">'
        f'{bitmap(rows, pal, p, ox, oy)}</svg>\n')

# ---------------------------------------------------------------- fastfetch
FW, FH = 960, 430
STAR = [
    "......y......",
    "......y......",
    ".....yyy.....",
    ".....yyy.....",
    "....yyyyy....",
    "..yyyyyyyyy..",
    "yyyyyyWyyyyyy",
    "..yyyyyyyyy..",
    "....yyyyy....",
    ".....yyy.....",
    ".....yyy.....",
    "......y......",
    "......y......",
]


def shade(rows):
    """Light edge on the upper left, dark edge on the lower right."""
    g = [list(r) for r in rows]
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch != "y":
                continue
            edge = any(not (0 <= r + dr < len(rows) and 0 <= c + dc < len(row)) or rows[r + dr][c + dc] == "."
                       for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)))
            if edge:
                g[r][c] = "d" if (r > 6 or c > 6) else "l"
    return ["".join(r) for r in g]


logo = bitmap(shade(STAR), {"y": "#e8c66a", "l": "#fff0b8", "d": "#a87f3a", "W": "#ffffff"}, 16, 74, 84)
logo += bitmap(SPARK, {"W": "#f3e6ff"}, 8, 30, 80) + bitmap(SPARK, {"W": "#c9b8e8"}, 6, 300, 270)

info = [
    ("", "mixad@cachyos"),
    ("", "-------------"),
    ("OS", "CachyOS x86_64"),
    ("WM", "niri · scrollable tiling"),
    ("DE", "angelOS (my own, Quickshell/QML)"),
    ("Shell", "fish"),
    ("Terminal", "kitty"),
    ("Editor", "Neovim"),
    ("CPU", "AMD Ryzen 7 5700X"),
    ("GPU", "GeForce RTX 4060"),
    ("Audio", "RØDECaster Duo"),
    ("Langs", "QML · Python · Go · C++ · Rust"),
    ("Location", "Bulgaria"),
]
lines = []
y0 = 92
for i, (k, v) in enumerate(info):
    y = y0 + i * 22
    d = 1.6 + i * .09
    if not k:
        cls = "host" if i == 0 else "dim"
        body = f'<tspan class="{cls}">{v}</tspan>'
    else:
        body = f'<tspan class="k">{k}</tspan><tspan class="v"> ♡ {v}</tspan>'
    lines.append(f'<text x="430" y="{y}" class="ln" style="animation-delay:{d:.2f}s">{body}</text>')
pal = ["#2b1840", "#ff5c7a", "#57e3a2", "#ffd36b", "#8aa0ff", "#ff5cad", "#4fe3ff", "#f3e6ff"]
blocks = "".join(f'<rect x="{430 + i * 32}" y="{y0 + len(info) * 22}" width="32" height="18" fill="{c}"/>'
                 for i, c in enumerate(pal))
cmd = "fastfetch"
cmd_vals = ";".join(f"{i * 9:.0f}" for i in range(len(cmd) + 1))
cmd_keys = ";".join(f"{i / len(cmd):.3f}" for i in range(len(cmd) + 1))
prompt_x = 28 + len("mixad@cachyos ~> ") * 9

fastfetch = f'''<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}" role="img" aria-label="fastfetch: MixaDoD on CachyOS, niri and angelOS">
<title>fastfetch — mixad@cachyos</title>
<defs><clipPath id="cmd"><rect x="{prompt_x}" y="34" height="22" width="0"><animate attributeName="width" begin=".3s" dur=".9s" values="{cmd_vals}" keyTimes="{cmd_keys}" calcMode="discrete" fill="freeze"/></rect></clipPath></defs>
<style>
text{{font:15px {MONO};font-variant-ligatures:none}}
.p1{{fill:#57e3a2;font-weight:700}}.p2{{fill:#ff5cad}}.c{{fill:#f3e6ff}}
.host{{fill:#ff5cad;font-weight:700}}.dim{{fill:#6b5a7a}}.k{{fill:#ff5cad;font-weight:700}}.v{{fill:#f3e6ff}}
.ttl{{font-size:12px;fill:#c9b8e8}}
.cap{{font-size:14px;fill:#ff5cad;letter-spacing:1px}}.cap2{{font-size:13px;fill:#b9a6d9;letter-spacing:5px}}
.ln,.late{{opacity:0;animation:in .01s linear forwards}}
.cur{{animation:bl 1s steps(1) infinite}}
@keyframes in{{to{{opacity:1}}}}
@keyframes bl{{0%{{opacity:1}}50%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.ln,.late{{animation:none;opacity:1}}.cur{{animation:none}}}}
</style>
<rect x="1" y="1" width="{FW - 2}" height="{FH - 2}" rx="8" fill="#1a1020" stroke="#ff5cad" stroke-width="2"/>
<text x="{FW // 2}" y="20" class="ttl" text-anchor="middle">kitty — fish — ~</text>
<path d="M2 28H{FW - 2}" stroke="#3b1f4f"/>
<text x="28" y="50"><tspan class="p1">mixad@cachyos</tspan><tspan class="p2"> ~&gt; </tspan></text>
<text x="{prompt_x}" y="50" class="c" clip-path="url(#cmd)">{cmd}</text>
<g class="late" style="animation-delay:1.5s"><g shape-rendering="crispEdges">{logo}</g>
<text x="178" y="324" class="cap" text-anchor="middle">✧ INTERNET ANGEL ✧</text>
<text x="178" y="346" class="cap2" text-anchor="middle">NEEDY GIRL OVERDOSE</text></g>
{"".join(lines)}
<g class="late" style="animation-delay:{1.6 + len(info) * .09:.2f}s">{blocks}</g>
<g class="late" style="animation-delay:3s">
<text x="28" y="{FH - 22}"><tspan class="p1">mixad@cachyos</tspan><tspan class="p2"> ~&gt; </tspan></text>
<rect class="cur" x="{prompt_x}" y="{FH - 36}" width="9" height="18" fill="#ff5cad"/></g>
</svg>
'''
(OUT / "fastfetch.svg").write_text(fastfetch)
print("ok")
