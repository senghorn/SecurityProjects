from q1 import frequency_analysis
from population_variance import p_variance

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
ngproperuseofinformationtechnologyaswellasthestudentcodeasmembersofthe""".upper()

def divide_frequency(frequency, divisor):
    total =0
    for s in frequency:
        frequency[s] = frequency[s]*1.0 / divisor
        total += frequency[s]
    
    
def wrapper_p_variance(plain):    
    plain = plain.replace('\n', '') ## Removes unnecessary new lines
    length = len(plain)
    freq = frequency_analysis(plain,1)
    divide_frequency(freq,length)
    chars = freq.keys()
    result = p_variance(freq,chars)
    return result

## print("{:.4E}".format(wrapper_p_variance(plainText))) ## Prints value of 2.2
