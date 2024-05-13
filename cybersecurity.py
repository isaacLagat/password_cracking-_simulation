import hashlib
def simulate_password_cracking(hashed_password, password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            return f"password cracked: {password}"
        return "password not found"
    
    # For example
    hashed_password_to_crack = "d033e22ae348aeb5660fc2140aec35850c4da997"
    common_password = ["password" , "123456" , "qwerty" , "admin"]
    result = simulate_password_cracking(hashed_password_to_crack, common_password)
    print(result)