from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):
    pass


class MustStartWithCharacterError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustNotContainWhiteSpaceError(Exception):
    pass


class InvalidNameError(Exception):
    pass


def email_validator(email):
    regex = r'^([a-zA-Z][a-zA-Z0-9\_]{3,232})\b'

    if len(email.split('@')[0]) <= MINIMUM_NAME_LEN:
        raise NameTooShortError('Name must be more than 4 characters!')

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @!')

    if email.split('.')[-1] not in VALID_DOMAINS or email.split('.')[-2] in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net!')

    if email.count('@') > 1:
        raise MustContainOnlyOneAtSymbolError('Email cannot contain more than one @!')

    if not email[0].isalpha():
        raise MustStartWithCharacterError('Email must start with letter from alphabet a-z!')

    if len(email.split('@')[0]) > MAXIMUM_NAME_LEN:
        raise NameTooLongError('Name exceeds the maximum allowed length of 232 characters!')

    if ' ' in email:
        raise MustNotContainWhiteSpaceError('Email address cannot contain whitespace!')

    if findall(regex, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must contains only letters, digits and underscores!')

    print('Email is valid')


# pattern = r'^((([a-z])[a-z0-9\_\-\.]{3,232})@([a-z\-]+)(\.[a-z]+)+)$'
MINIMUM_NAME_LEN = 4
MAXIMUM_NAME_LEN = 232
VALID_DOMAINS = ('com', 'bg', 'org', 'net')

while True:
    current_email = input()

    if current_email == 'End':
        break

    email_validator(current_email)


# Below can be found some inputs to try with.

# peter@gmail.com
# petergmail.com
# abc@abv.bg
# peter@gmail.hotmail
# testmail@mail.it
# ivan_vr@abv.bg
# goshomail@gmail.com
# tests@tests@gmail.com
# tests@@mail.bg
# 12test@mail.bg
# qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqweadsadasdasdasrtyu@abv.bg
# tests tests@mail.bg
# test_test@abv.bg
# tests-tests@tests.com
# test_test@tests.com.bg
