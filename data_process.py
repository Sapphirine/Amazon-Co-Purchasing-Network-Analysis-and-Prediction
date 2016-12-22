from random import randint
import fileinput

amazon_file = fileinput.FileInput('amazon-meta.txt')
dicts = {}

var = 0
xx=0
for line in amazon_file:
    line = line.strip().split(':')
    if line[0] == 'ASIN':
        dicts[line[1].strip()] = {}
        var = line[1].strip()
        xx = xx+1
        print xx

    if line[0] == 'title':
        dicts[var]['title'] = line[1]
    if line[0] == 'categories':
        dicts[var]['categories'] = []
    if 'Books'in line[0] or 'Music' in line[0] or 'DVDs' in line[0] or 'Videos' in line[0]:
        dicts[var]['categories'].append(line[0])
    if line[0] == 'similar':
        item = line[1].strip().split()
        dicts[var]['similar'] = item[2:]
    if line[0] == 'reviews':
        dicts[var]['rating'] = line[-1].strip()


def title_similarity(pair_set, dicts):
    asin1 = pair_set[0]
    asin2 = pair_set[1]
    t1 = dicts[asin1]['title']
    t2 = dicts[asin2]['title']
    t1 = t1.split()
    t2 = t2.split()
    common = list(set(t1).intersection(t2))
    title_similarity = float(len(common))/(len(t1)+len(t2))
    return title_similarity



# pass string asin1, asin2, dicts as parameters
# return the categories relationship
def category_similarity(pair_set, dicts):
    asin1 = pair_set[0]
    asin2 = pair_set[1]
    cat1 = dicts[asin1]['categories']
    cat2 = dicts[asin2]['categories']
    common = list(set(cat1).intersection(cat2))
    return float(len(common)) / (len(cat1) + len(cat2))


#print category_similarity('id1', 'id2', a)
def rating_similarity1(pair_set, dicts):
    asin1 = pair_set[0]
    asin2 = pair_set[1]
    rat1 = dicts[asin1]['rating']
    rat2 = dicts[asin2]['rating']
    return (float(rat1) + float(rat2)) / 2

def rating_similarity2(pair_set, dicts):
    asin1 = pair_set[0]
    asin2 = pair_set[1]
    rat1 = float(dicts[asin1]['rating'])
    rat2 = float(dicts[asin2]['rating'])
    if (rat1 >= 2.5 and rat2 >= 2.5) or (rat1 <= 2.5 and rat2 <= 2.5):
        return 1
    else:
        return 0

#return all the similar and non-similar pairs of ASIN's
def all_pairs (dicts):
    similar_pair = []
    nonsimilar_pair = []
    list_asin = dicts.keys()

    for asin1 in dicts:
        if len(similar_pair) < 25500:
            try:
                similar = dicts[asin1]['similar']
                #print similar
                key_copy = list(list_asin)
                key_copy.remove(asin1)

                for asin2 in similar:
                    if asin2 in key_copy:
                        key_copy.remove(asin2)

                for asin2 in similar:
                    if asin2 in list_asin:
                        sim = {asin1, asin2}
                        nonsim = {asin1, key_copy[randint(0, len(key_copy)-1)]}
                        if sim not in similar_pair and nonsim not in nonsimilar_pair:
                            similar_pair.append(sim)
                            nonsimilar_pair.append(nonsim)
                            print "len: "+ str(len(similar_pair))

            except:
                1==1
        else:
            break
    return [similar_pair, nonsimilar_pair]

temp = all_pairs(dicts)
similar_pairs = temp[0]
nonsimilar_pairs = temp[1]

old100_no_title = open('old100_no_title.txt', 'w')
old100_no_cate = open('old100_no_cate.txt', 'w')
old100_no_rate = open('old100_no_rate.txt', 'w')
old100_complete = open('old100_complete.txt', 'w')

old200_no_title = open('old200_no_title.txt', 'w')
old200_no_cate = open('old200_no_cate.txt', 'w')
old200_no_rate = open('old200_no_rate.txt', 'w')
old200_complete = open('old200_complete.txt', 'w')

old500_no_title = open('old500_no_title.txt', 'w')
old500_no_cate = open('old500_no_cate.txt', 'w')
old500_no_rate = open('old500_no_rate.txt', 'w')
old500_complete = open('old500_complete.txt', 'w')

old1000_no_title = open('old1000_no_title.txt', 'w')
old1000_no_cate = open('old1000_no_cate.txt', 'w')
old1000_no_rate = open('old1000_no_rate.txt', 'w')
old1000_complete = open('old1000_complete.txt', 'w')

old10000_no_title = open('old10000_no_title.txt', 'w')
old10000_no_cate = open('old10000_no_cate.txt', 'w')
old10000_no_rate = open('old10000_no_rate.txt', 'w')
old10000_complete = open('old10000_complete.txt', 'w')

old25000_no_title = open('old25000_no_title.txt', 'w')
old25000_no_cate = open('old25000_no_cate.txt', 'w')
old25000_no_rate = open('old25000_no_rate.txt', 'w')
old25000_complete = open('old25000_complete.txt', 'w')

########################################################

new100_no_title = open('new100_no_title.txt', 'w')
new100_no_cate = open('new100_no_cate.txt', 'w')
new100_no_rate = open('new100_no_rate.txt', 'w')
new100_complete = open('new100_complete.txt', 'w')

new200_no_title = open('new200_no_title.txt', 'w')
new200_no_cate = open('new200_no_cate.txt', 'w')
new200_no_rate = open('new200_no_rate.txt', 'w')
new200_complete = open('new200_complete.txt', 'w')

