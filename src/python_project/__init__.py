# https://github.com/flet-dev/examples/blob/main/python/controls/charts-matplotlib/mpl-finance.py
import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import os

from flet import AppBar
from flet import Card
from flet import Column
from flet import Container
from flet import ElevatedButton
from flet import IconButton
from flet import Row
from flet import Switch
from flet import Text
from flet import colors
from flet import icons

matplotlib.use("svg")

# https://colab.research.google.com/github/willismax/matplotlib_show_chinese_in_colab/blob/master/matplotlib_show_chinese_in_colab.ipynb#scrollTo=RfR0uymWF3cB
import os.path
if os.path.isfile('TaipeiSansTCBeta-Regular.ttf') == False:
    # 下載台北思源黑體並命名taipei_sans_tc_beta.ttf，移至指定路徑
    import urllib.request
    urllib.request.urlretrieve('https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download', 'TaipeiSansTCBeta-Regular.ttf')

# 改style要在改font之前
# plt.style.use('seaborn')
import matplotlib as mpl
from matplotlib.font_manager import fontManager
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

from responsive_menu_layout import ResponsiveMenuLayout

import numpy as np
import pandas as pd
def show_bar(ax, csv_data, json_data):
    # # 分析CSV數據（範例：新北市各區站點數量和剩餘車量）
    # site_count_by_area = csv_data.groupby('鄉鎮市區')['站點名稱'].count()
    # remaining_bikes_by_area = csv_data.groupby('區域')['剩餘車量'].sum()

    # 生成CSV數據的圖表
    # 将csv_data.head(5).to_numpy()转换为list类型的数据
    data_list = csv_data.head(5).to_numpy()
    data_list_sorted = data_list[data_list[:, 2].argsort()]
    ax[0].plot(data_list_sorted[:,1].tolist(),data_list_sorted[:,2].tolist())
    ax[0].set_ylabel('金額(千元)')
    ax[0].grid(True)
    # ax.figure(figsize=(12, 6))
    # ax.subplot(1, 2, 1)
    # ax[0].plot(csv_data.head(5))
    # ax[0].set_ylabel('金額(千元)')
    # ax[0].grid(True)
    # ax.subplot(1, 2, 2)
    # csv_data.plot(kind='bar', title='各區剩餘車量')
    # ax.tight_layout()
    # ax.show()

    # # 讀取JSON數據
    # with open('your_json_data.json', 'r') as json_file:
    #     json_data = json.load(json_file)

    # # 分析JSON數據（範例：各鄉鎮市區人口密度）
    # town_pop_density = {item['town']: item['population_density'] for item in json_data}

    # # 生成JSON數據的圖表
    # ax.figure(figsize=(8, 6))
    # towns = list(town_pop_density.keys())
    # densities = list(town_pop_density.values())
    # ax.barh(towns, densities)
    # ax.tight_layout()
    # ax.show()
    
    data_list = json_data.head(10).to_numpy()
    data_list_sorted = data_list[data_list[:, 2].argsort()]

    ax[1].plot(data_list_sorted[:,1].tolist(),data_list_sorted[:,2].tolist())
    ax[1].set_xlabel('人口密度')
    ax[1].set_title('各鄉鎮市區人口密度')
    ax[1].grid(True)

    return ax

from simpledt import DataFrame
def show_data_list(csv_data):
    simpledt_df = DataFrame(csv_data)  # Initialize simpledt DataFrame object
    simpledt_dt = simpledt_df.datatable  # Extract DataTable instance from simpledt
    return simpledt_dt

# set Flet path to an empty string to serve at the root URL (e.g., https://lizards.ai/)
# or a folder/path to serve beneath the root (e.g., https://lizards.ai/ui/path
DEFAULT_FLET_PATH = ''  # or 'ui/path'
DEFAULT_FLET_PORT = 8502

