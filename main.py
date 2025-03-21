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


@app.get("/api/v1/contact/{contact_id}")
def get_contact(contact_id: int) -> Contact:
    return Contact(ID=contact_id, Username="string", GivenName="string",
                   FamilyName="string", Phone=Phone(TypeID=0, CountryCode=0, Operator=0, Number=0), Email=["string"], Birthday=date.today())


@app.post("/api/v1/contact", status_code=status.HTTP_201_CREATED)
def post_contact(contact: Contact) -> Contact:
    return contact


@app.put("/api/v1/contact/{contact_id}")
def put_contact(contact_id: int, contact: Contact) -> Contact:
    return contact


@app.delete("/api/v1/contact/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int):
    return


@app.get("/api/v1/group/{group_id}")
def get_group(group_id: int) -> Group:
    return Group(ID=group_id, Title="string", Description="string", Contacts=[0])


@app.post("/api/v1/group", status_code=status.HTTP_201_CREATED)
def post_group(group: Group) -> Group:
    return group


@app.put("/api/v1/group/{group_id}")
def put_group(group_id: int, group: Group) -> Group:
    return group


@app.delete("/api/v1/group/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_group(group_id: int):
    return


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=6080)
