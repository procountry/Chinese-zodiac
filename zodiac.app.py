import streamlit as st
import pandas as pd

# Zodiac Information
zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements = ["Metal", "Water", "Wood", "Fire", "Earth"]
yin_yang = ["Yang", "Yin"]

# Create Zodiac Data
start_year = 1924
zodiac_data = []
for year in range(start_year, 2100):
    zodiac_sign = zodiac_animals[(year - start_year) % 12]
    element = elements[((year - start_year) % 10) // 2]
    yin_yang_polarity = yin_yang[(year - start_year) % 2]
    zodiac_data.append({"Year": year, "Zodiac": zodiac_sign, "Element": element, "Yin/Yang": yin_yang_polarity})

zodiac_df = pd.DataFrame(zodiac_data)

# Streamlit App
st.title("🐉 Chinese Zodiac Finder & Compatibility Checker")

# User Input
birth_year = st.number_input("Enter your birth year:", min_value=1924, max_value=2100, step=1)
zodiac_sign = zodiac_df[zodiac_df["Year"] == birth_year].iloc[0]["Zodiac"]
element = zodiac_df[zodiac_df["Year"] == birth_year].iloc[0]["Element"]
yin_yang_polarity = zodiac_df[zodiac_df["Year"] == birth_year].iloc[0]["Yin/Yang"]

st.subheader(f"Your Chinese Zodiac: {zodiac_sign}")
st.write(f"**Element:** {element}")
st.write(f"**Yin/Yang:** {yin_yang_polarity}")

# Compatibility Checker
st.subheader("🔮 Check Compatibility with Another Person")
partner_year = st.number_input("Enter their birth year:", min_value=1924, max_value=2100, step=1)
partner_zodiac = zodiac_df[zodiac_df["Year"] == partner_year].iloc[0]["Zodiac"]

st.write(f"Your partner's zodiac: {partner_zodiac}")
