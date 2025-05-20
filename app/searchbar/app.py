from flask import Flask, render_template, request, Blueprint, redirect, url_for
import requests
import os

search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['GET', 'POST'])
def search_form():
    if request.method == 'POST':
        item = request.form.get('item')
        return redirect(url_for('search.search_item', item=item))
    return render_template('search_form.html')

@search_bp.route('/<item>', methods=['GET'])
def search_item(item):
    api_key = os.getenv("API_KEY")
    app_id = os.getenv("APP_ID")
    url = "https://trackapi.nutritionix.com/v2/search/instant"
    headers = {
        "x-app-id": app_id,
        "x-app-key": api_key
    }
    params = {"query": item}
    response = requests.get(url, headers=headers, params=params)
    if response.ok:
        results = response.json()
    else:
        results = {"error": "API request failed."}
    return render_template('search.html', results=results, item=item)