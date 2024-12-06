"""This file contains the definition of several function prompting the user
for various pieces of information. This is done with InquirerPy and includes
validation of the data provided by the user."""

from InquirerPy import inquirer
from validators import validate_phone_number, validate_email_address, validate_decimal
from sanitizers import sanitize_phone_number, sanitize_email_address, sanitize_decimal
from models import Student, HourlyRate


def prompt_student(student=Student()) -> None:
    """Function prompting the user to enter the data related to a student.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives à l'étudiant :")

    student.first_name = inquirer.text(
        message="Prénom :",
        default=student.first_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le prénom doit comporter entre 3 et 50 caractères.",
    ).execute()

    student.last_name = inquirer.text(
        message="Nom :",
        default=student.last_name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le nom doit comporter entre 3 et 50 caractères.",
    ).execute()

    # The number is transformed following E164 standard format
    student.phone_number = inquirer.text(
        message="Numéro de téléphone :",
        default=student.phone_number,
        validate=validate_phone_number,
        invalid_message="Le numéro de téléphone renseigné n'est pas correct.",
        transformer=sanitize_phone_number,
        filter=sanitize_phone_number,
    ).execute()

    student.email_address = inquirer.text(
        message="Adresse email :",
        default=student.email_address,
        validate=validate_email_address,
        invalid_message="Either the syntax or the domain name of the address is invalid.",
        transformer=sanitize_email_address,
        filter=sanitize_email_address,
    ).execute()

    student.address = inquirer.text(
        message="Adresse :",
        default=student.address,
    ).execute()

    # We return the modified student instance
    return student


def prompt_hourly_rate(hourly_rate=HourlyRate()):
    """Function prompting the user to enter the data related to a hourly rate.
    The arguments can be used to specify default values for each field
    (useful when displaying the edition prompt)."""

    print("Veuillez entrer les informations relatives au taux horaire :")

    hourly_rate.name = inquirer.text(
        message="Nom du taux :",
        default=hourly_rate.name,
        validate=lambda result: 50 >= len(result) >= 3,
        invalid_message="Le nom doit comporter entre 3 et 50 caractères.",
    ).execute()

    hourly_rate.price = inquirer.text(
        message="Tarif (en euros) :",
        default=str(hourly_rate.price),
        validate=validate_decimal,
        invalid_message="Le tarif horaire doit être compris entre 0€ et 999.99€.",
        transformer=sanitize_decimal,
        filter=sanitize_decimal,
    ).execute()

    return hourly_rate
