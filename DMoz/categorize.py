from ttp import ttp
from ttp import utils
import json
import wikipedia
import extraction
import requests
from urllib import urlopen
import socket
from urlparse import urlparse
from ttp import utils
import re
from bs4 import BeautifulSoup, SoupStrainer
p = ttp.Parser()

level1=["Physical","Hardware", "Operations Control", "Management","Network","Application", "Access","Endpoint","Cloud Computing","Cyber","Attacks"]
stopwords= {'secondly': 1, 'all': 1, 'consider': 1, 'whoever': 1, 'results': 1, 'four': 1, 'edu': 1, 'go': 1, 'causes': 1, 'seemed': 1, 'whose': 1, 'certainly': 1, 'biol': 1, "when's": 1, 'itll': 1, 'ts': 1, 'to': 1, 'does': 1, 'those': 1, 'th': 1, 'under': 1, 'sorry': 1, 'sent': 1, 'insofar': 1, 'consequently': 1, 'outside': 1, 'far': 1, 'mg': 1, 'theyve': 1, 'every': 1, 'yourselves': 1, "we'll": 1, 'regardless': 1, 'did': 1, 'ref': 1, "they've": 1, 'hereafter': 1, 'try': 1, 'p': 1, 'havent': 1, 'shows': 1, 'noted': 1, "it'll": 1, "i'll": 1, 'the': 1, 'says': 1, "you'd": 1, 'past': 1, 'likely': 1, 'invention': 1, 'further': 1, 'even': 1, 'index': 1, 'what': 1, 'appear': 1, 'heres': 1, 'section': 1, 'brief': 1, 'above': 1, 'sup': 1, 'new': 1, 'poorly': 1, 'ever': 1, 'aint': 1, 'youd': 1, 'respectively': 1, 'never': 1, 'here': 1, 'let': 1, 'others': 1, "hadn't": 1, 'along': 1, 'promptly': 1, 'obtained': 1, 'my': 1, 'k': 1, 'allows': 1, "i'd": 1, 'resulting': 1, 'arent': 1, 'usually': 1, 'que': 1, "i'm": 1, 'changes': 1, 'thats': 1, 'hither': 1, 'via': 1, 'useful': 1, 'merely': 1, 'while': 1, 'put': 1, 'ninety': 1, 'viz': 1, 'ord': 1, 'readily': 1, 'everybody': 1, 'use': 1, 'from': 1, 'would': 1, 'contains': 1, 'two': 1, 'next': 1, 'few': 1, 'therefore': 1, 'taken': 1, 'themselves': 1, 'thru': 1, 'type': 1, 'tell': 1, 'more': 1, 'knows': 1, 'becomes': 1, 'hereby': 1, 'it': 1, 'everywhere': 1, 'particular': 1, 'known': 1, 'must': 1, 'me': 1, 'none': 1, 'wouldnt': 1, 'f': 1, 'this': 1, 'ml': 1, 'oh': 1, 'anywhere': 1, 'nine': 1, 'can': 1, 'mr': 1, 'following': 1, 'didnt': 1, 'example': 1, 'indicated': 1, 'give': 1, "didn't": 1, 'indicates': 1, 'weve': 1, 'something': 1, 'want': 1, 'arise': 1, 'information': 1, 'needs': 1, 'end': 1, 'rather': 1, 'ie': 1, 'six': 1, 'how': 1, 'instead': 1, 'shouldnt': 1, 'okay': 1, 'tried': 1, 'may': 1, 'overall': 1, 'after': 1, 'eighty': 1, 'different': 1, 'hereupon': 1, 'ff': 1, 'date': 1, 'such': 1, 'a': 1, 'third': 1, 'whenever': 1, 'maybe': 1, 'appreciate': 1, 'q': 1, 'ones': 1, 'so': 1, 'specifying': 1, 'allow': 1, 'keeps': 1, 'make': 1, "that's": 1, 'help': 1, "don't": 1, 'indeed': 1, 'itd': 1, 'werent': 1, 'mainly': 1, 'soon': 1, 'course': 1, 'isnt': 1, 'through': 1, 'looks': 1, 'still': 1, 'its': 1, 'before': 1, 'thank': 1, 'thence': 1, 'selves': 1, 'inward': 1, 'fix': 1, 'actually': 1, "he'd": 1, 'whether': 1, 'willing': 1, 'whole': 1, 'thanx': 1, 'ours': 1, 'might': 1, 'into': 1, "haven't": 1, 'then': 1, 'them': 1, 'someone': 1, 'somebody': 1, 'thereby': 1, 'auth': 1, "you've": 1, 'they': 1, 'not': 1, 'now': 1, 'nor': 1, 'nos': 1, 'wont': 1, 'several': 1, 'name': 1, 'always': 1, 'reasonably': 1, 'whither': 1, 'l': 1, 'sufficiently': 1, 'each': 1, 'found': 1, 'went': 1, "mustn't": 1, "isn't": 1, 'mean': 1, 'everyone': 1, 'significantly': 1, 'doing': 1, 'ed': 1, 'eg': 1, 'related': 1, 'owing': 1, "we'd": 1, 'substantially': 1, 'et': 1, 'beyond': 1, 'out': 1, 'shown': 1, 'furthermore': 1, 'since': 1, 'research': 1, 'looking': 1, 're': 1, 'seriously': 1, "shouldn't": 1, "they'll": 1, 'got': 1, 'forth': 1, 'thereupon': 1, 'howbeit': 1, "doesn't": 1, 'million': 1, 'given': 1, 'quite': 1, 'whereupon': 1, 'besides': 1, 'ask': 1, 'anyhow': 1, 'beginning': 1, 'g': 1, 'could': 1, 'hes': 1, 'tries': 1, 'keep': 1, 'caption': 1, 'ltd': 1, 'hence': 1, 'onto': 1, 'think': 1, 'first': 1, 'already': 1, 'dont': 1, 'omitted': 1, 'thereafter': 1, 'yourself': 1, 'done': 1, 'approximately': 1, 'another': 1, 'twas': 1, 'miss': 1, 'awfully': 1, 'anyone': 1, 'little': 1, 'necessarily': 1, 'similarly': 1, 'together': 1, 'accordingly': 1, 'least': 1, 'keep\tkeeps': 1, 'indicate': 1, 'too': 1, 'hundred': 1, 'really': 1, 'gives': 1, 'mostly': 1, 'that': 1, 'exactly': 1, 'took': 1, 'immediate': 1, 'part': 1, 'somewhat': 1, 'hadnt': 1, 'off': 1, 'believe': 1, 'herself': 1, 'than': 1, 'specify': 1, 'begins': 1, 'b': 1, 'unfortunately': 1, 'showed': 1, 'accordance': 1, 'rd': 1, 'gotten': 1, 'second': 1, 'youve': 1, 'i': 1, "what's": 1, 'r': 1, 'were': 1, 'toward': 1, 'anyways': 1, 'and': 1, 'ran': 1, 'beforehand': 1, 'say': 1, 'unlikely': 1, 'have': 1, 'need': 1, 'seen': 1, 'seem': 1, 'saw': 1, 'their': 1, 'relatively': 1, 'zero': 1, 'thoroughly': 1, 'latter': 1, "i've": 1, 'able': 1, 'aside': 1, 'thorough': 1, 'predominantly': 1, 'also': 1, 'take': 1, 'which': 1, 'begin': 1, 'added': 1, 'unless': 1, 'though': 1, 'any': 1, 'who': 1, "where's": 1, 'most': 1, 'eight': 1, 'amongst': 1, 'significant': 1, 'nothing': 1, 'why': 1, 'sub': 1, 'cause': 1, 'kg': 1, 'especially': 1, 'noone': 1, 'proud': 1, 'm': 1, 'km': 1, 'mrs': 1, 'giving': 1, "you'll": 1, 'regards': 1, 'normally': 1, 'came': 1, 'saying': 1, 'particularly': 1, 'show': 1, 'anyway': 1, 'ending': 1, 'fifth': 1, 'one': 1, 'behind': 1, 'should': 1, 'only': 1, 'going': 1, "here's": 1, 'announce': 1, 'over': 1, 'do': 1, 'his': 1, 'goes': 1, 'get': 1, 'between': 1, 'stop': 1, 'truly': 1, "they'd": 1, 'cannot': 1, 'hid': 1, 'nearly': 1, 'despite': 1, 'during': 1, 'him': 1, 'is': 1, 'regarding': 1, 'qv': 1, 'h': 1, 'twice': 1, 'she': 1, 'contain': 1, "won't": 1, 'where': 1, 'thanks': 1, 'ignored': 1, 'theirs': 1, 'up': 1, 'namely': 1, 'sec': 1, 'are': 1, 'best': 1, 'wonder': 1, 'said': 1, 'away': 1, 'currently': 1, 'please': 1, 'mug': 1, "there's": 1, 'various': 1, 'hopefully': 1, 'affecting': 1, 'probably': 1, 'neither': 1, 'youll': 1, 'across': 1, 'available': 1, 'we': 1, 'recently': 1, 'importance': 1, 'however': 1, 'no': 1, 'meantime': 1, 'come': 1, 'both': 1, 'c': 1, 'last': 1, 'many': 1, 'ill': 1, 'whereafter': 1, 'according': 1, 'against': 1, 'etc': 1, 's': 1, 'became': 1, 'com': 1, 'comes': 1, 'otherwise': 1, 'among': 1, 'liked': 1, 'co': 1, 'afterwards': 1, 'seems': 1, 'ca': 1, 'whatever': 1, 'hers': 1, 'cmon': 1, 'non': 1, "couldn't": 1, 'cs': 1, 'moreover': 1, 'throughout': 1, 'considering': 1, 'infobox': 1, 'pp': 1, "aren't": 1, 'described': 1, "it's": 1, 'three': 1, 'been': 1, 'whos': 1, 'wasnt': 1, 'much': 1, 'wherein': 1, 'certain': 1, 'hardly': 1, 'wants': 1, 'corresponding': 1, 'latterly': 1, 'concerning': 1, 'else': 1, 'former': 1, 'present': 1, 'myself': 1, 'novel': 1, 'look': 1, 'these': 1, 'means': 1, 'nd': 1, 'value': 1, 'n': 1, 'will': 1, 'near': 1, "wouldn't": 1, 'theres': 1, 'ive': 1, 'seven': 1, 'almost': 1, 'wherever': 1, 'refs': 1, 'thus': 1, 'herein': 1, 'cant': 1, 'vs': 1, 'im': 1, 'in': 1, 'affected': 1, 'alone': 1, 'id': 1, 'if': 1, 'containing': 1, 'anymore': 1, 'perhaps': 1, 'suggest': 1, 'nobody': 1, 'same': 1, 'clearly': 1, 'beside': 1, 'potentially': 1, 'gets': 1, "weren't": 1, 'used': 1, 'see': 1, 'somewhere': 1, 'upon': 1, 'effect': 1, 'uses': 1, 'theyll': 1, "he'll": 1, 'wheres': 1, 'recent': 1, 'kept': 1, 'whereby': 1, 'largely': 1, 'nevertheless': 1, 'makes': 1, 'youre': 1, 'well': 1, 'anybody': 1, 'obviously': 1, 'without': 1, "can't": 1, 'very': 1, 'meanwhile': 1, 'yours': 1, 'lest': 1, "she'll": 1, 'just': 1, 'less': 1, 'being': 1, 'downwards': 1, 'presumably': 1, 'greetings': 1, 'using': 1, 'followed': 1, 'yes': 1, 'tis': 1, 'yet': 1, 'unto': 1, 'like': 1, 'wed': 1, "we've": 1, 'had': 1, 'except': 1, 'sometimes': 1, 'lets': 1, 'other': 1, 'seeming': 1, 'has': 1, 'adj': 1, 'ought': 1, 'gave': 1, 'around': 1, "who's": 1, 'possible': 1, 'possibly': 1, 'five': 1, 'know': 1, 'immediately': 1, 'apart': 1, 'abst': 1, 'necessary': 1, 'd': 1, 'follows': 1, 'theyre': 1, 'either': 1, 'become': 1, 'page': 1, 'towards': 1, 'therein': 1, "why's": 1, 'shed': 1, 'because': 1, 'old': 1, 'often': 1, 'successfully': 1, 'some': 1, 'somehow': 1, 'self': 1, 'sure': 1, 'shes': 1, 'specified': 1, 'dear': 1, 'home': 1, 'ourselves': 1, "shan't": 1, 'happens': 1, 'for': 1, 'affects': 1, 'shall': 1, 'per': 1, 'everything': 1, 'asking': 1, 'provides': 1, 'tends': 1, 'be': 1, 'run': 1, 'sensible': 1, 'obtain': 1, 'nowhere': 1, 'although': 1, 'by': 1, 'on': 1, 'about': 1, 'ok': 1, 'anything': 1, 'getting': 1, 'of': 1, 'o': 1, 'ours\tourselves': 1, 'whence': 1, 'plus': 1, 'act': 1, 'slightly': 1, 'or': 1, 'seeing': 1, 'own': 1, 'whats': 1, 'formerly': 1, 'previously': 1, 'somethan': 1, 'image': 1, 'within': 1, 'due': 1, 'down': 1, 'appropriate': 1, 'doesnt': 1, 'primarily': 1, 'theyd': 1, 'couldnt': 1, 'quickly': 1, 'your': 1, "how's": 1, 'her': 1, 'whom': 1, 'aren': 1, 'apparently': 1, 'there': 1, 'specifically': 1, 'pages': 1, 'hed': 1, 'inasmuch': 1, 'inner': 1, 'way': 1, 'resulted': 1, 'was': 1, 'himself': 1, 'elsewhere': 1, 'enough': 1, 'becoming': 1, 'but': 1, 'back': 1, 'hi': 1, 'et-al': 1, 'line': 1, 'trying': 1, 'with': 1, 'he': 1, "they're": 1, 'made': 1, "wasn't": 1, 'wish': 1, 'j': 1, "hasn't": 1, 'us': 1, 'until': 1, 'placed': 1, 'below': 1, 'un': 1, 'similar': 1, 'ex': 1, 'strongly': 1, 'gone': 1, 'later': 1, 'associated': 1, 'ah': 1, 'am': 1, 'an': 1, 'images': 1, 'as': 1, 'sometime': 1, 'right': 1, 'at': 1, 'imagesize': 1, 'our': 1, 'inc': 1, 'again': 1, 'hasnt': 1, "'ll": 1, 'entirely': 1, 'nonetheless': 1, 'na': 1, 'whereas': 1, 'when': 1, 'lately': 1, 'definitely': 1, 'better': 1, 'you': 1, 'nay': 1, "you're": 1, 'showns': 1, 'briefly': 1, 'beginnings': 1, 'welcome': 1, "let's": 1, 'important': 1, 'serious': 1, 'e': 1, "he's": 1, "she'd": 1, 'having': 1, 'itself': 1, "we're": 1, "she's": 1, 'hello': 1, 'once': 1}

