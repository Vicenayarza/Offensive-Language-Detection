import streamlit as st
from transformers import pipeline
from langdetect import detect, LangDetectException


SPANISH_MODEL = "pysentimiento/robertuito-hate-speech"
ENGLISH_MODEL = "cardiffnlp/twitter-roberta-base-offensive"
CONFIDENCE_THRESHOLD = 0.60


@st.cache_resource
def load_models():
    spanish_model = pipeline(
        "text-classification",
        model=SPANISH_MODEL,
        top_k=None,
    )

    english_model = pipeline(
        "text-classification",
        model=ENGLISH_MODEL,
        top_k=None,
    )

    return spanish_model, english_model


def detect_language(text: str) -> str:
    try:
        language = detect(text)
    except LangDetectException:
        return "unknown"

    if language == "es":
        return "es"

    if language == "en":
        return "en"

    return "other"


def analyze_text(text: str, model):
    results = model(text)[0]

    scores = {
        result["label"].upper(): result["score"]
        for result in results
    }

    predicted_label = max(scores, key=scores.get)
    confidence = scores[predicted_label]

    if confidence < CONFIDENCE_THRESHOLD:
        return "NEUTRAL", 1 - confidence

    return predicted_label, confidence


def main():
    st.set_page_config(
        page_title="Offensive Language Detection",
        page_icon="🛡️",
    )

    st.title("🛡️ Offensive Language Detection")

    st.write(
        "Herramienta experimental para detectar lenguaje ofensivo "
        "y discurso de odio mediante modelos de NLP."
    )

    text = st.text_area(
        "Introduce un mensaje:",
        placeholder="Escribe aquí el texto que quieres analizar...",
    )

    if st.button("Analizar"):
        if not text.strip():
            st.warning("Introduce un texto antes de realizar el análisis.")
            return

        with st.spinner("Analizando el texto..."):
            spanish_model, english_model = load_models()

            language = detect_language(text)

            if language == "unknown":
                st.error("No se ha podido determinar el idioma.")
                return

            if language == "other":
                st.warning(
                    "Actualmente la aplicación solo admite español e inglés."
                )
                return

            model = (
                spanish_model
                if language == "es"
                else english_model
            )

            label, confidence = analyze_text(text, model)

        st.subheader("Resultado")

        language_name = {
            "es": "Español 🇪🇸",
            "en": "Inglés 🇬🇧",
        }[language]

        st.write(f"**Idioma detectado:** {language_name}")
        st.write(f"**Clasificación:** {label}")
        st.write(f"**Confianza:** {confidence:.2%}")

        offensive_labels = {
            "OFFENSIVE",
            "HATE",
            "HATEFUL",
        }

        if label in offensive_labels:
            st.error(
                "🚨 Se ha detectado contenido potencialmente ofensivo."
            )
        else:
            st.success(
                "✅ No se ha detectado contenido ofensivo."
            )


if __name__ == "__main__":
    main()