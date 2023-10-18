import streamlit as st

from st_pages import Page, show_pages


show_pages(
    [
        Page("main.py", "Home", ""),
        Page("pages/coffee_imports.py", "Coffee Exports", ""),
        Page("pages/coffee_exports.py", "Coffee Exports", ""),
        Page("pages/coffee_production.py", "Coffee Production", ""),
    ]
)

st.set_page_config(
    page_title="Coffe Visualization",
    page_icon="☕",
)


st.header("Coffe Visualization")
st.markdown("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In venenatis porttitor
    laoreet. Fusce tristique nulla neque, a maximus purus lacinia id. Etiam egestas
    posuere libero, dapibus pulvinar nisi volutpat a. Vestibulum sodales elit a
    erat mattis ultrices. Donec consequat, elit eget iaculis pellentesque, est
    ligula facilisis odio, id posuere lacus tortor nec augue. Suspendisse potenti.
    Etiam sit amet volutpat nunc.

    Mauris efficitur sit amet lorem a ultrices. Ut sit amet blandit nulla.
    Phasellus metus elit, imperdiet vel posuere ac, fermentum ac turpis. Donec eget
    enim eu leo malesuada rhoncus in eget ligula. In hac habitasse platea dictumst.
    Nunc quis libero velit. Integer vel elit sit amet urna efficitur viverra.
    Quisque sagittis ante ultrices dui rhoncus, nec gravida quam mollis. In
    consequat nulla pharetra, tristique quam hendrerit, blandit ipsum. Nulla ac
    turpis placerat, vulputate risus a, tempus diam.

    Donec hendrerit consectetur massa id aliquet. Morbi ac dolor finibus erat
    ornare maximus vitae sed est. In fermentum erat eget nibh consectetur lacinia.
    Proin lobortis enim ut magna luctus condimentum. Nam ac enim venenatis,
    imperdiet justo sit amet, fringilla dui. Nam nec pulvinar mauris. Donec in arcu
    at libero pretium venenatis. Ut quis mollis tortor. Nullam sed mauris est.
    Vestibulum vel fringilla odio. Nulla facilisi.
""")

st.subheader("Datasets")
st.markdown("Michał Sikora. (2022). *Coffee dataset* [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/4728784")
