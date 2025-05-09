import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import wikipediaapi

# Terim sözlüğü
terim_sozlugu = {
    "hipertansiyon": "yüksek tansiyon",
    "hiperkolesterolemi": "kandaki kolesterolün yüksek olması",
    "antihipertansif": "tansiyonu düşüren ilaç",
    "statin": "kolesterol düşürücü ilaç",
    "migren": "şiddetli ve tekrarlayan baş ağrısı ",
    "herniye": "fıtık",
    "lezyon": "Doku hasarı",
    "anemi": "kansızlık",
    "osteoporoz": "kemik erimesi",
    "hipotiroidi": "tiroit hormonu eksikliği olgusu",
}

# Wikipedia API başlat
wiki_wiki = wikipediaapi.Wikipedia(language='tr', user_agent='TibbiMetinBasitlestirici/1.0 (example@example.com)')


@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    return tokenizer, model


tokenizer, model = load_model()


def acikla_terim(terim):
    if terim.lower() in terim_sozlugu:
        return terim_sozlugu[terim.lower()]
    else:
        page = wiki_wiki.page(terim)
        if page.exists():
            summary = page.summary.split("\n")[0]
            return f"{terim}: {summary}"
        else:
            return f"[Bilinmeyen Terim: {terim}]"


st.title("TIBBİ METİN BASİTLEŞTİRİCİ 🩺")
metin = st.text_area("Tıbbi metni uygun boşluğa yazınız:")

if st.button("Basitleştir"):
    if metin.strip() == "":
        st.warning("Lütfen bir metin giriniz.")
    else:
        # İlk olarak metni direkt terim olarak ara
        sonuc = acikla_terim(metin)

        # Eğer bulunamazsa kelimelere böl ve tek tek ara
        if sonuc.startswith("[Bilinmeyen Terim"):
            kelimeler = metin.split()
            sonuclar = [acikla_terim(kelime) for kelime in kelimeler]
            sonuc = " ".join(sonuclar)

        st.subheader("Basitleştirilmiş Metniniz:")
        st.write(sonuc)
