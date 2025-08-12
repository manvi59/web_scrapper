# import streamlit as st
# import papermill as pm
# import nbformat

# import requests
# from bs4 import BeautifulSoup
# import json
# import time
# import re


# import pandas as pd
# from io import BytesIO


# # Function to extract the last output from a notebook
# def get_last_output_cell(notebook_path):
#     nb = nbformat.read(notebook_path, as_version=4)
#     for cell in reversed(nb.cells):
#         if cell.cell_type == 'code':
#             outputs = cell.get("outputs", [])
#             for output in outputs:
#                 if output.output_type == "stream":
#                     return output.text.strip()
#                 elif output.output_type == "execute_result":
#                     return output["data"].get("text/plain", "").strip()
#     return "No output found"

# st.title("🏡 Real Estate Scraper - Realtor.com")

# with st.form("user_form"):
#     # location = st.text_input("Enter Location (e.g., Indiana or Los-Angeles_CA)")
#     cities = [
#     { "label": "New York, NY", "value": "new-york_ny" },
#     { "label": "Los Angeles, CA", "value": "los-angeles_ca" },
#     { "label": "Chicago, IL", "value": "chicago_il" },
#     { "label": "Houston, TX", "value": "houston_tx" },
#     { "label": "Phoenix, AZ", "value": "phoenix_az" },
#     { "label": "Philadelphia, PA", "value": "philadelphia_pa" },
#     { "label": "San Antonio, TX", "value": "san-antonio_tx" },
#     { "label": "San Diego, CA", "value": "san-diego_ca" },
#     { "label": "Dallas, TX", "value": "dallas_tx" },
#     { "label": "San Jose, CA", "value": "san-jose_ca" },
#     { "label": "Austin, TX", "value": "austin_tx" },
#     { "label": "Jacksonville, FL", "value": "jacksonville_fl" },
#     { "label": "Fort Worth, TX", "value": "fort-worth_tx" },
#     { "label": "Columbus, OH", "value": "columbus_oh" },
#     { "label": "Indianapolis, IN", "value": "indianapolis_in" },
#     { "label": "Charlotte, NC", "value": "charlotte_nc" },
#     { "label": "San Francisco, CA", "value": "san-francisco_ca" },
#     { "label": "Seattle, WA", "value": "seattle_wa" },
#     { "label": "Denver, CO", "value": "denver_co" },
#     { "label": "Oklahoma City, OK", "value": "oklahoma-city_ok" },
#     { "label": "Nashville, TN", "value": "nashville_tn" },
#     { "label": "El Paso, TX", "value": "el-paso_tx" },
#     { "label": "Washington, DC", "value": "washington_dc" },
#     { "label": "Las Vegas, NV", "value": "las-vegas_nv" },
#     { "label": "Boston, MA", "value": "boston_ma" },
#     { "label": "Portland, OR", "value": "portland_or" },
#     { "label": "Detroit, MI", "value": "detroit_mi" },
#     { "label": "Memphis, TN", "value": "memphis_tn" },
#     { "label": "Louisville, KY", "value": "louisville_ky" },
#     { "label": "Baltimore, MD", "value": "baltimore_md" },
#     { "label": "Milwaukee, WI", "value": "milwaukee_wi" },
#     { "label": "Albuquerque, NM", "value": "albuquerque_nm" },
#     { "label": "Tucson, AZ", "value": "tucson_az" },
#     { "label": "Fresno, CA", "value": "fresno_ca" },
#     { "label": "Mesa, AZ", "value": "mesa_az" },
#     { "label": "Sacramento, CA", "value": "sacramento_ca" },
#     { "label": "Atlanta, GA", "value": "atlanta_ga" },
#     { "label": "Kansas City, MO", "value": "kansas-city_mo" },
#     { "label": "Colorado Springs, CO", "value": "colorado-springs_co" },
#     { "label": "Raleigh, NC", "value": "raleigh_nc" },
#     { "label": "Omaha, NE", "value": "omaha_ne" },
#     { "label": "Miami, FL", "value": "miami_fl" },
#     { "label": "Long Beach, CA", "value": "long-beach_ca" },
#     { "label": "Virginia Beach, VA", "value": "virginia-beach_va" },
#     { "label": "Oakland, CA", "value": "oakland_ca" },
#     { "label": "Minneapolis, MN", "value": "minneapolis_mn" },
#     { "label": "Tulsa, OK", "value": "tulsa_ok" },
#     { "label": "Arlington, TX", "value": "arlington_tx" },
#     { "label": "New Orleans, LA", "value": "new-orleans_la" },
#     { "label": "Wichita, KS", "value": "wichita_ks" },
#     { "label": "Cleveland, OH", "value": "cleveland_oh" },
#     { "label": "Tampa, FL", "value": "tampa_fl" },
#     { "label": "Bakersfield, CA", "value": "bakersfield_ca" },
#     { "label": "Aurora, CO", "value": "aurora_co" },
#     { "label": "Honolulu, HI", "value": "honolulu_hi" },
#     { "label": "Anaheim, CA", "value": "anaheim_ca" },
#     { "label": "Santa Ana, CA", "value": "santa-ana_ca" },
#     { "label": "Riverside, CA", "value": "riverside_ca" },
#     { "label": "Corpus Christi, TX", "value": "corpus-christi_tx" },
#     { "label": "Lexington, KY", "value": "lexington_ky" },
#     { "label": "Henderson, NV", "value": "henderson_nv" },
#     { "label": "Stockton, CA", "value": "stockton_ca" },
#     { "label": "Saint Paul, MN", "value": "saint-paul_mn" },
#     { "label": "Cincinnati, OH", "value": "cincinnati_oh" },
#     { "label": "St. Louis, MO", "value": "st-louis_mo" },
#     { "label": "Pittsburgh, PA", "value": "pittsburgh_pa" },
#     { "label": "Greensboro, NC", "value": "greensboro_nc" },
#     { "label": "Lincoln, NE", "value": "lincoln_ne" },
#     { "label": "Anchorage, AK", "value": "anchorage_ak" },
#     { "label": "Plano, TX", "value": "plano_tx" },
#     { "label": "Orlando, FL", "value": "orlando_fl" },
#     { "label": "Irvine, CA", "value": "irvine_ca" },
#     { "label": "Newark, NJ", "value": "newark_nj" },
#     { "label": "Durham, NC", "value": "durham_nc" },
#     { "label": "Chula Vista, CA", "value": "chula-vista_ca" },
#     { "label": "Toledo, OH", "value": "toledo_oh" },
#     { "label": "Fort Wayne, IN", "value": "fort-wayne_in" },
#     { "label": "St. Petersburg, FL", "value": "st-petersburg_fl" },
#     { "label": "Laredo, TX", "value": "laredo_tx" },
#     { "label": "Jersey City, NJ", "value": "jersey-city_nj" },
#     { "label": "Chandler, AZ", "value": "chandler_az" },
#     { "label": "Madison, WI", "value": "madison_wi" },
#     { "label": "Lubbock, TX", "value": "lubbock_tx" },
#     { "label": "Scottsdale, AZ", "value": "scottsdale_az" },
#     { "label": "Reno, NV", "value": "reno_nv" },
#     { "label": "Buffalo, NY", "value": "buffalo_ny" },
#     { "label": "Gilbert, AZ", "value": "gilbert_az" },
#     { "label": "Glendale, AZ", "value": "glendale_az" },
#     { "label": "North Las Vegas, NV", "value": "north-las-vegas_nv" },
#     { "label": "Winston-Salem, NC", "value": "winston-salem_nc" },
#     { "label": "Chesapeake, VA", "value": "chesapeake_va" },
#     { "label": "Norfolk, VA", "value": "norfolk_va" },
#     { "label": "Fremont, CA", "value": "fremont_ca" },
#     { "label": "Garland, TX", "value": "garland_tx" },
#     { "label": "Irving, TX", "value": "irving_tx" },
#     { "label": "Hialeah, FL", "value": "hialeah_fl" },
#     { "label": "Richmond, VA", "value": "richmond_va" },
#     { "label": "Boise, ID", "value": "boise_id" },
#     { "label": "Spokane, WA", "value": "spokane_wa" }
#     ]
 
