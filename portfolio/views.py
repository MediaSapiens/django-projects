from annoying.decorators import render_to
from portfolio.models import Gallery, Image


@render_to('index.html')
def main(request):
    gallery = Gallery.objects.all()[0]
    image = Image.objects.filter(gallery=gallery)
    galleries = Gallery.objects.all()
    return {'galleries': galleries,
            'image': image}


@render_to('index.html')
def gallery(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    image = Image.objects.filter(gallery=gallery)
    galleries = Gallery.objects.all()
    return {'galleries': galleries,
            'image': image}
