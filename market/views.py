from django.shortcuts import render
import os
from .models import Farmer, Buyer
from market.cpp_algos.compile_and_run import run_cpp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CPP_PATH = os.path.join(BASE_DIR, "market", "cpp_algos")

def index(request):
    return render(request, "index.html")

def search(request):
    output = ""
    if request.method == "POST":
        keyword = request.POST.get("keyword", "")
        search_type = request.POST.get("search_type", "1")
        exe_file = os.path.join(CPP_PATH, "search.exe")
        output = run_cpp(exe_file, keyword, search_type)
    return render(request, "results.html", {"output": output, "title": "Search Results"})

def sort_market(request):
    output = ""
    if request.method == "POST":
        sort_choice = request.POST.get("sort_choice", "1")
        order = request.POST.get("order", "1")
        exe_file = os.path.join(CPP_PATH, "sort.exe")
        output = run_cpp(exe_file, sort_choice, order)
    return render(request, "results.html", {"output": output, "title": "Sorted Market Data"})

def match_buyers(request):
    output = ""
    if request.method == "POST":
        crop = request.POST.get("crop", "")
        region = request.POST.get("region", "")
        budget = request.POST.get("budget", "0")
        exe_file = os.path.join(CPP_PATH, "match.exe")
        output = run_cpp(exe_file, crop, region, budget)
    return render(request, "results.html", {"output": output, "title": "Buyer-Farmer Matches"})
