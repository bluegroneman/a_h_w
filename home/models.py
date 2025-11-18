from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    """Home page with hero section and feature cards"""

    hero_title = models.CharField(
        max_length=255,
        default="Almost Home Wyoming",
        help_text="Main hero title"
    )

    hero_subtitle = models.CharField(
        max_length=255,
        default="Homeless to Hopeful with just a little help",
        help_text="Hero subtitle/tagline"
    )

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Hero background image"
    )

    about_title = models.CharField(
        max_length=100,
        default="About us",
        help_text="About section title"
    )

    about_description = models.TextField(
        default="Learn more about our mission and story",
        help_text="About section description"
    )

    about_link_text = models.CharField(
        max_length=50,
        default="Read On",
        help_text="About section button text"
    )

    donate_title = models.CharField(
        max_length=100,
        default="Ways to Give",
        help_text="Donate section title"
    )

    donate_description = models.TextField(
        default="Lend a helping hand",
        help_text="Donate section description"
    )

    donate_link_text = models.CharField(
        max_length=50,
        default="Donate",
        help_text="Donate section button text"
    )

    contact_title = models.CharField(
        max_length=100,
        default="Reach out to us",
        help_text="Contact section title"
    )

    contact_description = models.TextField(
        default="Please reach out with any questions or concerns, we are here to help",
        help_text="Contact section description"
    )

    contact_link_text = models.CharField(
        max_length=50,
        default="Contact Us",
        help_text="Contact section button text"
    )

    body = RichTextField(
        blank=True,
        help_text="Place for embedded video content"
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_image'),
        FieldPanel('about_title'),
        FieldPanel('about_description'),
        FieldPanel('about_link_text'),
        FieldPanel('donate_title'),
        FieldPanel('donate_description'),
        FieldPanel('donate_link_text'),
        FieldPanel('contact_title'),
        FieldPanel('contact_description'),
        FieldPanel('contact_link_text'),
        FieldPanel('body'),
    ]

    max_count = 1

    def get_context(self, request):
        context = super().get_context(request)
        context['stories'] = StoryPage.objects.all()
        return context


class AboutPage(Page):
    """About page with mission statement and quotes"""

    heading = models.CharField(
        max_length=255,
        default="About our Organization",
        help_text="Main page heading"
    )

    subheading = models.CharField(
        max_length=255,
        default="People Helping People",
        help_text="Page subheading"
    )

    mission_heading = models.CharField(
        max_length=100,
        default="Our Mission",
        help_text="Mission section heading"
    )

    mission_statement = RichTextField(
        default="Almost Home Wyoming is a non-profit 501(c)3 in Lander, Wyoming, ran entirely by volunteer support. Our mission is to provide safe and secure housing for people who are homeless or facing homelessness.",
        help_text="Organization mission statement"
    )

    contact_email = models.EmailField(
        default="[email protected]",
        help_text="Contact email for applications"
    )

    quote_1 = models.TextField(
        default="Overcoming poverty is not a task of charity, it is an act of justice",
        help_text="First inspirational quote"
    )

    quote_1_author = models.CharField(
        max_length=100,
        default="Nelson Mandela",
        help_text="Author of first quote"
    )

    quote_2 = models.TextField(
        default="Rock bottom became the solid foundation on which I rebuilt my life.",
        help_text="Second inspirational quote"
    )

    quote_2_author = models.CharField(
        max_length=100,
        default="J.K Rowling",
        help_text="Author of second quote"
    )

    quote_3 = models.TextField(
        default="I always wondered why somebody didn't do something about that. Then I realized, I am somebody.",
        help_text="Third inspirational quote"
    )

    quote_3_author = models.CharField(
        max_length=100,
        default="Unknown",
        help_text="Author of third quote"
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('subheading'),
        FieldPanel('mission_heading'),
        FieldPanel('mission_statement'),
        FieldPanel('contact_email'),
        FieldPanel('quote_1'),
        FieldPanel('quote_1_author'),
        FieldPanel('quote_2'),
        FieldPanel('quote_2_author'),
        FieldPanel('quote_3'),
        FieldPanel('quote_3_author'),
    ]

    max_count = 1


class ContactPage(Page):
    """Contact page with organization details"""

    heading = models.CharField(
        max_length=255,
        default="Reach out for help",
        help_text="Page heading"
    )

    mailing_address = models.TextField(
        default="P.O. Box 44\nLander, WY 82520",
        help_text="Mailing address"
    )

    phone_number = models.CharField(
        max_length=20,
        default="(307) 332-6127",
        help_text="Contact phone number"
    )

    email = models.EmailField(
        default="[email protected]",
        help_text="Contact email"
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('mailing_address'),
        FieldPanel('phone_number'),
        FieldPanel('email'),
    ]

    max_count = 1


class StoriesIndexPage(Page):
    """Index page for stories (donor showcase, funding, client stories)"""

    intro = RichTextField(
        blank=True,
        default="Read about our organization",
        help_text="Introduction text"
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    max_count = 1

    subpage_types = ['home.StoryPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['stories'] = self.get_children().live().order_by('-first_published_at')
        return context


class StoryPage(Page):
    """Individual story page for donor showcase, funding info, or client stories"""

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Featured story image"
    )

    summary = models.TextField(
        blank=True,
        help_text="Short summary for story listing"
    )

    body = RichTextField(
        blank=True,
        help_text="Full story content"
    )

    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('body'),
    ]

    parent_page_types = ['home.StoriesIndexPage']


class DonatePage(Page):
    """Donation page"""

    heading = models.CharField(
        max_length=255,
        default="Ways to Give",
        help_text="Page heading"
    )

    intro = RichTextField(
        default="Your donation helps provide safe and secure housing for people facing homelessness in Lander, Wyoming.",
        help_text="Introduction text"
    )

    body = RichTextField(
        blank=True,
        help_text="Donation information and options"
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    max_count = 1
