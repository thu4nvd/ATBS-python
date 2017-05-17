import shelve


#shelfFile = shelve.open('mydata')
sgekfFile = shelve.cats

cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
