s1 = "EDHMLQDZLZCSTYEDZDOSDRHEYECZECEOEPEPPNZCSPEPXOPYSOFXREYSLPRGZEVPFYESCZYOAASZSCLPFPGTOPRTPCQCDPPWSRTMPESYELESSYECCEYYXYRXTXPDTZLVZYZTHRYZWZCM"
s2 = "LXIERPEJPGIIBGLMVIVIEVMEWXILQIIGLMPHRIXSSESCSXXWEIRISFIYXHWIHWMVHGLESRXESSIJIPVJKWIWQXPVWILSFEHWIEEVHWMKLPEIMXIWILHGMWSIRXXYXHPIWXRSELFQHYIC"
s3= "FIBUEPDNPFXDUFFEHOFOZFMOUIUJFVSMFTZCXIIPWEJEOPSBUTOEPFPHFVBSFMCFFFBWOBNOTTBNZPPJSUNUVIFFTBJPFWVBNUNPVVTUFMMNTFSPBBWFOQGTWPPFUPESPFWOZQVQZUMX"
s4 = "MSFVTDOWQFWYMBHSSWGOWGZRYSIGBDWCRDUMVWSASWZSSXSMHKMVRTTGGRMHOSSRQGHSUGORGGACOCIFSVOOGSPUHYGATWRTGZVYRDPSZSYOJBKPQBSCRSVSWFHGSFROTFSGHWHHCCSO"
s5 = "AZENHONHWUPBOPRJXKOPJOJWQZNWPKJOKNNPKIXWDJAIUWAEDEYABKPQKAEDZXSPKPPPLDNYEAKJOGJOWAZGPSKWDKXPKJAPWAKAASKWKUOXEYWYPCJJKWENAADHZAKXPENDDLEHQBIH"
s6 = "SMFGATLCDKZGWKHLMJWAYAGYOMFHOFYAGGSOXASFALLSGUZFWXDOGJZJFKFMTGAZFZZZWWJSTKMWCAVLDQWWZJOJWFSAJYUWQSMFEAOEUSLGGGDZKWYZXCKNLDWGLVFSWFKSJWKQSQWL"
s7 = "BNQLZEYKQDKBFYBQCKCYKYDKKNCKROKXBWLYYXDNCRDXGUYQNOKKBOOSDBQCOGVOFOOOBSSXVCXIPXDDSRKKKYCNIODVODKBSCCDODVKKXYEVEDKGBOSDSDOXKSGRYXDXQKVYCZDBYXO"
s8 = "QMIMAGVBZWKAMVMMPLBVOVAQQMBZMVVOPXJUZBPAPMPLMQZBCJQAQWBVPCMBIALLQUGEAAMBGBBBWOPPHIUVDVSTJWPMTPTBVBMPMPQBTLBBMVMSQIIAMVQLIBAEMVGAMKBNCQZWMCBZ"
subset_array = [s1, s2, s3, s4, s5, s6, s7, s8]


## Decryption code
def shift_backward(text,key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = key
    shifted_text = ''
    for char in text:
        shifted_char_index = (alphabet.index(char) - shift) % 26
        shifted_text += alphabet[shifted_char_index]
    return shifted_text

## Vigenere Cipher Decryption
def vigenere_decrypt(text, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ''
    key_index = 0
    for char in text:
        shift = alphabet.index(key[key_index])
        decrypted_char_index = (alphabet.index(char) - shift) % 26
        decrypted_text += alphabet[decrypted_char_index]
        key_index = (key_index + 1) % len(key)
    return decrypted_text

string = "HELLO"
shift_by = ord('F') - ord('A')

## Counts frequency of characters and return it
def frequency_analysis(text):
    analysis = {}
    characters = [char for char in text];
    for i in range(0,len(text)):
        c = characters[i]
        if c in analysis:
            analysis[c] = analysis[c] + 1
        else:
            analysis[c] = 1
    return analysis

array = []
for s in subset_array:        
    distribution = frequency_analysis(s)
    sorted_distribution = sorted(distribution.items(), key=lambda x: x[1], reverse=True)
    top_3 = [i[0] for i in sorted_distribution[:3]]
    array.append(top_3)

## The resulting array contains the possible map of E(most frequent character in English)
print(array)

def get_shift_to_e(char):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = (alphabet.index(char) - alphabet.index('E')) % 26
    return alphabet[shift]

key = []
for a in array:
    a_arr = []
    for c in a:
        a_arr.append(get_shift_to_e(c))
    key.append(a_arr)

print(key)