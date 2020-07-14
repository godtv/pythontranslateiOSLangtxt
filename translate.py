import googletrans
import time

translator = googletrans.Translator()

f = open('lang.txt','r')
filedata = f.readlines()

emptylist = []

for godindex,line in enumerate(filedata):
    split_list = line.split('=')   #format :[' "xxx" = "xxxx", .... '],convert to["xxx","xxx"]

    for index, item in enumerate(split_list):
        if index % 2 == 1:
            result = translator.translate(item, dest='ja').text
            #sleep 5 second, avoid Google translate api check
            time.sleep(5)
            item = ' = %s\n' % result
            split_list[index] = item
        emptylist.append(split_list[index])


with open('lang1.txt', 'w') as f2:
    for subitem in emptylist:
        print(subitem)
        f2.write("%s" % subitem)












