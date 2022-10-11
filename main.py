from flask import Flask, render_template

app = Flask(__name__)

artikel=[
    {
        'id' : 1,
        'img' : '/static/img/artikel-1.webp',
        'judul' : '6 Cara Merawat Printer yang Benar Agar Awet dan Tahan Lama.',
        'routing' : '6-Cara-Merawat-Printer-yang-Benar-Agar-Awet-dan-Tahan-Lama',
        'penulis' : 'DIFADIN QUDSY',
        'tanggal' : 'AGUSTUS 30, 2022',
        'isi_konten' : 'KEBUMEN, DIVAPRINTER.COM - Canon melalui PT Datascrip meluncurkan tiga printer ink tank anyar di Indonesia, yakni G6070, G5070, dan GM2070. (Liputan6.com/Agustinus M.Damar) Cara merawat printer yang pertama bisa diawali dari kebiasaan untuk menggunakan printer secara rutin. Sebab, di dalam body dari printer terdapat sangat banyak suku cadang yang berfungsi untuk menggerakan bagian-bagian dari printer. Pada tiap suku cadang tersebut terdapat semacam pelumas yang membuat kinerja printer menjadi lebih halus...'
    },
    {
        'id' : 2,
        'img' : '/static/img/artikel-2.jpg',
        'judul' : 'SSD atau Hardisk? Mana yang Lebih Baik.',
        'routing' : 'SSD-atau-Hardisk-Mana-yang-Lebih-Baik',
        'penulis' : 'DIFADIN QUDSY',
        'tanggal' : 'AGUSTUS 30, 2022',
        'isi_konten' : 'KEBUMEN, DIVAPRINTER.COM - Pada dasarnya, SSD dan HDD memiliki fungsi yang sama: menyimpan aplikasi dan file pribadi serta menjalankan booting sistem. Jika Anda ingin menambahkan kecepatan pada PC desktop atau laptop lama, atau jika Anda sedang memilih drive untuk PC khusus, server, atau sistem khusus, bagaimana cara Anda menentukan pilihan? Apakah sebaiknya Anda memilih SSD (solid-state drive) atau HDD (hard disk drive)...'
    },
    {
        'id' : 3,
        'img' : '/static/img/artikel-3.png',
        'judul' : '5 Tips Memilih Printer, Lebih Baik Sedikit Mahal tetapi Awet dan Hemat Biaya Perawatan.',
        'routing' : '5-Tips-Memilih-Printer-Lebih-Baik-Sedikit-Mahal-tetapi-Awet-dan-Hemat-Biaya-Perawatan',
        'penulis' : 'DIFADIN QUDSY',
        'tanggal' : 'AGUSTUS 30, 2022',
        'isi_konten' : 'KEBUMEN, DIVAPRINTER.COM - Pada era digital, pencetak dokumen atau printer masih dibutuhkan kehadirannya, baik untuk keperluan pribadi maupun perusahaan. Banyak orang memang sudah memanfaatkan dokumen digital, tetapi dokumen berbentuk fisik juga masih diperlukan, terutama dokumen-dokumen yang berkaitan dengan kepentingan perusahaan...'
    },
    {
        'id' : 4,
        'img' : '/static/img/EPSON L3110 Print _ Scan & Copy.jpg',
        'judul' : 'Review Printer Epson L3110: Spesifikasi dan Keunggulannya.',
        'routing' : 'Review-Printer-Epson-L3110:-Spesifikasi-dan-Keunggulannya',
        'penulis' : 'DIFADIN QUDSY',
        'tanggal' : 'AGUSTUS 30, 2022',
        'isi_konten' : 'KEBUMEN, DIVAPRINTER.COM - Jika anda mencari printer multifungsi terjangkau dengan kinerja terbaik, Epson L3110 bisa dimasukan ke dalam daftar belanja anda. Printer ini dapat memastikan tingkat kinerja yang optimal dengan mengintegrasikan botol tinta isi otomatis yang setara dengan 35 set kartrid tinta , memungkinkan hasil tinta lebih tinggi dan penghematan sumber daya yang substansial...'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', judul_head='Beranda')

@app.route('/home/service')
def service():
    return render_template('service.html', judul_head='Layanan')

@app.route('/home/about')
def about():
    return render_template('contact.html', judul_head='Tentang')

@app.route('/home/article')
def article():
    return render_template('artikel.html', artikel=artikel, judul_head='Artikel')

@app.route('/home/article/<routing>', methods=['GET'])
def get_article(routing):
    if routing == '6-Cara-Merawat-Printer-yang-Benar-Agar-Awet-dan-Tahan-Lama' :
        prev = 'Review Printer Epson L3110: Spesifikasi dan Keunggulannya.'
        next = 'SSD atau Hardisk? Mana yang Lebih Baik.'
        return render_template('artikel-1.html', routing=routing, artikel=artikel, p=prev, n=next, art=1)
    if routing == 'SSD-atau-Hardisk-Mana-yang-Lebih-Baik':
        prev = '6 Cara Merawat Printer yang Benar Agar Awet dan Tahan Lama.'
        next = '5 Tips Memilih Printer, Lebih Baik Sedikit Mahal tetapi Awet dan Hemat Biaya Perawatan.'
        return render_template('artikel-2.html', routing=routing, artikel=artikel, p=prev, n=next, art=2)
    if routing == '5-Tips-Memilih-Printer-Lebih-Baik-Sedikit-Mahal-tetapi-Awet-dan-Hemat-Biaya-Perawatan':
        prev = 'SSD atau Hardisk? Mana yang Lebih Baik.'
        next = 'Review Printer Epson L3110: Spesifikasi dan Keunggulannya.'
        return render_template('artikel-3.html', routing=routing,artikel=artikel, p=prev, n=next)
    if routing == 'Review-Printer-Epson-L3110:-Spesifikasi-dan-Keunggulannya' :
        prev = '5 Tips Memilih Printer, Lebih Baik Sedikit Mahal tetapi Awet dan Hemat Biaya Perawatan.'
        next = '6 Cara Merawat Printer yang Benar Agar Awet dan Tahan Lama.'
        return render_template('artikel-4.html', routing=routing, artikel=artikel, p=prev, n=next)
    else:
        return render_template('artikel.html', artikel=artikel, judul_head='Artikel')

if __name__ == "__main__":
    app.run()