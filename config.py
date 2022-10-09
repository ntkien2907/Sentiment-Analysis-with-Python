HOST = '192.168.1.5'
PORT = 5000

TRAINED_MODEL_DIR = 'output'
ABBREVIATIONS_CSV = 'vietnamese_slang-abbreviation.csv'

######################################################################

W2V_MODEL = f'{TRAINED_MODEL_DIR}/word2vec.model'
CLS_MODEL = f'{TRAINED_MODEL_DIR}/sa_cnn_model.h5'

SEQUENCE_LENGTH = 200
EMBEDDING_SIZE  = 128

LABELS = {0: 'Neutral', 1: 'Positive', 2: 'Negative'}