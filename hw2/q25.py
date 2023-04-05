from q22 import wrapper_p_variance
from encrypter import Vigenere

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



plainText = """ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyincsfortyfourfortyisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaoneofseveralfederallawsthatbroadlycriminalizescomputerintrusioniehackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewtheuniversitysacceptableusepolicyconcerningproperuseofinformationtechnologyaswellasthestudentcodeasmembersofthe"""

keys = ["yz","xyz","wxyz","vwxyz","uvwxyz"]

encrypted_strings = []
for k in keys:
    encrypted_strings.append(Vigenere(plainText,k))

for k in keys:
    ee = Vigenere(plainText,k)
    print(len(ee))
    substrings = get_caeser_text(Vigenere(plainText,k), len(k))
    total = 0.0
    freq_variances = []
    for s in substrings:
        p= wrapper_p_variance(s)
        total += p
    pv = total/len(k)
    print(k,"{:.4E}".format(pv))
    print("===========================")
