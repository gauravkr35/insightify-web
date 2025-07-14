# File: app.py (Streamlit + Google Sheets Integration)
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Insightify – Smart Data Solutions",
    page_icon="📊",
    layout="wide"
)

# -------------------- Google Sheet Function --------------------
def send_to_google_sheet(name, email, phone, objective, timestamp):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Insightify Contacts").sheet1
    sheet.append_row([timestamp, name, email, phone, objective])

# -------------------- SIDEBAR NAV --------------------
st.sidebar.title("Insightify")
selection = st.sidebar.radio("Go to", ["Home", "Services", "About", "Contact"])

# -------------------- HOME --------------------
if selection == "Home":
    st.markdown("""
        <div style='background-color: #f0f4f8; padding: 3rem 2rem; border-radius: 1rem;'>
            <h1 style='font-size: 2.5rem;'>📊 Insightify – Smart Data Insights for Your Business</h1>
            <p style='font-size: 1.2rem;'>We help schools, retailers, HR teams, and manufacturers turn their data into actionable insights and smarter decisions using advanced analytics, machine learning, and AI-driven tools.</p>
        </div>
    """, unsafe_allow_html=True)

# -------------------- SERVICES --------------------
elif selection == "Services":
    st.markdown("<h2 id='Services' style='color: #2c3e50;'>🔍 What We Offer</h2>", unsafe_allow_html=True)

    use_cases = {
        "🏫 Schools & Colleges": [
            "Analyze student performance and attendance trends",
            "Identify at-risk students early with predictive analysis",
            "Improve academic planning with insights from past results"
        ],
        "🛍️ Retail & Sales": [
            "Discover top-selling products and sales patterns",
            "Forecast future demand and manage inventory smarter",
            "Evaluate impact of discounts and seasonal trends"
        ],
        "👩‍💼 HR & Workforce": [
            "Monitor headcount, recruitment, and team productivity",
            "Detect attrition risks and improve retention strategies",
            "Plan resource allocation using historical patterns"
        ],
        "🏭 Manufacturing": [
            "Track machine downtime, usage, and output trends",
            "Forecast production levels and optimize operations",
            "Spot inefficiencies and improve material usage"
        ],
        "🧑‍⚕️ Healthcare Data Analysis": [
            "Patient record analysis (hospital visits, prescriptions)",
            "Disease trend tracking",
            "Doctor efficiency and appointment time optimization",
            "Medicine inventory and usage analytics"
        ],
        "🚜 Agricultural Data Monitoring": [
            "Crop yield by region",
            "Weather vs. productivity patterns",
            "Market price trends for produce",
            "Fertilizer/Water usage optimization"
        ],
        "🏗️ Manufacturing/Production Analytics": [
            "Machine downtime prediction",
            "Daily/shift-wise production tracking",
            "Material wastage and optimization",
            "Worker efficiency and batch quality comparison"
        ],
        "💼 Business Dashboard (Startup Metrics)": [
            "Customer acquisition cost, LTV",
            "Ad spend vs. conversion rate",
            "SaaS subscription plan performance",
            "Feedback sentiment analysis from reviews"
        ],
        "📊 Survey or Feedback Analytics": [
            "Analyze satisfaction scores from different regions/products",
            "Text feedback summary using NLP",
            "Common issues/trends spotted in feedback"
        ],
        "💰 Finance/Expense Tracker": [
            "Monthly vs. yearly income/spending breakdown",
            "Category-wise spending (Food, Travel, etc.)",
            "Identify cost-saving areas",
            "Budget prediction"
        ],
        "🏛️ Government & Public Sector Projects": [
            "Schemes usage data (per state/district)",
            "Job employment analysis",
            "Road/building project completion status",
            "Fund utilization trends"
        ]
    }

    for title, points in use_cases.items():
        with st.expander(title):
            for p in points:
                st.markdown(f"- {p}")

    st.markdown("<h3 style='margin-top: 2rem; color: #2c3e50;'>📂 Submit Your Data for Analysis</h3>", unsafe_allow_html=True)
    with st.form("data_upload_form"):
        st.write("Upload your dataset and describe your requirement.")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Mobile Number")
        objective = st.text_area("What do you want from your data?")
        uploaded_files = st.file_uploader("Upload Your Dataset(s) (CSV, XLSX, etc.)", accept_multiple_files=True)
        submitted = st.form_submit_button("Submit")

        if submitted:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            send_to_google_sheet(name, email, phone, objective, timestamp)

            os.makedirs("uploads", exist_ok=True)
            for file in uploaded_files:
                with open(f"uploads/{file.name}", "wb") as f:
                    f.write(file.read())

            st.success("✅ Thank you! Your request has been received.")

# -------------------- ABOUT --------------------
elif selection == "About":
    st.markdown("<h2 id='About' style='color: #2c3e50;'>👨‍💼 About the Analyst</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background-color: #fdfdfd; padding: 1.5rem; border-left: 4px solid #3498db;'>
            <ul>
                <li>🎓 BTech + MTech from IIT Bhubaneswar</li>
                <li>🧠 Experience in data analytics, machine learning & automation</li>
                <li>📈 Delivered real-world insights across education, retail, HR, and industry</li>
                <li>✅ Certified in SQL, Python, Power BI, and ML by IBM, Stanford, and Google</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# -------------------- CONTACT --------------------
elif selection == "Contact":
    st.markdown("<h2 id='Contact' style='color: #2c3e50;'>📬 Let's Work Together</h2>", unsafe_allow_html=True)
    with st.form("contact_form"):
        st.write("Tell me more about your project or data needs. I'll get back to you quickly.")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Mobile Number")
        message = st.text_area("Describe your analysis need")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            send_to_google_sheet(name, email, phone, message, timestamp)
            st.success("✅ Thank you! I'll get back to you shortly.")

# -------------------- FOOTER --------------------
st.markdown("---")
