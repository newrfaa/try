import streamlit as st

def mm1_model(lmbda, mu):
    if lmbda >= mu:
        return {"error": "λ harus lebih kecil dari μ agar sistem stabil."}
    
    rho = lmbda / mu
    L = lmbda / (mu - lmbda)
    Lq = (lmbda ** 2) / (mu * (mu - lmbda))
    W = 1 / (mu - lmbda)
    Wq = lmbda / (mu * (mu - lmbda))

    return {
        "rho": round(rho, 4),
        "L": round(L, 4),
        "Lq": round(Lq, 4),
        "W": round(W, 4),
        "Wq": round(Wq, 4)
    }

# Streamlit UI
st.title("Model Antrian M/M/1")

st.markdown("""
Model ini menghitung metrik performa dari sistem antrian **M/M/1** berdasarkan:
- **λ (lambda)** = laju kedatangan (arrival rate)
- **μ (mu)** = laju pelayanan (service rate)

Masukkan nilai untuk melihat hasilnya.
""")

lmbda = st.number_input("Masukkan nilai λ (lambda)", min_value=0.0, format="%.4f")
mu = st.number_input("Masukkan nilai μ (mu)", min_value=0.0, format="%.4f")

if st.button("Hitung"):
    if lmbda == 0 or mu == 0:
        st.warning("λ dan μ harus lebih besar dari 0.")
    else:
        hasil = mm1_model(lmbda, mu)
        if "error" in hasil:
            st.error(hasil["error"])
        else:
            st.subheader("Hasil Perhitungan:")
            st.write(f"**ρ (Utilisasi):** {hasil['rho']}")
            st.write(f"**L (Jumlah rata-rata dalam sistem):** {hasil['L']}")
            st.write(f"**Lq (Jumlah rata-rata dalam antrian):** {hasil['Lq']}")
            st.write(f"**W (Waktu rata-rata dalam sistem):** {hasil['W']} satuan waktu")
            st.write(f"**Wq (Waktu rata-rata dalam antrian):** {hasil['Wq']} satuan waktu")
