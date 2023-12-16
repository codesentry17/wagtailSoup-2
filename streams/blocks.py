from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class Carousel(blocks.StructBlock):
    banner_image = ImageChooserBlock()
    banner_header = blocks.CharBlock()
    banner_subheader = blocks.CharBlock(required=False)
    page_redirect = PageChooserBlock(required=False)

    def __str__(self) -> str:
        return self.banner_image.title