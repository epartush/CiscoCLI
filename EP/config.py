
def load_config(path):
    attbr = {
            'HOSTNAME' : 'Router',
            }
    f = open(path,'r')
    for line in f.readlines():
#         for char in line:
#            if char == '%':
#                print "MFMF MF"
        words = line.split(' ')
        for word in words:
            if word[0] == '%':
               print word[1:]
               print attbr[word[1:]]
               #words[words.index(word)] = attbr[word[1:]]
               #print attbr['HOSTNAME']
        #print line + '\r'
        print ' '.join(words)

