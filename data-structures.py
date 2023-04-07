# list_of_no = []
# list_of_no.append(1)
# list_of_no.append(2)
# list_of_no.append("Santosh")
# print(list_of_no)
list_of_cloud = ["aws","azure","gcp","oracle"]
list_of_env = ["dev","test","prod"]
# print(list_of_cloud[0])
# print(list_of_env[1])
for i in list_of_cloud:
    if i == "aws":
        print("AWS is the best clod service")

#dictionary
dict_of_cloud = {
    "aws":"amazon web service",
    "azure":"Microsoft Azure",
    "gcp":"google cloud platform"
}

print(dict_of_cloud["aws"])
print(dict_of_cloud.get("azure"))
print(dict_of_cloud.get("linode","Not found"))

dict_of_cloud.update({"linode":"Linode Cloud"})
print(dict_of_cloud)
