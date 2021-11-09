userReply=input("would you like to buy stamps , buy an envelope, or make a copy?(Enter stamps,envelop,or copy)")
if userReply == "stamps":
    print("we have many stamps desings to choose from.")
elif userReply == "envelope":
    print("we have many envelope sizes to choose from")
elif userReply== "copy":
    copies =input("How many copies would you like?(enter a no)")
    print ("here are{} copies.".format(copies))
else:
    print("thank you, please come again.")
