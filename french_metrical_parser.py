import codecs, re, math

vowels = [u'a', u'e', u'i', u'o', u'u', u'y', u'A', u'E', u'I', u'O', u'U', u'Y', u'à', u'â', u'æ', u'è', u'é', u'ê', u'ë', u'î', u'ï', u'ô', u'ù', u'û',\
                  u'ü', u'ÿ', u'À', u'Â', u'Æ', u'È', u'É', u'Ê', u'Ë', u'Î', u'Ï', u'Ô', u'Ù', u'Û', u'Ü', u'Ÿ']

vowel_combinations_2 = [u'ai', u'au', u'ou', u'oi', u'eu', u'ae', u'oe', u'ue', u'ei', u'ui', u'ye', u'ie']
vowel_combinations_3 = [u'eau', u'oui', u'eui']

v = codecs.open ('verbs.csv', 'r', 'utf-8')
verbs = []
for line_verbs in v:
    verbs += line_verbs.split(';')
v.close()
for verb in verbs:
    verb = verb.strip('\n')

def count_syllables(line, vowels, vowel_combinations_2, vowel_combinations_3):
    words = []
    words = line.split()

    stripped_words = []
    for word in words:
        word_s = word.strip('.,!?;:()*"')
        stripped_words.append(word_s)

    syllables_in_line = 0
    for i in range (0, len(stripped_words)):
        syllables_in_word = 0
            
        if len(stripped_words) > 1:
            if i != len(stripped_words)-1:
                if len(stripped_words[i]) > 1 and len(stripped_words[i+1]) > 1: # случай encore ignore
                    h_done = 'no'
                    v_done = 'no'
                    if len(stripped_words[i+1]) >= 4:
                        if stripped_words[i][-1] == u'e' and words[i+1][0] == u'h' and words[i+1][1] + words[i+1][2] + words[i+1][3] in vowel_combinations_3:
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][4:]
                            h_done = 'yes'
                        
                    if len(stripped_words[i+1]) >= 3:
                        if stripped_words[i][-1] == u'e' and words[i+1][0] == u'h' and words[i+1][1] + words[i+1][2] in vowel_combinations_2 and h_done == 'no':
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][3:]
                            h_done = 'yes'
                        elif stripped_words[i][-1] == u'e' and words[i+1][0] + words[i+1][1] + words[i+1][2] in vowel_combinations_3:
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][3:]
                            v_done = 'yes'
                        
                    if len(stripped_words[i+1]) >= 2:
                        if stripped_words[i][-1] == u'e' and words[i+1][0] == u'h' and words[i+1][1] in vowels and h_done == 'no':
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][2:]
                        elif stripped_words[i][-1] == u'e' and words[i+1][0] + words[i+1][1] in vowel_combinations_2 and v_done == 'no':
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][2:]
                            v_done = 'yes'
                        elif stripped_words[i][-1] == u'e' and words[i+1][0] in vowels and v_done == 'no':
                            syllables_in_word += 1
                            stripped_words[i] = stripped_words[i][:-1]
                            stripped_words[i+1] = stripped_words[i+1][1:]
                    
                elif len(stripped_words[i]) > 1 and stripped_words[i][-2] + stripped_words[i][-1] not in vowel_combinations_2 and len(stripped_words[i+1]) == 1: # случай foudre a
                    if stripped_words[i][-1] == u'e':
                        syllables_in_word += 1
                        stripped_words[i] = stripped_words[i][:-1]
                        stripped_words[i+1] = u''

                elif len(stripped_words[i]) == 1 and len(stripped_words[i+1]) == 1: # случай il y a
                    syllables_in_word += 1
                    stripped_words[i] = u''
                    stripped_words[i+1] = u''
                
        combination_search = re.findall(u'((?:ai)|(?:Ai)|(?:e?au)|(?:Eau)|(?:Au)|(?:oui?)|(?:Oui?)|(?:eo)|(?:Eo)|(?:oie?)|(?:Oie?)|(?:eui?)|(?:Eui?)|(?:ae)|(?:Ae)|(?:oei?)|(?:Oei?)|(?:ue)|(?:Ue)|(?:ei)|(?:Ei)|(?:ui)|(?:Ui)|(?:ée$)|(?:yeu?)|(?:Yeu?)|(?:es$)|(?:ie)|(?:Ie))', stripped_words[i])
        word_stripped = re.sub(u'(ai)', u'', stripped_words[i], flags = re.U)
        word_stripped = re.sub(u'(Ai)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(e?au)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Eau)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Au)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(oui?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Oui?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(oie?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Oie?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(eo)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Eo)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(eui?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Eui?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ae)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Ae)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(oei?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Oei?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ue)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Ue)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ie)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Ie)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ei)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Ei)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ui)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Ui)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(ée)$', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(qu)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Qu)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(es)$', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(yeu?)', u'', word_stripped, flags = re.U)
        word_stripped = re.sub(u'(Yeu?)', u'', word_stripped, flags = re.U)
        if combination_search != None:
            for i in combination_search:
                syllables_in_word += 1

        vowels_search = re.findall(u'([aeiouyAEIOUYàâæèéêëîïôùûüÿÀÂÆÈÉÊËÎÏÔÙÛÜŸ]{1})', word_stripped)
        if vowels_search != None:
            for i in vowels_search:
                syllables_in_word += 1
        syllables_in_line += syllables_in_word   

    return syllables_in_line

