import streamlit as st
import pandas as pd
import altair as alt

customer_df = pd.read_csv("dashboard/visualisasi_banyak_customer.csv")
delivery_slowest_df = pd.read_csv("dashboard/visualisasi_pengiriman_terlambat.csv")
delivery_fastest_df = pd.read_csv("dashboard/visualisasi_pengiriman_tercepat.csv")

st.header("**Visualisasi Data Pelanggan**")

st.write("Oleh Muhammad Rizki Putra")

st.subheader("**Visualisasi banyak customer**")

if "customer_city" in customer_df.columns and "customer_count" in customer_df.columns:
    chart_customer = alt.Chart(customer_df).mark_bar(color="blue").encode(
        x=alt.X("customer_count:Q", axis=alt.Axis(title="Jumlah Customer")),
        y=alt.Y("customer_city:N", sort="-x", axis=alt.Axis(title="Kota Pelanggan")),
        tooltip=["customer_city", "customer_count"]
    ).properties(title="Jumlah Customer per Kota")

    st.altair_chart(chart_customer, use_container_width=True)
else:
    st.error("Columns 'customer_city' or 'customer_count' not found in the CSV file.")

st.subheader("**Pengiriman tercepat dan terlambat**")

col1, col2 = st.columns(2)

with col1:
    st.write("Visualisasi pengiriman terlama")

    if "customer_city" in delivery_slowest_df.columns and "delivery_time_day" in delivery_slowest_df.columns:
        chart_slowest = alt.Chart(delivery_slowest_df).mark_bar(color="red").encode(
            x=alt.X("delivery_time_day:Q", axis=alt.Axis(title="Waktu Pengiriman (Hari)")),
            y=alt.Y("customer_city:N", sort="-x", axis=alt.Axis(title="Kota Pelanggan")),
            tooltip=["customer_city", "delivery_time_day"]
        ).properties(title="Pengiriman Terlama")

        st.altair_chart(chart_slowest, use_container_width=True)
    else:
        st.error("Columns 'customer_city' or 'delivery_time_day' not found in the CSV file.")

with col2:
    st.write("Visualisasi pengiriman tercepat")

    if "customer_city" in delivery_fastest_df.columns and "delivery_time_day" in delivery_fastest_df.columns:
        chart_fastest = alt.Chart(delivery_fastest_df).mark_bar(color="green").encode(
            x=alt.X("delivery_time_day:Q", axis=alt.Axis(title="Waktu Pengiriman (Hari)")),
            y=alt.Y("customer_city:N", sort="x", axis=alt.Axis(title="Kota Pelanggan")),
            tooltip=["customer_city", "delivery_time_day"]
        ).properties(title="Pengiriman Tercepat")

        st.altair_chart(chart_fastest, use_container_width=True)
    else:
        st.error("Columns 'customer_city' or 'delivery_time_day' not found in the CSV file.")
