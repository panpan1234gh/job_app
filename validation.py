import re
from datetime import datetime


def employee_validator(employee, datatime=None):

    errors = []

    if not (type(employee[0])) == int and (employee[0] > 0):
        errors.append("Invalid Id")

    if not (type(employee[1])) == str and re.match(r"^[\w\s]{3,60}&",employee[1]):
        errors.append("Invalid Name")

    if not (type(employee[2])) == str and re.match(r"^[\w\s]{3,30}&",employee[2]):
        errors.append("Invalid Job")

    if not (type(employee[3])) == str and re.match(r"^[\w\s]{3,30}&",employee[3]):
        errors.append("Invalid Workplace")

    try:
        datatime.strptime(employee[4], "%m/%d/%Y")
    except:
        errors.append("Invalid Date")
    return errors
