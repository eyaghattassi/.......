import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Configuration de la page ---
st.set_page_config(page_title="Maintenance Prédictive IA", layout="wide")

# --- Titre ---
st.title("🤖 Tableau de Bord - Maintenance Prédictive par IA")
st.markdown("Suivi en temps réel des équipements, prédictions de pannes et indicateurs de performance.")

# --- Simulation de données capteurs ---
np.random.seed(42)
data = pd.DataFrame({
    "Temps (s)": np.arange(1, 101),
    "Vibration (mm/s)": np.random.normal(5, 1, 100),
    "Température (°C)": np.random.normal(60, 5, 100),
    "Courant (A)": np.random.normal(10, 2, 100),
})

# --- Calcul de la probabilité de panne ---
data["Probabilité de panne (%)"] = (
    0.5 * data["Vibration (mm/s)"] +
    0.03 * data["Température (°C)"] +
    0.2 * data["Courant (A)"] +
    np.random.normal(0, 1, 100)
)

# --- Vérification des données ---
if data.isnull().values.any():
    st.warning("⚠️ Des valeurs manquantes ont été détectées dans les données.")

# --- Séparation en colonnes ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("⚙️ Machines surveillées", "12")
    st.metric("📉 Pannes évitées", "7")
with col2:
    st.metric("📊 Disponibilité", "94 %")
    st.metric("⏱️ Temps moyen entre pannes (MTBF)", "210 h")
with col3:
    st.metric("💰 Économie mensuelle", "7 500 TND")
    st.metric("🔔 Alertes actives", "1")

# --- Graphique des capteurs ---
st.subheader("📈 Évolution des capteurs en temps réel")
fig = px.line(data, x="Temps (s)", y=["Vibration (mm/s)", "Température (°C)", "Courant (A)"],
              title="Suivi des variables capteurs", markers=True)
st.plotly_chart(fig, use_container_width=True)

# --- Probabilité de panne ---
st.subheader("⚠️ Analyse prédictive de panne")
fig2 = px.area(data, x="Temps (s)", y="Probabilité de panne (%)",
               color_discrete_sequence=["red"], title="Probabilité de panne prédite par IA")
st.plotly_chart(fig2, use_container_width=True)

# --- Seuil d'alerte dynamique ou manuel ---
st.markdown("### 🔧 Paramétrage du seuil d'alerte")
seuil_utilisateur = st.slider("Définir le seuil d'alerte (%)", min_value=50, max_value=100, value=80)

# --- Alerte ---
last_prob = data["Probabilité de panne (%)"].iloc[-1]
if last_prob > seuil_utilisateur:
    st.error(f"🚨 Risque élevé de panne : {last_prob:.2f}% — Intervention recommandée !")
else:
    st.success(f"✅ Système stable : Probabilité de panne = {last_prob:.2f}%")

st.markdown("*(Ce tableau de bord simule les prédictions IA à partir de données de capteurs.)*")