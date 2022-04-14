import streamlit
import snowflake.connector

streamlit.title('You are cordially invited to the Private Snowflake Exchange ACME-ADU')

option = st.selectbox(
     'Run the command [SELECT CURRENT_REGION();] What is the result?',
     ('AWS_CA_CENTRAL_1', 'Something that is not AWS and Canada Central')

st.write('You selected:', option)
st.write('Did you know Private Exchanges only exist on one Region/Cloud? Our ACME-ADU Exchange only exists in the AWS Central Canada Region. We can only add your account if it is in the same region as the exchange.')
  
  




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