def mf_rhyme(line, syllables, verbs):
    if syllables != 0:
        words = []
        words += line.split()
        stripped_last_word = words[-1].strip('.,!?;:()*"')
        f_rhyme_search = re.search(u'.+?[^àâæèéêëîïôùûüÿaouyi]es?$', stripped_last_word)
        if f_rhyme_search != None or stripped_last_word in verbs:
            return u'f'
        else:
            return u'm'
    else:
        return u'no rhyme'

def caesura_search(text, vowels):
    boundaries = []
    first_line_words = []
    first_line_words += text[0].split()
    first_line_sum = 0
    for i in range(0, len(first_line_words)):
        if i != len(first_line_words) - 1:
            first_line_words[i] = first_line_words[i].strip('.,!?;:()*"')
            if first_line_words[i][-1] != 'e':
                syll_in_word = count_syllables(first_line_words[i], vowels, vowel_combinations_2, vowel_combinations_3)
                first_line_sum += syll_in_word
                boundaries.append(first_line_sum)
            else:                
                if first_line_words[i+1][0] not in vowels and first_line_words[i+1][0] != 'h':
                    syll_in_word = count_syllables(first_line_words[i], vowels, vowel_combinations_2, vowel_combinations_3)
                    first_line_sum += syll_in_word
                    boundaries.append(first_line_sum)
                else:
                    syll_in_word = count_syllables(first_line_words[i], vowels, vowel_combinations_2, vowel_combinations_3)
                    syll_in_word -= 1
                    first_line_sum += syll_in_word
                    boundaries.append(first_line_sum)
        else:
            break
   
    for j in range (1, len(text)):
        other_boundaries = []
        line_words = []
        line_words += text[j].split()
        another_sum = 0
        for ii in range(0, len(line_words)):
            if ii != len(line_words) - 1:
                line_words[ii] = line_words[ii].strip('.,!?;:()*"')
                if line_words[ii][-1] != 'e':
                    syll_in_word = count_syllables(line_words[ii], vowels, vowel_combinations_2, vowel_combinations_3)
                    another_sum += syll_in_word
                    other_boundaries.append(another_sum)
                else:                
                    if line_words[ii+1][0] not in vowels and line_words[ii+1][0] != 'h':
                        syll_in_word = count_syllables(line_words[ii], vowels, vowel_combinations_2, vowel_combinations_3)
                        another_sum += syll_in_word
                        other_boundaries.append(another_sum)
                    else:
                        syll_in_word = count_syllables(line_words[ii], vowels, vowel_combinations_2, vowel_combinations_3)
                        syll_in_word -= 1
                        another_sum += syll_in_word
                        other_boundaries.append(another_sum)
            else:   
                break
        new_boundaries = []
        for iii in boundaries:
            if iii in other_boundaries:
                new_boundaries.append(iii)
            else:
                continue
        boundaries = new_boundaries

    if len(boundaries) == 0:
        return [u'no caesura']
    else:
        return boundaries


poem = raw_input(u"Введите имя файла (без расширения): ")
poem2 = poem + u'.txt'
f = codecs.open (poem2, 'r', 'utf-8')
lines = []
for l in f:
    lines.append(l)
f.close()

result = poem + u'.xml'
g = codecs.open(result, 'w', 'utf-8')

caes = caesura_search(lines, vowels)
caesura = u''
caesura_in_line = []

