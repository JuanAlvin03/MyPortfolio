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
    - **Frameworks/Tools:** Node.js, Express.js, D3.js, Figma, Vue.js
    - **Databases:** MySQL, PostgreSQL, Supabase, MongoDB
    - **Other Skills:** OOP, SDLC, UML, ERD, DFD, AWS
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

# Work Experience Section
st.header("Experience")
st.write("""
**Data and Management Analytics Intern, Prompcorp**  
_February 2025 - May 2025_  
- Analysed business processes and developed custom ERPNext modules to streamline operations
- Created client-side scripts using JavaScript to extend ERP system functionality
- Built integrated data dashboards with Frappe Insights for real-time business intelligence
- Collaborated with team members to design solutions and authored technical and user documentation
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
# st.header("Work Experience")
# st.write("""
# **Retail Team Member (Volunteer Work), Red Cross Shop**
# _Dec 2023 - Sep 2024_
# - Served customers and managed transactions using the cash register.
# - Lifted boxes, tidied storage, sorted, and tagged items.
#
# **Boba Barista, Boba Buddy**
# _Apr 2024 - Jul 2024_
# - Served and took customers' orders using a Point-of-Sale system.
# - Prepared drinks and desserts with accuracy and care.
#
# **Kitchen Team Member, Panties Pizza Surabaya**
# _Mar 2020 - Mar 2023_
# - Prepared ingredients and worked with pizza dough.
# - Handled plating, serving, and general kitchen cleaning.
# """)

# Projects Section
st.header("University Projects")
st.write("""
**Business Digitalisation Industry Capstone Project**  
_WordPress_
- Led a team of four in delivering a client-facing website for a small cleaning business
- Managed project planning, task delegation, and team communication to ensure timely delivery
- Conducted client meetings and needs assessments to define project scope and goals
- Designed and developed a responsive website using WordPress.org, including SEO and hosting setup
- Delivered comprehensive project documentation, presentations, and client handover materials

**ICT Innovation Project**  
_Streamlit, Plotly, Pandas, Data Analysis_
- Developed a web application using Streamlit for interactive and responsive data visualisation
- Processed and analyzed cybersecurity data from the MITRE ATT&CK framework using Python and Pandas  
- Created dynamic visualisations with Plotly to present insights on attack techniques and patterns
- Collaborated in a team environment to design and deliver a functional software prototype

**ICT Project A (scenario-based aged care management system)**  
_PHP, Supabase, HTML, CSS, Agile_
- Collaborated in a team of four to develop an aged care management web application based on given requirements
- Designed system architecture, including Entity-Relationship Diagrams and detailed project planning documents
- Built the application using PHP, Supabase, HTML, and CSS, following an agile, sprint-based development process
- Defined project scope and gathered functional requirements to guide development and ensure alignment with user needs

**Recipe Sharing Web Application**  
_Vue.js, Vite, npm, Bootstrap, PHP, MySQL_
- Developed a responsive recipe-sharing website using Vue.js with Vite and npm for frontend interface design project
- Implemented Vue concepts such as lazy-loaded routes, navigation guards, and component based architecture
- Styled the interface with Bootstrap for consistent and mobile-friendly design
- Built backend API endpoints using PHP and MySQL to support dynamic content and user interactions
""")

# Footer
st.write("---")
st.write("Built with Streamlit by Juan Alvin Sebastian Sutanto.")
