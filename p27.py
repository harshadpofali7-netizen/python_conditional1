#Program to check login status by username and password
user_database = {
    "admin " : "Admin@123",
    "john_doe" : "password2026",
    "alice_smith" : "securepass78"
}
input_username = input("Enter username ")
input_password = input("Enter password ")
if input_username in user_database:
    if user_database[input_username] == input_password:
        print("\n **login successful** welcome back",input_username)
    else:
        print("\n **Login failed** incorrect password ")
else:
    print("\n **login failed** username not found ")
    