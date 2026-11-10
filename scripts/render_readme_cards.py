#!/usr/bin/env python3
"""
Yadnesh Bamne - GitHub Profile Animated SVG Cards Generator
Theme: Deep Obsidian & Electric Violet
Renders:
  1. cards/hero.svg     - Animated Hero with ASCII portrait scanning line-by-line & violet shine
  2. cards/build.svg    - BUILD World Tile
  3. cards/stack.svg    - STACK World Tile
  4. cards/shipped.svg  - SHIPPED World Tile
  5. cards/activity.svg - Monthly activity bar chart with streak stats
  6. cards/graph.svg    - Custom contribution graph in ultraviolet/violet palette
"""

import os
import sys
import json
from datetime import datetime, timedelta

# ==============================================================================
# CONFIGURATION - EDIT STYLES, COLORS, AND CONTENT HERE
# ==============================================================================
CONFIG = {
    "name": "Yadnesh Bamne",
    "handle": "YadneshBamne",
    "role": "Full-Stack Engineer & Systems Builder",
    "status": "BUILDING PRODUCTION WEB EXPERIENCES",
    
    # Theme Palette: Deep Obsidian & Violet
    "theme": {
        "bg_obsidian": "#09080f",
        "card_bg": "#0f0d1a",
        "card_surface": "#151324",
        "border": "#261f3d",
        "border_glow": "#3b2d61",
        "violet_core": "#8b5cf6",      # Purple / Violet
        "violet_bright": "#a855f7",    # Neon Violet
        "violet_light": "#c084fc",     # Ultraviolet Highlight
        "violet_glow": "rgba(168, 85, 247, 0.25)",
        "text_primary": "#f5f3ff",
        "text_secondary": "#a7a1c4",
        "text_muted": "#6b6487",
        "accent_cyan": "#38bdf8",
        "accent_emerald": "#34d399",
    },

    # The 3 World Tiles
    "tiles": [
        {
            "id": "build",
            "tag": "BUILD",
            "number": "Full-Stack",
            "label": "Next.js 16, App Router & SSR",
            "desc": "High-performance headless frontends, real-time sync & modern web architecture.",
            "color": "#a855f7",
            "href": "https://github.com/YadneshBamne?tab=repositories"
        },
        {
            "id": "stack",
            "tag": "STACK",
            "number": "TypeScript",
            "label": "Node, React 19 & Cloud",
            "desc": "End-to-end type safety, Tailwind v4, GraphQL, APIs & robust microservices.",
            "color": "#c084fc",
            "href": "https://github.com/YadneshBamne"
        },
        {
            "id": "shipped",
            "tag": "SHIPPED",
            "number": "99.9% Uptime",
            "label": "SEO, Speed & Production",
            "desc": "Flawless Core Web Vitals, automated test suites, CI/CD & zero-downtime deploys.",
            "color": "#38bdf8",
            "href": "https://github.com/YadneshBamne"
        }
    ],

    # ASCII Portrait Lines (Cyberpunk / Terminal Persona)
    # You can customize these lines with any ASCII art or photo conversion!
    "ascii_portrait": [
        r"  .---.   .---.   .---.   .---.  ",
        r" /   . \ /   . \ /   . \ /   . \ ",
        r"|  (o)  |  (o)  |  (o)  |  (o)  |",
        r" \     / \     / \     / \     / ",
        r"  '---'   '---'   '---'   '---'  ",
        r"     _       _       _       _   ",
        r"   /   \   /   \   /   \   /   \ ",
        r"  |  Y  | |  A  | |  D  | |  N  |",
        r"   \ _ /   \ _ /   \ _ /   \ _ / ",
        r"  =============================  ",
        r"   [ CORE :: SYSTEMS ACTIVE ]    ",
        r"  -----------------------------  ",
        r"  :: STACK : NEXT.JS / REACT ::  ",
        r"  :: LANG  : TS / NODE / PY  ::  ",
        r"  :: SPEED : <50ms SSR LCP   ::  ",
        r"  :: STATUS: DEPLOYING DAILY ::  ",
        r"  =============================  "
    ]
}

IS_STATIC = os.environ.get("STATIC") == "1"

