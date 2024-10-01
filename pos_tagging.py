#1ο ΜΕΡΟΣ
def tagged2lst():
    in_tagged_txt = """\n Ο|At νόμος|No της|At Ταυτότητας|No ,|PUNCT ο|At νόμος|No της|At
Αντίφασης|No ,|PUNCT ο|At νόμος|No της|At Αποκλίσεως|No του|At Τρίτου|Nm και|Cj
ο|At νόμος|No του|At Αποχρώντος|Aj Λόγου|No είναι|Vb οι|At τέσσερεις|Nm
θεμελιώδεις|Aj ΝΟΜΟΙ|No που|Pn περιγράφουν|Vb την|At τυπική|Aj λογική|No κατά|Pp
τον|At Αριστοτέλη|No .|PUNCT Λόγου|No ,|PUNCT Λόγου|No ,|PUNCT ΑριστοΤέλη|No
,|PUNCT Ταυτότητάς|No ,|PUNCT ΑντίφασΉς|No .|PUNCT"""

    # Διαχωρίζουμε το κείμενο σε λέξεις με βάση τα κενά
    words = in_tagged_txt.split()
    result = []
    for word in words:
        # Αγνοούμε τα στοιχεία που δεν περιέχουν το σύμβολο |
        if '|' in word:
            token, tag = word.split('|')
            # Αγνοούμε τα στοιχεία με tag PUNCT
            if tag != 'PUNCT':
                result.append((token, tag))

    wordscount = len(result)
    return result, wordscount

# Κλήση της συνάρτησης
result_list, total_count = tagged2lst()
print()
print("Λίστα:", result_list)
print()
print("Πλήθος λέξεων:", total_count)

#2ο ΜΕΡΟΣ
def handle_2ndaccent_case(word):
    # Δημιουργία ενός λεξικού με τους τονισμένους ελληνικούς χαρακτήρες και τους αντίστοιχους άτονους ως τιμές
    accented_to_unaccented = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ό': 'ο', 'ύ': 'υ', 'ώ': 'ω',
                              'Ά': 'Α', 'Έ': 'Ε', 'Ή': 'Η', 'Ί': 'Ι', 'Ό': 'Ο', 'Ύ': 'Υ', 'Ώ': 'Ω'}

    # Ελέγχει αν όλοι οι χαρακτήρες είναι κεφαλαίοι ή το μήκος της λέξης είναι μικρότερο από 2
    if word.isupper() or len(word) < 2:
        return word

    # Μετατρέπει σε μικρά γράμματα το μέρος της λέξης από τον δεύτερο χαρακτήρα και μετά
    word = word[0] + word[1:].lower()

    # Εύρεση τονισμένων χαρακτήρων με List Comprehension
    accented_chars = [char for char in word if char in accented_to_unaccented]

    # Αντικαθιστά τον τελευταίο τονισμένο χαρακτήρα με την άτονη εκδοχή του, μόνο αν υπάρχουν δύο τονισμένοι χαρακτήρες
    if len(accented_chars) == 2:
        # Βρίσκει τον δείκτη του τελευταίου τονισμένου χαρακτήρα ψάχνοντας από το τέλος προς την αρχή
        last_accented_index = word.rfind(accented_chars[-1])
        # Αντικαθιστά τον τελευταίο τονισμένο χαρακτήρα με την άτονη μορφή του
        word = (word[:last_accented_index] +
                # Ανατρέχει στο λεξικό accented_to_unaccented για να βρει την άτονη εκδοχή του τελευταίου τονισμένου χαρακτήρα
                accented_to_unaccented[word[last_accented_index]] +
                word[last_accented_index + 1:])

    return word

# Έλεγχος της συνάρτησης με διάφορες λέξεις
example_words = ['ΕυτυχΊΑΣ', 'διΆθΕΣΗ', 'κΆποΤΕ','ο', 'ΆΝΘΡΩΠΟΣ', 'ΌρΑΜΆ', 'ΚΊνησΉ', 'Άβολος']
processed_words = [handle_2ndaccent_case(word) for word in example_words]
print()
print()
print(processed_words)

