# Gözlük Tespit Web Uygulaması

Bu proje, yüklenen bir görüntüde kişinin gözlük takıp takmadığını tespit etmek için eğitilmiş bir evrişimli sinir ağı (CNN) modeli kullanan bir web uygulamasıdır. Uygulama Flask kullanılarak geliştirilmiş olup, görüntü yüklemeleri ve sonuçların gösterimi için kullanıcı dostu bir arayüz sunmaktadır.

## Proje Hakkında

Görüntü işleme teknikleri ve derin öğrenme modellerinin pratik bir uygulaması olan bu proje, kişilerin gözlük takıp takmadığını otomatik olarak tespit edebilmektedir. Eğitilmiş CNN modeli, yüklenen görüntüleri analiz ederek yüksek doğrulukla sonuç üretmektedir.

## Proje Yapısı

```
gözlük-tespit-uygulaması
├── app
│   ├── static
│   │   ├── gallery.js         # Galeri işlevselliği için JavaScript dosyası
│   │   └── styles.css         # Web uygulaması için CSS stilleri
│   ├── templates
│   │   └── index.html         # Web uygulaması için HTML yapısı
│   ├── app.py                 # Ana uygulama dosyası
│   └── model
│       └── glasses_cnn_model.h5 # Eğitilmiş model dosyası
├── Train.py                   # Model eğitimi için Python betiği
├── requirements.txt           # Proje bağımlılıkları
└── README.md                  # Proje dokümantasyonu
```

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekmektedir:

- Python 3.6 veya üzeri
- Flask
- TensorFlow
- NumPy
- OpenCV
- `requirements.txt` dosyasında listelenen diğer gerekli kütüphaneler

## Kurulum

1. Depoyu klonlayın:
   ```
   git clone <depo-url>
   cd gözlük-tespit-uygulaması
   ```

2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Uygulamayı Çalıştırma

1. `app` dizinine gidin:
   ```
   cd app
   ```

2. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

3. Web tarayıcınızı açın ve uygulamaya erişmek için `http://127.0.0.1:5001` adresine gidin.

## Kullanım

- Ana sayfadaki form aracılığıyla bir görüntü yükleyin.
- Uygulama görüntüyü işleyecek ve gözlük tespit edilip edilmediğini gösterecektir.
- Sonuçlar, görüntünün işlenmesinden sonra kullanıcı dostu bir arayüzle sunulacaktır.

## Model Eğitimi

Proje, önceden eğitilmiş bir CNN modeli içermektedir. Kendi veri setinizle modeli yeniden eğitmek isterseniz:

1. Veri setinizi hazırlayın (gözlüklü ve gözlüksüz kişilerin görüntüleri).
2. `Train.py` betiğini çalıştırın:
   ```
   python Train.py
   ```
## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.

## İletişim

Sorularınız veya geri bildirimleriniz için lütfen bir Issue açın veya doğrudan proje sahibiyle iletişime geçin.
