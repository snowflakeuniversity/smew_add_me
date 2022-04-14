import streamlit as st
import snowflake.connector 



st.title('You are cordially invited to...')
st.header('The Private Snowflake Exchange ACME-ADU')


st.write('Did you know Private Exchanges only exist on one Region/Cloud?') 
st.write('Our ACME-ADU Exchange only exists in the AWS Central Canada Region.') 
st.write('We can only add your account if it is in the same region as the exchange.')
  
current_region_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_region_function.png"
st.image(current_region_function)

option = st.selectbox(
     'What REGION do you see if you run the CURRENT_REGION function?',
     ('<pick one>','AWS_CA_CENTRAL_1', 'Something that is not AWS and Canada Central')) 
st.write('You selected:', option)

current_account_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_account_function.png"
st.image(current_account_function)
title = st.text_input('What is listed if your run the CURRENT ACCOUNT function?', 'abc12345')
st.write('Your Account Locator is ', title)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
