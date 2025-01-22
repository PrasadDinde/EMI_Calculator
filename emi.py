import streamlit as st

# EMI Calculation Function
def calculate_emi(principal, rate, tenure):
    """
    Calculate the EMI for a loan.
    :param principal: Loan amount (P)
    :param rate: Annual interest rate in percentage (R)
    :param tenure: Loan tenure in months (n)
    :return: EMI
    """
    monthly_rate = rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    emi = principal * monthly_rate * ((1 + monthly_rate) ** tenure) / (((1 + monthly_rate) ** tenure) - 1)
    return emi

# Streamlit UI
st.set_page_config(page_title="EMI Calculator", page_icon="💰", layout="centered")

# Header
st.markdown(
    """
    <style>
    .header {
        font-size: 32px;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .result {
        background-color: #f0f9ff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .info-box {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    </style>
    <div class="header">💰 EMI Calculator 💰</div>
    """,
    unsafe_allow_html=True,
)

# Input fields in columns
with st.form("emi_form"):
    st.markdown('<div class="info-box">Enter your loan details below:</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        principal = st.number_input("Loan Amount (₹)", min_value=0.0, value=500000.0, step=10000.0, format="%.2f")
    with col2:
        annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=8.5, step=0.1, format="%.2f")
    with col3:
        tenure_years = st.number_input("Loan Tenure (Years)", min_value=1, value=5, step=1)

    calculate = st.form_submit_button("Calculate EMI")

# EMI Calculation and Results
if calculate:
    tenure_months = tenure_years * 12
    emi = calculate_emi(principal, annual_rate, tenure_months)

    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    st.markdown(
        f"""
        <div class="result">
            <h3>Results:</h3>
            <p><strong>Monthly EMI:</strong> ₹{emi:,.2f}</p>
            <p><strong>Total Principal:</strong> ₹{principal:,.2f}</p>
            <p><strong>Total Interest Payable:</strong> ₹{total_interest:,.2f}</p>
            <p><strong>Total Amount Payable:</strong> ₹{total_payment:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; font-size: 14px; color: gray;">
        Created with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
