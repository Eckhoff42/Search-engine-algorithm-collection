from InvertedIndex import InvertedIndex


class Compressor():
    def __init__(self) -> None:
        self.stop_list = ['er', 'og', 'i', 'et', 'en', 'ei', 'den', 'til', 'på',
                          'de', 'som', 'med', 'for', 'at', 'av', 'fra', 'har', 'om', 'å']

    def compress_inverted_index_stop_words(self, inverted_index: InvertedIndex) -> None:
        """
        Compresses the inverted index by removing stop words.
        These are common words that carry little meaning
        """
        del_terms = []
        for term in inverted_index.index.keys():
            if term in self.stop_list:
                del_terms.append(term)

        for term in del_terms:
            del inverted_index.index[term]

    def remove_stop_words(self, string: str):
        new_string = ""
        for term in string.split():
            if term not in self.stop_list:
                new_string += " " + term

        return new_string
