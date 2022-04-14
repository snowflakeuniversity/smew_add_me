import streamlit as st
import snowflake.connector 



st.title('You are cordially invited to...')
st.header('The ACME-ADU Private Exchange')
st.text('Powered by Snowflake')
 
current_region_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_region_function.png"
st.image(current_region_function)

my_region = st.selectbox(
     'What REGION do you see if you run the CURRENT_REGION function?',
     ('<pick one>','AWS_CA_CENTRAL_1', 'Some other region.', 'Azure Canada Central'))

if st.button('Submit My Region'):
     if my_region == 'AWS_CA_CENTRAL_1':
        #st.write(my_region)
        current_account_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_account_function.png"
        st.image(current_account_function)
        my_account_locator = st.text_input('What is listed if your run the CURRENT ACCOUNT function?', 'abc12345')
        st.write('Your Account Locator is ', my_account_locator)    
        if st.button('Add My Account to the Private Exchange'):
          st.write('Thanks for submitting your Account Locator')
        else:
          st.write('Your Account Locator has an issue.')
     else: 
        st.write('Sign up for a Snowflake Trial Account on AWS in the Canada Central Region, please')
else:
     st.write('Please enter your Region')



my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
#st.text("Hello from Snowflake:")
#st.text(my_data_row)