count=0
fla=0
f=open("dmozURLS",'r')
for category in level1:
    with open("TwitterURLScore"+category,"w") as f3:
        f3.write('')
with open("mixed","w") as f2:
    f2.write('')

for line in f:
    dic={}
    for category in level1:
        f=open("WikiLevel2Terms"+category,"r")
        k=f.readline()
        while k!='':
            try:
                dic[category].union(eval(f.readline()))
            except KeyError:
                dic[category]=eval(f.readline())
            k=f.readline()
    temp=line.split(',')
    url=temp[0].strip(' \n')
    tweet=' '.join(temp[1:])
    if url.strip()[-3:]=='pdf':
            continue
    try:
        html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'},timeout=6).text
    except:
        print "------------------PROBLEM---------------------"
        continue
    try:
        extracted = extraction.Extractor().extract(html, source_url=url)
    except:
        pass
    try:
        title=extracted.title
    except:
        title='+++'
    try:
        desc=extracted.description
    except:
        desc='+++'
    try:
        lastmod=str(urlopen(url).info().getdate('date'))
        lastmod=lastmod.replace(',',':') 
    except:
        lastmod='+++'
    try:
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    except:
        domain='+++'
    indom=0
    outdom=0
    suburls=[]
    soup=BeautifulSoup(html)
    for link in soup.find_all('a', href=True):
        try:
            import urlparse
            n=urlparse.urlparse(link['href']).netloc
        except:
            continue
        if domain in link['href'] or not bool(n):
            indom+=1
        else:
            outdom+=1

    size=len(html)
    try:
        alltext=title+' '
    except:
        alltext=''
    try:
        alltext+=desc+' '
    except:
        pass
    try:
        alltext+=tweet
    except:
        pass
    for ch in "{},();./\&@#*:?><|!":
        alltext=alltext.replace(ch,' ')
    alltext=''.join(x for x in alltext if (x.isalpha() or x==' '))
    pattern = re.compile(r"\s+")
    alltext = re.sub(pattern, " ", alltext)
    alltext=alltext.strip('\n ')
    textdict={}
    for i in alltext.split():
        if i not in stopwords:
            textdict[i.lower()]=1

    sc=0.0
    cat=""
    for category in level1:
        partscore=0.0
        try:
            terms=dic[category]
        except:
            continue
        for phrase in terms:
            for ch in "{},();./\&@#*:?><|!":
                phrase=phrase.replace(ch,' ')
            pattern = re.compile(r"\s+")
            phrase = re.sub(pattern, " ", phrase)
            for word in phrase.split():
                if word.lower() not in stopwords and word.lower() in textdict:
                    partscore+=1.0/len(phrase)
        if abs(partscore-sc)<0.1:
            with open("mixed","a") as f2:
                f2.write(url+","+cat+","+category+","+str(partscore)+","+str(sc)+"\n")
                print "%%%%%%%%%%%%%%%%%%%MIXED%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        if partscore>sc:
            sc=partscore
            cat=category


      

    print url+','+cat+','+str(partscore)+','+lastmod+','+domain+','+str(size)+','+alltext+','+str(indom)+','+str(outdom)+'\n'
    
    try:
        with open("TwitterURLScore"+cat,"a") as f3:
            f3.write(url+','+str(partscore)+','+lastmod+','+domain+','+str(size)+','+alltext+','+str(indom)+','+str(outdom)+'\n')
    except:
        continue
    count+=1
    print '##########',count






