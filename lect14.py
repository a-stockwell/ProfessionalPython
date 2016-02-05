writeMe = 'Example Text\nTrying with\n\tsaveFile.open()\ninstead of\n\tsaveFile = open(''exampleWrite.txt'',''w'')'

saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()
