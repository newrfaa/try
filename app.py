import streamlit as st
from scipy.optimize import linprog

st.title("Optimasi Produksi Banner & Brosur")

st.header("Input Data Produksi")
# Input keuntungan per unit
profit_banner = st.number_input("Keuntungan per Banner (Rp)", value=60000)
profit_brosur = st.number_input("Keuntungan per 100 Brosur (Rp)", value=20000)

# Input waktu produksi per unit
time_banner = st.number_input("Waktu Produksi per Banner (jam)", value=1.0)
time_brosur = st.number_input("Waktu Produksi per 100 Brosur (jam)", value=0.5)

# Total waktu tersedia
total_hours = st.number_input("Total Waktu Produksi Tersedia (jam)", value=32.0)

if st.button("Hitung Optimasi Produksi"):
    # Fungsi objektif (dikalikan -1 karena linprog meminimasi)
    c = [-profit_banner, -profit_brosur]

    # Kendala waktu: time_banner * x + time_brosur * y <= total_hours
    A = [[time_banner, time_brosur]]
    b = [total_hours]

    # Batasan variabel (x >= 0, y >= 0)
    x_bounds = (0, None)
    y_bounds = (0, None)

    result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    if result.success:
        num_banner = result.x[0]
        num_brosur = result.x[1]
        total_profit = -result.fun

        st.success("Optimasi Berhasil!")
        st.write(f"Produksi Banner: {num_banner:.2f} unit")
        st.write(f"Produksi Brosur: {num_brosur:.2f} paket (100 lembar)")
        st.write(f"Total Keuntungan Maksimal: Rp {total_profit:,.0f}")
    else:
        st.error("Optimasi gagal. Periksa kembali input data.")

