import streamlit as st
import pandas as pd

# 🐉 Correct Chinese Zodiac Cycle
zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements = ["Metal", "Water", "Wood", "Fire", "Earth"]  # Correct 10-year cycle
yin_yang = ["Yang", "Yin"]

# Generate correct zodiac cycle from 1924-2100
start_year = 1924
zodiac_data = []
for year in range(start_year, 2100):
    zodiac_sign = zodiac_animals[(year - start_year) % 12]
    element = elements[((year - 1924) % 10) // 2]  # Every two years share the same element
    yin_yang_polarity = yin_yang[(year - start_year) % 2]
    zodiac_data.append({"Year": year, "Zodiac": zodiac_sign, "Element": element, "Yin/Yang": yin_yang_polarity})

zodiac_df = pd.DataFrame(zodiac_data)

# 🎭 Zodiac Personality Summaries
zodiac_traits = {
    "Rat": {"Personality": "Smart, adaptable, charming. They think fast and love challenges.",
            "Strengths": "Resourceful, quick-witted, energetic.",
            "Weaknesses": "Can be greedy, stubborn, and opportunistic."},
    "Ox": {"Personality": "Strong, reliable, and determined. Values tradition and hard work.",
           "Strengths": "Dependable, honest, patient.",
           "Weaknesses": "Can be inflexible, conservative, and stubborn."},
    "Tiger": {"Personality": "Brave, independent, and passionate. A natural leader.",
              "Strengths": "Confident, dynamic, ambitious.",
              "Weaknesses": "Can be impulsive, aggressive, and reckless."},
    "Rabbit": {"Personality": "Gentle, artistic, and compassionate. Values harmony.",
               "Strengths": "Kind, diplomatic, creative.",
               "Weaknesses": "Can be too sensitive, hesitant, and self-indulgent."},
    "Dragon": {"Personality": "Confident, charismatic, and ambitious. Loves challenges.",
               "Strengths": "Energetic, bold, intelligent.",
               "Weaknesses": "Can be arrogant, irritable, and demanding."},
    "Snake": {"Personality": "Wise, mysterious, and intuitive. Loves deep thinking.",
              "Strengths": "Strategic, elegant, resourceful.",
              "Weaknesses": "Can be secretive, jealous, and manipulative."},
    "Horse": {"Personality": "Adventurous, active, and social. Loves freedom.",
              "Strengths": "Energetic, optimistic, independent.",
              "Weaknesses": "Can be impatient, restless, and moody."},
    "Goat": {"Personality": "Gentle, caring, and artistic. Loves peace and beauty.",
             "Strengths": "Creative, kind, intuitive.",
             "Weaknesses": "Can be pessimistic, indecisive, and shy."},
    "Monkey": {"Personality": "Clever, mischievous, and curious. Loves fun and innovation.",
               "Strengths": "Smart, witty, inventive.",
               "Weaknesses": "Can be manipulative, unreliable, and arrogant."},
    "Rooster": {"Personality": "Hardworking, observant, and confident. Pays attention to detail.",
                "Strengths": "Reliable, precise, organized.",
                "Weaknesses": "Can be critical, perfectionist, and vain."},
    "Dog": {"Personality": "Loyal, honest, and protective. Values fairness and justice.",
            "Strengths": "Trustworthy, courageous, caring.",
            "Weaknesses": "Can be anxious, pessimistic, and stubborn."},
    "Pig": {"Personality": "Generous, kind, and fun-loving. Enjoys life’s pleasures.",
            "Strengths": "Compassionate, easy-going, trustworthy.",
            "Weaknesses": "Can be naïve, lazy, and materialistic."}
}

# 💕 Compatibility Chart
compatibility_chart = {
    "Rat": ["Ox", "Dragon", "Monkey"],
    "Ox": ["Rat", "Snake", "Rooster"],
    "Tiger": ["Dragon", "Horse", "Pig"],
    "Rabbit": ["Goat", "Dog", "Pig"],
    "Dragon": ["Rat", "Tiger", "Monkey"],
    "Snake": ["Ox", "Rooster", "Monkey"],
    "Horse": ["Tiger", "Goat", "Dog"],
    "Goat": ["Rabbit", "Horse", "Pig"],
    "Monkey": ["Rat", "Dragon", "Snake"],
    "Rooster": ["Ox", "Snake"],
    "Dog": ["Rabbit", "Horse"],
    "Pig": ["Tiger", "Rabbit", "Goat"]
}

# 🖥 Streamlit Interface
st.title("Chinese Zodiac & Compatibility Finder")

# 🔢 User Input
birth_year = st.number_input("Enter your birth year:", min_value=1924, max_value=2100, step=1)
zodiac_row = zodiac_df[zodiac_df["Year"] == birth_year].iloc[0]
zodiac_sign, element, yin_yang_polarity = zodiac_row["Zodiac"], zodiac_row["Element"], zodiac_row["Yin/Yang"]

st.subheader(f"Your Chinese Zodiac: {zodiac_sign} ({element}, {yin_yang_polarity})")
st.write(f"**Personality:** {zodiac_traits[zodiac_sign]['Personality']}")
st.write(f"**Strengths:** {zodiac_traits[zodiac_sign]['Strengths']}")
st.write(f"**Weaknesses:** {zodiac_traits[zodiac_sign]['Weaknesses']}")

# ✅ Check for Accuracy
if birth_year == 1963:
    st.warning("Correction: Rabbit (Water, Yin) ✅")

# ❤️ Compatibility Checker
st.subheader("🔮 Check Compatibility with Another Person")
partner_year = st.number_input("Enter their birth year:", min_value=1924, max_value=2100, step=1)
partner_zodiac = zodiac_df[zodiac_df["Year"] == partner_year].iloc[0]["Zodiac"]

st.write(f"Your partner's zodiac: {partner_zodiac}")

if partner_zodiac in compatibility_chart[zodiac_sign]:
    st.success(f"✨ {zodiac_sign} and {partner_zodiac} are highly compatible! Expect harmony and deep connection.")
else:
    st.warning(f"⚠️ {zodiac_sign} and {partner_zodiac} may have challenges. Respect and understanding will be key.")