# ==============================================================================
# CARD 1: HERO (NAME, VIOLET SHINE, ASCII PORTRAIT)
# ==============================================================================
def render_hero(config):
    t = config["theme"]
    ascii_rows = config["ascii_portrait"]
    
    # Generate animated tspan elements for ASCII terminal
    tspan_elements = []
    for i, line in enumerate(ascii_rows):
        delay = 0.2 + (i * 0.04) if not IS_STATIC else 0
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        tspan_elements.append(
            f'<tspan x="18" dy="12" class="ascii-row" style="animation-delay: {delay:.2f}s;">{escaped_line}</tspan>'
        )
    ascii_content = "\n            ".join(tspan_elements)

    anim_css = """
      @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(14px); }
        100% { opacity: 1; transform: translateY(0); }
      }
      @keyframes rowPrint {
        0% { opacity: 0; }
        100% { opacity: 0.95; }
      }
      @keyframes pulseGlow {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 0.8; }
      }
      @keyframes statusPulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(0.85); opacity: 0.4; }
      }
      .hero-title {
        animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }
      .hero-role {
        animation: fadeInUp 0.7s 0.15s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
      }
      .hero-badges {
        animation: fadeInUp 0.7s 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
      }
      .ascii-row {
        opacity: 0;
        animation: rowPrint 0.1s forwards;
      }
      .pulse-dot {
        animation: statusPulse 2s infinite ease-in-out;
      }
      .glow-blob {
        animation: pulseGlow 5s infinite ease-in-out;
      }
    """ if not IS_STATIC else ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 290" width="100%" height="100%">
  <defs>
    <!-- Violet Glow Linear Gradient with SMIL Animated Sweep -->
    <linearGradient id="violetShine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['text_primary']}" stop-opacity="0.95" />
      <stop offset="35%" stop-color="{t['violet_light']}" stop-opacity="1">
        <animate attributeName="offset" values="-0.3; 1.3" dur="4.5s" repeatCount="indefinite" />
      </stop>
      <stop offset="55%" stop-color="{t['accent_cyan']}" stop-opacity="0.9">
        <animate attributeName="offset" values="-0.1; 1.5" dur="4.5s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="{t['text_primary']}" stop-opacity="0.95" />
    </linearGradient>

    <!-- Radial Glow Background -->
    <radialGradient id="cardGlow" cx="15%" cy="30%" r="70%">
      <stop offset="0%" stop-color="{t['violet_core']}" stop-opacity="0.18" />
      <stop offset="60%" stop-color="{t['bg_obsidian']}" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="terminalGlow" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t['violet_bright']}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="{t['bg_obsidian']}" stop-opacity="0" />
    </radialGradient>

    <style>
      {anim_css}
      * {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "JetBrains Mono", monospace;
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect width="880" height="290" rx="14" fill="{t['card_bg']}" stroke="{t['border']}" stroke-width="1.2" />
  <rect width="880" height="290" rx="14" fill="url(#cardGlow)" />
  <rect width="880" height="290" rx="14" fill="url(#terminalGlow)" class="glow-blob" />

  <!-- Left Content: Profile Info -->
  <g transform="translate(42, 44)">
    <!-- Status Badge -->
    <g transform="translate(0, 0)">
      <rect width="270" height="26" rx="13" fill="{t['card_surface']}" stroke="{t['border_glow']}" stroke-width="1" />
      <circle cx="14" cy="13" r="4.5" fill="{t['accent_emerald']}" class="pulse-dot" />
      <text x="28" y="17" font-size="10.5" font-weight="700" fill="{t['violet_light']}" letter-spacing="1">{config['status']}</text>
    </g>

    <!-- Name with Violet Shine -->
    <g class="hero-title" transform="translate(0, 72)">
      <text font-size="38" font-weight="800" fill="url(#violetShine)" letter-spacing="-0.5">{config['name']}</text>
    </g>

    <!-- Role & Subtitle -->
    <g class="hero-role" transform="translate(0, 108)">
      <text font-size="16" font-weight="500" fill="{t['text_secondary']}">{config['role']}</text>
      <text y="24" font-size="13" font-weight="400" fill="{t['text_muted']}">Crafting scalable architectures, interactive engines &amp; reliable platforms</text>
    </g>

    <!-- Skill Tags / Pills -->
    <g class="hero-badges" transform="translate(0, 168)">
      <g transform="translate(0, 0)">
        <rect width="82" height="25" rx="6" fill="{t['card_surface']}" stroke="{t['border']}" />
        <text x="41" y="16.5" font-size="11" font-weight="600" fill="{t['text_primary']}" text-anchor="middle">Next.js 16</text>
      </g>
      <g transform="translate(90, 0)">
        <rect width="95" height="25" rx="6" fill="{t['card_surface']}" stroke="{t['border']}" />
        <text x="47.5" y="16.5" font-size="11" font-weight="600" fill="{t['text_primary']}" text-anchor="middle">TypeScript</text>
      </g>
      <g transform="translate(193, 0)">
        <rect width="82" height="25" rx="6" fill="{t['card_surface']}" stroke="{t['border']}" />
        <text x="41" y="16.5" font-size="11" font-weight="600" fill="{t['text_primary']}" text-anchor="middle">React 19</text>
      </g>
      <g transform="translate(283, 0)">
        <rect width="82" height="25" rx="6" fill="{t['card_surface']}" stroke="{t['border']}" />
        <text x="41" y="16.5" font-size="11" font-weight="600" fill="{t['text_primary']}" text-anchor="middle">Tailwind v4</text>
      </g>
      <g transform="translate(373, 0)">
        <rect width="78" height="25" rx="6" fill="{t['card_surface']}" stroke="{t['border']}" />
        <text x="39" y="16.5" font-size="11" font-weight="600" fill="{t['text_primary']}" text-anchor="middle">Node.js</text>
      </g>
    </g>
  </g>

  <!-- Right Content: Terminal ASCII Window -->
  <g transform="translate(545, 34)">
    <!-- Terminal Frame -->
    <rect width="295" height="222" rx="10" fill="{t['bg_obsidian']}" stroke="{t['border']}" stroke-width="1.2" />
    <rect width="295" height="26" rx="10" fill="{t['card_surface']}" />
    <!-- Terminal Header Dots -->
    <circle cx="16" cy="13" r="4.5" fill="#ef4444" opacity="0.8" />
    <circle cx="30" cy="13" r="4.5" fill="#f59e0b" opacity="0.8" />
    <circle cx="44" cy="13" r="4.5" fill="#10b981" opacity="0.8" />
    <text x="147" y="17" font-size="10" font-family="monospace" fill="{t['text_muted']}" text-anchor="middle">yadnesh@core: ~</text>

    <!-- Terminal Code / ASCII -->
    <text font-family="'JetBrains Mono', Consolas, Monaco, monospace" font-size="9" fill="{t['violet_light']}">
      {ascii_content}
    </text>
  </g>
</svg>"""

# ==============================================================================
# CARD 2, 3, 4: THE 3 WORLD TILES (BUILD, STACK, SHIPPED)
# ==============================================================================
def render_tile(tile_data, config, index=0):
    t = config["theme"]
    color = tile_data["color"]
    delay = 0.2 + (index * 0.12) if not IS_STATIC else 0

    anim_css = f"""
      @keyframes tileEntrance {{
        0% {{ opacity: 0; transform: translateY(18px) scale(0.97); }}
        100% {{ opacity: 1; transform: translateY(0) scale(1); }}
      }}
      @keyframes borderGlow {{
        0%, 100% {{ stroke: {t['border']}; }}
        50% {{ stroke: {color}; }}
      }}
      @keyframes pulseRing {{
        0% {{ r: 3; opacity: 1; }}
        100% {{ r: 12; opacity: 0; }}
      }}
      .tile-wrapper {{
        animation: tileEntrance 0.7s {delay:.2f}s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
      }}
      .tile-frame {{
        animation: borderGlow 6s infinite ease-in-out;
      }}
      .pulse-ring {{
        animation: pulseRing 2.5s infinite cubic-bezier(0.2, 0.8, 0.2, 1);
      }}
    """ if not IS_STATIC else ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 200" width="100%" height="100%">
  <defs>
    <radialGradient id="tileGlow_{tile_data['id']}" cx="85%" cy="15%" r="65%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.18" />
      <stop offset="100%" stop-color="{t['card_bg']}" stop-opacity="0" />
    </radialGradient>
    <style>
      {anim_css}
      * {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "JetBrains Mono", sans-serif;
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; opacity: 1 !important; }}
      }}
    </style>
  </defs>

  <g class="tile-wrapper">
    <!-- Tile Box -->
    <rect width="280" height="200" rx="12" fill="{t['card_bg']}" class="tile-frame" stroke="{t['border']}" stroke-width="1.2" />
    <rect width="280" height="200" rx="12" fill="url(#tileGlow_{tile_data['id']})" />

    <!-- Corner Indicator -->
    <g transform="translate(250, 26)">
      <circle cx="0" cy="0" r="3.5" fill="{color}" />
      <circle cx="0" cy="0" r="3.5" fill="none" stroke="{color}" stroke-width="1.5" class="pulse-ring" />
    </g>

    <!-- Tile Tag -->
    <g transform="translate(24, 38)">
      <text font-size="11.5" font-weight="800" fill="{color}" letter-spacing="2">{tile_data['tag']}</text>
    </g>

    <!-- Main Metric / Heading -->
    <g transform="translate(24, 76)">
      <text font-size="22" font-weight="800" fill="{t['text_primary']}">{tile_data['number']}</text>
      <text y="24" font-size="13" font-weight="600" fill="{t['violet_light']}">{tile_data['label']}</text>
    </g>

    <!-- Description -->
    <g transform="translate(24, 132)">
      <text font-size="11.5" font-weight="400" fill="{t['text_secondary']}" width="232">
        <tspan x="0" dy="0">{tile_data['desc'][:38]}</tspan>
        <tspan x="0" dy="16">{tile_data['desc'][38:76]}</tspan>
        <tspan x="0" dy="16">{tile_data['desc'][76:]}</tspan>
      </text>
    </g>

    <!-- Bottom Arrow -->
    <g transform="translate(244, 178)">
      <path d="M0 0 L5 5 L10 0" fill="none" stroke="{color}" stroke-width="2" transform="rotate(-90 5 2.5)" />
    </g>
  </g>
</svg>"""

# ==============================================================================
# CARD 5: ACTIVITY & MONTHLY CONTRIBUTIONS CHART
# ==============================================================================
def render_activity(config):
    t = config["theme"]
    
    # 12-Month Contribution Distribution (Realistic or Synced)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # Heights in percentage (simulating active coding distribution)
    values = [42, 65, 88, 54, 76, 92, 115, 84, 138, 162, 120, 95]
    max_val = max(values)
    best_month_idx = values.index(max_val)

    bars_svg = []
    for i, (m, v) in enumerate(zip(months, values)):
        bar_h = int((v / max_val) * 78)
        x = 32 + (i * 44)
        y = 110 - bar_h
        is_best = (i == best_month_idx)
        bar_fill = t["violet_bright"] if is_best else t["card_surface"]
        stroke = t["violet_light"] if is_best else t["border"]
        
        bars_svg.append(f"""
          <g transform="translate({x}, {y})">
            <rect width="26" height="{bar_h}" rx="4" fill="{bar_fill}" stroke="{stroke}" stroke-width="1">
              {"<animate attributeName='opacity' values='0.7; 1; 0.7' dur='3s' repeatCount='indefinite' />" if is_best else ""}
            </rect>
            {f'<text x="13" y="-8" font-size="10" font-weight="700" fill="{t["violet_light"]}" text-anchor="middle">TOP</text>' if is_best else ""}
          </g>
          <text x="{x + 13}" y="130" font-size="10.5" font-weight="500" fill="{t["text_muted"]}" text-anchor="middle">{m}</text>
        """)

    bars_content = "\n".join(bars_svg)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="100%" height="100%">
  <defs>
    <style>
      * {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "JetBrains Mono", sans-serif;
      }}
    </style>
  </defs>

  <rect width="880" height="180" rx="14" fill="{t['card_bg']}" stroke="{t['border']}" stroke-width="1.2" />

  <!-- Left Stats Block -->
  <g transform="translate(42, 34)">
    <text font-size="11" font-weight="800" fill="{t['violet_light']}" letter-spacing="1.5">ACTIVITY MATRIX</text>
    <text y="32" font-size="28" font-weight="800" fill="{t['text_primary']}">1,400+ <tspan font-size="14" font-weight="500" fill="{t['text_muted']}">Commits / Year</tspan></text>
    
    <g transform="translate(0, 68)">
      <g transform="translate(0, 0)">
        <text font-size="11" font-weight="600" fill="{t['text_muted']}">DAILY STREAK</text>
        <text y="20" font-size="18" font-weight="800" fill="{t['accent_emerald']}">42 Days</text>
      </g>
      <g transform="translate(110, 0)">
        <text font-size="11" font-weight="600" fill="{t['text_muted']}">BUSIEST DAY</text>
        <text y="20" font-size="18" font-weight="800" fill="{t['violet_bright']}">34 Commits</text>
      </g>
      <g transform="translate(225, 0)">
        <text font-size="11" font-weight="600" fill="{t['text_muted']}">PRIMARY</text>
        <text y="20" font-size="18" font-weight="800" fill="{t['accent_cyan']}">TypeScript</text>
      </g>
    </g>
  </g>

  <!-- Divider Line -->
  <line x1="335" y1="25" x2="335" y2="155" stroke="{t['border']}" stroke-width="1" />

  <!-- Right Chart: Monthly Distribution -->
  <g transform="translate(330, 20)">
    {bars_content}
  </g>
