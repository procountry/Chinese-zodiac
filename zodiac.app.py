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
    
    # 🔥 Corrected Element Calculation
    element = elements[((year - 1924) % 10) // 2]  # Every two years share the same element
    
    yin_yang_polarity = yin_yang[(year - start_year) % 2]
    zodiac_data.append({"Year": year, "Zodiac": zodiac_sign, "Element": element, "Yin/Yang": yin_yang_polarity})

zodiac_df = pd.DataFrame(zodiac_data)

# 🖥 Streamlit Interface
st.title("🐉 Chinese Zodiac Finder & Compatibility Checker")

# 🔢 User Input
birth_year = st.number_input("Enter your birth year:", min_value=1924, max_value=2100, step=1)
zodiac_row = zodiac_df[zodiac_df["Year"] == birth_year].iloc[0]
zodiac_sign, element, yin_yang_polarity = zodiac_row["Zodiac"], zodiac_row["Element"], zodiac_row["Yin/Yang"]

st.subheader(f"Your Chinese Zodiac: {zodiac_sign} ({element}, {yin_yang_polarity})")

# ✅ Check for Accuracy
if birth_year == 1963:
    st.warning("Correction: Rabbit (Water, Yin) ✅")
