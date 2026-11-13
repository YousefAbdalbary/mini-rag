from enum import Enum

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXCEEDED = "File Size Exceeded"
    FILE_UPLOADED_SUCCESSFULLY = "File Uploaded Successfully"
    FILE_UPLOADED_FAILED = "File Uploaded Failed"
    