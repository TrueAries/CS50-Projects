media = input("File name: ")
if media.endswith((".gif", ".jpg", ".jpeg")):
    print("image/gif")
elif media.endswith(".png"):
    print("image/png")
elif media.endswith(".pdf"):
    print("application/pdf")
elif media.endswith(".txt"):
    print("text/plain")
elif media.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")