#3ο ΜΕΡΟΣ
# Ορισμός της συνάρτησης get_pos_stats
def get_pos_stats(pos_type, sort_POS_tokens_by_freq_only=True):

    # Δημιουργία νέας λίστας και αγνόηση της δεύτερης τιμής (πλήθος των καθαρών λέξεων)
    tagged_list, _ = tagged2lst()

    # Δημιουργία νέας λίστας με List Comprehension και εφαρμογή της συνάρτησης handle_2ndaccent_case μόνο στα tokens
    processed_tagged_list = [(handle_2ndaccent_case(token), tag) for token, tag in tagged_list]

    # Φιλτράρισμα των λέξεων που αντιστοιχούν στο δοσμένο μέρος του λόγου (pos_type)
    pos_words = [word for word, tag in processed_tagged_list if tag == pos_type]

    # Υπολογισμός του πλήθους των λέξεων του δοσμένου μέρους του λόγου
    pos_type_count = len(pos_words)

    # Υπολογισμός του ποσοστού των λέξεων του δοσμένου μέρους του λόγου με ακρίβεια 2 δεκαδικών ψηφίων
    pos_type_freq = round((pos_type_count / total_count) * 100, 2)

    # Καταμέτρηση της συχνότητας εμφάνισης κάθε λέξης του δοσμένου μέρους του λόγου
    pos_word_count = {}
    for word in pos_words:
        pos_word_count[word] = pos_word_count.get(word, 0) + 1

    # Δημιουργία λεξικού κατά σειρά φθίνουσας συχνότητας εμφάνισης των λέξεων
    pos_word_count_dict_sorted_by_freq = dict(sorted(pos_word_count.items(), key=lambda item: item[1], reverse=True))

    # Επιπλέον δημιουργία λεξικού με αλφαβητική ταξινόμηση μόνο σε περίπτωση που ζητηθεί
    if not sort_POS_tokens_by_freq_only:
        pos_word_count_dict_sorted_alphabetically = dict(
            sorted(pos_word_count.items(), key=lambda item: item[0].lower()))
        return pos_type_count, pos_type_freq, pos_word_count_dict_sorted_by_freq, pos_word_count_dict_sorted_alphabetically

    return pos_type_count, pos_type_freq, pos_word_count_dict_sorted_by_freq


# Εκτέλεση της συνάρτησης με παράδειγμα χρήσης για τα ουσιαστικά και επιστροφή των αποτελεσμάτων
example_pos_type = 'No'
example_results = get_pos_stats(example_pos_type, sort_POS_tokens_by_freq_only=True)
example_results_2nd = get_pos_stats(example_pos_type, sort_POS_tokens_by_freq_only=False)

print()
print()
print(example_results)
print()
print(example_results_2nd)

#4ο ΜΕΡΟΣ
#Ουσιαστικά
noun_stats = get_pos_stats('No', sort_POS_tokens_by_freq_only=True)
noun_stats_2nd = get_pos_stats('No', sort_POS_tokens_by_freq_only=False)
print()
print()
print("=====Part of Speech selected: Noun =============================== START OF REPORT ============================")
print("Nouns found:", noun_stats[0])
print("Percentage of Nouns in cleaned words:", noun_stats[1], "%")
print("Nouns found sorted by occurrence frequency:", noun_stats[2])
print("Nouns found sorted alphabetically (case-insensitive sort):", noun_stats_2nd[3])
print("=====Part of Speech selected: Noun =============================== END OF REPORT ==============================")

#Άρθρα
article_stats = get_pos_stats('At', sort_POS_tokens_by_freq_only=True)
print()
print("=====Part of Speech selected: Article =============================== START OF REPORT ============================")
print("Articles found:", article_stats[0])
print("Percentage of Articles in cleaned words:", article_stats[1], "%")
print("Articles found sorted by occurrence frequency:", article_stats[2])
print("=====Part of Speech selected: Article =============================== END OF REPORT ==============================")







