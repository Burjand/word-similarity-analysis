stopwords = []

for i in range(3):

    file = open(f"stopwords{i+1}.txt","r", encoding="UTF-8")
    raw_file = file.readlines()
    file.close()

    for line in raw_file:

        stopwords.append(line)

stopwords = sorted(list(set(tuple(stopwords))))[1:]



file = open("stopwords_es.txt","w+",encoding="UTF-8")
file.writelines(stopwords)
file.close()