#     # Convert to a dictionary for easy label-value handling
#     label_to_value = { city['label']: city['value'] for city in cities }

#     # Streamlit selectbox
#     selected_label = st.selectbox("Select a city", list(label_to_value.keys()))

#     # property_type = st.text_input("Property Type (e.g., multi-family-home, condo)")
#     # days = st.number_input("Days on Realtor", min_value=0, step=1)
#     # price = st.number_input("Max Price", min_value=0, step=1000)
#     property_type_map = {
#     "Single Family Home": "/type-single-family-home",
#     "Multi Family Home": "/type-multi-family-home",
#     "Any": "",
#     "House": "/type-single-family-home",
#     "Condo": "/type-condo",
#     "Townhome": "/type-townhome",
#     "Land": "/type-land",
#     "Mobile": "/type-mfd-mobile-home",
#     "Farm": "/type-farms-ranches"
#     }
#     property_type = st.selectbox("Property Type", list(property_type_map.keys()))
#     property_type_url = property_type_map[property_type]

#     # --- Custom Price Dropdowns ---
#     # min_price_display_map = {
#     #     "No Min": None,
#     #     "$80k": "80000",
#     #     "$90k": "90000",
#     #     "$120k": "120000",
#     #     "$250k": "250000"
#     # }

#     min_price_display_map = {
#     "No Min": None,
#     "$500k": "500000",
#     "$600k": "600000",
#     "$700k": "700000",
#     "$800k": "800000",
     
     
# }

