import creator, reader, sender

filename = "text"

creator.write(filename)
x = reader.read(filename)
sender.send(x)
