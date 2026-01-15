from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile, Document, Gallery


class ProfileModelTest(TestCase):
    """Test Profile model."""

    def test_create_profile(self):
        """Test creating a profile."""
        profile = Profile.objects.create(
            name="Test User",
            bio="Test bio"
        )
        self.assertEqual(profile.name, "Test User")
        self.assertEqual(str(profile), "Test User")


class DocumentModelTest(TestCase):
    """Test Document model."""

    def test_create_document(self):
        """Test creating a document."""
        # Create a simple test file
        test_file = SimpleUploadedFile(
            "test.txt",
            b"file content",
            content_type="text/plain"
        )
        document = Document.objects.create(
            title="Test Document",
            file=test_file
        )
        self.assertEqual(document.title, "Test Document")
        self.assertTrue(document.file)


class GalleryModelTest(TestCase):
    """Test Gallery model."""

    def test_create_gallery_image(self):
        """Test creating a gallery image."""
        # Create a simple test image
        test_image = SimpleUploadedFile(
            "test.jpg",
            b"image content",
            content_type="image/jpeg"
        )
        gallery = Gallery.objects.create(
            title="Test Image",
            image=test_image
        )
        self.assertEqual(gallery.title, "Test Image")
        self.assertFalse(gallery.is_featured)
