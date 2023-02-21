from chat_gpt_reviews_rates import make_rating
import os
import shutil
import pandas as pd


def test_make_rating(reviews_path):
    file_path = os.path.abspath('./tests/test_data/reviews.csv')
    shutil.copyfile(file_path, reviews_path)
    make_rating(filepath=reviews_path)
    output_filename = f"{os.path.splitext(reviews_path)[0]}_analyzed.csv"
    df = pd.read_csv(output_filename)
    assert df['rate'][0] >= df['rate'][1]
    assert df['rate'][0] == 10
    assert df['rate'].iloc[-1] == 1
