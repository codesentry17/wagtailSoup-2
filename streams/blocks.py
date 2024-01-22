from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class BannerCarouselSlide(blocks.StructBlock):
    slide_header = blocks.CharBlock()
    slide_subheader = blocks.CharBlock()
    slide_image = ImageChooserBlock()
    page_redirect = PageChooserBlock(required=False)

    def __str__(self):
        return self.slide_header
    

class BannerCarousel(blocks.StructBlock):
    """MAIN BANNER"""
    purpose = blocks.CharBlock(default = "Main Page Banner", help_text="This field describes what this component does. Best left untouched")
    slides = blocks.ListBlock(BannerCarouselSlide())




    



class AboutUs(blocks.StructBlock):
    """About Us"""
    purpose = blocks.CharBlock(default = "About Us", help_text="This field describes what this component does. Best left untouched")

    img1 = ImageChooserBlock()
    img2 = ImageChooserBlock(required=False)

    pre_header = blocks.CharBlock()
    main_header = blocks.CharBlock()
    body = blocks.TextBlock()
    page_redirect = PageChooserBlock(required=False)









class BlogSection(blocks.StructBlock):
    """This is for the blog Section"""
    
    purpose = blocks.CharBlock(default = "Section for Blog cards")
    pre_header = blocks.CharBlock(max_length=20)
    header = blocks.CharBlock(max_length=50)
    sub_header = blocks.CharBlock()