new500_no_title = open('new500_no_title.txt', 'w')
new500_no_cate = open('new500_no_cate.txt', 'w')
new500_no_rate = open('new500_no_rate.txt', 'w')
new500_complete = open('new500_complete.txt', 'w')

new1000_no_title = open('new1000_no_title.txt', 'w')
new1000_no_cate = open('new1000_no_cate.txt', 'w')
new1000_no_rate = open('new1000_no_rate.txt', 'w')
new1000_complete = open('new1000_complete.txt', 'w')

new10000_no_title = open('new10000_no_title.txt', 'w')
new10000_no_cate = open('new10000_no_cate.txt', 'w')
new10000_no_rate = open('new10000_no_rate.txt', 'w')
new10000_complete = open('new10000_complete.txt', 'w')

new25000_no_title = open('new25000_no_title.txt', 'w')
new25000_no_cate = open('new25000_no_cate.txt', 'w')
new25000_no_rate = open('new25000_no_rate.txt', 'w')
new25000_complete = open('new25000_complete.txt', 'w')


row = ['', '1', '', '', '', '']

i = 0
for pair_sim in similar_pairs:
    try:
        pair1 = list(pair_sim)
        row[0] = str(pair1[0])+':'+str(pair1[1])+','
        row[2] = str(title_similarity(pair1, dicts))
        row[3] = str(category_similarity(pair1, dicts))
        row[4] = str(rating_similarity1(pair1, dicts))
        row[5] = str(rating_similarity2(pair1, dicts))

        old25000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
        old25000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
        old25000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
        old25000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
        new25000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
        new25000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
        new25000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
        new25000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
        if i < 10000:
            old10000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
            old10000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
            old10000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
            old10000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
            new10000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
            new10000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
            new10000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
            new10000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
            if i < 1000:
                old1000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                old1000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                old1000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                old1000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                new1000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                new1000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                new1000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                new1000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                if i < 500:
                    old500_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                    old500_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                    old500_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                    old500_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                    new500_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                    new500_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                    new500_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                    new500_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                    if i < 200:
                        old200_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                        old200_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                        old200_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                        old200_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                        new200_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                        new200_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                        new200_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                        new200_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                        if i < 100:
                            old100_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                            old100_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                            old100_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                            old100_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                            new100_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                            new100_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                            new100_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                            new100_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
        i += 1
        print "sim: "+str(i)
    except:
        1==1


row = ['', '0', '', '', '', '']
i = 0
for pair_non in nonsimilar_pairs:
    try:
        pair2 = list(pair_non)
        row[0] = str(pair2[0])+':'+str(pair2[1])+','
        row[2] = str(title_similarity(pair2, dicts))
        row[3] = str(category_similarity(pair2, dicts))
        row[4] = str(rating_similarity1(pair2, dicts))
        row[5] = str(rating_similarity2(pair2, dicts))

        old25000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
        old25000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
        old25000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
        old25000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
        new25000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
        new25000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
        new25000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
        new25000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
        if i < 10000:
            old10000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
            old10000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
            old10000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
            old10000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
            new10000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
            new10000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
            new10000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
            new10000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
            if i < 1000:
                old1000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                old1000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                old1000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                old1000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                new1000_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                new1000_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                new1000_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                new1000_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                if i < 500:
                    old500_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                    old500_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                    old500_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                    old500_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                    new500_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                    new500_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                    new500_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                    new500_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                    if i < 200:
                        old200_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                        old200_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                        old200_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                        old200_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                        new200_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                        new200_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                        new200_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                        new200_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
                        if i < 100:
                            old100_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[4]+'\n')
                            old100_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[4]+'\n')
                            old100_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                            old100_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+'\n')
                            new100_no_title.write(row[1]+' 1:'+row[3]+' 2:'+row[5]+'\n')
                            new100_no_cate.write(row[1]+' 1:'+row[2]+' 2:'+row[5]+'\n')
                            new100_no_rate.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+'\n')
                            new100_complete.write(row[1]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[5]+'\n')
        i += 1
        print "non_sim: " + str(i)
    except:
        1==1


old100_no_title.close()
old100_no_cate.close()
old100_no_rate.close()
old100_complete.close()

old200_no_title.close()
old200_no_cate.close()
old200_no_rate.close()
old200_complete.close()

old500_no_title.close()
old500_no_cate.close()
old500_no_rate.close()
old500_complete.close()

old1000_no_title.close()
old1000_no_cate.close()
old1000_no_rate.close()
old1000_complete.close()

old10000_no_title.close()
old10000_no_cate.close()
old10000_no_rate.close()
old10000_complete.close()

old25000_no_title.close()
old25000_no_cate.close()
old25000_no_rate.close()
old25000_complete.close()

#############################

new100_no_title.close()
new100_no_cate.close()
new100_no_rate.close()
new100_complete.close()

new200_no_title.close()
new200_no_cate.close()
new200_no_rate.close()
new200_complete.close()

new500_no_title.close()
new500_no_cate.close()
new500_no_rate.close()
new500_complete.close()

new1000_no_title.close()
new1000_no_cate.close()
new1000_no_rate.close()
new1000_complete.close()

new10000_no_title.close()
new10000_no_cate.close()
new10000_no_rate.close()
new10000_complete.close()

new25000_no_title.close()
new25000_no_cate.close()
new25000_no_rate.close()
new25000_complete.close()
