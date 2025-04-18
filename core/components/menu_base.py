from reactpy import component, html
import requests
from django.urls import reverse, NoReverseMatch
from django.templatetags.static import static
from reactpy_django.components import django_js

def safe_reverse(name):
    try:
        return reverse(name)
    except NoReverseMatch:
        return "#"

@component
def MenuBase():

    menu_items = [
        {'name': 'Pricing', 'url': safe_reverse('pricing')},
        {'name': 'Producto', 'url': safe_reverse('producto')},
        {
            'name': 'Recursos',
            'url': '',
            'submenu': [
                {'name': 'Proba1', 'url': safe_reverse('proba1')},
                {'name': 'Proba2', 'url': safe_reverse('proba2')}
            ]
        },
        {
            'name': 'About',
            'url': '',
            'submenu': [
                {'name': 'Proba1', 'url': safe_reverse('proba1')},
                {'name': 'Proba2', 'url': safe_reverse('proba2')}
            ]
        },
    ]

    return html.header({"class": "py-10 bg-primary_color_bg text-white"},
        html.div({"class": "mx-auto max-w-[90%] xl:max-w-[80%] flex items-center h-20"},
            html.h1({"class": "w-[10%] text-3xl font-bold flex items-center"}, "Finovara"),
            Menu_PC(menu_items),
            Menu_Mobile(menu_items),
            django_js("js/core_components/menu_base.js")
        )
    )


@component
def Menu_PC(menu_items):
    def render_menu_item(item):
        icon_path = f"/static/svg/arrow.svg"
        if 'submenu' in item:
            return html.div({"class": "group relative inline-block px-5 cursor-pointer"},
                html.span({"class": "hover:text-secondary_color flex items-center space-x-2"},
                    html.span({}, item['name']),
                    html.img({"src": icon_path, "class": "w-6 h-6 rotate-180 transform transition-transform duration-100 delay-150 group-hover:rotate-0 scale-50"})
                ),
                html.div({"class": "hidden group-hover:block absolute w-60 transition-opacity delay-300 duration-200 left-0"},
                    html.div({"class": "py-2"}),
                    html.div({"class": "bg-[#FEFFF5] text-black shadow-lg rounded-lg"},
                        *[html.a({
                            "href": sub['url'],
                            "class": "block px-4 py-2 hover:bg-[#FEFFF5] hover:rounded-lg"
                        }, sub['name']) for sub in item['submenu']]
                    )
                )
            )
        else:
            return html.a({
                "href": item['url'],
                "class":  "hover:underline px-3"
            }, item['name'])
        
    
    def render_AuthLinks():
        return html.div({"class": "px-4 flex space-x-3"},
            html.a({
                "href": safe_reverse('signup'),
                "class": "px-2 py-1.5 text-base text-black bg-red-100 w-[130px] border-2 border rounded-full font-semibold flex justify-center"
            }, html.div("Sign Up")),
            
            html.a({
                "href": safe_reverse('login'),
                "class": "px-2 py-1.5 text-base w-[130px] border-2 border rounded-full font-semibold flex justify-center"
            }, html.div("Login"))
        )

    return html.nav({"class": "max-lg:hidden w-[90%] text-xl flex justify-end items-center"},
        html.div({"class": "space-x-2 xl:space-x-8"},
            *[render_menu_item(item) for item in menu_items],
        ),
        render_AuthLinks()
    )

@component
def Menu_Mobile(menu_items):

    menu_path = f"/static/svg/menu.svg"

    def render_menu_item(item):
        return html.div({},
                html.a({
                    "href": item['url'],
                    "class":  "hover:underline px-3"
                }, item['name'])          
            )

    return html.div({"class": "min-lg:hidden w-[90%] text-xl flex justify-end items-center relative"},
            html.img({"src": menu_path, "class": "w-10 h-10"}),
            html.div({"class": "absolute w-[300px] right-0 top-14 rounded-lg bg-[#FEFFF5] text-black shadow-lg"},
                *[render_menu_item(item) for item in menu_items],
            )
        )

