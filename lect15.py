appendMe = '\n\nThis is more information to put in the file.'

saveFile = open('appendingFile.txt', 'a')
saveFile.write(appendMe)
saveFile.close()
