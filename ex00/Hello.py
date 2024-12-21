# Original data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

country = "World!"
city = "Morocco"
campus_city = "Benguerir!"
campus_name = "1337!"

ft_list[1] = country

ft_tuple = (ft_tuple[0], city)

ft_set.remove("tutu!")
ft_set.add(campus_city)

ft_dict["Hello"] = campus_name

print(ft_list)  
print(ft_tuple) 
print(ft_set) 
print(ft_dict)
