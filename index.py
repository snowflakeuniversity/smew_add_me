import streamlit as st
import snowflake.connector 

def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

def add_locator(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def build_command(my_account_locator):
    alter_command=("ALTER DATA EXCHANGE ACME_ADU ADD CONSUMERS = AWS_CA_CENTRAL_1." + my_account_locator)
    return alter_command

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
          build_command(my_account_locator)
        else:
          st.write()
     else: 
        st.write('Sign up for a Snowflake Trial Account on AWS in the Canada Central Region, please')
else:
     st.write()

st.write(alter_command)