#     # max_price_display_map = {
#     #     "No Max": None,
#     #     "$90k": "90000",
#     #     "$1M": "1000000",
#     #     "$1.2M": "1200000",
#     #     "$1.25M": "1250000"
#     # }

#     max_price_display_map = {
#         "No Max": None,
#         "$900k": "900000",
#         "$1M": "1000000",
#         "$1.2M": "1200000",
#         "$1.25M": "1250000"
#     }

#     min_display = st.selectbox("Minimum Price", list(min_price_display_map.keys()))
#     max_display = st.selectbox("Maximum Price", list(max_price_display_map.keys()))

#     min_price = min_price_display_map[min_display]
#     max_price = max_price_display_map[max_display]

#     if min_price and not max_price:
#         price_filter = f"/price-{min_price}-na"
#     elif not min_price and max_price:
#         price_filter = f"/price-na-{max_price}"
#     elif min_price and max_price:
#         price_filter = f"/price-{min_price}-{max_price}"
#     else:
#         price_filter = ""

#     # --- Days on Market Dropdown ---
#     days_map = {
#         "Any": "",
#         "Today": "/dom-1",
#         "30 Days": "/dom-30",
#         "90 Days":"/dom-90",
#         "60 Days": "/dom-60",
#         "180 Days": "/dom-180"
#     }
#     days_on_market = st.selectbox("Days on Market", list(days_map.keys()))
#     days_url = days_map[days_on_market]

#     # --- Sort By Dropdown ---
#     sort_by_map = {
#         "Relevant Listing": "",
#         "New Listings": "/sby-6",
#         "Lowest Price": "/sby-1",
#         "Highest Price": "/sby-2",
#         "Year Built": "/sby-17",
#         "Open House Date": "/sby-5",
#         "Recent Reduction": "/sby-7",
#         "Largest Sqft": "/sby-14",
#         "Lot Size": "/sby-9",
#         "Photo Count": "/sby-16"
#     }
#     sort_option = st.selectbox("Sort By", list(sort_by_map.keys()))
#     sort_url = sort_by_map[sort_option]

#     # --- Price Reduced Checkbox ---
#     price_reduced = st.checkbox("Show Only Price Reduced")
#     price_reduced_url = "/show-price-reduced" if price_reduced else ""

#     # --- Construct Final URL ---
#     final_url = f"{property_type_url}{price_reduced_url}{days_url}{price_filter}{sort_url}"
#     # url = f"https://www.realtor.com/realestateandhomes-search/{location}"
#     st.markdown(f"**Generated URL Path:** `https://www.realtor.com/realestateandhomes-search/{label_to_value[selected_label]}{final_url}`")

