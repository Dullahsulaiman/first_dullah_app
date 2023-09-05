import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
)

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
        return my_cur.fetchall()
        
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)
