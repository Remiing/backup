def read():
    read_data = open('union.txt', 'r')
    characters = []
    while True:
        line = read_data.readline()
        if not line: break
        data = line.replace('\n', '').split(',')
        characters.append(data)
    read_data.close()
    return characters


#def placement():


if __name__ == '__main__':
    read()
