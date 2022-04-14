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
    alter_command=('ALTER DATA EXCHANGE ACME_ADU ADD CONSUMERS = AWS_CA_CENTRAL_1.' + my_account_locator)
    return alter_command

st.title('You are cordially invited to...')
st.header('The ACME-ADU Private Exchange')
st.text('Powered by Snowflake')
 
current_region_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_region_function.png"
st.image(current_region_function)

my_region = st.selectbox(
     'What REGION do you see if you run the CURRENT_REGION function?',
     ('<pick one>','AWS_CA_CENTRAL_1', 'Some other region.', 'Azure Canada Central'))


 
current_account_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_account_function.png"
st.image(current_account_function)

my_account_locator = st.text_input('What is listed if your run the CURRENT ACCOUNT function?', 'abc12345')

st.write('Does your URL start like this? https://app.snowflake.com/ca-central-1.aws/'  +  my_account_locator + '/...')    

if st.button('Looks Good - Add Me'):
     what_ran=build_command(my_account_locator)
     st.write('COMMAND: '+ what_ran)
else:
     st.write()


