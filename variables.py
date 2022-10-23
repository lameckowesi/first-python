Name = "Lameck"
FullName = "Lameck"  #Pascal Casing
fullName = "Lameck"  #camel Casing
full_name = "Lameck"  #snake_casing
Age = 50 
Stipend = "600"

if FullName == full_name:
    print("the names are the same")  #identation is important

print(f"Hello {Name}! Your Age is {Age}")
print("Hello " + full_name + "Your age is " + str(Age))

#Logical operators

if FullName == "Lameck" and Age == 50:
    print("TRUE")

if FullName == "Lameck" and Age ==50:
    print("Lameck is present")

if Name == "Lameck" and Stipend >= "500":
    print("Lameck's stipend matched")
