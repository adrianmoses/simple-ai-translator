from dotenv import load_dotenv
from langchain.schema import Document
from langchain_community.document_transformers import GoogleTranslateTransformer
import streamlit as st

load_dotenv()


def main():
    st.title("Simple AI Translator")

    source_choice = st.selectbox("Pick Source Language", ["en", "es", "fr", "it", "pt"])
    target_choice = st.selectbox("Pick Target Language", ["en", "es", "fr", "it", "pt"])

    text = st.text_area("Text to translate")

    documents = [Document(page_content=text)]
    translator = GoogleTranslateTransformer(project_id="day-gen-ai")

    if source_choice == target_choice:
        st.error("Source and Target Languages cannot be the same", icon="🚨")

    translated_documents = translator.transform_documents(
        documents, target_language_code=target_choice
    )

    for doc in translated_documents:
        st.text(doc.metadata)
        st.text(doc.page_content)


if __name__ == '__main__':
    main()
