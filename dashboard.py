import streamlit as st

def show_dashboard():

    # ======================
    # 🎨 STYLE
    # ======================
    st.markdown("""
    <style>

    .block-container{
        padding-top:0rem;
        padding-bottom:2rem;
    }

    .hero{
        width:100vw;
        margin-left:calc(-50vw + 50%);
        margin-top:-6.2rem;
        height:100vh;

        display:flex;
        align-items:center;
        justify-content:center;
        text-align:center;
        color:white;

        background:
        linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.45)),
        url('https://asset-2.tstatic.net/newsmaker/foto/bank/images/Janti-Park-di-Klaten-Jawa-Tengah-9.jpg');

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
    }

    .hero h1{
        font-size:52px;
        font-weight:700;
        margin-bottom:10px;
    }

    .hero p{
        font-size:18px;
        opacity:.9;
    }

    .section{
        max-width:1000px;
        margin:auto;
        padding:0px 30px 60px 30px;
    }

    .title{
        font-size:26px;
        font-weight:600;
        margin-bottom:15px;
    }

    .text{
        font-size:16px;
        color:#555;
        line-height:1.8;
        text-align:justify;
    }

    iframe{
        border-radius:14px;
        width:100%;
        height:300px;
        border:none;
    }

    </style>
    """, unsafe_allow_html=True)

    # ======================
    # HERO
    # ======================
    st.markdown("""
    <div class="hero">
        <div>
            <h1>Janti Park</h1>
            <p>Analisis & Prediksi Pengunjung Wisata</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ======================
    # DESKRIPSI
    # ======================
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>Tentang Janti Park</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='text'>
    Janti Park adalah destinasi wisata air yang menyenangkan di Kabupaten Klaten, Jawa Tengah, yang menawarkan pengalaman rekreasi keluarga
    dengan suasana alam yang asri. Terletak di kawasan Desa Wisata Janti yang kaya akan sumber mata air alami, tempat ini memadukan wahana modern
    seperti kolam arus, area bermain anak, dan taman rekreasi dengan nuansa pedesaan yang sejuk dan nyaman.
    Berbeda dari waterpark perkotaan, Janti Park memanfaatkan air alami yang jernih dan segar dari sumber pegunungan, sehingga memberikan pengalaman
    berenang yang lebih alami. Kawasan yang luas, pepohonan rindang, gazebo santai, serta pemandangan sawah hijau menjadikan tempat ini pilihan ideal untuk
    liburan keluarga maupun wisata rombongan.Selain sebagai tempat rekreasi, Janti Park juga menjadi simbol pengembangan pariwisata desa yang berkelanjutan. Pengelolaannya melibatkan masyarakat setempat melalui BUMDes sehingga mampu meningkatkan perekonomian warga sekitar.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>Sejarah Singkat Janti Park</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='text'>
    Awalnya, kawasan Janti dikenal sebagai area pemancingan dan pemandian alami yang dimanfaatkan masyarakat sekitar.
    Karena memiliki sumber air yang melimpah dan lingkungan yang indah, kawasan ini kemudian dikembangkan menjadi destinasi wisata modern
    tanpa meninggalkan unsur alam dan budaya desa. Seiring waktu, Janti Park berkembang menjadi salah satu ikon wisata unggulan di Klaten dan
    sering menjadi tujuan wisata keluarga, kegiatan sekolah, gathering, serta berbagai acara komunitas.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='title'>Analisis dan Prediksi Pengunjung</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='text'>
    Sebagai destinasi wisata yang terus berkembang, jumlah pengunjung Janti Park mengalami perubahan pada periode tertentu, terutama saat akhir pekan,
    musim liburan, maupun hari besar nasional. Oleh karena itu, diperlukan analisis data kunjungan untuk mengetahui pola peningkatan maupun penurunan jumlah wisatawan.
    Melalui dashboard ini, data historis pengunjung diolah menggunakan metode regresi linier untuk menghasilkan prediksi jumlah pengunjung pada periode mendatang.
    Hasil prediksi ini dapat membantu pengelola dalam merencanakan kapasitas area wisata, kebutuhan tenaga kerja, strategi promosi, serta peningkatan pelayanan agar operasional
    menjadi lebih efektif dan efisien.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ======================
    # INFORMASI
    # ======================
    st.divider()

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Informasi")
            st.write("📍 Janti Park, Klaten, Jawa Tengah")
            st.write("📞 0812-1500-7979")
            st.markdown("[🌐 www.jantipark.com](https://www.jantipark.com)")

            # Instagram dikembalikan
            st.markdown("""
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="margin-top:-28px;">

            <a href="https://www.instagram.com/jantipark.klaten"
            target="_blank"
            style="
                text-decoration:none;
                display:flex;
                align-items:center;
                gap:8px;
                font-size:1rem;
                font-weight:400;
                color:white;
            ">

            <i class="bi bi-instagram"
            style="
                font-size:1rem;
                color:#ff2f7d;
            "></i>

            @jantipark.klaten

            </a>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.subheader("Lokasi")
            st.components.v1.html("""
            <iframe src="https://www.google.com/maps?q=Janti+Park&output=embed"></iframe>
            """, height=300)

    st.divider()
    st.caption("© 2025 Janti Park - Sistem Prediksi Pengunjung")