def main(page: ft.Page):
    page.title = "You Enjoy Mychatbot"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    menu_button = IconButton(icons.MENU)

    page.appbar = AppBar(
        leading=menu_button,
        leading_width=40,
        bgcolor=colors.SURFACE_VARIANT,
    )

    # 讀取CSV數據
    csv_data = pd.read_csv('./src/python_project/109_165-9.csv')
    json_data = pd.read_json('./src/python_project/10909.json')
    fig, ax = plt.subplots(2, 1)
    plt.subplots_adjust(hspace=0.5)  # Adjust the value as needed
    ax = show_bar(ax, csv_data, json_data)
    simpledt_dt = show_data_list(csv_data.head(5))

    def route_change(route):
        # page.views.clear()
        pages = [
            (
                dict(icon=icons.LANDSCAPE_OUTLINED, selected_icon=icons.LANDSCAPE, label="barChart"),
                Row(
                    [
                        MatplotlibChart(fig, expand=True),
                        # simpledt_dt
                    ],
                    expand=True
                ),
            ),
            (
                dict(icon=icons.PORTRAIT_OUTLINED, selected_icon=icons.PORTRAIT, label="Menu in portrait"),
                create_page(
                    "Menu in portrait",
                    "Menu in portrait is mainly expected to be used on a smaller mobile device."
                    "\n\n"
                    "The menu is by default hidden, and when shown with the menu button it is placed on top of the main "
                    "content."
                    "\n\n"
                    "In addition to the menu button, menu can be dismissed by a tap/click on the main content area.",
                ),
            ),
            (
                dict(
                    icon=icons.INSERT_EMOTICON_OUTLINED, selected_icon=icons.INSERT_EMOTICON, label="Minimize to icons"
                ),
                create_page(
                    "Minimize to icons",
                    "ResponsiveMenuLayout has a parameter minimize_to_icons. "
                    "Set it to True and the menu is shown as icons only, when normally it would be hidden.\n"
                    "\n\n"
                    "Try this with the 'Minimize to icons' toggle in the top bar."
                    "\n\n"
                    "There are also landscape_minimize_to_icons and portrait_minimize_to_icons properties that you can "
                    "use to set this property differently in each orientation.",
                ),
            ),
            (
                dict(icon=icons.COMPARE_ARROWS_OUTLINED, selected_icon=icons.COMPARE_ARROWS, label="Menu width"),
                create_page(
                    "Menu width",
                    "ResponsiveMenuLayout has a parameter manu_extended. "
                    "Set it to False to place menu labels under the icons instead of beside them."
                    "\n\n"
                    "Try this with the 'Menu width' toggle in the top bar.",
                ),
            ),
            (
                dict(icon=icons.ROUTE_OUTLINED, selected_icon=icons.ROUTE, label="Route support", route="custom-route"),
                create_page(
                    "Route support",
                    "ResponsiveMenuLayout has a parameter support_routes, which is True by default. "
                    "\n\n"
                    "Routes are useful only in the web, where the currently selected page is shown in the url, "
                    "and you can open the app directly on a specific page with the right url."
                    "\n\n"
                    "You can specify a route explicitly with a 'route' item in the menu dict (see this page in code). "
                    "If you do not specify the route, a slugified version of the page label is used "
                    "('Menu width' becomes 'menu-width').",
                ),
            ),
            (
                dict(icon=icons.PLUS_ONE_OUTLINED, selected_icon=icons.PLUS_ONE, label="Fine control"),
                create_page(
                    "Adjust navigation rail",
                    "NavigationRail is accessible via the navigation_rail attribute of the ResponsiveMenuLayout. "
                    "In this demo it is used to add the leading button control."
                    "\n\n"
                    "These NavigationRail attributes are used by the ResponsiveMenuLayout, and changing them directly "
                    "will probably break it:\n"
                    "- destinations\n"
                    "- extended\n"
                    "- label_type\n"
                    "- on_change\n",
                ),
            ),
        ]

        # 在頁面加載時檢查是否已經存在 ResponsiveMenuLayout 的實例
        existing_menu_layout = None
        for control in page.controls:
            if isinstance(control, ResponsiveMenuLayout):
                existing_menu_layout = control
                break

        if existing_menu_layout is None:
            # 如果不存在 ResponsiveMenuLayout 的實例，則創建一個新的實例並添加到頁面中
            menu_layout = ResponsiveMenuLayout(page, pages)
            page.add(menu_layout)
        else:
            # 如果已經存在 ResponsiveMenuLayout 的實例，則使用現有的實例
            menu_layout = existing_menu_layout

        page.appbar.actions = [
            Row(
                [
                    Text("Minimize\nto icons"),
                    Switch(on_change=lambda e: toggle_icons_only(menu_layout)),
                    Text("Menu\nwidth"),
                    Switch(value=True, on_change=lambda e: toggle_menu_width(menu_layout)),
                ]
            )
        ]

        menu_layout.navigation_rail.leading = ElevatedButton(
            "Add", icon=icons.ADD, expand=True, on_click=lambda e: print("Add clicked")
        )

        page.add(menu_layout)

        # menu_button.on_click = lambda e: menu_layout.toggle_navigation()

        # page.views.append(
        #     ft.View(
        #         "/",
        #         [
        #             ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
        #             menu_layout,
        #             # MatplotlibChart(fig, expand=True),
        #             # simpledt_dt,
        #             ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
        #         ],
        #     )
        # )
        # if page.route == "/store":
        #     page.views.append(
        #         ft.View(
        #             "/store",
        #             [
        #                 ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
        #                 ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
        #             ],
        #         )
        #     )
        # page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def create_page(title: str, body: str):
        return Row(
            controls=[
                Column(
                    horizontal_alignment="stretch",
                    controls=[
                        Card(content=Container(Text(title, weight="bold"), padding=8)),
                        Text(body),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    
    def toggle_icons_only(menu: ResponsiveMenuLayout):
        menu.minimize_to_icons = not menu.minimize_to_icons
        menu.page.update()

    def toggle_menu_width(menu: ResponsiveMenuLayout):
        menu.menu_extended = not menu.menu_extended
        menu.page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    # page.go(page.route)
    page.add(ft.Text("Reba put a stopper in the bottom of the tub"))

if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(name=flet_path, target=main, view=None, port=flet_port)

# import pandas as pd
# import os

# df = pd.read_excel('./src/python_project/廚具logo設計 (回覆)1.xlsx')
# column_name = '一個傢具行的商品，您希望怎麼樣的呈現最佳，請選擇兩項。'
# replace_symbols = ['>', '<', ':', '"', '/', '\\\\', '\|', '\?', '\*']
# df[column_name] = (
#     df[column_name].replace(replace_symbols, '', regex=True).str.strip().str.title()
# )
# unique_values = df[column_name].unique()

# for unique_value in unique_values:
#     df_output = df[df[column_name].str.contains(unique_value)]
#     df_output.to_excel('./廚具logo設計 (回覆)2.xlsx', sheet_name='廚具logo設計 (回覆)2.xlsx', index=False)