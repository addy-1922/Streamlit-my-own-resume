import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Aditya Naik | Resume", page_icon="💼", layout="centered")

# --- Header ---
st.title("💼 Aditya Sachin Naik")
st.subheader("🎓 Electronics & Computer Engineering Student | Aspiring Data Scientist")
st.write("📍 Pune, India | ✉️ adityasachinnaik@gmail.com")

st.markdown("---")

# --- About ---
st.header("👨‍💻 About Me")
st.write("""
Hi! I'm **Aditya Naik**, a passionate **Electronics and Computer Engineering student** at SPPU (2019 pattern).
I’m learning **Data Science, Machine Learning, and Python Development** and love building real-world projects that solve problems.
""")
st.write("""Looking for Internship opportunities in Data Science and Data Analytics""")

# --- Skills ---
st.header("🧠 Skills")
skills = ["Python", "Machine Learning", "Pandas", "NumPy", "Matplotlib", "SQL", "Streamlit"]
st.write(", ".join(skills))

# --- Projects ---
st.header("🚀 Projects")
st.write("""
- 🧾 **Student Management System** (Flask + MongoDB)
- 📊 **Netflix Recommendation System**
- 📈 **Stock Price Prediction using ML**
- 🧠 **AI Resume Builder (Streamlit)**
""")

# --- Education ---
st.header("🎓 Education")
st.write("**B.E. Electronics and Computer Engineering**, Savitribai Phule Pune University (2019 Pattern)")
st.write("_Expected Graduation: 2027_")

# --- Contact ---
st.markdown("8767103012")
st.header("📞 Contact Me")
st.write("If you'd like to connect or collaborate on projects, feel free to reach out!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        st.success("✅ Thanks for reaching out! I'll get back to you soon.")

st.markdown("---")
st.caption("Made by ❤️ Aditya Sachin Naik")
