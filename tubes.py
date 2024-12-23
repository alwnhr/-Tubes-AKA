import streamlit as st
import time

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

hitung_recursive = st.button("Calculate Recursive")
hitung_iterative = st.button("Calculate Iterative")

def ExponentBySquaring(base, exponent):
    """
    Exponentiation by squaring (fast exponentiation).
    """

    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return base * ExponentBySquaring(base*base, (exponent-1)/2)
    else:
        return ExponentBySquaring(base*base,exponent/2)
    
def iterative(durasi, tabungan, retur):
    for _ in range(durasi):
        tabungan *= retur
    return tabungan

if hitung_recursive:

    retur = 1 + suku_bunga / 100 / 260

    start = time.time()
    result_recursive = ExponentBySquaring(retur, durasi) * tabungan
    end = time.time()

    result = format(result_recursive, ',.0f')
    st.write(f"Nilai Masa Depan (Recursive): Rp {result}")
    st.write(f"Time Execute (Recursive): {(end - start) * 1000:.4f} ms")

if hitung_iterative:
    
    retur = 1 + suku_bunga / 100 / 260

    start = time.time()
    result_iterative = iterative(durasi, tabungan, retur)
    end = time.time()

    result = format(result_iterative, ',.0f')
    st.write(f"Nilai Masa Depan (Iterative): Rp {result}")
    st.write(f"Time Execute (Iterative): {(end - start) * 1000:.4f} ms")
