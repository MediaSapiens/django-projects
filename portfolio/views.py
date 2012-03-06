from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from annoying.decorators import render_to

from portfolio.models import Gallery, Image


@render_to('index.html')
def gallery(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    image = Image.objects.filter(gallery=gallery)
    galleries = Gallery.objects.all()
    return {'galleries': galleries,
            'images': image}


def main(request):
    return gallery(request, 1)


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        upload = request.FILES['Filedata']
        try:
            dest = open('media/images/' + upload.name, "wb+")
            for block in upload.chunks():
                dest.write(block)
                dest.close()
        except IOError:
            pass # ignore failed uploads for now

        gallery_id = int(request.POST['folder'].split('/')[-2])
        gallery = Gallery.objects.get(id=gallery_id)
        Image.objects.create(name=upload.name.split('.')[0],
                             image='images/' + upload.name,
                             gallery=gallery)

    response = HttpResponse()
    response.write("%s\r\n" % upload.name)
    return response
