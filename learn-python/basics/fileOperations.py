with open('sample.txt', 'w') as f:
    # f.write('thank you')
    read_data = f.read()
    print(read_data)
    print(f.readline())

f.close()