#     submitted = st.form_submit_button("Search")

# if submitted:
#     output_path = "executed_notebook.ipynb"

#     # Run the notebook with user inputs
#     pm.execute_notebook(
#         input_path="python_notebook.ipynb",
#         output_path=output_path,
#         parameters={
#             # "location": location,
#             "location": label_to_value[selected_label],
#             "final_url":final_url
#             # "property_type": property_type,
#             # "days": days,
#             # "price": price
#         }
#     )

#     # Extract and show result
#     result = get_last_output_cell(output_path)
#     st.success("✅ Notebook executed successfully!")
#     # st.write("### 🔍 Result:")
#     # st.code(result)

#     # try:
#     #     parsed_result = json.loads(result)
#     #     if isinstance(parsed_result, list):
#     #         for item in parsed_result:
#     #             st.json(item)
#     #     elif isinstance(parsed_result, dict):
#     #         st.json(parsed_result)
#     #     else:
#     #         st.code(result)
#     # except:
#     #     st.code(result)

    
#     # ---------------------------tabluar format ----------------

#     try:
#         parsed_result = json.loads(result)
        
#         if isinstance(parsed_result, (list, dict)):
#             # Convert to DataFrame
#             if isinstance(parsed_result, dict):
#                 parsed_result = [parsed_result]
#             df = pd.DataFrame(parsed_result)

#             # Display in tabular format
#             st.write("### 🗃️ Data Table")
#             st.dataframe(df)

#             # Create a BytesIO buffer to hold the Excel file
#             output = BytesIO()
#             # with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#             #     df.to_excel(writer, index=False, sheet_name='RealEstateData')
#             #     writer.save()
#             with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#                 df.to_excel(writer, index=False, sheet_name='RealEstateData')

#             output.seek(0)

#             # Download button
#             st.download_button(
#                 label="📥 Download Excel",
#                 data=output,
#                 file_name="real_estate_data.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )
#         else:
#             st.code(result)
#     except Exception as e:
#         st.error("⚠️ Could not parse or process the result.")
#         st.code(str(e))




# ---------------------------------------------login authentication----------------------------------------------

import streamlit as st
import requests
from streamlit_browser_storage import LocalStorage
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript
import papermill as pm
import nbformat
import pandas as pd
from io import BytesIO
import json
# from streamlit_js_eval import streamlit_js_eval 

# from streamlit_javascript import st_javascript

API_BASE_URL = "https://expresjs-authentication.onrender.com"
storage = LocalStorage(key="auth_token")

st.set_page_config(page_title="Auth App", layout="centered")
st.title("🛂 Authentication ")

# -----------------------------------------------
import json
from streamlit_javascript import st_javascript
import streamlit as st
from streamlit.components.v1 import html
 

def get_token_from_local_storage():
    return st_javascript("window.localStorage.getItem('token') || null")

# def set_token_to_local_storage(token):
     
#     st_javascript("window.localStorage.setItem('token','kkkkk')" )
 

def set_token_to_local_storage(token,username):
    print("inside the function" , token , username)
    token_js = json.dumps(token)  # safely encode token as JS string
    username_js = json.dumps(username)  # safely encode token as JS string
    html_code = f"""
    <script>
    (function() {{
        window.localStorage.setItem('token', {token_js});
        window.localStorage.setItem('username', {username_js});
        console.log('Token set in localStorage:', {token_js});
    }})();
    </script>
    """
    html(html_code)

  

def remove_token_from_local_storage():
    st_javascript("window.localStorage.removeItem('token');")
    st_javascript("window.localStorage.removeItem('username');")
    st_javascript("window.location.href = window.location.href;")


# print("get from localStorage:", get_token_from_local_storage())
# print("Token from localStorage:", set_token_to_local_storage("shiiiiiiiiiiiiiiiiiiiiii"))
# remove_token_from_local_storage()




# ----------------------------------------------verification-------

