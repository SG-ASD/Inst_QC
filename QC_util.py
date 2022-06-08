import os


class Util:
    # 파일 upload 기능
    def upload_files(self, FILES_getlist, path, files_name):
        """
        FILES_getlist : upload 할 파일 리스트(요소 : <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>)
        path : 파일 upload 경로
        files_name : 파일명
        """
        os.makedirs(path, exist_ok=True)  # 디렉토리 생성
        file_list = []

        for idx, f in enumerate(FILES_getlist):
            extension = f.name.split('.')[-1]  # 파일 확장자
            f.name = f"{files_name}_{idx + 1}.{extension}"  # 파일명 설정
            tmp = open(os.path.join(path, f.name), 'wb+')  # 디렉토리에 파일 생성
            file_list.append(f.name)

            for chunk in f.chunks():
                tmp.write(chunk)  # 파일 write

        file_name = ', '.join(file_list)  # 리스트를 문자열로 변환
        file_name = path + '\\' + file_name

        return file_name  # 경로 + 파일명 리턴
