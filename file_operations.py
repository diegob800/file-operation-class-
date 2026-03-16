import os
import shutil


class File:
    def __init__(self,file_name:str,file_extension:str,create_now_or_not:bool):
        self.filename=file_name
        self.fileext=file_extension
        self.create_now_or_not=create_now_or_not


        if create_now_or_not == True:
            self.create()
            
        



    def create(self) -> None:
        with open(f"{self.file_name}.{self.file_extension}", "w") as my_file:
            my_file.write('')

    def write(self, content:str) -> None:
        with open(f"{self.file_name}.{self.file_extension}", "w", encoding='utf-8') as my_file:
            my_file.write(content)

    def read(self) -> str:
        with open(f"{self.file_name}.{self.file_extension}", "r", encoding="utf-8") as my_file:
            file_contents = my_file.read()
        return file_contents
    
    def delete(self) -> None:
        os.remove(f"{self.file_name}.{self.file_extension}")

    def rename(self,name:str,extension:str) -> None:
        os.rename(src=f'{self.file_name}.{self.file_extension}',dst=f'{name}.{extension}')

    def copy(self,path:str) -> None:
        shutil.copy(f'{self.file_name}.{self.file_extension}', path)