# token = storage.get("token")
token =get_token_from_local_storage()
print("tokennnnn",token)
if token:
    # st.session_state.page = "profile"
    # st.session_state.logged_in = True
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/verify", headers=headers)
    # print("response is ",response.json())
    if response.status_code == 200:
        st.session_state.logged_in = True
        st.session_state.user_data = response.json()
        st.session_state.page = "profile"

if "token" not in st.session_state:
    st.session_state.token = storage.get("token")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_data" not in st.session_state:
    st.session_state.user_data = None
if "checked_token" not in st.session_state:
    st.session_state.checked_token = False
if "page" not in st.session_state:
    st.session_state.page = "profile" if st.session_state.token else "login"

def go_to(page_name):
    st.session_state.page = page_name

def check_token():
    # token = st.session_state.get("token")
    # token = get_token_from_local_storage()
    # print("jjjjjjjjjj" ,token)
    if not token:
        return
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_BASE_URL}/verify", headers=headers)
        # print("response is ",response.json())
        if response.status_code == 200:
            st.session_state.logged_in = True
            st.session_state.user_data = response.json()
            st.session_state.page = "profile"
    except requests.exceptions.RequestException:
        pass
    st.session_state.checked_token = True

if not st.session_state.checked_token:
    check_token()


 
# ---------------- Profile Page (Scraper) ---------------- #
if st.session_state.logged_in and st.session_state.page == "profile":
    name=storage.get("username")
    if name:

        st.success("Welcome , " + name + "!")   
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_data = None
        st.session_state.token = None
        # storage = LocalStorage(key="auth_token")

        # storage.delete("token")  # Properly delete the token key from browser storage
        # # storage.set("token","new")
        # vv=storage.get("token")
        # storage.delete("username")
        # print(vv)
        # components.html(
        #     """
        #     <script>
        #         localStorage.removeItem("token");
        #         localStorage.removeItem("auth_token");
        #         localStorage.removeItem("username");
                 
        #         window.location.reload();
        #     </script>
        #     """,
        #     height=0,
        #     scrolling=False,
        # )
        remove_token_from_local_storage()

        st.session_state.page = "login"
         
        # st.rerun()
         


    

    # ---------------- Real Estate Scraper Starts ---------------- #
    st.header("🏡 Real Estate Scraper - Realtor.com")
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

    # st.title("🏡 Real Estate Scraper - Realtor.com")

    with st.form("user_form"):
        # location = st.text_input("Enter Location (e.g., Indiana or Los-Angeles_CA)")
        cities = [
        { "label": "New York, NY", "value": "new-york_ny" },
        { "label": "Los Angeles, CA", "value": "los-angeles_ca" },
        { "label": "Chicago, IL", "value": "chicago_il" },
        { "label": "Houston, TX", "value": "houston_tx" },
        { "label": "Phoenix, AZ", "value": "phoenix_az" },
        { "label": "Philadelphia, PA", "value": "philadelphia_pa" },
        { "label": "San Antonio, TX", "value": "san-antonio_tx" },
        { "label": "San Diego, CA", "value": "san-diego_ca" },
        { "label": "Dallas, TX", "value": "dallas_tx" },
        { "label": "San Jose, CA", "value": "san-jose_ca" },
        { "label": "Austin, TX", "value": "austin_tx" },
        { "label": "Jacksonville, FL", "value": "jacksonville_fl" },
        { "label": "Fort Worth, TX", "value": "fort-worth_tx" },
        { "label": "Columbus, OH", "value": "columbus_oh" },
        { "label": "Indianapolis, IN", "value": "indianapolis_in" },
        { "label": "Charlotte, NC", "value": "charlotte_nc" },
        { "label": "San Francisco, CA", "value": "san-francisco_ca" },
        { "label": "Seattle, WA", "value": "seattle_wa" },
        { "label": "Denver, CO", "value": "denver_co" },
        { "label": "Oklahoma City, OK", "value": "oklahoma-city_ok" },
        { "label": "Nashville, TN", "value": "nashville_tn" },
        { "label": "El Paso, TX", "value": "el-paso_tx" },
        { "label": "Washington, DC", "value": "washington_dc" },
        { "label": "Las Vegas, NV", "value": "las-vegas_nv" },
        { "label": "Boston, MA", "value": "boston_ma" },
        { "label": "Portland, OR", "value": "portland_or" },
        { "label": "Detroit, MI", "value": "detroit_mi" },
        { "label": "Memphis, TN", "value": "memphis_tn" },
        { "label": "Louisville, KY", "value": "louisville_ky" },
        { "label": "Baltimore, MD", "value": "baltimore_md" },
        { "label": "Milwaukee, WI", "value": "milwaukee_wi" },
        { "label": "Albuquerque, NM", "value": "albuquerque_nm" },
        { "label": "Tucson, AZ", "value": "tucson_az" },
        { "label": "Fresno, CA", "value": "fresno_ca" },
        { "label": "Mesa, AZ", "value": "mesa_az" },
        { "label": "Sacramento, CA", "value": "sacramento_ca" },
        { "label": "Atlanta, GA", "value": "atlanta_ga" },
        { "label": "Kansas City, MO", "value": "kansas-city_mo" },
        { "label": "Colorado Springs, CO", "value": "colorado-springs_co" },
        { "label": "Raleigh, NC", "value": "raleigh_nc" },
        { "label": "Omaha, NE", "value": "omaha_ne" },
        { "label": "Miami, FL", "value": "miami_fl" },
        { "label": "Long Beach, CA", "value": "long-beach_ca" },
        { "label": "Virginia Beach, VA", "value": "virginia-beach_va" },
        { "label": "Oakland, CA", "value": "oakland_ca" },
        { "label": "Minneapolis, MN", "value": "minneapolis_mn" },
        { "label": "Tulsa, OK", "value": "tulsa_ok" },
        { "label": "Arlington, TX", "value": "arlington_tx" },
        { "label": "New Orleans, LA", "value": "new-orleans_la" },
        { "label": "Wichita, KS", "value": "wichita_ks" },
        { "label": "Cleveland, OH", "value": "cleveland_oh" },
        { "label": "Tampa, FL", "value": "tampa_fl" },
        { "label": "Bakersfield, CA", "value": "bakersfield_ca" },
        { "label": "Aurora, CO", "value": "aurora_co" },
        { "label": "Honolulu, HI", "value": "honolulu_hi" },
        { "label": "Anaheim, CA", "value": "anaheim_ca" },
        { "label": "Santa Ana, CA", "value": "santa-ana_ca" },
        { "label": "Riverside, CA", "value": "riverside_ca" },
        { "label": "Corpus Christi, TX", "value": "corpus-christi_tx" },
        { "label": "Lexington, KY", "value": "lexington_ky" },
        { "label": "Henderson, NV", "value": "henderson_nv" },
        { "label": "Stockton, CA", "value": "stockton_ca" },
        { "label": "Saint Paul, MN", "value": "saint-paul_mn" },
        { "label": "Cincinnati, OH", "value": "cincinnati_oh" },
        { "label": "St. Louis, MO", "value": "st-louis_mo" },
        { "label": "Pittsburgh, PA", "value": "pittsburgh_pa" },
        { "label": "Greensboro, NC", "value": "greensboro_nc" },
        { "label": "Lincoln, NE", "value": "lincoln_ne" },
        { "label": "Anchorage, AK", "value": "anchorage_ak" },
        { "label": "Plano, TX", "value": "plano_tx" },
        { "label": "Orlando, FL", "value": "orlando_fl" },
        { "label": "Irvine, CA", "value": "irvine_ca" },
        { "label": "Newark, NJ", "value": "newark_nj" },
        { "label": "Durham, NC", "value": "durham_nc" },
        { "label": "Chula Vista, CA", "value": "chula-vista_ca" },
        { "label": "Toledo, OH", "value": "toledo_oh" },
        { "label": "Fort Wayne, IN", "value": "fort-wayne_in" },
        { "label": "St. Petersburg, FL", "value": "st-petersburg_fl" },
        { "label": "Laredo, TX", "value": "laredo_tx" },
        { "label": "Jersey City, NJ", "value": "jersey-city_nj" },
        { "label": "Chandler, AZ", "value": "chandler_az" },
        { "label": "Madison, WI", "value": "madison_wi" },
        { "label": "Lubbock, TX", "value": "lubbock_tx" },
        { "label": "Scottsdale, AZ", "value": "scottsdale_az" },
        { "label": "Reno, NV", "value": "reno_nv" },
        { "label": "Buffalo, NY", "value": "buffalo_ny" },
        { "label": "Gilbert, AZ", "value": "gilbert_az" },
        { "label": "Glendale, AZ", "value": "glendale_az" },
        { "label": "North Las Vegas, NV", "value": "north-las-vegas_nv" },
        { "label": "Winston-Salem, NC", "value": "winston-salem_nc" },
        { "label": "Chesapeake, VA", "value": "chesapeake_va" },
        { "label": "Norfolk, VA", "value": "norfolk_va" },
        { "label": "Fremont, CA", "value": "fremont_ca" },
        { "label": "Garland, TX", "value": "garland_tx" },
        { "label": "Irving, TX", "value": "irving_tx" },
        { "label": "Hialeah, FL", "value": "hialeah_fl" },
        { "label": "Richmond, VA", "value": "richmond_va" },
        { "label": "Boise, ID", "value": "boise_id" },
        { "label": "Spokane, WA", "value": "spokane_wa" }
        ]
    
        # Convert to a dictionary for easy label-value handling
        label_to_value = { city['label']: city['value'] for city in cities }

        # Streamlit selectbox
        selected_label = st.selectbox("Select a city", list(label_to_value.keys()))
 
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
 

        min_price_display_map = {
        "No Min": None,
        "$500k": "500000",
        "$600k": "600000",
        "$700k": "700000",
        "$800k": "800000",
        
        
    }
 
        max_price_display_map = {
            "No Max": None,
            "$900k": "900000",
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
        st.markdown(f"**Generated URL Path:** `https://www.realtor.com/realestateandhomes-search/{label_to_value[selected_label]}{final_url}`")

        submitted = st.form_submit_button("Search")

    if submitted:
        output_path = "executed_notebook.ipynb"

        # Run the notebook with user inputs
        pm.execute_notebook(
            input_path="python_notebook.ipynb",
            output_path=output_path,
            parameters={
                # "location": location,
                "location": label_to_value[selected_label],
                "final_url":final_url
                # "property_type": property_type,
                # "days": days,
                # "price": price
            }
        )

        # Extract and show result
        result = get_last_output_cell(output_path)
        st.success("✅ Notebook executed successfully!")
         

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


# ---------------- Signup Page ---------------- #
elif st.session_state.page == "signup":
    st.header("Create Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=0, step=1)

    if st.button("Sign Up"):
        if not (username and email and password):
            st.warning("Please fill all fields.")
        else:
            data = {"username": username, "email": email, "password": password, "age": age}
            try:
                response = requests.post(f"{API_BASE_URL}/create", json=data)
                if response.status_code == 200:
                    st.success("Account created! Please login now.")
                    go_to("login")
                    st.rerun()
                else:
                    st.error(f"Signup failed: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")

    if st.button("Go to Login"):
        go_to("login")
        st.rerun()

# ---------------- Login Page ---------------- #
elif st.session_state.page == "login":
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not (email and password):
            st.warning("Please fill all fields.")
        else:
            data = {"email": email, "password": password}
            try:
                response = requests.post(f"{API_BASE_URL}/login", json=data)
                if response.status_code == 200:
                    result = response.json()
                    token = result["token"]
                    user = result["user"]
                    st.session_state.token = token
                    st.session_state.user_data = user
                    st.session_state.logged_in = True
                    st.session_state.page = "profile"
                    # storage.set("token", token)
                    # storage.set("username",user["username"])
                    print('-----------' , result)
                    set_token_to_local_storage(token , user["username"])
 
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error(f"Login failed: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")

    if st.button("Go to Signup"):
        go_to("signup")
        st.rerun()


 