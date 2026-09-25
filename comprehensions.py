sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extratc_title_traditional(articles):
    """Extrae solo los titulos usando un for"""
    tittles = []
    for article in articles:
        if len(article["title"]) > 200:
            tittles.append(article["title"])
    return tittles


def extract_titles(articles):
    """extra solo los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 200]


def extrac_article_sumaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"])>5
    }


# print(extratc_title_traditional(sample_articles))
# print("==============")
# print(extract_titles(sample_articles))
print(extrac_article_sumaries(sample_articles))