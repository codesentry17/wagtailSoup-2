from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


"""MAIN BANNER"""
class BannerCarouselSlide(blocks.StructBlock):
    slide_header = blocks.CharBlock()
    slide_subheader = blocks.CharBlock()
    slide_image = ImageChooserBlock()
    page_redirect = PageChooserBlock(required=False)

    def __str__(self):
        return self.slide_header
    

class BannerCarousel(blocks.StructBlock):
    purpose = blocks.CharBlock(default = "Main Page Banner")
    slides = blocks.ListBlock(BannerCarouselSlide())




    



"""About Us"""
class AboutUs(blocks.StructBlock):
    purpose = blocks.CharBlock(default = "About Us")

    img1 = ImageChooserBlock()
    img2 = ImageChooserBlock(required=False)

    pre_header = blocks.CharBlock()
    main_header = blocks.CharBlock()
    body = blocks.TextBlock()
    page_redirect = PageChooserBlock(required=False)






