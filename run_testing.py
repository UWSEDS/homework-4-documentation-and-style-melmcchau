
"""
This module exists to run and test the data being imported from the chosen columns
and the selected url. The main funtion of this module is to store the called URLS
for running the program (although any url or column can be used from the terminal)

"""
import test_dataframe

CHOSEN_COLUMNS = ['title', 'category', 'source']
CHOSEN_URL = "https://github.com/BuzzFeedNews/2018-12-fake-news-top-50/raw/master/data/top_2018.csv"

# Run Functions from test_dataframe
print(test_dataframe.test_create_dataframe(CHOSEN_COLUMNS, CHOSEN_URL))
