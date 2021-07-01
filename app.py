import os
import sys

from helper import Helper


class FileCrawler:
    files_count = 0
    folders_count = 0
    hidden_files_count = 0
    total_size = 0
    
    def start_crawling(self, path: str):
        if Helper.is_existing_path(path):
            self._crawl_path(path)
            self._resume_crawling_stats(path)
        else:
            raise FileNotFoundError('Ce chemin n\'existe pas')


    def _crawl_path(self, path: str):
        for path, dirs, files in os.walk(path):
            self.files_count += len(files)
            self.folders_count += len(dirs)
            self.hidden_files_count += Helper.count_hidden_files(files)
            self.total_size += Helper.get_folder_size(path, files)

        print('Crawling finished ! ✅ You can see stats in the 📝crawler-stats.txt file📝')


    def _resume_crawling_stats(self, path: str):
        stats = {
            "path": path,
            "Directories": Helper.get_notation_with_k(self.folders_count),
            "Files": Helper.get_notation_with_k(self.files_count),
            "Hidden files": Helper.get_notation_with_k(self.hidden_files_count),
            "total_size": Helper.get_size_format(self.total_size)
        }

        Helper.write_in_file('crawler-stats.txt', stats)


if __name__ == "__main__":
    #path = sys.argv[1]
    path = r"{Your_path}"
    crawl_process = FileCrawler()
    crawl_process.start_crawling(path)
