import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from googletrans import Translator
import numpy as np
from PIL import Image

# Load model
model = load_model("alatmusiktrad.h5")

# Kelas alat musik tradisional dan deskripsinya
class_info = {
    'banten_dogdoglojor': 'Dogdog Lojor\n\nDinamakan Dogdog lonjor karena alat musik tradisional Banten Selatan ini menghasilkan bunyi dog-dog saat dimainkan. Sementara lonjor sendiri dalam bahasa Banten berarti panjang, sesuai dengan bentuknya yang panjang hampir 1 meter. Dog-dog lonjor terbuat dari batang kayu berdiameter 20 sampai 30 cm yang berongga di bagian tengahnya. Di salah satu ujung rongga ditutup dengan kulit hewan sebagai membrannya. Semakin renggang membran kulit hewan yang dipasang, maka semakin nyaring pula bunyi instrumen ini saat dimainkan. Dog dog lonjor biasanya dimainkan secara bersama-sama dalam upacara seren taun bersama angklung buhun atau sebagai pengiring lagu-lagu daerah Banten.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = ""\n\n link video = "https://www.youtube.com/watch?v=sCsPgA4M8vM"',
    'jakarta_tehyan': 'Tehyan \n\nTehyan berasal dari ibu kota jakarta yang memiliki jenis suara kordofon yang digunakan dengan cara di gesek di bagian dawai atau senarnya, hampir sama dengan memainkan biola.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/rori160614/ready-tehyan-bukan-cort-fender-ibanez-gibson-godin-takamine?extParam=ivf%3Dfalse%26keyword%3Dtehyan%26search_id%3D202506240309434734BA6F3DE83D2648ZZ%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=yUyYvlnVfwc"',
    'jawabarat_angklung': 'Angklung\n\n Angklung adalah alatmusik tradisional yangberasal dari Jawa baratyang dimainkan dengan caradigoyangkan. Jenis bambu yangbiasa digunakan untuk membuatangklung adalah awi wulung(bambu hitam) dan awi temen(bambu putih). Setiap laras atau nada dihasilkan dihasilkan dari bunyi tabung bambu yang berbentuk wilahan (bilah) setiap ruas bambu mulai ukuran besar.\n\nTokoh angklung yang terkenal di sunda adalah Udjo Ngalagena, pendiri saung angklung Udjo di Bandung yang telah mengembangkan teknik permainan angklung berdasarkan laras-laras salendro, pelog dan madenda sejak tahun 1966.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/craftnusantara/angklung-satuan-bambu-hitam-3-tabung-tali-rotan-hitam-nada-do-tinggi?extParam=ivf%3Dfalse%26keyword%3Dangklung%26search_id%3D20250624034547320722549D17513B4TPQ%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=COqgqRlrrWY"',
    'jawabarat_calung': 'Calung \n\nCalung merupakan alatmusik sunda yang hampirsama dengan angklung.Cara memainkan alat musik calung adalah dengan memukul batang dari ruas-ruas yang disusun berdasarkan titi laras atau tangga nada pentatonik (da-mi-na-ti-la).\n\n Salah satu maestro calung sunda adalah mbah Darso (Alm) yang telah mempopulerkan angklung dengan karya-karyanya. Sehingga alat musik tradisional sunda ini lebih dikenal di masyarakat.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/poppymar/dijual-calung-sunda-satu-set-4-sisir-diskon?extParam=ivf%3Dfalse%26keyword%3Dcalung%26search_id%3D20250624035347DB8E1AF0CB3ACA179HHZ%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=WKWNb4FM_h8"',
    'jawabarat_celempung': 'Celempung\n\n Celempung memanfaatkan Cara memainkan alat musik ini ada gelombang resonansi yang ada di dalam ruas batang bambu, alat musik ini sendiri terbuat dari hinis bambu. Alat pemukul celempung terbuat dari bahan kayu atau bambu yang ujungnya telah diberi kain atau benda tipis lainnya agar menghasilkan bunyi nyaring.\n\n Cara memainkan alat ini dengan dipukul atau dengan mengatus sendiri besar kecilnya udara yang keluar dari badan celempung dengan tangan.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/giripurwaseni/celempung-bambu-sunda-1729578148059777661?extParam=ivf%3Dfalse%26keyword%3Dcelempung%26search_id%3D2025062404031234ED066DF378EF0D5DJP%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=RUXKTjjk-QM"',
    'jawabarat_gong': 'Gong \n\nGong termasuk alat musik pukul khas Jawa Barat. Gong dapat dijumpai pada rangkaian alat musik gamelan dan bentuknya bulat besar.\n\n Gong merupakan sebuah alat musik pukul yang terkenal di Asia Tenggara dan Asia Timur. Saat ini tidak banyak lagi perajin gong seperti ini. Gong yang telah ditempa belum dapat ditentukan nadanya. Nada gong baru terbentuk setelah dibilas dan dibersihkan. Apabila nadanya masih belum sesuai, gong dikerok sehingga lapisan perunggunya menjadi lebih tipis.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/garasi08561303623sasi/gong-peresmian-diameter-80cm-besi-plat-sewa?extParam=ivf%3Dfalse%26keyword%3Dgong+besi%26search_id%3D20250624040518B3967A0E938DC211850O%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=tkTXxUR0k_4"',
    'jawabarat_karinding': 'Karinding\n\n Alat musik ini mulai populer di kalangan anak muda sunda sejak tahun 2008, setelah alat ini dikenalkan oleh anak-anak metal UjungBerung rebels. Terutama dengan kelompok musik Karinding attack nya. Alat musik sunda yang dibuat dari batang pohon kawung (aren) atau bambu dan dimainkan dengan cara dibetrik ujung jari dan di simpan di mulut.\n\n Karinding telah digunakan di daerah sunda sejak abad 15 terutama di daerah Tasikmalaya. Alat musik ini dapat dimainkan secara solo atau berkelompok (2-5 orang). Karinding masuk dalam keluarga alat musik harpa mulut dan masih satu jenis dengan alat musik génggong dari bali dan kuriding dari Kalimantan Selatan. Meskipun belum teruji secara ilmiah, Masyarakat sunda baheula percaya bahwa suara yang dihasilkan alat musik tradisional sunda ini dapat mengusir hama di sawah, karena mengeluarkan suara low decible atau ultrasonik.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/dansdoang/karinding-bambu?extParam=ivf%3Dfalse%26keyword%3Dkarinding%26search_id%3D20250624040555577BCC914F9E55319PXX%26src%3Dsearch"\n\n link video = "https://www.tiktok.com/@yogi_karinding_real/video/7437466208435326263"',
    'jawabarat_kecapi': 'Kecapi\n\n Alat musik tradisional sunda ini dimainkan dengan cara dipetik dan biasanya ditemani alunan suling sunda untuk mengiringi kawih sunda ataupun tembang cianjuran.\n\nKecapi biasanya dibuat dari kayu kenanga sedangkan senar kecapi terbuat dari kawat baja, jaman dahulu senar kecapi terbuat dari campuran logam emas dan tembaga sehingga suara yang di hasilkan lebih nyaring. \n\nAlunan dari kecapi suling kan membuat orang terutama orang sunda yang berada di perantauan, mengalihkan imajinasi nya ke kampung halaman mereka. Dengan sawah yang terhampa pepohonan yang hijau, gunung sefta orang yang beraktivitas disekitarnya.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/ayusatriani/terlaris-guzheng-kecapi-alat-musik-tradisional-cina-termurah-1731170720675759114?extParam=ivf%3Dfalse%26keyword%3Dalat+musik+kecapi%26search_id%3D202506240407433FE94A002317B5203NM6%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=HxWLZxlRw_o"',
    'jawabarat_rebab': 'Rebab\n\n Bahan yang di gunakan untuk membuat rebab adalah tembaga, namun pada perkembangannya bagian yang memanjang pada rebab d buat dari bahan kayu nangka Sedangkan bagian tubuhnya terbuat dari kayu yang berongga yang ditutupi kulit, usus atau kemih lembu yang dikeringkan.\n\nCara memainkan alat musik ini sama seperti biola, yaitu dengan cara digesek. Selain itu, rebab memiliki dua sampai tiga senar yang terbuat dari logam.\n\nRebab termasuk dalam rangkaian perangkat gamelah yang biasa dipakai untuk mengiring pertunjukan wayang celempungan, kliningan atau pengiring tembang cianjuran. Rebab memiliki fungsi sebagai penuntun arah lagu dan masuk ke Indonesia melalui jalur - jalur perdagangan Islam.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/maliko-1/rebab-gamelan-jawa-kayu-sonokeling-murah?extParam=ivf%3Dfalse%26keyword%3Drebab%26search_id%3D202506240408173AD7C2EBB96FCB03AKAS%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=FgRFM4g6mBI"',
    'jawabarat_suling': 'Suling \n\nAlat musik suling merupakan jenis alat instrument karawitan sunda yang dimainkan dengan cara ditiup. Suling sunda ada yang memiliki lubang 4 dan 6 dan memiliki suara yang khas. \n\n Suling sunda terbuat dari bambu tamiang (bambu lemang) yang memiliki bentuk tipis dan berdiameter kecil. Ukuran suling menentukan tinggi rendahnya suara, untuk lagu-lagu tembang, suling yang digunakan berkisar sekitar 60-65 cm (suaranya lebih rendah), ukuran ini lebih panjang dibandingkan suling yang digunakan untuk penggiring kawin atau degung dengan panjang 50-59 cm.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://shopee.co.id/Mainan-Anak-Edukatif-Alat-Musik-Tradisional-Seruling-Bambu-i.9543076.19450912158?sp_atk=987dc337-0a89-4ea8-a1b1-a4ce35f33900&xptdk=987dc337-0a89-4ea8-a1b1-a4ce35f33900"\n\n link video = "https://www.youtube.com/watch?v=cVumThGBdEg"',
    'jawabarat_tarawangsa': 'Tarawangsa\n\nAlat musik sunda tarawangsa merupakan alat musik kayu yang dimainkan dengan cara digesek dan dipetik bersamaan, terdiri dari bagian tangkai dan bagian penggesek. Dawainya mempunyai dua senar, senar paling dekat dimainkan dengan di petik dengan cara digesek dan senar satunya dimainkan dengan cara dipetik. Tarawangsa yang terbuat dari jenis kayu dadap, jengkol, kemiri dan kenangan ini di jaman dahulu dimainkan saat perayaan panen untuk persembangan pada Dewa penguasa padi (Dewi sri) dengan dipimpin oleh sesepuh adat.\n\nTarawangsa yang terbuat dari jenis kayu dadap, jengkol, kemiri dan kenangan ini di jaman dahulu dimainkan saat perayaan panen untuk persembangan pada Dewa penguasa padi (Dewi sri) dengan dipimpin oleh sesepuh adat. Ketika musik dari alat musik sunda jentréng dan tarawangsa di mainkan. Para penari yang terdiri dari lelaki ataupun perempuan akan menari dengan gaya tak beraturan atau tanpa pola tertentu.\n\nKarena gerakannya inilah sebagian orang menganggap bahwa penari telah dimasuki oleh roh lain dan tak menyadari apa yang dilakukannya.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://shopee.co.id/Kacapi-Jentreng-Tarawangsa-i.10971128.284559901?sp_atk=dd9177d9-6682-4dcb-a76c-bb272f08cfa2&xptdk=dd9177d9-6682-4dcb-a76c-bb272f08cfa2"\n\n link video = "https://www.tiktok.com/@egargarda/video/7335266141775924486"',
    'jawatengah_bonang': 'Bonang\n\nBonang merupakan alat musik pukul khas Jawa Tengah yang dibuat dari kuningan, besi, atau perunggu. Untuk memainkannya, dibutuhkan sebuah pemukul khusus yang terbuat dari kayu yang sudah dilapisi dengan karet atau kain.\n\nBonang terbagi menjadi dua jenis berdasarkan ukurannya. Yang pertama adalah bonang barung yang ukurannya lebih besar dan bonang penerus yang ukurannya lebih kecil.\n\nBonang barung mempunyai nada dengan oktaf tengah hingga tinggi dan biasa menjadi pembuka dalam ansambel. Alat musik ini juga bisa menjadi penuntun instrumen-instrumen lain jika dimainkan dengan teknik tabuhan pipilan.\n\nSelain itu, bonang barung bisa juga menjadi pembentuk pola-pola dan hiasan-hiasan lagu jika dimainkan dengan teknik tabuhan imbal-imbalan.\n\nSementara itu, bonang penerus mempunyai nada dengan oktaf yang tinggi. Saat dimainkan dengan teknik tabuhan pipilan, bonang panerus berkecepatan dua kali lipat dibanding bonang barung.\n\nKemudian, jika dimainkan dengan teknik tabuhan imbal-imbalan, bonang penerus dapat memainkan pola-pola lagu yang jalin menjalin.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://shopee.co.id/Gamelan-Bonang-Besi-Pencu-Kuningan-i.109649775.1940168819?sp_atk=f0e9a585-e51d-4e97-819b-c64b7924fb55&xptdk=f0e9a585-e51d-4e97-819b-c64b7924fb55"\n\n link video = "https://www.youtube.com/watch?v=-oBi_7_YtJA"',
    'jawatengah_demung': 'Demung\n\n Demung merupakan alat musik tradisional dari Jawa Tengah yang menjadi bagian dari keluarga balungan. Demung dalam pagelaran musik gamelan dibagi menjadi dua jenis, yakni demung bernada pelog dan demung bernada slendro.\n\nUniknya, walaupun memiliki bentuk yang cukup besar, demung justru memiliki nada dengan oktaf terendah dibanding alat musik balungan lainnya. Alat musik yang satu ini terbuat dari logam kuningan dan dimainkan dengan cara dipukul menggunakan alat pemukul khusus.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/manunggal-jaya-art/demung-gamelan-kuningan-pelog-dplw7k?extParam=ivf%3Dfalse%26keyword%3Ddemung%26search_id%3D2025062403154034ED066DF378EF2D4LFM%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=UVgMGoU2IIA"',
    'jawatengah_siter': 'Siter\n\n Siter Mirip seperti demung, Siter juga termasuk alat musik dengan bunyi yang bernada pelog serta slendro. Hanya saja, siter mempunyai 11 hingga 13 pasang  senar dan dimainkan dengan cara dipetik.\n\nSenar-senar siter dimainkan menggunakan ibu jari, sementara jari yang lain bertugas menahan getaran saat senar lain dipetik.  Biasanya, alat musik tradisional yang satu ini mempunyai panjang sekitar 30 cm dan dimasukan ke dalam sebuah kotak yang menjadi resonatornya.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://shopee.co.id/siter-ricikan-gamelan-siter-i.925765362.26533991958?sp_atk=6f6f6de7-1333-4326-a068-8ec714f48798&xptdk=6f6f6de7-1333-4326-a068-8ec714f48798"\n\n link video = "https://www.youtube.com/watch?v=SHJIPUfF07Q"',
    'jawatimur_kluncing': 'Kluncing\n\n Kluncing merupakan alat musik khas Jawa Timur yang tampilannya persis alat musik Triangel. Hal ini dipengaruhi oleh masuknya budaya asing Eropa. Bahan untuk membuat Kluncing ialah dari logam. Adapun untuk memainkan alat musik Kluncing sangatlah mudah, cukup dipukul saja, maka akan melahirkan bunyi yang terdengar ditelinga.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = ""\n\n link video = ""',
    'jawatimur_saronen': 'Saronen\n\n Saronen merupakan alat musik tradisional asal Madura yang panjangnya mencapai 40 cm dan dimainkan dengan cara ditiup. Seperti suling, untuk mengatur nada-nada yang dihasilkan, pemainnya harus menggunakan jari tangan. Saat dimainkan, saronen dapat mengeluarkan suara yang keras sekaligus nyaring.\n\nPerbedaan Saronen dengan suling pada umumnya adalah jumlah lubangnya. Saronen memiliki tujuh buah lubang, satu lubangnya berderetan di belakang sedangkan enam lubang lainnya berdertan di bagian depan.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://shopee.co.id/slompret-i.35857352.26362636299?sp_atk=04d20aa5-8fd6-4071-80b9-758a49a89644&xptdk=04d20aa5-8fd6-4071-80b9-758a49a89644"\n\n link video = "https://www.youtube.com/watch?v=MG3zTJul1OQ"' ,
    'yogjakarta_kendang': 'Kendang\n\n Kendang atau kendhang adalah instrumen dalam gamelan Jawa Tengah dan Jawa Barat yang salah satu fungsi utamanya mengatur irama. Instrument ini dibunyikan dengan tangan, tanpa alat bantu. Jenis kendang yang kecil disebut ketipung, yang menengah disebut kendang ciblon/kebar. Pasangan ketipung ada satu lagi bernama kendang gedhe biasa disebut kendang kalih. Kendang kalih dimainkan pada lagu atau gendhing yang berkarakter halus seperti ketawang, gendhing kethuk kalih, dan ladrang irama dadi.\n\nBisa juga dimainkan cepat pada pembukaan lagu jenis lancaran,ladrang irama tanggung. Untuk wayangan ada satu lagi kendhang yang khas yaitu kendhang kosek.\n\nKendang kebanyakan dimainkan oleh para pemain gamelan profesional, yang sudah lama menyelami budaya Jawa. Kendang kebanyakan di mainkan sesuai naluri pengendang, sehingga bila dimainkan oleh satu orang dengan orang lain maka akan berbeda nuansanya.\n\n dibawah ini adalah link untuk membeli dan cara memainkan alat musik tersebut \n*disclaimer admin tidak bertanggung jawab atas link dibawah\n\nlink pembelian = "https://www.tokopedia.com/giripurwaseni/kendang-jaipong-1-set-rampak-kayu-mangga-1729579804834368125?extParam=ivf%3Dfalse%26keyword%3Dkendang%26search_id%3D2025062403373594F6D7E04A4D453C0IY5%26src%3Dsearch"\n\n link video = "https://www.youtube.com/watch?v=3F6FsJp1zXw"'
}

