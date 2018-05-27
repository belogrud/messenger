import pytest
from client import Action

class TestAction:

    def test_presence(self):

        exemplar = Action()

        assert exemplar.presence['action'] == 'presence'
        assert exemplar.presence['time'] != None
        assert exemplar.presence['type'] == 'status'
        assert exemplar.presence['user']['account_name'] == 'username1'

# manual_test_exemplar = Action()
# print(manual_test_exemplar.presence['type'])
# print(manual_test_exemplar.presence['user']['account_name'])
