try:
    file = open('text.txt', 'r').close()
except FileNotFoundError:
    print('File not found or path is incorrect')
finally:
    print('File found')



