import streamlit as st
import time
import sys

st.title("Compound Interest Calculator")

def validasi_input(value):
    try:
        return float(value.replace(".", "").replace(",","."))
    except ValueError:
        st.error("Invalid input. Please enter a valid number")
        return 0.0

suku_bunga = st.number_input("Suku Bunga (%)", min_value=0, value=5)
durasi = st.number_input("Jumlah Periode (hari)", min_value=0)

tabungan_input = st.text_input("Nilai uang (Rp)", value="1.000.000,00")
tabungan = validasi_input(tabungan_input)

sys.setrecursionlimit(durasi+100)

hitung_recursive = st.button("Calculate Recursive")
hitung_iterative = st.button("Calculate Iterative")

def Power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base 
    else:
        return base * Power(base,exponent-1)
    
def iterative(durasi, tabungan, retur):
    for _ in range(durasi):
        tabungan *= retur
    return tabungan

retur = 1 + suku_bunga / 100 / 260

if hitung_recursive:
    start = time.time()
    base = retur
    exponent = durasi
    result_recursive = Power(base, exponent) * tabungan
    end = time.time()

    result = format(result_recursive, ',.0f')
    st.write(f"Nilai Masa Depan (Recursive): Rp {result}")
    st.write(f"Time Execute (Recursive): {(end - start) * 1000:.4f} ms")

if hitung_iterative:
    start = time.time()
    result_iterative = iterative(durasi, tabungan, retur)
    end = time.time()

    result = format(result_iterative, ',.0f')
    st.write(f"Nilai Masa Depan (Iterative): Rp {result}")
    st.write(f"Time Execute (Iterative): {(end - start) * 1000:.4f} ms")
