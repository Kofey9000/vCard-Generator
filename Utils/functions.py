from datetime import date

from ContactsGenerators.EnglishContactGenerator import *
from Utils.Strings import *


def isNewContact(self, line):
    if line[:len(self.generator.vcardStartQ)] == self.generator.vcardStartQ:
        return True
    else:
        return False


def isCellLine(self, line):
    if line[:len(self.generator.vcardCellQ)] == self.generator.vcardCellQ:
        return True
    else:
        return False


def isLineName(self, line):
    if line[:len(self.generator.vcardNameQ)] == self.generator.vcardNameQ:
        return True
    else:
        return False


def isLineFirstName(self, line):
    if line[:len(self.generator.vcardFirstNameQ)] == self.generator.vcardFirstNameQ:
        return True
    else:
        return False


def isOrgLine(self, line):
    if line[:len(self.generator.vcardOrgQ)] == self.generator.vcardOrgQ:
        return True
    else:
        return False


def generateTestEnContact(count=7):
    testContacts = []
    for nameLength in range(1, count, 1):
        contact = generateSimpleSingleEnContact(nameLength)
        testContacts.append(contact)
    return testContacts


def getLinesIn(text) -> str:
    for line in text.split(newLine):
        yield line


def getContactNameParsed(contact: Contact) -> str:
    nameList = contact.username.split()
    if len(nameList) == 1:
        return f";{nameList[0]};;;"
    elif len(nameList) == 2:
        return f"{nameList[1]};{nameList[0]};;;"
    elif len(nameList) == 3:
        return f"{nameList[2]};{nameList[0]};{nameList[1]};;"
    else:
        return f"{nameList[-1]}; {' '.join(nameList[0:-2])};{nameList[-2]};;"


def getVcardLineContent(line) -> str:
    return "".join(line.split(":")[1:])


def isUserSpecifiedFileName(filename) -> bool:
    if filename is not None:
        return True
    return False


def getFormattedUserFileName(filename) -> str:
    if filename.endswith(".vcf"):
        filename = f'{filename[:-4]}-{date.today()}.vcf'
    else:
        filename += f'-{date.today()}.vcf'
    return filename
