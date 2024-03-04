
# %%
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
tmo_lst = list(ft_tuple)
tmo_lst[1] = "Spain!"
ft_tuple = tuple(list(tmo_lst))
ft_set.discard("tutu!")
ft_set.add("Madrid!")
ft_dict["Hello"] = "42Madrid!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# %%
