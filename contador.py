from datetime import datetime

# Defina aqui a sua data-alvo (Ano, Mês, Dia)
target_date = datetime(2026, 10, 01)  
today = datetime.now()

# Calcula a diferença de dias
remaining_days = (target_date - today).days
if remaining_days < 0:
    remaining_days = 0

# Criação do arquivo SVG dinâmico e moderno
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="350" height="100" viewBox="0 0 350 100">
  <style>
    .title {{ fill: #cdd6f4; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 15px; font-weight: bold; }}
    .counter {{ fill: #89b4fa; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 28px; font-weight: bold; }}
  </style>
  <rect width="350" height="100" rx="12" fill="#1e1e2e" stroke="#313244" stroke-width="2"/>
  <text x="20" y="38" class="title">⏳ Dias para a Meta Final</text>
  <text x="20" y="78" class="counter">{remaining_days} dias restantes</text>
</svg>"""

# Salva o arquivo SVG na raiz do repositório
with open("countdown.svg", "w", encoding="utf-8") as f:
  f.write(svg_content)

print(f"Countdown atualizado com sucesso: {remaining_days} dias restantes.")
