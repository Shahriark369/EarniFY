import streamlit as st 

# Set the title of the page
st.title("About Us")

# Add social media links
st.subheader("Connect with Us")

# Social Media Links with Images
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://i.postimg.cc/WzPHJj5X/fb.png", width=150)  
    st.write("**Facebook**")
    st.markdown("[Visit our Facebook](https://www.facebook.com/earni.fy.409082)")

with col2:
    st.image("https://i.postimg.cc/P5qFDSMs/project2.jpg", width=150) 
    st.write("**Telegram**")
    st.markdown("[Join us on Telegram](https://t.me/earnify321)")
    
with col3:
    st.image("https://i.postimg.cc/Hn4PwKKH/yt.png", width=150)
    st.write("**Youtube**")
    st.markdown("[Visit our Youtube](https://www.youtube.com/channel/UCw75pR6ToMg2fnIaa1ZjhlA)")


# Add contact information (optional)
st.subheader("Contact Us")
st.write("Feel free to reach out to us for more information or inquiries!")
st.write("Email: earnify123@gmail.com")
