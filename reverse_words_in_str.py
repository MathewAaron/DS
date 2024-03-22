sting_var = "hello my name is Aaron"

sting_var = sting_var.split()
res = ' '.join(sting_var[::-1]) # Aaron is name my hello
#print(res)

print(res.rfind("name"))