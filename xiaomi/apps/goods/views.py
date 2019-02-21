from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from  django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from mixin.mixin import LoginRequiredMixin
import re

class index(View):
    def get(self,request):
            user=request.user
            return  render(request,"index.html",{"user":user})

