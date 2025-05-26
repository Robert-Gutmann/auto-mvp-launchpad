import json
import openai
import os

# OpenAI Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Lade die MVP-Datei
with open("mvps.json", "r") as f:
    mvps = json.load(f)

# Wähle einen MVP (z. B. erstes Thema + erstes Item)
first_topic = list(mvps.keys())[0]
first_idea = mvps[first_topic][0]["idea"]
query = mvps[first_topic][0]["query"]

# Prompt an GPT-4: generiere HTML Landingpage
prompt = f"""
Ausgehend von dieser Geschäftsidee:
---
{first_idea}
---

Erstelle eine vollständige HTML-Landingpage im modernen Stil mit:
- Titel & Untertitel
- Problem / Lösung
- 3 Haupt-Features
- Preismodell (mit Preis, Button, CTA)
- Footer mit Kontaktadresse
- Klarer Struktur
- Verwende Tailwind CSS Klassen (aber ohne externen Link)

Code nur als HTML. Ohne Erklärtext.
"""

# Anfrage an GPT-4
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

html_code = response.choices[0].message.content.strip()

# In Datei speichern
with open("landingpage.html", "w") as f:
    f.write(html_code)

print("✅ Landingpage gespeichert als landingpage.html")
