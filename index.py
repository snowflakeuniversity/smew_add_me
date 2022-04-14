import streamlit as st
import snowflake.connector 

current_account_function = "//learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_account_function.png"

st.image(current_account_function, caption="Find your account locator.")

st.title('You are cordially invited to...')
st.header('The Private Snowflake Exchange ACME-ADU')


st.write('Did you know Private Exchanges only exist on one Region/Cloud?') 
st.write('Our ACME-ADU Exchange only exists in the AWS Central Canada Region.') 
st.write('We can only add your account if it is in the same region as the exchange.')
  
option = st.selectbox(
     'Run the command [SELECT CURRENT_REGION();] What is the result?',
     ('<pick one>','AWS_CA_CENTRAL_1', 'Something that is not AWS and Canada Central')) 
st.write('You selected:', option)

title = st.text_input('Your Account Locator', 'abc12345')
st.write('Your Account Locator is ', title)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
