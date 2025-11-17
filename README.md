

## 🚀 Codexia Landing Page

Bu proje, bir ürün veya hizmet için geri sayım sayacı ve iletişim (teklif toplama) formu içeren, Python Flask tabanlı, modern bir **Landing Page** uygulamasıdır. Gelen tüm teklifler, sunucu yeniden başlasa bile kaybolmayacak şekilde kalıcı olarak saklanır.

-----

## ✨ Özellikler
  * **Kalıcı Veri Depolama:** Kullanıcılardan gelen mesajlar, **SQLite** veritabanı (Flask-SQLAlchemy aracılığıyla) kullanılarak kalıcı olarak saklanır.
  * **Teklif Formu:** Kullanıcı adını, e-postasını ve hizmet talebi mesajını toplayarak veritabanına kaydeder.
  * **Teknolojiler:** Python, Flask, Flask-SQLAlchemy, Bootstrap 5.

-----

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel olarak çalıştırmak için aşağıdaki adımları izleyin.

### 1\. Ortamın Hazırlanması

Projeyi klonlayın ve dizine gidin:

```bash
git clone https://github.com/CodexiaTechHQ/codexia-landing-page
cd codexia-landing-page
```

### 2\. Bağımlılıkları Yükleme

Sanal ortam oluşturun, etkinleştirin ve gerekli kütüphaneleri yükleyin.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS için
# .venv\Scripts\activate # Windows için

pip install -r requirements.txt
```

> **Not:** `requirements.txt` dosyanızda **`Flask-SQLAlchemy`** kütüphanesinin bulunduğundan emin olun.

### 3\. Gizli Anahtarı Ayarlama

Flask'ın oturum yönetimi için bir gizli anahtar (`SECRET_KEY`) tanımlamanız zorunludur.

```bash
# Terminalde ayarlama (Geçici)
export SECRET_KEY="Sizin_cok_gizli_ve_benzersiz_bir_anahtarınız"
```

### 4\. Uygulamayı Başlatma

Uygulama çalıştırıldığında, veritabanı tabloları (`site.db` dosyası) otomatik olarak oluşturulur.

```bash
python app.py
```

Uygulamanız artık `http://127.0.0.1:5000` adresinde çalışıyor olmalıdır. Gelen form verileri **güvenle** veritabanına kaydedilecektir.

