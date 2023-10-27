# https://github.com/flet-dev/examples/blob/main/python/controls/charts-matplotlib/mpl-finance.py
import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import os

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
import json
def show_bar(ax, csv_data):
    # # 分析CSV數據（範例：新北市各區站點數量和剩餘車量）
    # site_count_by_area = csv_data.groupby('鄉鎮市區')['站點名稱'].count()
    # remaining_bikes_by_area = csv_data.groupby('區域')['剩餘車量'].sum()

    # 生成CSV數據的圖表
    # 将csv_data.head(5).to_numpy()转换为list类型的数据
    data_list = csv_data.head(10).to_numpy()
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
    # ax.xlabel('人口密度')
    # ax.title('各鄉鎮市區人口密度')
    # ax.tight_layout()
    # ax.show()

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

    # 讀取CSV數據
    csv_data = pd.read_csv('https://eip.fia.gov.tw/data/ias/ias109/109_165-9.csv')
    fig, ax = plt.subplots(2, 1)
    ax = show_bar(ax, csv_data)
    simpledt_dt = show_data_list(csv_data.head(5))

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    MatplotlibChart(fig, expand=True),
                    simpledt_dt,
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.add(ft.Text("Reba put a stopper in the bottom of the tub"))

if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(name=flet_path, target=main, view=None, port=flet_port)