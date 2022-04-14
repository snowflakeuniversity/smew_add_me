import streamlit as st
import snowflake.connector 
from urllib.error import URLError 

def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

my_cnx = init_connection()

def add_locator(query):
    my_cur = my_cnx.cursor()
    try:
      result=my_cur.execute(query)
    except URLError as e:
      st.error()
    return result

def build_command(my_account_locator):
    alter_command=('ALTER DATA EXCHANGE ACME_ADU ADD CONSUMERS = AWS_CA_CENTRAL_1.' + my_account_locator)
    return alter_command

st.title('You are cordially invited to...')
st.header('The ACME-ADU Private Exchange')
st.text('Powered by Snowflake')
 
current_region_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_region_function.png"
st.image(current_region_function)

st.markdown('Only accounts in the AWS Central Canada Region (as shown above) can be added to the ACME-ADU Private Exchange that Max and Lottie set up to share data with each other. If your account is in the correct region, submit your account locator below.')


 
current_account_function = "https://learn.snowflake.com/asset-v1:snowflake+ESS-SMEW+C+type@asset+block@current_account_function.png"
st.image(current_account_function)

my_account_locator = st.text_input('What result do you get if you run the CURRENT_ACCOUNT function?', 'abc12345')

st.write('Does your URL start like this? https://app.snowflake.com/ca-central-1.aws/'  +  my_account_locator + '/...')    

if st.button('Looks Good - Add Me'):
     try:
        what_ran=build_command(my_account_locator)
        what_really_ran=add_locator(what_ran)   
        st.write(what_really_ran)
     except URLError as e:
        st.error()
else:
     st.write()


