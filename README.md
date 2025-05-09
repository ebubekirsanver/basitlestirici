# basitlestirici

TIBBİ METİN BASİTLEŞTİRİCİ 🩺
Bu proje, karmaşık tıbbi terimleri daha basit ve anlaşılır ifadelere dönüştüren bir Streamlit web uygulamasıdır. Kullanıcı tarafından girilen tıbbi metin, öncelikle bir terim sözlüğü kullanılarak basitleştirilir. Eğer terim sözlükte yoksa, Wikipedia API üzerinden açıklaması getirilir. 


KULLANILAN TEKNOLOJİLER
Python 3.x
Streamlit → Web arayüzü
Transformers (Hugging Face) → FLAN-T5 dil modeli
wikipedia-api → Wikipedia üzerinden terim açıklamaları
PyTorch (transformers modeli için backend)

KURULUM
Gerekli paketleri yükleyin:
pip install streamlit transformers wikipedia-api

Uygulamayı çalıştırın:
streamlit run app.py

KODLARIN AÇIKLAMASI
1️-Terim Sözlüğü
Belirli tıbbi terimlerin kısa ve basit açıklamaları terim_sozlugu adlı bir Python sözlüğünde tutulur:

terim_sozlugu = {
    "hipertansiyon": "yüksek tansiyon",
    "hiperkolesterolemi": "kandaki kolesterolün yüksek olması",
    ...
}
➡️ Eğer kullanıcı tarafından girilen terim burada varsa, direkt açıklama döner.

2️-Wikipedia API
Eğer terim sözlükte bulunamazsa, Türkçe Wikipedia'dan özetini almak için wikipediaapi kütüphanesi kullanılır:

wiki_wiki = wikipediaapi.Wikipedia(language='tr', user_agent='TibbiMetinBasitlestirici/1.0 (example@example.com)')
👉 acikla_terim fonksiyonu önce sözlükte arar, yoksa Wikipedia’dan çeker, o da yoksa "[Bilinmeyen Terim]" yazar.

3-Streamlit Arayüzü
Kullanıcıdan metin alınır: st.text_area
"Basitleştir" butonu: st.button
Sonuç görüntüleme: st.subheader, st.write
Basitleştirme işlemi:
Girilen tüm metin bir terim gibi işlenir → sözlükte ya da Wikipedia’da arama yapılır.
Bulunamazsa metin kelimelere bölünür, her kelime ayrı ayrı aranır.

Örneğin:
Girdi: "hipertansiyon hiperkolesterolemi"
Çıktı: "yüksek tansiyon kandaki kolesterolün yüksek olması"
