"""Секция 1. Практическое задание Python.
1.1 Экранирование.
"""


class EmailEscaper:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.email

    def escape_email(self, email):
        self.email = email
        self.email.split("@")
        mail, domain = self.email.split("@")
        new_email = self.symbol * len(mail)
        result = "{}@{}".format(new_email, domain)
        return result


class PhoneNumberEscaper:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def escape_number(self):
        result = self.number.replace(self.number[-1:], "x")
        return result


class SkypeEscaper:
    def __init__(self, skype):
        self.skype = skype

    def __str__(self):
        return self.skype

    def escape_skype(self):
        symbol = "x"
        self.skype.split("skype:")
        domain, name = self.skype.split("skype:")
        new_skype = symbol * 3
        result = "{}skype:{}".format(domain, new_skype)
        return result


# 1
answer1 = EmailEscaper(symbol="x")
answer1.escape_email(email="aaa@aaa.com")
answer2 = EmailEscaper(symbol="x")
answer2.escape_email(email="aaaa@aaa.com")
# 2
answer1 = PhoneNumberEscaper(number="+7 666 777 888")
answer1.escape_number()
answer2 = PhoneNumberEscaper(number="+7 666 777       888")
answer2.escape_number()
# 3
answer1 = SkypeEscaper(skype="skype:alex.max")
answer1.escape_skype()
answer2 = SkypeEscaper(skype=r"<a href=\"skype:alex.max?call\">skype</a>")
answer2.escape_skype()
