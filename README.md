# EyewearSense: Gözlük Tespit Web Uygulaması

<div align="center">

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-blue.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-v2.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</div>

## 🎯 Proje Hakkında

EyewearSense, derin öğrenme teknolojilerini kullanarak görüntülerdeki gözlük varlığını ve türünü tespit eden modern bir web uygulamasıdır. Evrişimli Sinir Ağı (CNN) modelimiz, yüklenen fotoğraflarda gözlük takılıp takılmadığını ve türünü yüksek doğrulukla analiz edebilmektedir.

## ✨ Özellikler

- 🔍 Hızlı ve doğru gözlük ve gözlük türü tespiti
- 📱 Responsive ve kullanıcı dostu arayüz
- 🖼️ Anlık görüntü yükleme ve işleme
- 📊 Sonuçların görsel sunumu
- 💾 Son analiz edilen görüntülerin galeri görünümü

## 🛠️ Teknolojiler

- **Backend:** Python, Flask
- **Deep Learning:** TensorFlow, OpenCV
- **Frontend:** HTML5, CSS3, JavaScript
- **Veri İşleme:** NumPy, Pandas

## ⚙️ Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekmektedir:

- Python 3.6 veya üzeri
- Flask
- TensorFlow
- NumPy
- OpenCV
- `requirements.txt` dosyasında listelenen diğer gerekli kütüphaneler

## ⚙️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/username/EyewearSense.git
cd EyewearSense
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv eyewear_env
eyewear_env\Scripts\activate     # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## 🚀 Kullanım

1. Uygulamayı başlatın:
```bash
cd glasses-detection-webapp/app
python app.py
```

2. Web tarayıcınızda `http://127.0.0.1:5001` adresine gidin
3. "Choose an image" butonunu kullanarak bir fotoğraf seçin
4. "Detect Glasses" butonuna tıklayarak sonucu görüntüleyin

- Ana sayfadaki form aracılığıyla bir görüntü yükleyin.
- Uygulama görüntüyü işleyecek ve gözlük tespit edilip edilmediğini ve edilirse türünü gösterecektir.
- Sonuçlar, görüntünün işlenmesinden sonra kullanıcı dostu bir arayüzle sunulacaktır.

## 🧠 Model Eğitimi

Kendi veri setinizle modeli eğitmek için:

1. Veri setinizi hazırlayın:
```
dataset/
├── train/
│   ├── glasses/
│   └── no_glasses/
└── val/
    ├── glasses/
    └── no_glasses/
```

2. Modeli eğitin:
```bash
python train.py
python train_sunglasses.py
```
