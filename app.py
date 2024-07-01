import streamlit as st
import pandas as pd
import pickle
import time

def nearest_bank_recommendation(user_query):
    user_query = user_query.lower().strip()
    matching_rows = bank[bank['loc'] == user_query]
    
    if not matching_rows.empty:
        bank_index = matching_rows.index[0]
        distance = similarity[bank_index]
        bank_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[:3]
        
        recommended_banks = []
        for i in bank_list:
            bank_name = bank.iloc[i[0]]['Blood Bank Name']
            state = bank.iloc[i[0]]['State']
            city = bank.iloc[i[0]]['City']
            pincode = bank.iloc[i[0]]['Pincode']
            contact_info = bank.iloc[i[0]]['contact info']
            nodal_officer = bank.iloc[i[0]]['Contact Nodal Officer']
            mobile = bank.iloc[i[0]]['Mobile Nodal Officer']
            email = bank.iloc[i[0]]['Email Nodal Officer']
            
            bank_details = {
                'Blood Bank Name': bank_name,
                'State': state,
                'City': city,
                'Pincode': pincode,
                'Contact Info': contact_info,
                'Nodal Officer': nodal_officer,
                'Nodal officer Mobile': mobile,
                'Nodal Officer Email': email
            }
            recommended_banks.append(bank_details)
        
        return recommended_banks
    else:
        print("No matching blood banks found.")
        return []
        


bank_list = pickle.load(open('bank.pkl','rb'))
bank = pd.DataFrame(bank_list)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Blood Bank Recommendation System")
st.divider()

st.header("select Your Location from Side-bar")

with st.sidebar:
    state = st.selectbox("Select State", bank['State'].unique())
    district = st.selectbox("Select District", bank[bank['State'] == state]['District'].unique())
    city = st.selectbox("Select City", bank[(bank['State'] == state) & (bank['District'] == district)]['City'].unique())
    pincode = st.selectbox("Select Pincode", bank[(bank['State'] == state) & (bank['District'] == district) & (bank['City']==city)]['Pincode'].unique() )
# st.write("You selected:", option)

query = f"{state} {district} {city} {pincode}"

if st.button("Find Blood Bank"):
    st.write("Recommended Blood Banks:")
    recommended_banks = nearest_bank_recommendation(query)
    for bank in recommended_banks:
        st.markdown(f"- **{bank['Blood Bank Name']}**")
        st.markdown(f"  State: {bank['State']}")
        st.markdown(f"  City: {bank['City']}")
        st.markdown(f"  Pincode: {bank['Pincode']}")
        st.markdown(f"  Contact Info: {bank['Contact Info']}")
        st.markdown(f"  Nodal Officer: {bank['Nodal Officer']}")
        st.markdown(f"  Nodal officer Mobile: {bank['Nodal officer Mobile']}")
        st.markdown(f"  Nodal Officer Email: {bank['Nodal Officer Email']}")
        st.write("---")
        time.sleep(0.2)
