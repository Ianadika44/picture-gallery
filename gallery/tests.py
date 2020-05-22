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