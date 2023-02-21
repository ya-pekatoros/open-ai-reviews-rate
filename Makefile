install:
		poetry install

lint:
		{ \
    	poetry run flake8 openai_reviews_rates;\
		poetry run flake8 tests;\
    	}

test:
		poetry run pytest

.PHONY: install