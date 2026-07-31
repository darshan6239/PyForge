class demo:
    def __init__(self):
        print("Default Construtor Called! ")

# Objname = cn()
obj = demo()


print("===============")

class demo:
    ins_name = "Linkcode"

# 1) clasname.varname 
# print(ins_name) === will throw error 
print(demo.ins_name)

# 2) objrefvar.varname 
obj = demo()
print(obj.ins_name)



