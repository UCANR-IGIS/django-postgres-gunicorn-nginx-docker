from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Profile, Document, Gallery


def home(request):
    """Home page view."""
    return render(request, 'myapp/home.html')


class ProfileListView(ListView):
    """List all profiles."""
    model = Profile
    template_name = 'myapp/profile_list.html'
    context_object_name = 'profiles'
    paginate_by = 10


class ProfileDetailView(DetailView):
    """Detail view for a single profile."""
    model = Profile
    template_name = 'myapp/profile_detail.html'
    context_object_name = 'profile'


class GalleryListView(ListView):
    """List all gallery images."""
    model = Gallery
    template_name = 'myapp/gallery_list.html'
    context_object_name = 'images'
    paginate_by = 12

    def get_queryset(self):
        """Featured images first."""
        return Gallery.objects.order_by('-is_featured', '-uploaded_at')


class DocumentListView(ListView):
    """List all documents."""
    model = Document
    template_name = 'myapp/document_list.html'
    context_object_name = 'documents'
    paginate_by = 20
