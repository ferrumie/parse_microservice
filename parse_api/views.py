import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.settings import api_settings

# Create your views here.


payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


class ExcelAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request):
        file_path = request.data.get('file_path')
        if file_path:
            df = pd.read_excel(file_path, encoding='utf-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            return Response(final_data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'file path can not be empty'}, status=status.HTTP_404_NOT_FOUND)

        # excel = LinkUpload.objects.all()
        # serializer = LinkUploadSerializers(excel, many=True)
        # if serializer.is_valid():
        #     text = serializer.validated_data['link']
        #     for file in os.listdir(text):
        #         filename = os.fsdecode(file)
        #         try:
                    # filename.endswith('.xlsx' or '.xls')
                    # filename = os.path.join(text, filename)

        # file_path = request.POST.get('file_path')
        # print(file_path)
        # for file in os.listdir(file_path):
        #     filename = os.fsdecode(file)
        #     if filename.endswith('.xlsx' or '.xls'):
        #         file_name = os.path.join(file_path, filename)
        #
        #         df = pd.read_excel(file_name, encoding='utf-8')
        #         data = df.dropna(axis=0, how='any')
        #         data.columns = data.columns.map(lambda x: str(x))
        #         data.columns = data.columns.map(lambda x: x.replace('\n', ''))
        #         final_data = data.to_json(orient='records')

                # return Response(final_data, status=status.HTTP_200_OK)
                # return HttpResponse(final_data, content_type='text/plain')
            # else:
                #     return Response(FileExtensionValidator(['xlsx', 'xls']), status=status.HTTP_406_NOT_ACCEPTABLE)
