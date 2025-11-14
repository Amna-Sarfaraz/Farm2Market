from django.shortcuts import render
import os
from .models import Farmer, Buyer
from market.cpp_algos.compile_and_run import run_cpp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CPP_PATH = os.path.join(BASE_DIR, "market", "cpp_algos")


def index(request):
    return render(request, "index.html")


def search_page(request):
    """Render the page with search/sort/match forms."""
    return render(request, "search.html")


def parse_cpp_output(output):
    """Convert C++ output lines into dictionaries for the template."""
    results = []
    for line in output.splitlines():
        line = line.strip()
        if not line or line == "NoMatch":
            continue
    
        parts = line.split(",")
        if len(parts) >= 4:
            results.append({
                "farmer": {
                    "name": parts[0],
                    "region": parts[2]  
                },
                "crop": parts[1],
                "price": parts[3],
                "expiry_date": parts[4] if len(parts) > 4 else None
            })
    return results


def search(request):
    results = []
    if request.method == "POST":
        keyword = request.POST.get("keyword", "")
        search_type = request.POST.get("search_type", "1")
        exe_file = os.path.join(CPP_PATH, "search.exe")
        output = run_cpp(exe_file, keyword, search_type)
        results = parse_cpp_output(output)

    return render(request, "results.html", {
        "output_lines": results,
        "title": "Search Results"
    })


def sort_market(request):
    results = []
    if request.method == "POST":
        sort_choice = request.POST.get("sort_choice", "1")
        order = request.POST.get("order", "1")
        exe_file = os.path.join(CPP_PATH, "sort.exe")
        output = run_cpp(exe_file, sort_choice, order)
        results = parse_cpp_output(output)

    return render(request, "results.html", {
        "output_lines": results,
        "title": "Sorted Market Data"
    })


def match_buyers(request):
    results = []
    if request.method == "POST":
        crop = request.POST.get("crop", "")
        region = request.POST.get("region", "")
        budget = request.POST.get("budget", "0")
        exe_file = os.path.join(CPP_PATH, "match.exe")
        output = run_cpp(exe_file, crop, region, budget)
        results = parse_cpp_output(output)

    return render(request, "results.html", {
        "output_lines": results,
        "title": "Buyer-Farmer Matches"
    })


def farmers(request):
    """Show all farmers and handle adding new farmers."""
    farmers_list = Farmer.objects.all()
    output_lines = []

    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        produce = request.POST.get("produce")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        Farmer.objects.create(
            name=name,
            city=city,
            produce=produce,
            price=price,
            quantity=quantity
        )

        exe_file = os.path.join(CPP_PATH, "farmer.exe")
        if os.path.exists(exe_file):
            output = run_cpp(exe_file)
            output_lines = output.splitlines()
        else:
            output_lines = ["C++ executable not found."]

        farmers_list = Farmer.objects.all()

    return render(request, "farmers.html", {
        "farmers": farmers_list,
        "output_lines": output_lines
    })
