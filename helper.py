import os
from typing import Dict, List
from tqdm import tqdm


class Helper:

    @staticmethod
    def is_existing_path(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def is_hidden_file(file) -> bool:
        return file.startswith('.')

    @staticmethod
    def get_notation_with_k(number: int) -> str:
        if number >= 1000:
            number = number/1000
            return f"{number:.2f}K"
        else:
            return number

    @staticmethod
    def get_size_format(size: int, factor=1024) -> str:
        for unit in ["", "K", "M", "G", "T"]:
            if size < factor:
                return f"{size:.2f}{unit}B"
            size /= factor

    @staticmethod
    def write_in_file(filepath: str, data: Dict) -> str:
        with open(filepath, 'a') as file:
            for key, value in data.items():
                file.write(f"{key} : {value}\n")
            file.write("-------------------------------\n\n")
    
    @staticmethod
    def count_hidden_files(files: List[str]) -> int:
        counter: int = 0
        for file in files:
            if Helper.is_hidden_file(file):
                counter += 1
                
        return counter

    @staticmethod
    def get_file_size(file_path: str) -> int:
        size = 0
        if os.path.isfile(file_path):
            size =  os.path.getsize(file_path)

        return size if size is not None else 0
    
    @staticmethod
    def get_folder_size(path: str, files: List[str]) -> int:
        total_size: int = 0
        for file in tqdm(files, desc="crawling...", leave=False):
            file_path = os.path.join(path, file)
            total_size += Helper.get_file_size(file_path)

        return total_size