import streamlit as st

def display_page():
    st.title(" Welcome to Streamlit Spielwiese.st.title("Startseite [why.py](https://github.com/itbsStefan/streamlit_datasaurus/blob/main/docs/00_why.py)")
    ")")
    c2, c1 = st.columns([4,6])
    image_placeholder = c1.empty()
    c1.markdown("""[why.py](https://github.com/itbsStefan/streamlit_datasaurus/blob/main/docs/00_why.py)""")

    # Markdown for image
    image_markdown_format = "![Alt Text](https://github.com/sebastiandres/streamlit_datasaurus/blob/main/images/{}?raw=true)"

    # Content
    image_placeholder.markdown(image_markdown_format.format("mrdna1.gif"))
    c2.markdown("""    
    Did you know that **Jurassic Park** and **Data Science** are very similar?
    """)

    #markdown_placeholder = c2.empty()
    button_placeholder = c2.empty()

    if button_placeholder.button("Why?"):
        image_placeholder.markdown(image_markdown_format.format("mrdna2.gif"))
        c2.markdown("""
        * Scientists are so preoccupied with whether they can, they don't stop to think if they should.
        * Everything seems to work _until_ your first real customer. 
        * You have to dig for the relevant data and patch it in the most unusual ways. It might look ok but mayhem can (and will) arise later.
        * Your creations will likely bite you back (?).
        * It was all good until lawyers and business man started making decisions.
        """)
        button_placeholder.empty()

        c1, c2, c3 = st.columns([1,2,1])

        c2.markdown("Join the quest to learn about the ellusive Datasaurus.")

        c2.markdown("Use the sidebar to navigate through this interactive Streamlit app")

display_page()