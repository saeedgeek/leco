from django.core.validators import RegexValidator
from utils.strings import phone_not_in_format_message, national_code_in_format_message


phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message=phone_not_in_format_message)
national_code_validator = RegexValidator(regex=r'^\+?1?\d{10}$', message=national_code_in_format_message)
