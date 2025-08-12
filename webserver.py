#%%
import streamlit as st
from password_generator import generate_password, random_passphrase_generator

st.title(":green[Your secret is safe with us]")
st.header(":violet[Random password generator]", divider = "violet")
random_password = st.toggle(":blue[password]")

if random_password:
    l = st.slider("Lowercase letters", 2, 100, 5)
    u = st.slider("Uppercase letter", 2, 100, 5)
    p = st.slider("Special characters", 3, 100, 5)
    d = st.slider("Digits", 3, 100, 5)
    total = l + u + p + d
    password = generate_password(l,u,p,d, total=total)
    st.write("Password")
    st.code(password, language="plaintext")


if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=password,
        file_name="password.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )

st.header(":violet[Random passphrase generator]", divider = "violet")
random_passphrase = st.toggle(":blue[passphrase]")

if random_passphrase:
    word_count = st.slider("Words count", 8,36,12)
    passphrase = random_passphrase_generator(word_count=word_count)
    st.write("Passphrase")
    st.code(passphrase, language = ("plaintext"))


