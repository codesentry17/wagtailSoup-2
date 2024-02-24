from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class Section(blocks.StructBlock):
    """Para Block"""
    header = blocks.CharBlock()

    image = ImageChooserBlock(required=False, help_text="image for the paragraph")
    image_position = blocks.ChoiceBlock(
        [
            ("L", "Left Aligned"),
            ("R", "Right Aligned"),
        ],
        required=False,
        help_text="Image position (default Center)",
        
    )

    body = blocks.RichTextBlock()

    class Meta:
        help_text = "CREATING SECTIONS IN THIS BLOG POST"
        label_format = "Section"




