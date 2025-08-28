with open("practice.txt","r") as f:
    data = f.read()

new_data=data.replace("Java","python") #replace method of strings used here
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
    
