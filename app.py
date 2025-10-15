import streamlit as st
import matplotlib.pyplot as plt
import random

# Заглавие на приложението
st.title("📊 Хистограма на възрастите на клиентите в ресторанта")

# Генерираме случайни възрасти
ages = [random.randint(1, 67) for _ in range(20)]

# Показваме ги като текст
st.write("**Възрасти на клиентите:**", ages)

# Създаваме фигура и хистограма
fig, ax = plt.subplots()
ax.hist(ages, bins=10, edgecolor='black', color='skyblue')
ax.set_title('Разпределение на възрастите на клиентите')
ax.set_xlabel('Възраст')
ax.set_ylabel('Брой клиенти')

# Показваме графиката в Streamlit
st.pyplot(fig)