for ll in range(0, len(lines)):
    
    lines[ll] = lines[ll].strip(u'\r\n')

    syllables = count_syllables(lines[ll], vowels, vowel_combinations_2, vowel_combinations_3)
    
    if caes[0] != u'no caesura':
        other_caes = []
        if len(caes) == 1:
            main_caes = caes[0]
        else:
            new_caes = []
            for c in caes: 
                r = syllables - c
                if c <= 2 or r <= 2:
                    other_caes.append(c)
                else:
                    new_caes.append(c)

            caes = new_caes
            if len(caes) == 1:
                main_caes = caes[0]
            else:
                ceasura_choices = []
                for c2 in caes:
                    r2 = syllables - c2 - c2
                    r2 = math.fabs(r2)
                    ceasura_choices.append((c2, r2))
                minimum = 100
                finals = []
                for choice in range(0, len(ceasura_choices)):
                    while choice != len(ceasura_choices) - 1:
                        if ceasura_choices[choice][1] < ceasura_choices[choice+1][1] and ceasura_choices[choice][1] < minimum:
                            minimum = ceasura_choices[choice][1]
                        elif ceasura_choices[choice][1] > ceasura_choices[choice+1][1] and ceasura_choices[choice+1][1] < minimum:
                            minimum = ceasura_choices[choice+1][1]
                        if ceasura_choices[choice][1] == minimum:
                            finals.append(ceasura_choices[choice][0])
                main_caes = finals[0]
                for cc in caes:
                    if cc != main_caes:
                        other_caes.append(cc)
                  
        caes_place = 0 #место тэга <caes/>
        first_half_line = u''
        first_half_words = []
        second_half_line = u''
        w_words = []
        w_words += lines[ll].split()
        second_start_number = 0
        for w in range (0, len(w_words)):
            syll_in_w = count_syllables(w_words[w], vowels, vowel_combinations_2, vowel_combinations_3)
            if len(w_words) > 1:
                if w != len(w_words)-1:
                    this_word = w_words[w].strip('.,!?;:()*"')
                    if len(this_word) > 2 and len(w_words[w+1]) > 1:
                        w_h_done = 'no'
                        w_v_done = 'no'
                        if len(w_words[w+1]) >= 4:
                            if this_word[-1] == u'e' and w_words[w+1][0] == u'h' and w_words[w+1][1] + w_words[w+1][2] + w_words[w+1][3] in vowel_combinations_3:
                                syll_in_w -= 1
                                w_h_done = 'yes'                            

                        if len(w_words[w+1]) >= 3:
                            if this_word[-1] == u'e' and w_words[w+1][0] == u'h' and w_words[w+1][1] + w_words[w+1][2] in vowel_combinations_2 and w_h_done == 'no':
                                syll_in_w -= 1
                                w_h_done = 'yes'                    
                            elif this_word[-1] == u'e' and w_words[w+1][0] + w_words[w+1][1] + w_words[w+1][2] in vowel_combinations_3:
                                syll_in_w -= 1
                                w_v_done = 'yes'
                                
                        if len(w_words[w+1]) >= 2:
                            if this_word[-1] == u'e' and w_words[w+1][0] == u'h' and w_words[w+1][1] in vowels and w_h_done == 'no':
                                syll_in_w -= 1
                            elif this_word[-1] == u'e' and w_words[w+1][0] + w_words[w+1][1] in vowel_combinations_2 and w_v_done == 'no':
                                syll_in_w -= 1
                                w_v_done = 'yes'
                            elif this_word[-1] == u'e' and w_words[w+1][0] in vowels and w_v_done == 'no':
                                syll_in_w -= 1
                        
                    elif len(this_word) > 2 and this_word[-2] + this_word[-1] not in vowel_combinations_2 and len(w_words[w+1]) == 1:
                        if this_word[-1] == u'e':
                            syll_in_w -= 1

                    elif len(this_word) == 1 and len(w_words[w+1]) == 1: 
                        syll_in_w -= 1
            
            caes_place += syll_in_w
            first_half_line = first_half_line + w_words[w] + ' '
            first_half_words.append(w_words[w])
            if caes_place == main_caes:
                second_start_number = w + 1
                break     
        for ww in range(second_start_number, len(w_words)):
            second_half_line = second_half_line + w_words[ww] + ' '
        
        first_half_line_syllables = count_syllables(first_half_line, vowels, vowel_combinations_2, vowel_combinations_3)
        first_half_line_words = []
        first_half_line_words += first_half_line.split()
        last_word_stripped = first_half_line_words[-1].strip(u' ')
        e_search = re.search(u'.+?[^àâæèéêëîïôùûüÿaouyi]es?$', last_word_stripped)
        if e_search != None or last_word_stripped in verbs:
            first_half_line_syllables -= 1

        second_half_line_syllables = count_syllables(second_half_line, vowels, vowel_combinations_2, vowel_combinations_3)
        if ll == 0:
            min_second_syllables = second_half_line_syllables
        else:
            if second_half_line_syllables < min_second_syllables:
                min_second_syllables = second_half_line_syllables
        
        caesura = str(first_half_line_syllables) + u'+' + str(second_half_line_syllables)

        caesura_in_line.append((ll, first_half_line_syllables, second_half_line_syllables, first_half_line, second_half_line))


for ll in range(0, len(lines)):

    if caes[0] == u'no caesura':
        caesura = u'no caesura'
        write_line = lines[ll]
        syllables = count_syllables(lines[ll], vowels, vowel_combinations_2, vowel_combinations_3)
        
    else:
        for cl in caesura_in_line:
            if cl[0] == ll:
                syllables = cl[1] + cl[2]
                caesura = str(cl[1]) + u'+' + str(min_second_syllables)
                if min_second_syllables != cl[2]:
                    caesura += u'[' + str(cl[1]) + u'+' + str(cl[2]) + u']'
                if other_caes != []:
                    caesura += u'( '
                    for oc in other_caes:
                        sec = syllables - oc
                        caesura += str(oc) + u'+' + str(sec) + u' '
                    caesura += u' )'
                write_line = cl[3] + u'<caes/> ' + cl[4]

    rhyme = mf_rhyme(lines[ll], syllables, verbs)
            
    xml = u'<l id="' + str(ll+1) + u'" m="' + str(syllables) + u'" rh="' + rhyme + u'" caes ="' + caesura + u'"> ' + write_line + u'</l>\r\n'
    g.write(xml)
g.close()
