from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class BannerCarouselSlide(blocks.StructBlock):
    slide_header = blocks.CharBlock()
    slide_subheader = blocks.CharBlock()
    slide_image = ImageChooserBlock()

    def __str__(self):
        return self.slide_header
    

class BannerCarousel(blocks.StructBlock):
    """MAIN BANNER"""
    slides = blocks.ListBlock(BannerCarouselSlide())

    class Meta:
        help_text = "COMPONENT FOR RENDERING CAROUSEL"
        label_format = "Carousel Component"

    


    



class AboutUs(blocks.StructBlock):
    """About Us"""

    img1 = ImageChooserBlock()
    img2 = ImageChooserBlock(required=False)

    pre_header = blocks.CharBlock()
    main_header = blocks.CharBlock()
    body = blocks.TextBlock()
    page_redirect = PageChooserBlock(required=False)

    class Meta:
        help_text = "COMPONENT TO RENDER ABOUT US"
        label_format = "About Us Component"









class BlogSection(blocks.StructBlock):
    """This is for the blog Section"""
    
    pre_header = blocks.CharBlock(max_length=20)
    header = blocks.CharBlock(max_length=50)
    sub_header = blocks.CharBlock()

    class Meta:
        help_text = "COMPONENT TO RENDER BLOG CARDS (ONLY IF CHILD PAGE EXISTS)"
        label_format = "Blog Section Component"

