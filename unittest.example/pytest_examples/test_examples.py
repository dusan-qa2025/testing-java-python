import pytest

@pytest.fixture
def db_conn_fixture():
    print("connected to database")
    yield {'name': 'John Smith', 'email': 'email@email.com', 'balance': 2355.52}
    print("disconnected from database")

def test_update_user_balance(db_conn_fixture):
    print("Test started")
    print(f"value received: {db_conn_fixture}")
    result = db_conn_fixture['balance'] - db_conn_fixture['balance']
    assert result == 0
