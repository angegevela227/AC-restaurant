#
personalusername = "ange"
lastpassword = "barks"
#logging in to check if the person have the correct credentials in the system
username = input("Username: ")
password = input("Password: ")

if username == personalusername and password == lastpassword:
    print("Login succesful!You may proceed to the next step")
    print("Enter the names of your desired products: ")#type'done'if you have settled on the product that you have.
    
    products = []
    #ask the user to input the product they desire
    while True:
        product = input()
        if product == 'done':
            break
        products.append(product)
    
    print("the list of the product are ",products)

else:
     print("You put invalid password or username. try again!")