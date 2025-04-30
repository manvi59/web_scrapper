import streamlit as st
import papermill as pm
import nbformat

import requests
from bs4 import BeautifulSoup
import json
import time
import re


import pandas as pd
from io import BytesIO


# Function to extract the last output from a notebook
def get_last_output_cell(notebook_path):
    nb = nbformat.read(notebook_path, as_version=4)
    for cell in reversed(nb.cells):
        if cell.cell_type == 'code':
            outputs = cell.get("outputs", [])
            for output in outputs:
                if output.output_type == "stream":
                    return output.text.strip()
                elif output.output_type == "execute_result":
                    return output["data"].get("text/plain", "").strip()
    return "No output found"

st.title("🏡 Real Estate Scraper - Realtor.com")

with st.form("user_form"):
    location = st.text_input("Enter Location (e.g., Indiana or Los-Angeles_CA)")
    # property_type = st.text_input("Property Type (e.g., multi-family-home, condo)")
    # days = st.number_input("Days on Realtor", min_value=0, step=1)
    # price = st.number_input("Max Price", min_value=0, step=1000)
    property_type_map = {
    "Single Family Home": "/type-single-family-home",
    "Multi Family Home": "/type-multi-family-home",
    "Any": "",
    "House": "/type-single-family-home",
    "Condo": "/type-condo",
    "Townhome": "/type-townhome",
    "Land": "/type-land",
    "Mobile": "/type-mfd-mobile-home",
    "Farm": "/type-farms-ranches"
    }
    property_type = st.selectbox("Property Type", list(property_type_map.keys()))
    property_type_url = property_type_map[property_type]

    # --- Custom Price Dropdowns ---
    min_price_display_map = {
        "No Min": None,
        "$80k": "80000",
        "$90k": "90000",
        "$120k": "120000",
        "$250k": "250000"
    }

    max_price_display_map = {
        "No Max": None,
        "$90k": "90000",
        "$1M": "1000000",
        "$1.2M": "1200000",
        "$1.25M": "1250000"
    }

    min_display = st.selectbox("Minimum Price", list(min_price_display_map.keys()))
    max_display = st.selectbox("Maximum Price", list(max_price_display_map.keys()))

    min_price = min_price_display_map[min_display]
    max_price = max_price_display_map[max_display]

    if min_price and not max_price:
        price_filter = f"/price-{min_price}-na"
    elif not min_price and max_price:
        price_filter = f"/price-na-{max_price}"
    elif min_price and max_price:
        price_filter = f"/price-{min_price}-{max_price}"
    else:
        price_filter = ""

    # --- Days on Market Dropdown ---
    days_map = {
        "Any": "",
        "Today": "/dom-1",
        "30 Days": "/dom-30",
        "90 Days":"/dom-90",
        "60 Days": "/dom-60",
        "180 Days": "/dom-180"
    }
    days_on_market = st.selectbox("Days on Market", list(days_map.keys()))
    days_url = days_map[days_on_market]

    # --- Sort By Dropdown ---
    sort_by_map = {
        "Relevant Listing": "",
        "New Listings": "/sby-6",
        "Lowest Price": "/sby-1",
        "Highest Price": "/sby-2",
        "Year Built": "/sby-17",
        "Open House Date": "/sby-5",
        "Recent Reduction": "/sby-7",
        "Largest Sqft": "/sby-14",
        "Lot Size": "/sby-9",
        "Photo Count": "/sby-16"
    }
    sort_option = st.selectbox("Sort By", list(sort_by_map.keys()))
    sort_url = sort_by_map[sort_option]

    # --- Price Reduced Checkbox ---
    price_reduced = st.checkbox("Show Only Price Reduced")
    price_reduced_url = "/show-price-reduced" if price_reduced else ""

    # --- Construct Final URL ---
    final_url = f"{property_type_url}{price_reduced_url}{days_url}{price_filter}{sort_url}"
    # url = f"https://www.realtor.com/realestateandhomes-search/{location}"
    st.markdown(f"**Generated URL Path:** `https://www.realtor.com/realestateandhomes-search/{location}{final_url}`")

    submitted = st.form_submit_button("Search")

if submitted:
    output_path = "executed_notebook.ipynb"

    # Run the notebook with user inputs
    pm.execute_notebook(
        input_path="python_notebook.ipynb",
        output_path=output_path,
        parameters={
            "location": location,
            "final_url":final_url
            # "property_type": property_type,
            # "days": days,
            # "price": price
        }
    )

    # Extract and show result
    result = get_last_output_cell(output_path)
    st.success("✅ Notebook executed successfully!")
    # st.write("### 🔍 Result:")
    # st.code(result)

    # try:
    #     parsed_result = json.loads(result)
    #     if isinstance(parsed_result, list):
    #         for item in parsed_result:
    #             st.json(item)
    #     elif isinstance(parsed_result, dict):
    #         st.json(parsed_result)
    #     else:
    #         st.code(result)
    # except:
    #     st.code(result)

    
    # ---------------------------tabluar format ----------------

    try:
        parsed_result = json.loads(result)
        
        if isinstance(parsed_result, (list, dict)):
            # Convert to DataFrame
            if isinstance(parsed_result, dict):
                parsed_result = [parsed_result]
            df = pd.DataFrame(parsed_result)

            # Display in tabular format
            st.write("### 🗃️ Data Table")
            st.dataframe(df)

            # Create a BytesIO buffer to hold the Excel file
            output = BytesIO()
            # with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            #     df.to_excel(writer, index=False, sheet_name='RealEstateData')
            #     writer.save()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='RealEstateData')

            output.seek(0)

            # Download button
            st.download_button(
                label="📥 Download Excel",
                data=output,
                file_name="real_estate_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.code(result)
    except Exception as e:
        st.error("⚠️ Could not parse or process the result.")
        st.code(str(e))




