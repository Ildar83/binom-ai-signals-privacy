from pathlib import Path

import markdown


root = Path(__file__).parent
source = (root / "README.md").read_text(encoding="utf-8")
body = markdown.markdown(source, extensions=["tables", "sane_lists"])

html = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Политика конфиденциальности Android-приложения Binom AI Signals">
  <title>Политика конфиденциальности — Binom AI Signals</title>
  <style>
    :root {{ color-scheme: light; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    body {{ margin: 0; background: #f5f7fb; color: #172033; line-height: 1.65; }}
    main {{ width: min(920px, calc(100% - 32px)); margin: 32px auto; padding: 36px; background: #fff; border-radius: 18px; box-shadow: 0 12px 40px rgba(15, 32, 64, .08); }}
    h1, h2 {{ color: #07142e; line-height: 1.25; }}
    h1 {{ font-size: clamp(1.8rem, 5vw, 2.6rem); }}
    h2 {{ margin-top: 2rem; border-top: 1px solid #e5eaf2; padding-top: 1.2rem; }}
    a {{ color: #075fc9; overflow-wrap: anywhere; }}
    blockquote {{ margin: 1.5rem 0; padding: 1rem 1.25rem; background: #eef6ff; border-left: 4px solid #1688ff; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; display: block; overflow-x: auto; }}
    th, td {{ border: 1px solid #dfe5ef; padding: .75rem; text-align: left; vertical-align: top; }}
    th {{ background: #f2f5fa; }}
    code {{ background: #f0f3f8; padding: .15rem .35rem; border-radius: 4px; }}
    @media (max-width: 640px) {{ main {{ width: auto; margin: 0; padding: 22px 18px; border-radius: 0; }} }}
  </style>
</head>
<body>
  <main>{body}</main>
</body>
</html>
"""

(root / "index.html").write_text(html, encoding="utf-8")
