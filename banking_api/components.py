from reactpy import component, html

@component
def hello_world():
    return html.h1(f"Hello!")