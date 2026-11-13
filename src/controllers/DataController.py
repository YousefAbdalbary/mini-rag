import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from Models import ResponseSignal
import re 
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        
    def validate_uploaded_file(self,file:UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size is None:
            return False, "Unable to determine file size"

        if file.size > self.app_settings.FILE_MAX_SIZE:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True ,ResponseSignal.FILE_UPLOADED_SUCCESSFULLY.value
    
    def generate_unique_filepath(self,orig_filename:str,project_id:str):
        
        random_key = self.generate_random_string()
        project_path =  ProjectController().get_project_path(project_id=project_id)
        cleaned_filename = self.cleaned_file_name(orig_filename)
        new_file_path = f"{project_path}/{random_key}_{cleaned_filename}"
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                f"{random_key}_{cleaned_filename}")
        return new_file_path , f"{random_key}_{cleaned_filename}"

    def cleaned_file_name(self,filename:str):
        cleaned_filename = filename.strip()
        cleaned_filename = re.sub(r'\s+', '_', cleaned_filename)
        cleaned_filename = re.sub(r'[^a-zA-Z0-9_.-]', '', cleaned_filename)
        
        return cleaned_filename
    