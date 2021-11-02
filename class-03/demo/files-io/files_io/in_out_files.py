
def read_file(path):
    try:
        file = open(path)
    except FileNotFoundError:
        content = "Error : Sorry file not found"
    else:
        content = file.read()
        file.close()
        with open('files_io/assets/spam.copy.txt', 'w') as f:
            f.write("THIS IS A COPY\n"+content)
    finally:
        return content

        

def read_file_using_with(path):
    with open(path) as f:
        content = f.read()
    return content





if __name__=="__main__":
    content = read_file('files_io/assets/spam.txt')
    print(content)
    # content = read_file('files_io/assets/spam1.txt')
    # print(content)
    # content2 = read_file_using_with('files_io/assets/spam.txt')
    # print(content2)


    # Images as binary
    with open('files_io/assets/brain.jpg', 'rb') as img:
        content = img.read()

    with open('files_io/assets/brain.copy.jpg', 'wb') as img2:
        img2.write(content[:len(content)//2])
