#file handling - need in python because it stores data permanently (read "r", write"w",append"a") (w,r,a are called the modes) 
# must close the file "file.close()" (append is used to avoid overwrite)
# file=open("C:\\Users\\ayesh\\Downloads\\Advance Python Programming 3 Months PMYSD (1).docx","r")
# data=file.read()
# print(data)

# file=open("C:\\Users\\ayesh\\Downloads\\Advance Python Programming 3 Months PMYSD (1).docx","w")
# data=file.write("Salam World")
# print(data)


# file=open("C:\\Users\\ayesh\\Downloads\\Advance Python Programming 3 Months PMYSD (1).docx","a")
# file.write("I'm gonna create an AI model")
# file.close()

# with open("C:\\Users\\ayesh\\Downloads\\Advance Python Programming 3 Months PMYSD.docx","a") as file:
#     content=file.write("I'm gonna create an AI model")
#     print(content)

with open("C:\\Users\\ayesh\\Downloads\\Advance Python Programming 3 Months PMYSD (1).docx", "a") as file:
    file.write("I'm gonna create an AI model")
