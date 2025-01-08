import streamlit as st

st.set_page_config(page_title="Juan Alvin Sebastian Sutanto - About Me", layout="wide")

# Header
st.title("Juan Alvin Sebastian Sutanto")
st.write("Final year Software Technology student passionate about software development and problem-solving.")

# Contact Information
st.sidebar.header("Contact Information")
st.sidebar.write("""
📍 Melbourne VIC 3000  
📞 0499803667  
📧 juanalvinss03@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/juan-alvin-sebastian-sutanto-b18532277/)  
🔗 [GitHub](https://github.com/JuanAlvin03)  
""")

# About Me Section
st.header("Summary")
st.write("""
Ambitious and detail-oriented final year Software Technology major student, with a strong foundation in programming 
languages such as PHP, JavaScript, Python, and C#. Experienced in developing software solutions through academic projects, 
including websites, desktop applications, and mobile applications. Eager to apply problem-solving skills and technical knowledge in a real-world environment.
""")

# Skills Section
st.header("Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Skills")
    st.write("""
    - **Programming Languages:** PHP, JavaScript, Python, C#, Java, Kotlin, C++
    - **Frameworks/Tools:** Node.js, Express.js, D3.js, Figma
    - **Databases:** MySQL, PostgreSQL, Supabase, MongoDB
    - **Other Skills:** OOP, SDLC, UML, ERD, DFD
    """)

with col2:
    st.subheader("Soft Skills")
    st.write("""
    - Teamwork
    - Communication
    - Problem-Solving
    - Analytical Thinking
    - Attention to Detail
    - Quick Learner, Hardworking, Reliable
    """)

# Education Section
st.header("Education")
st.write("""
**Swinburne University of Technology, Melbourne**  
*Bachelor of Information Communication and Technology (Software Technology Major)*  
_Aug 2023 - Aug 2025_

**ISTTS, Surabaya**  
*Bachelor of Information Technology (incomplete)*  
_Aug 2021 - June 2023_
""")

# Work Experience Section
st.header("Work Experience")
st.write("""
**Retail Team Member (Volunteer Work), Red Cross Shop**  
_Dec 2023 - Sep 2024_  
- Served customers and managed transactions using the cash register.  
- Lifted boxes, tidied storage, sorted, and tagged items.

**Boba Barista, Boba Buddy**  
_Apr 2024 - Jul 2024_  
- Served and took customers' orders using a Point-of-Sale system.  
- Prepared drinks and desserts with accuracy and care.  

**Kitchen Team Member, Panties Pizza Surabaya**  
_Mar 2020 - Mar 2023_  
- Prepared ingredients and worked with pizza dough.  
- Handled plating, serving, and general kitchen cleaning.  
""")

# Projects Section
st.header("University Projects")
st.write("""
**ICT Project B (Capstone Project)**  
- Developed a website for a client using WordPress.org.  
- Managed the project as team leader, delegating tasks and ensuring timely delivery.  

**ICT Innovation Project**  
- Built a web application with Streamlit and interactive data visualization using Pandas and Plotly.  

**ICT Project A**  
- Designed and developed a website based on requirements using PHP and Supabase.  
""")

# Footer
st.write("---")
st.write("Built with Streamlit by Juan Alvin Sebastian Sutanto.")
