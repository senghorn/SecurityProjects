from q22 import wrapper_p_variance

def get_caeser_text( text, length):
    characters = [char for char in text];
    all_sub = []
    for i in range(length):
        sub = ""
        for i in range(i,len(text),length):
            c = characters[i]
            sub+=c
        all_sub.append(sub)
    return all_sub

from encrypter import Vigenere

plainText = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot
hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt
ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolate
thelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev
enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpuls
ioncivilfinesandjailtimeourpolicyincsfortyfourfortyisthatyoumustrespec
ttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecour
seactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomput
erfraudandabuseactcfaaoneofseveralfederallawsthatbroadlycriminalizesco
mputerintrusioniehackingunderstandwhatthelawprohibitsifindoubtwecanref
eryoutoanattorneypleasereviewtheuniversitysacceptableusepolicyconcerni
ngproperuseofinformationtechnologyaswellasthestudentcodeasmembersofthe"""

keys = ["yz","xyz","wxyz","vwxyz","uvwxyz"]

encrypted_strings = []
for k in keys:
    encrypted_strings.append(Vigenere(plainText,k))

i = 0
for e in encrypted_strings:
    ## Get substrings of key positions
    substrings = get_caeser_text(e,len(keys[i]))
    total = 0.0
    freq_variances = []
    for s in substrings:
        print(s)
        p= wrapper_p_variance(s)
        freq_variances.append(p)
        total += p
  
    print(keys[i],float(p/len(keys[i])))
    print("=====================")
    print("\n")
    i+=1 ## Different key length
