# import streamlit as st

# # --- Property Type Dropdown ---
# property_type_map = {
#     "Single Family Home": "/type-single-family-home",
#     "Multi Family Home": "/type-multi-family-home",
#     "Any": "",
#     "House": "/type-single-family-home",
#     "Condo": "/type-condo",
#     "Townhome": "/type-townhome",
#     "Land": "/type-land",
#     "Mobile": "/type-mfd-mobile-home",
#     "Farm": "/type-farms-ranches"
# }
# property_type = st.selectbox("Property Type", list(property_type_map.keys()))
# property_type_url = property_type_map[property_type]

# # --- Price Range Dropdown ---
# min_price = st.selectbox("Minimum Price", ["No Min", "100000", "200000", "300000", "400000", "500000"])
# max_price = st.selectbox("Maximum Price", ["No Max", "200000", "300000", "400000", "500000", "1000000"])

# if min_price != "No Min" and max_price == "No Max":
#     price_filter = f"/price-{min_price}-na"
# elif min_price == "No Min" and max_price != "No Max":
#     price_filter = f"/price-na-{max_price}"
# elif min_price != "No Min" and max_price != "No Max":
#     price_filter = f"/price-{min_price}-{max_price}"
# else:
#     price_filter = ""

# # --- Days on Market Dropdown ---
# days_map = {
#     "Any": "",
#     "Today": "/dom-1",
#     "30 Days": "/dom-30",
#     "60 Days": "/dom-60",
#     "180 Days": "/dom-180"
# }
# days_on_market = st.selectbox("Days on Market", list(days_map.keys()))
# days_url = days_map[days_on_market]

# # --- Sort By Dropdown ---
# sort_by_map = {
#     "Relevant Listing": "",
#     "New Listings": "/sby-6",
#     "Lowest Price": "/sby-1",
#     "Highest Price": "/sby-2",
#     "Year Built": "/sby-17",
#     "Open House Date": "/sby-5",
#     "Recent Reduction": "/sby-7",
#     "Largest Sqft": "/sby-14",
#     "Lot Size": "/sby-9",
#     "Photo Count": "/sby-16"
# }
# sort_option = st.selectbox("Sort By", list(sort_by_map.keys()))
# sort_url = sort_by_map[sort_option]

# # --- Price Reduced Checkbox ---
# price_reduced = st.checkbox("Show Only Price Reduced")
# price_reduced_url = "/show-price-reduced" if price_reduced else ""

# # --- Construct Final URL ---
# final_url = f"{property_type_url}{price_filter}{days_url}{sort_url}{price_reduced_url}"
# st.markdown(f"**Generated URL Path:** `{final_url}`")


import streamlit as st

# --- Property Type Dropdown ---
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
final_url = f"{property_type_url}{price_filter}{days_url}{sort_url}{price_reduced_url}"
st.markdown(f"**Generated URL Path:** `{final_url}`")
