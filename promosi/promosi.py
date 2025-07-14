import streamlit as st

# CSS untuk mempercantik tampilan
def add_custom_css():
    st.markdown("""
        <style>
            .main {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
            }
            .title {
                text-align: center;
                color: #1f5c9a;
            }
            .subtitle {
                text-align: center;
                font-size: 18px;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

def main():
    add_custom_css()

    st.markdown('<h1 class="title">PLS 2025 SMA PLUS PGRI CIBINONG</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Selamat datang di kegiatan Pengenalan Lingkungan Sekolah tahun 2025!</p>', unsafe_allow_html=True)
    st.markdown("---")

    # Gambar berdampingan
    col1, col2 = st.columns(2)
    with col1:
        st.image("logo pesat.png", caption="SMA Plus PGRI Cibinong", use_container_width=True, width=-200)
    with col2:
        st.image("logo prodesk.png", caption="Student Day Programming Desktop", use_container_width=True, width=10)

    st.markdown("---")

    # Form input nama
    with st.container():
        name = st.text_input("Masukkan nama Anda:")

        if st.button("Submit"):
            if name:
                st.success(f"👋 Selamat datang, {name}! Selamat mengikuti PLS 2025 🎉")
                st.balloons()
            else:
                st.warning("⚠️ Silakan masukkan nama Anda terlebih dahulu.")

    # Penutup
    st.markdown("---")
    st.info("💡 Jangan lupa untuk mengikuti seluruh rangkaian kegiatan PLS dengan semangat dan antusias!")

if __name__ == "__main__":
    main()
