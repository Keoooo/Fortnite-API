from django.test import TestCase
from .models import fortniteskins

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.fortniteskins = "Write Test"
        self.fortniteskins = fortniteskins(name=self.fortniteskins_name)

    def test_model_can_create_a_fort(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = fortniteskins.objects.count()
        self.fortniteskins.save()
        new_count = fortniteskins.objects.count()
        self.assertNotEqual(old_count, new_count)

