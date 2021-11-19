from typing import Dict, Any, List

from task1 import get_words_by_label, generate_ngrams
from utils import import_dataset, OUTPUT_PATH_TASK3, DATA_PATH, TRAIN_FILE_NAME, EXTENSION, INITIAL_COLUMNS, \
    apply_transform_functions


def data_pre_processing(words_dict: Dict[Any, List]) -> Dict[Any, List]:
    for label in words_dict.keys():
        words_dict[label] = list(map(lambda word: apply_transform_functions(word), words_dict[label]))

    return words_dict


if __name__ == "__main__":
    training_dataset = import_dataset(f'{DATA_PATH}{TRAIN_FILE_NAME}{EXTENSION}',
                                      INITIAL_COLUMNS)  # import file train.txt
    label_words_dict = get_words_by_label(training_dataset)
    label_words_dict = data_pre_processing(label_words_dict)
    generate_ngrams(label_words_dict, 1, OUTPUT_PATH_TASK3)
    generate_ngrams(label_words_dict, 2, OUTPUT_PATH_TASK3)