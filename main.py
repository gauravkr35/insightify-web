import streamlit as st
import os

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Insightify – Smart Data Solutions",
    page_icon="📊",
    layout="wide"
)

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
        # -------------------- SUBMIT YOUR DATA SECTION --------------------
    st.markdown("---")
    st.markdown("### 📤 Submit Your Data for Analysis")
    st.markdown("""
        If you have a dataset you'd like us to analyze, please submit it using the link below.
        We'll review your data and get back to you with insights tailored to your needs.
        
        👉 [Click here to submit your data](https://docs.google.com/forms/d/e/1FAIpQLSfk5Ugl9_vK7WxbTQhkHzp5PhJ6k6ZbQ09IXNItjdW9io5f4g/viewform)  
        
    """, unsafe_allow_html=True)


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
    st.markdown("""
        <p>Click the link below to open the contact form:</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScyMNKII3x3Cmy4jgcDrp7Nf3IlWOlnf9tL3wCKmagvdnMlgw/viewform" target="_blank">
            👉 Open Google Contact Form
        </a>
    """, unsafe_allow_html=True)



# -------------------- FOOTER --------------------
st.markdown("---")