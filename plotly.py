import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Veri setini genişlet ve oluştur
def create_data(n=200):
    np.random.seed(0)
    cities = ['Berlin', 'Münih', 'Frankfurt', 'Hamburg', 'Köln']
    data = {
        'Yaş': np.random.randint(18, 65, size=n),
        'Gelir': np.random.randint(20000, 120000, size=n),
        'Cinsiyet': np.random.choice(['Erkek', 'Kadın'], size=n),
        'Hesap Türü': np.random.choice(['Mevduat', 'Kredi', 'Yatırım'], size=n),
        'Şehir': np.random.choice(cities, size=n),
    }
    return pd.DataFrame(data)

df = create_data()

# Başlık
st.title('Interaktif Müşteri Veri Dashboardu')

# Veri setini göster
st.write("Genişletilmiş Müşteri Verileri", df)

# Cinsiyete ve Hesap Türüne Göre Müşteri Dağılımı
fig = px.histogram(df, x='Cinsiyet', color='Hesap Türü', barmode='group',
                   hover_data=df.columns, title="Cinsiyete ve Hesap Türüne Göre Müşteri Dağılımı")
st.plotly_chart(fig, use_container_width=True)

# Müşteri Yaş Dağılımı
fig = px.histogram(df, x='Yaş', marginal='box', color='Cinsiyet',
                   hover_data=df.columns, title="Müşteri Yaş Dağılımı")
st.plotly_chart(fig, use_container_width=True)

# Müşteri Gelir Dağılımı
fig = px.box(df, x='Cinsiyet', y='Gelir', color='Cinsiyet',
             hover_data=df.columns, title="Müşteri Gelir Dağılımı")
st.plotly_chart(fig, use_container_width=True)

# Plotly ile Şehirlere Göre Müşteri Dağılımı
fig = px.histogram(df, x='Şehir', color='Şehir', title="Şehirlere Göre Müşteri Dağılımı",
                   hover_data=df.columns)
st.plotly_chart(fig, use_container_width=True)