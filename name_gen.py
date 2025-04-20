import random

word_structures = ["0f","01f","021f","0221f"]

allowed_type_0_vows = ["a","o","u","i"]

allowed_type_1_cons = ["b","d","st","sh","s","t","th","ch","l","f","g","k","p","j"]
allowed_type_1_aprs = ["","l","r"]
allowed_type_1_vows = ["a","o","u","ay","ee","i"]

allowed_type_2_cons = ["b","d","l","f","g","k"]
allowed_type_2_vows = ["a","i","o","u"]

allowed_type_f_cons = ["m","r","ng","b","rb","mb","g","lg","l","lb","lm","k","nk","ld","d","rsn"]
allowed_type_f_vows = ["is","us","er","in"]
limited_type_f_vows = ["is","us"]

class Syllable:
    def __init__(self, syl_type, syl_con, syl_vow):
        self.syl_type = syl_type
        self.syl_con = syl_con
        self.syl_vow = syl_vow

def get_type_1_syl(syls, vow):
    con = random.choice(allowed_type_1_cons)
    apr = random.choice(allowed_type_1_aprs)
    
    # Cluster of "ll" is forbidden.
    if(con.endswith("l") and apr=="l"):
        apr = ""

    return Syllable("1",con+apr,vow)

def get_type_2_syl(syls, vow):
    con = random.choice(allowed_type_2_cons)
    return Syllable("2",con,vow)

def get_type_f_syl(syls, vow):
    con = random.choice(allowed_type_f_cons)
    return Syllable("f",con,vow)

def get_kobold_name(english_word):

    random.seed(english_word)

    kobold_word = ""
    syl_0_vow = random.choice(allowed_type_0_vows,)
    syl_1_vow = random.choice(allowed_type_1_vows)
    syl_2_vow = random.choice(allowed_type_2_vows)
    syl_f_vow = random.choice(limited_type_f_vows) if (syl_1_vow.endswith("ee") or syl_1_vow.endswith("i")) else random.choice(allowed_type_f_vows)

    word_structure = random.choice(word_structures)
    syls = []

    for char in word_structure:
        syl =  get_type_1_syl(syls, syl_0_vow) if char == "0" else \
                get_type_1_syl(syls, syl_1_vow) if char == "1" else \
                get_type_2_syl(syls, syl_2_vow) if char == "2" else \
                get_type_f_syl(syls, syl_f_vow)
        syls.append(syl)
    
    for x in syls:
        kobold_word += x.syl_con + x.syl_vow
    return kobold_word