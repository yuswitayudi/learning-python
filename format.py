first_name = "Yudi" 
last_name = "Yuswita"
age = 25
pesan = "and Your umur is"
message = f"{first_name} '{last_name}' {pesan} {age}"

length = len(message)
yudi = "yudi"
print(message.upper(), "and  character of message is ".upper(), length)
print(message.replace("a", "b").lower(), "and  character of message is ".upper().lower().upper(), length)

print(first_name in yudi.title())