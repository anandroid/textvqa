from pythia.utils.text_utils import generate_ngrams



TOKENS = ["this", "will", "be", "a", "test", "of", "tokens"]

n_grams = generate_ngrams(TOKENS, 2)

print(n_grams)