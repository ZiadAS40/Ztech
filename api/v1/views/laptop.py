#!/usr/bin/python3
"""make the laptops section"""

from api.v1.views import app_views
from flask import jsonify, make_response



laptops = [
    {
        "name": "Dell XPS 13",
        "ram": 16,
        "ssd": 512,
        "gpu": "Intel Iris Xe, 1.5 GB",
        "cpu": "Intel Core i7-1165G7",
        "img": "https://i.dell.com/sites/csimages/Video_Imagery/all/xps-13-9310-1.png",
        "price": 1299
    },
    {
        "name": "HP Spectre x360",
        "ram": 16,
        "ssd": 512,
        "gpu": "Intel Iris Xe, 1.5 GB",
        "cpu": "Intel Core i7-1165G7",
        "img": "https://www.hp.com/us-en/shop/app/assets/images/product/1Q881AV_1/center_facing.png",
        "price": 1349
    },
    {
        "name": "Lenovo ThinkPad X1 Carbon",
        "ram": 16,
        "ssd": 128,
        "gpu": "Intel UHD Graphics, 1.5 GB",
        "cpu": "Intel Core i7-10510U",
        "img": "https://www.lenovo.com/medias/lenovo-laptop-thinkpad-x1-carbon-gen8-feature-1.png?context=bWFzdGVyfHJvb3R8MzMwMDc2fGltYWdlL3BuZ3xoMWMvaDNiLzEwODY2MzU0MzE3NDc4LnBuZ3wwNjY4ZDkwYjZkNTk2ODU4MDQxOTc4MWM0ZTAzNTM3NmM1MWQ3ZDhlZDExNTNhY2E0NTMxNjM0NmI4YWEzODlm",
        "price": 1429
    },
    {
        "name": "ASUS ROG Zephyrus G14",
        "ram": 16,
        "ssd": 1,
        "gpu": "NVIDIA GeForce RTX 2060, 6 GB",
        "cpu": "AMD Ryzen 9 4900HS",
        "img": "https://dlcdnwebimgs.asus.com/gain/AE792F0A-F59B-47E1-AB2B-EA523E7037D6",
        "price": 1449
    },
    {
        "name": "Acer Swift 3",
        "ram": 8,
        "ssd": 512,
        "gpu": "Intel Iris Xe, 1.5 GB",
        "cpu": "Intel Core i5-1135G7",
        "img": "https://www.acer.com/ac/en/US/content/model/1/NR.A16AA.001",
        "price": 679
    },
    {
        "name": "Microsoft Surface Laptop 4",
        "ram": 16,
        "ssd": 512,
        "gpu": "Intel Iris Plus, 1.5 GB",
        "cpu": "Intel Core i7-1065G7",
        "img": "https://c.s-microsoft.com/en-us/CMSImages/1920_Panel2_Hero_190412.jpg?version=d24d2fd7-d4f5-e364-d03b-90be2a3fd6e0",
        "price": 1599
    },
    {
        "name": "Razer Blade 15",
        "ram": 16,
        "ssd": 1,
        "gpu": "NVIDIA GeForce GTX 1660 Ti, 6 GB",
        "cpu": "Intel Core i7-10750H",
        "img": "https://assets2.razerzone.com/images/pnx.assets/189c245a0635fa6a1e64a16cfc0a2e9a/razer-blade-15-gallery-hero.jpg",
        "price": 1699
    },
    {
        "name": "LG Gram 17",
        "ram": 16,
        "ssd": 1,
        "gpu": "Intel Iris Xe, 1.5 GB",
        "cpu": "Intel Core i7-1165G7",
        "img": "https://www.lg.com/us/images/laptops/md07504016/gallery/desktop-01.jpg",
        "price": 1799
    },
    {
        "name": "Alienware m15 R3",
        "ram": 32,
        "ssd": 2,
        "gpu": "NVIDIA GeForce RTX 2070, 8 GB",
        "cpu": "Intel Core i9-10980HK",
        "img": "https://www.dell.com/sites/csimages/Video_Imagery/all/alienware-m15-r3-1.png",
        "price": 2549
    },
    {
        "name": "Gigabyte Aero 15",
        "ram": 16,
        "ssd": 1,
        "gpu": "NVIDIA GeForce RTX 2070, 8 GB",
        "cpu": "Intel Core i7-10875H",
        "img": "https://images.gigabyte.com/visual/Default-Product-Gallery/Aero-15-YB_0-scaled.jpg",
        "price": 1999
    },
    {
        "name": "Huawei MateBook X Pro",
        "ram": 16,
        "ssd": 512,
        "gpu": "NVIDIA GeForce MX250, 2 GB",
        "cpu": "Intel Core i7-10510U",
        "img": "https://consumer.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/laptops/matebook-x-pro-2019/img/specs/grey.png",
        "price": 1499
    },
    {
        "name": "MSI GS66 Stealth",
        "ram": 16,
        "ssd": 1,
        "gpu": "NVIDIA GeForce RTX 2080 Super, 8 GB",
        "cpu": "Intel Core i7-10750H",
        "img": "https://asset.msi.com/resize/image/global/product/product_8_20200727155257_5f1f5e3963af1.png62405b38c58fe0f07fcef2367d8a9ba1/600.png",
        "price": 2299
    },
    {
        "name": "Acer Predator Helios 300",
        "ram": 16,
        "ssd": 512,
        "gpu": "NVIDIA GeForce GTX 1660 Ti, 6 GB",
        "cpu": "Intel Core i7-9750H",
        "img": "https://static.acer.com/up/Resource/Acer/Laptops/Predator_Helios_300/PH315-53%20BAS_05B/20200505/20200504/acer-laptop-predator-ph315-53-05b-backlit-keyboard-ph315-53.jpg",
        "price": 1199
    },
    {
        "name": "Samsung Galaxy Book Ion",
        "ram": 8,
        "ssd": 512,
        "gpu": "Intel UHD Graphics, 1.5 GB",
        "cpu": "Intel Core i7-10510U",
        "img": "https://images.samsung.com/is/image/samsung/p6pim/levant/galaxy-book-ion-np950xcj-k01sa/gallery/levant-galaxy-book-ion-np950xcj-k01sa-321676-np950xcj-k01sa-360826476?$720_576_PNG$",
        "price": 1399
    },
    {
        "name": "Dell G5 15 SE",
        "ram": 16,
        "ssd": 512,
        "gpu": "AMD Radeon RX 5600M, 6 GB",
        "cpu": "AMD Ryzen 7 4800H",
        "img": "https://i.dell.com/sites/csimages/Video_Imagery/all/g-series-15-5505-hero.png",
        "price": 1149
    },
    {
        "name": "Asus ZenBook 13",
        "ram": 8,
        "ssd": 512,
        "gpu": "Intel Iris Xe, 1.5 GB",
        "cpu": "Intel Core i5-1135G7",
        "img": "https://dlcdnwebimgs.asus.com/gain/47F8D51A-CFA6-4644-B50C-A3A0CB43A5AA",
        "price": 999
    }
]


@app_views.route('/products/laptops', methods=['GET'], strict_slashes=False)
def laptops_getter():
    """getting all the laptops"""
    f_id = 0
    for laptop in laptops:
        laptop['id'] = f_id
        laptop['category'] = "windows"
        if laptop['ssd'] == 1:
            laptop['ssd'] = 128
        if laptop['ssd'] == 2:
            laptop['ssd'] = 256
        f_id += 1
    
    return make_response(jsonify(laptops), 200)
