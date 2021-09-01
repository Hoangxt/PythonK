
def emailProcess(email):
    # abc@gmail.com
    # => abc
    email_username = email[0:email.index("@")]
    # abc@gmail.com
    # => lay tu @ + 1 index
    email_domain = email[email.index("@")+1:]  # : include all behind
    return [email_username, email_domain]


def printMes(email_username, email_domain):
    print(f"User is {email_username}; Domain is {email_domain}")


def main():
    # string type input
    email = input("Please enter your email address: ").strip()
    email_username, email_domain = emailProcess(email)
    printMes(email_username, email_domain)


if __name__ == "__main__":
    main()
