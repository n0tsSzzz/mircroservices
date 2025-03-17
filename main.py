from dataclasses import dataclass
from datetime import date
from fastapi import FastAPI, status
import uvicorn

@dataclass
class Phone:
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

@dataclass
class Contact:
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    Phone: Phone
    Email: list[str]
    Birthday: date

@dataclass
class Group:
    ID: int
    Title: str
    Description: str
    Contacts: list[int]
app = FastAPI()

phone_ = Phone(TypeID=0, CountryCode=0, Operator=0, Number=0)
contact_ = Contact(ID=0, Username="string", GivenName="string", FamilyName="string", Phone=phone_, Email=["string"], Birthday=date.today())
group_ = Group(ID=0, Title="string", Description="string", Contacts=[0])
@app.get("/api/v1/contact")
def main():
    return contact_

@app.post("/api/v1/contact", status_code=status.HTTP_201_CREATED)
def main(contact: Contact) -> Contact:
    return contact

@app.put("/api/v1/contact")
def main(contact: Contact) -> Contact:
    return contact

@app.delete("/api/v1/contact")
def main():
    return contact_

@app.get("/api/v1/group")
def main_group():
    return group_

@app.post("/api/v1/group", status_code=status.HTTP_201_CREATED)
def main_group(group: Group) -> Group:
    return group

@app.put("/api/v1/group")
def main_group(group: Group) -> Group:
    return group

@app.delete("/api/v1/group")
def main_group():
    return group_

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=6080)
