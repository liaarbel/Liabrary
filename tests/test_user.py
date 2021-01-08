import pytest
import peewee

from app.models import User


class TestUserDb(object):
    def test_insert_user_with_username_select_finds(self):
        user = User.create(
            name="Lia",
            age=15,
            email="lia.arbel@gmail.com",
            phone="052-2635147"
        )
        search = User.get(User.name == user.name)
        assert search.age == user.age
        assert search.email == user.email
        assert search.phone == user.phone

