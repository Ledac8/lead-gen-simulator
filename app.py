import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Paid Lead Gen Waterfall", layout="centered")

st.title("🌊 Paid Lead Gen 'Waterfall' Simulator")
st.markdown("Founders: Enter your assumptions below to see how many leads actually reach the bottom.")

# Sidebar Inputs
st.sidebar.header("Campaign Settings")
budget = st.sidebar.number_input("Monthly Budget ($)", value=1000, step=100)
cpm = st.sidebar.number_input("CPM (Cost per 1k Impressions)", value=20.0, step=1.0)
ctr = st.sidebar.slider("Click-Through Rate (CTR %)", 0.1, 10.0, 2.0) / 100
lp_conv = st.sidebar.slider("Landing Page Conv Rate (%)", 0.1, 30.0, 10.0) / 100
lead_to_sql = st.sidebar.slider("Lead-to-Meeting Rate (%)", 0.1, 50.0, 15.0) / 100

# Calculations
impressions = (budget / cpm) * 1000
clicks = impressions * ctr
leads = clicks * lp_conv
meetings = leads * lead_to_sql

# Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Impressions", f"{impressions:,.0f}")
col2.metric("Clicks", f"{clicks:,.0f}")
col3.metric("Meetings", f"{meetings:,.1f}")

# Funnel Chart
fig = go.Figure(go.Funnel(
    y = ["Impressions", "Clicks", "Leads", "Meetings"],
    x = [impressions, clicks, leads, meetings],
    textinfo = "value+percent initial",
    marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA"]}
))

fig.update_layout(title_text="The Reality of Your Funnel Leak")
st.plotly_chart(fig, use_container_width=True)

st.info(f"💡 **Insight:** To get one meeting, you are currently paying approx. ${budget/max(meetings, 1):,.2f}")
