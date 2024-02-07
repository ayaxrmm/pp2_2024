def ishigh(movies):
    if movies["imdb"] > 5.5:
        return True
    else:
        return False
    
movies ={
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}
print(ishigh(movies))

