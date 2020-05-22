from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.ian= Editor(first_name = 'ian', last_name ='adika', email ='adika19ian@gmail.com')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ian,Editor))
        
       # Testing Save Method
    def test_save_method(self):
        self.ian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.ian= Editor(first_name = 'ian', last_name ='adika', email ='adika19ian@gmail.com')
        self.ian.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.ian)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
        
    def test_get_gallery_today(self):
        today_gallery = Article.todays_gallery()
        self.assertTrue(len(today_gallery)>0)
