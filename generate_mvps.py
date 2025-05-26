import json
import openai
import os

# OpenAI-Key sicher aus Secret laden
openai.api_key = os.getenv("OPENAI_API_KEY")

# Trenddaten einlesen
with open("trends.json", "r") as f:
    trends = json.load(f)

mvps = {}


# GPT-4 Prompt bauen
def build_prompt(query):
    return f"""
Erstelle eine umsetzbare Geschäftsidee (MVP) zum Thema: "{query}"

Bitte liefere:
- 📛 Produktname
- 🧠 Zielgruppe
- 🚨 Problem
- 💡 Lösung
- 💸 Preismodell (Abo, einmalig, kostenlos + Upsell etc.)
- 🔧 Technologiestack (Website, App, KI, API, etc.)
"""


# Für jeden Trend GPT-4 fragen
for topic, items in trends.items():
    mvps[topic] = []
    for item in items:
        query = item["query"]
        prompt = build_prompt(query)
        print(f"🔍 Generiere MVP für: {query}")

        try:
            response = openai.ChatCompletion.create(model="gpt-4",
                                                    messages=[{
                                                        "role": "user",
                                                        "content": prompt
                                                    }],
                                                    temperature=0.7)
            idea = response.choices[0].message.content.strip()
            mvps[topic].append({"query": query, "idea": idea})
        except Exception as e:
            print(f"❌ Fehler bei {query}: {e}")

# Ergebnis speichern
with open("mvps.json", "w") as f:
    json.dump(mvps, f, indent=2, ensure_ascii=False)

print("✅ MVPs gespeichert in mvps.json")
