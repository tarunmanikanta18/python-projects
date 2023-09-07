while True:

    def main():
        print(" welcome to the email slicer ")
        print("")

        email_input = input("input yur Email address here: ")

        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")

        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension)

    main()
