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
