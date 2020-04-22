from django.core.validators import RegexValidator

from utils.strings import phone_not_in_format_message, national_code_in_format_message, password_in_format_message

phone_regex = RegexValidator(regex=r'^9\+?1?\d{9}$', message=phone_not_in_format_message)
national_code_validator = RegexValidator(regex=r'^\+?1?\d{10}$', message=national_code_in_format_message)
password_regex = RegexValidator(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message=password_in_format_message)
