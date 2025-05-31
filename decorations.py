color_main = '#303030'
color_decorate = "#4B4B4B"
color_input = "#535353"
color_button = "#1E688A"

base_button_style = {
    "bg": color_button,
    "fg": "white",
    "bd": 0,
    "relief": "flat",
    "font": ("Helvetica", 14, "bold"),
}

button_style = {
    **base_button_style,
    "width": 10,
    "height": 2,
}

button_technique_style = {
    **base_button_style,
    "font": ("Helvetica", 12, "bold"),
    "width": 20,
    "height": 2,
}

text_style = {
    "bg": color_main,
    "fg": "white",
    "font": ("Helvetica", 15, "bold"),
}

text_enter = {
    "fg": "white",
    "font": ("Helvetica", 15, "bold"),
}

text_input = {
    "fg": "white",
    "font": ("Helvetica", 13, "bold"),
}