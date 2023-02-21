import os
import pandas as pd
import openai
from dotenv import load_dotenv

# Определить функцию, которая будет использовать OpenAI для оценки текста по шкале от 1 до 10
def get_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Please rate the sentiment of the following review on a scale of 1 to 10, with 1 being very negative and 10 being very positive:\n\n{text}\n\nRating:"),
        temperature=0,
        max_tokens=1,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    rating = int(response.choices[0].text)
    return rating

def make_rating(filepath=None):
    # Загрузить API ключ из файла .env
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key
    # Открыть файл с отзывами и прочитать его в pandas DataFrame
    if not filepath:
        filepath = "reviews.csv"
    df = pd.read_csv(filepath)

    # Применить функцию get_sentiment для каждого отзыва и создать новую колонку с рейтингом
    df['rate'] = df['review text'].apply(get_sentiment)

    # Отсортировать DataFrame по колонке rate в убывающем порядке
    df = df.sort_values(by='rate', ascending=False)

    # Записать DataFrame в новый CSV-файл
    output_filename = f"{os.path.splitext(filepath)[0]}_analyzed.csv"
    df.to_csv(output_filename, index=False)

    print(f"Результаты сохранены в файл {output_filename}.")

if __name__ == '__main__':
    make_rating()
