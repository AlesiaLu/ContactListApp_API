from api.contacts import ContactList
from random_data_generation import first_name, last_name
import pytest

contact = ContactList()


def test_add_contact(get_token):
    id_contact, status = contact.add_contact(first_name, last_name, get_token)
    assert status
    assert status == 201, f"'{status}' is not our expectation"
    assert id_contact is not None, "Contact ID was not returned"