def translate_to_english(text):
    try:
        translator = Translator()
        translated = translator.translate(text, src='id', dest='en')
        return translated.text
    except Exception as e:
        return f" Translation failed: {e}"
    
# Konfigurasi tampilan
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #8B4513;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stFileUploader, .stCameraInput {
        background-color: #8B4513;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# SESSION NAVIGASI
if "page" not in st.session_state:
    st.session_state.page = "Welcome"

def set_page(p):
    st.session_state.page = p

# SIDEBAR
st.sidebar.title("Navigasi")

welcome_btn = st.sidebar.button("Welcome", on_click=set_page, args=("Welcome",))
prediction_btn = st.sidebar.button("Prediction", on_click=set_page, args=("Prediction",))
information_btn = st.sidebar.button("Information", on_click=set_page, args=("Information",))

# WELCOME
if st.session_state.page == "Welcome":
    st.title("🎼 Selamat Datang di Aplikasi Klasifikasi Alat Musik Tradisional")
    st.markdown("""
    Aplikasi ini membantu mengenali **alat musik tradisional Indonesia** berbasis gambar secara cepat dan akurat.
    
    Anda dapat mengunggah atau mengambil foto alat musik, lalu sistem akan memprediksi dan memberikan informasi terkait.

    ---
    ### Cara Menggunakan Aplikasi
    1. Klik menu **Prediction** di sidebar.
    2. Upload gambar alat musik atau gunakan kamera.
    3. Sistem akan menampilkan hasil prediksi beserta deskripsinya.
    4. Jika ingin membaca deskripsi semua alat musik, klik menu **Information**.

    ---
    """)
    st.title("🎼 Welcome to the Traditional Musical Instrument Classification App")
    st.markdown("""
    This application helps recognize **traditional Indonesian musical instruments** from images quickly and accurately.
    
    You can upload or take a photo of a musical instrument, and the system will predict and provide related information..

    ---
    ### How to Use the App
    1. Click the **Prediction** menu in the sidebar.
    2. Upload an image of a traditional musical instrument or use the camera.
    3. The system will display the prediction and its description.
    4. To read the descriptions of all instruments, click the **Information** menu.

    ---
    """)

