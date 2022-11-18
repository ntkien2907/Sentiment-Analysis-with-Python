HOST = '192.168.1.10'
PORT = 5000

TRAINED_MODEL_DIR = 'output'
ABBREVIATIONS_CSV = 'vietnamese_slang-abbreviation.csv'

AUGMENT = ''                    ### '', 'upsampling', 'downsampling'
NN_ARCHITECTURE = 'lstm-cnn'    ### 'cnn', 'lstm-cnn'

##########################################################################

WORD2ID_PKL = f'{TRAINED_MODEL_DIR}/word2id.pkl'
W2V_MODEL   = f'{TRAINED_MODEL_DIR}/word2vec.model'
CLS_MODEL   = f'{TRAINED_MODEL_DIR}/{AUGMENT}sa_{NN_ARCHITECTURE}_model.h5'

EMBEDDING_SIZE  = 128
SEQUENCE_LENGTH = 200

LABELS = {0: 'Neutral', 1: 'Positive', 2: 'Negative'}