#敬語を常体に変換

#翻訳する文を形態素解析する関数
def mecab(task):
    tagger = MaCab.Tagger("-Ochasen")
    node = tagger.parseToNode(task)
    sentence = []
    genkei = []
    katuyo = []
    hinshi = []

    while node:
        word = node.surface
        wclass = node.feature.split(",")

        if not wclass[0]=="BOS/EOS":
            sentence.append(word)
            genkei.append(wclass[6])
            katuyo.append(wclass[5])
            hinshi.append(wclass[0])
        
        node = node.next

    return sentence,genkei,katuyo,hinshi

#単語を尊敬語または謙譲語に変換する関数

if sonkei==1:
    num = -1
    for a in genkei:
        num+=1
        if a in sonkeigo:
            katuyokei = katyyo[num]
            keigo = sonkeigo[a]
            hinsi = hinshi[num]

            result = henkan(keigo,hinsi,katuyokei,num,sentence)

            sentence[num] = result

if kenjo == 1:
    num = -1
    for a in genkei:
        if a in genkei:
            num+=1
            if a in kenjogo:
                katuyokei = katuyokei[num]
                keigo = kenjogo[a]
                hinsi = hinshi][num]
                
                result = henkan(keigo,hinsi,katuyokei,num,sentence)

                sentence[num] = result
semifinal = "".join(sentence)
#指定された活用形の動詞を検索する関数

def kensaku(part,word,form):
    if part == "動詞":
        file_name = "Verb.csv"
    elif part == "助動詞":
        file_name = "Auxil.csv"
    else :
        sys.exit()

    f = open(file_name,'r')
    dataReader = csv.reader(f)
    for row in dataReader:
        if word == row[10]:
            if form in row[9]:
                return row[0]