# PREDIKSI
elif st.session_state.page == "Prediction":
    st.title("🎶 Klasifikasi Alat Musik Tradisional")
    st.markdown("Upload gambar atau gunakan kamera untuk memulai klasifikasi alat musik.")

    input_mode = st.radio("Pilih metode input:", ("📸 Kamera", "📁 Upload File"))

    if input_mode == "📸 Kamera":
        uploaded_file = st.camera_input("Ambil gambar menggunakan kamera")
    else:
        uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='📷 Gambar yang Diproses', use_column_width=True)

        img = img.resize((224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array)
        confidence = np.max(prediction)
        predicted_class = list(class_info.keys())[np.argmax(prediction)]

        if confidence < 0.5:
            st.error("🚫 Gambar tidak dikenali sebagai alat musik tradisional.")
        else:
            st.success(f"🎼 Prediksi: **{predicted_class}** ({confidence:.2f} confidence)")
            st.markdown("### Deskripsi:")
            st.info(class_info[predicted_class])
        if st.button("🔄 Translate to English"):
            translated_text = translate_to_english(class_info[predicted_class])
            st.markdown("### 📝 English Description:")
            st.success(translated_text)

# INFORMASI 
elif st.session_state.page == "Information":
    st.title("📚 Informasi Alat Musik Tradisional")
    for alat, deskripsi in class_info.items():
        nama_alat = alat.replace('_', ' ').title()
        st.subheader(f"{nama_alat}")
        st.info(deskripsi)

        # Tombol translate per alat musik
        if st.button(f"🔄 Translate {nama_alat} to English", key=f"btn_translate_{alat}"):
            translated = translate_to_english(deskripsi)
            st.markdown("### English Description:")
            st.success(translated)

        st.markdown("---")
