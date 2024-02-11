from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class Section(blocks.StructBlock):
    """Para Block"""
    header = blocks.CharBlock()

    image = ImageChooserBlock(required=False, help_text="image for the paragraph")
    iamge_position = blocks.ChoiceBlock(
        [
            ("C", "Full Central"),
            ("L", "Left Aligned"),
            ("R", "Right Aligned"),
        ],
        required=False,
        help_text="Tells where the image should be positioned"
    )

    body = blocks.RichTextBlock()

    class Meta:
        help_text = "CREATING SECTIONS IN THIS BLOG POST"
        label_format = "Section"




