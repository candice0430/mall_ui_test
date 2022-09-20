import os


class FileHandle:

    @staticmethod
    def base_path():
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @staticmethod
    def settings_path():
        return os.path.join(FileHandle.base_path(),'config','settings.ini')

    @staticmethod
    def absolute_path(file_path,file_name):
        return os.path.join(FileHandle.base_path(),'testdatas',file_name)


# file_handle = FileHandle()

