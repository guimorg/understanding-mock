import pytest

from unittest.mock import patch

from app import (
    is_it_friday, 
    is_today_friday
)


def test_is_it_friday_fail():
    wrong_date = 151293
    with pytest.raises(TypeError):
        is_it_friday(wrong_date)


def test_is_it_friday_false():
    date = '20-06-2019'
    assert not is_it_friday(date)


from datetime import timedelta
def test_is_it_friday_true():
    date = '21-06-2019'
    assert is_it_friday(date)


# I love using patch as a decorator but let's show both ways!
@patch('app.date')
def test_is_today_friday_false(
    mock_date
):
    from datetime import date
    mock_date.today.return_value.weekday.return_value = 2

    assert not is_today_friday()


# Here we are using patch as a contextmanager
def test_is_today_friday_true():
    with patch('app.date') as mock_date:
        from datetime import date
        mock_date.today.return_value.weekday.return_value = 4

        assert is_today_friday()