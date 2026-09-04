import streamlit as st

st.set_page_config(
    page_title="AI Credit Risk Assessment Agent",
    page_icon="💳"
)

st.title("💳 AI Credit Risk Assessment Agent")
st.subheader("Loan Decision Support System")

st.write(
    "This application provides a preliminary assessment of "
    "credit risk based on an applicant's financial information."
)

st.divider()

st.header("Applicant Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

monthly_income = st.number_input(
    "Monthly Income (USD)",
    min_value=0.0,
    value=1000.0
)

loan_amount = st.number_input(
    "Loan Amount (USD)",
    min_value=0.0,
    value=5000.0
)

existing_debt = st.number_input(
    "Existing Debt (USD)",
    min_value=0.0,
    value=1000.0
)

employment = st.selectbox(
    "Employment Status",
    [
        "Permanent",
        "Self-employed",
        "Temporary",
        "Unemployed"
    ]
)

credit_history = st.selectbox(
    "Credit History",
    [
        "Good",
        "Average",
        "Poor"
    ]
)

loan_term = st.number_input(
    "Loan Term (months)",
    min_value=1,
    max_value=120,
    value=24
)

st.divider()

if st.button("🔍 Assess Credit Risk"):

    risk_score = 0

    # Assess loan relative to annual income
    if monthly_income > 0:

        annual_income = monthly_income * 12
        loan_to_income = loan_amount / annual_income

        if loan_to_income > 1:
            risk_score += 30

        elif loan_to_income > 0.5:
            risk_score += 15

        else:
            risk_score += 5

    # Assess existing debt
    if monthly_income > 0:

        annual_income = monthly_income * 12
        debt_ratio = existing_debt / annual_income

        if debt_ratio > 0.5:
            risk_score += 25

        elif debt_ratio > 0.25:
            risk_score += 15

        else:
            risk_score += 5

    # Assess employment
    if employment == "Unemployed":
        risk_score += 25

    elif employment == "Temporary":
        risk_score += 15

    elif employment == "Self-employed":
        risk_score += 10

    # Assess credit history
    if credit_history == "Poor":
        risk_score += 20

    elif credit_history == "Average":
        risk_score += 10

    # Assess age
    if age < 21:
        risk_score += 10

    elif age > 65:
        risk_score += 5

    # Keep score between 0 and 100
    risk_score = min(risk_score, 100)

    # Determine risk category
    if risk_score <= 30:

        risk_category = "LOW"
        recommendation = (
            "Low-risk applicant. Proceed to human review."
        )

    elif risk_score <= 60:

        risk_category = "MEDIUM"
        recommendation = (
            "Medium-risk applicant. Further assessment is recommended."
        )

    else:

        risk_category = "HIGH"
        recommendation = (
            "High-risk applicant. Careful human review is required."
        )

    st.divider()

    st.header("Credit Risk Assessment")

    st.metric(
        "Risk Score",
        f"{risk_score}/100"
    )

    if risk_category == "LOW":

        st.success(
            f"🟢 {risk_category} CREDIT RISK"
        )

    elif risk_category == "MEDIUM":

        st.warning(
            f"🟠 {risk_category} CREDIT RISK"
        )

    else:

        st.error(
            f"🔴 {risk_category} CREDIT RISK"
        )

    st.subheader("Recommendation")

    st.write(recommendation)

    st.subheader("Assessment Information")

    st.write(f"**Employment:** {employment}")
    st.write(f"**Credit History:** {credit_history}")
    st.write(f"**Monthly Income:** ${monthly_income:,.2f}")
    st.write(f"**Loan Amount:** ${loan_amount:,.2f}")
    st.write(f"**Existing Debt:** ${existing_debt:,.2f}")
    st.write(f"**Loan Term:** {loan_term} months")

    st.info(
        "This is a decision-support prototype and should not be "
        "used as the sole basis for approving or rejecting a loan."
    )
