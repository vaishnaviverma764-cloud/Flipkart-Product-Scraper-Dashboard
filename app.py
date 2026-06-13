import streamlit as st
from scraper import scrape_flipkart

st.set_page_config(
    page_title="Flipkart Product Scraper",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Flipkart Product Scraper Dashboard")

st.markdown(
    "Search products from Flipkart and export the scraped data."
)

col1, col2 = st.columns(2)

with col1:
    product = st.text_input(
        "Enter Product Name",
        "mobiles under 50000"
    )

with col2:
    pages = st.slider(
        "Number of Pages",
        min_value=1,
        max_value=20,
        value=5
    )

if st.button("🚀 Start Scraping"):

    with st.spinner("Scraping Data..."):

        df = scrape_flipkart(product, pages)

    st.success("Scraping Completed Successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Products",
            len(df)
        )

    with col2:
        st.metric(
            "Pages Scraped",
            pages
        )

    st.subheader("Scraped Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="flipkart_products.csv",
        mime="text/csv"
    )