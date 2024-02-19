from fastapi import FastAPI
from CSVparser import read_users_from_csv
from JSONparser import read_users_from_json
from XMLparser import read_users_from_xml
from YAMLparser import read_users_from_yaml

app = FastAPI()

@app.get("/xml")
def read_xml():
    users = read_users_from_xml("../files/file5.xml")
    usersString = ', '.join([user.printUser() for user in users])
    return {"xml_data": usersString}

@app.get("/csv")
def read_csv():
    users = read_users_from_csv("../files/file3.csv")
    usersString = ', '.join([user.printUser() for user in users])
    return {"csv_data": usersString}

@app.get("/yaml")
def read_yaml():
    users = read_users_from_yaml("../files/file2.yaml")
    usersString = ', '.join([user.printUser() for user in users])
    return {"yaml_data": usersString}

@app.get("/txt")
def read_txt():
    users = read_users_from_txt("../files/file1.txt")
    usersString = ', '.join([user.printUser() for user in users])
    return {"txt_data": usersString}

@app.get("/json")
def read_json():
    users = read_users_from_json("../files/file4.json")
    usersString = ', '.join([user.printUser() for user in users])
    return {"json_data": usersString}