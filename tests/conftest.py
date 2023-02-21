import pytest


@pytest.fixture(scope="session")
def reviews_path(tmp_path_factory):
    return tmp_path_factory.mktemp("reviews_test") / "reviews.csv"
