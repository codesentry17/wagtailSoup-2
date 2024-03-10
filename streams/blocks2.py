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





class Fact(blocks.StructBlock):
    """for individual facts"""
    number = blocks.IntegerBlock()
    fact = blocks.CharBlock(max_length=50)


class FactsBand(blocks.StructBlock):
    """for the whole band"""

    facts = blocks.ListBlock(Fact())

    class Meta:
        help_text = "COMPONENT FOR RENDERING FACT BAND"
        label_format = "Fact Band Component"
