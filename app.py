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
    property_type = st.text_input("Property Type (e.g., multi-family-home, condo)")
    days = st.number_input("Days on Realtor", min_value=0, step=1)
    price = st.number_input("Max Price", min_value=0, step=1000)
    submitted = st.form_submit_button("Search")

if submitted:
    output_path = "executed_notebook.ipynb"

    # Run the notebook with user inputs
    pm.execute_notebook(
        input_path="python_notebook.ipynb",
        output_path=output_path,
        parameters={
            "location": location,
            "property_type": property_type,
            "days": days,
            "price": price
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




