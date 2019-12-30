
# -*- coding: utf-8 -*-
import monpa
import jieba
import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('jieba_dict/dict.txt.big')

    # load stopwords set
    stopword_set = set()
    with open('jieba_dict/stopwords.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))
    
    output = open('output.txt', 'w', encoding='utf-8')
    with open('input.txt', 'r', encoding='utf-8') as content :
        for texts_num, line in enumerate(content):

            #line = line.strip('\n')
            #line = line.replace(' ','')
            seg = []
            for item in line.split("，"):
                if item != "\n":
                    seg.extend(monpa.cut(str(item+"，")))
            
            for word in seg[:-1]:
               
                output.write(word + ' ')
            #output.write(line +'\n')
    output.close()
    

if __name__ == '__main__':
    main()