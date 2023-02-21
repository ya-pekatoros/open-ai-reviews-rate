install:
		poetry install

lint:
		{ \
    	poetry run flake8 chat_gpt_reviews_rates;\
		poetry run flake8 tests;\
    	}

test:
		poetry run pytest

.PHONY: install