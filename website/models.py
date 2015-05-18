from django.db import models
from django.conf import settings 
from image_cropping import ImageRatioField, ImageCropField
from taggit.managers import TaggableManager
# Create your models here.

class CategorieTe(models.Model):
    titolo = models.CharField("Titolo:", max_length=100)

    def __unicode__(self):
		return self.titolo
    class Meta:
        verbose_name_plural = "Categorie Te'"

class UnnostroTe(models.Model):
    nome = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(CategorieTe, null=True, blank=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    imgSfuso = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    imgContenitore = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    imgTazza = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    # per ora tempo/temperatura in numeri interi
    tempoInfusione_min = models.IntegerField(default=0)
    temperatura = models.IntegerField(default=0)
    prezzo_hg = models.IntegerField(default=0)
    croppingslider = ImageRatioField('imgSfuso', '500x469', verbose_name="Slider Revolution")
    cropping = ImageRatioField('imgSfuso', '500x469', verbose_name="Cropping")

    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Un nostro te'"
        ordering = ['id']

class AccessoriTe(models.Model):
    nome = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    immagine = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    prezzo= models.IntegerField(default=0)

    croppingminiatura = ImageRatioField('image', '500x469', verbose_name="Miniatura")
    croppingslider = ImageRatioField('image', '500x469', verbose_name="Slider Revolution")
    cropping = ImageRatioField('image', '500x469', verbose_name="Cropping")
    croppingfree = ImageRatioField('image', '500x469', verbose_name="Free Crop")

    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Accessori te'"
        ordering = ['id']


class ImmaginiLocale(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo: ")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	didascalia = models.TextField(null=True, blank=True)
	cropping = ImageRatioField('image', '500x480')
	slidepage = ImageRatioField('image', '870x480')
	croppingthumb = ImageRatioField('image', '600x450')
	croppingslide = ImageRatioField('image', '1140x487')
	croppingcarousel = ImageRatioField('image', '198x132')
	croppingrender = ImageRatioField('image', '1199x674')
	designthumb = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
	designbig = ImageRatioField('image', '1200x800', verbose_name="Design HD")
	designnews = ImageRatioField('image', '1200x1125', verbose_name="News")
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo
	class Meta:
		verbose_name_plural = "Immagini Locale"
        ordering = ['id']

class ImmaginiChiSiamo(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo: ")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	didascalia = models.TextField(null=True, blank=True)
	descrizione = models.TextField(null=True, blank=True, verbose_name="Descrizione")
	cropping = ImageRatioField('image', '500x480')
	slidepage = ImageRatioField('image', '870x480')
	croppingthumb = ImageRatioField('image', '600x450')
	croppingslide = ImageRatioField('image', '1140x487')
	croppingcarousel = ImageRatioField('image', '198x132')
	croppingrender = ImageRatioField('image', '1199x674')
	designthumb = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
	designbig = ImageRatioField('image', '1200x800', verbose_name="Design HD")
	designnews = ImageRatioField('image', '1200x1125', verbose_name="News")
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo
	class Meta:
		verbose_name_plural = "Immagini 'Chi Siamo' "
        ordering = ['id']



class Slider(models.Model):
	titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
	image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
	active = models.BooleanField(default=False)
	didascalia = models.TextField(null=True, blank=True)
	cropping = ImageRatioField('image', '1170x500')
	slidepage = ImageRatioField('image', '870x480')
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.titolo
        
	class Meta:
		verbose_name_plural = "Slider in Homepage"
        ordering = ['id']
