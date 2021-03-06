# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "fund.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "Music"
}

pagination = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmNTg3ZWY5YjEwZjA0ZmQ5M2MzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODg2OTk5NzYsImV4cCI6MTU4ODc5OTk3NiwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.urbN9apKhItdhkAlvmAPXRLLnMUj7urnaJffmVObVi0",
    "executive_producer" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmYzc2N2YxYmEwZWJiNDIwMTYzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODg2OTk5NzYsImV4cCI6MTU4ODc5OTk3NiwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.yRlQqOZOxxsuj6_KacV7xpAyly5b8PWtsan7-gKoSCo",
    "casting_director" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmOTA3ZWY5YjEwZjA0ZmQ5M2ZiIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODg2OTk5NzYsImV4cCI6MTU4ODc5OTk3NiwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZWRpdDphY3RvcnMiLCJlZGl0Om1vdmllcyIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.zLh0K7CLN_DcJoULn0ns7KdhBKqVr9GEONfgoxBagc4"
}