from django.core.files.uploadhandler import *
from django.core.files.uploadedfile import *


class myFileUploadHandler(TemporaryFileUploadHandler):
    def new_file(self, *args, **kwargs):
        super().new_file(*args, **kwargs)
        print('This is my FileUploadHandler')
        self.file = TemporaryUploadedFile(self.field_name,
                                          self.content_type,
                                          0,
                                          self.charset,
                                          self.content_type_extra)