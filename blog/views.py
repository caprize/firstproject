from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import Post,Order
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,OrderForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import telebot
from telebot.types import Message
import requests
from telebot import types
BASE_URL='https://api.telegram.org/bot/731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4'
TOKEN = '731947153:AAETaq49IdPhGCg9YssRF6RmW3ZIjzAdX4o'
tb = telebot.TeleBot(TOKEN)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
