import random

def write(file):
    f = open("{}.txt".format(file), "w")
    f.write(str.join("", random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm1234567890", k=10)))