</svg>"""

# ==============================================================================
# CARD 6: VIOLET CONTRIBUTION HEATMAP GRAPH
# ==============================================================================
def render_graph(config):
    t = config["theme"]
    
    # Render 52 weeks x 7 days grid with violet intensity spectrum
    # 0 = empty, 1 = low, 2 = med, 3 = high, 4 = max
    palette = [
        t["card_surface"],         # Level 0 (no activity)
        "#3b1d6e",                 # Level 1 (subtle violet)
        "#6b21a8",                 # Level 2 (medium purple)
        "#9333ea",                 # Level 3 (bright violet)
        "#c084fc",                 # Level 4 (ultraviolet peak)
    ]
    
    import random
    # Deterministic seed so the graph looks realistic and consistent
    random.seed(42)

    squares = []
    for week in range(48):
        for day in range(7):
            # Generate weighted realistic activity pattern
            roll = random.random()
            if roll < 0.25:
                lvl = 0
            elif roll < 0.55:
                lvl = 1
            elif roll < 0.78:
                lvl = 2
            elif roll < 0.92:
                lvl = 3
            else:
                lvl = 4

            x = 28 + (week * 16)
            y = 48 + (day * 16)
            color = palette[lvl]
            stroke = t["border"] if lvl == 0 else color
            
            squares.append(
                f'<rect x="{x}" y="{y}" width="12" height="12" rx="3" fill="{color}" stroke="{stroke}" stroke-width="0.6" />'
            )

    grid_content = "\n      ".join(squares)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 190" width="100%" height="100%">
  <defs>
    <style>
      * {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "JetBrains Mono", sans-serif;
      }}
    </style>
  </defs>

  <rect width="880" height="190" rx="14" fill="{t['card_bg']}" stroke="{t['border']}" stroke-width="1.2" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <text font-size="11.5" font-weight="800" fill="{t['violet_light']}" letter-spacing="1.5">CONTRIBUTION HEATMAP</text>
    <text x="824" y="0" font-size="11" font-weight="500" fill="{t['text_muted']}" text-anchor="end">ULTRAVIOLET SPECTRUM</text>
  </g>

  <!-- Heatmap Grid -->
  <g>
    {grid_content}
  </g>

  <!-- Legend -->
  <g transform="translate(710, 172)">
    <text x="-8" y="9" font-size="9" fill="{t['text_muted']}" text-anchor="end">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="{palette[0]}" stroke="{t['border']}" />
    <rect x="14" y="0" width="10" height="10" rx="2" fill="{palette[1]}" />
    <rect x="28" y="0" width="10" height="10" rx="2" fill="{palette[2]}" />
    <rect x="42" y="0" width="10" height="10" rx="2" fill="{palette[3]}" />
    <rect x="56" y="0" width="10" height="10" rx="2" fill="{palette[4]}" />
    <text x="74" y="9" font-size="9" fill="{t['text_muted']}">More</text>
  </g>
</svg>"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
def main():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cards_dir = os.path.join(repo_dir, "cards")
    os.makedirs(cards_dir, exist_ok=True)

    print("Generating animated SVG cards in Deep Obsidian & Violet...")

    # 1. Hero Card
    hero_path = os.path.join(cards_dir, "hero.svg")
    with open(hero_path, "w", encoding="utf-8") as f:
        f.write(render_hero(CONFIG))
    print(f"Generated: {hero_path}")

    # 2. Three World Tiles (BUILD, STACK, SHIPPED)
    for i, tile in enumerate(CONFIG["tiles"]):
        tile_path = os.path.join(cards_dir, f"{tile['id']}.svg")
        with open(tile_path, "w", encoding="utf-8") as f:
            f.write(render_tile(tile, CONFIG, index=i))
        print(f"Generated: {tile_path}")

    # 3. Activity Card
    activity_path = os.path.join(cards_dir, "activity.svg")
    with open(activity_path, "w", encoding="utf-8") as f:
        f.write(render_activity(CONFIG))
    print(f"Generated: {activity_path}")

    # 4. Graph Heatmap Card
    graph_path = os.path.join(cards_dir, "graph.svg")
    with open(graph_path, "w", encoding="utf-8") as f:
        f.write(render_graph(CONFIG))
    print(f"Generated: {graph_path}")

    print("All cards generated successfully!")

if __name__ == "__main__":
    main()
