#!/usr/bin/python3
"""make the accessories section"""

from api.v1.views import app_views
from flask import jsonify, make_response

apple_desktops = [
    {
        "name": "iMac 24-inch (M1, 2021)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M1, 7-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-pink-select-202104?wid=904&hei=840&fmt=jpeg&qlt=80&.v=1617492405000",
        "price": 1299
    },
    {
        "name": "iMac 27-inch (5K, 2020)",
        "ram": 8,
        "ssd": 256,
        "gpu": "AMD Radeon Pro 5300, 4 GB",
        "cpu": "Intel Core i5-10500",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-27-retina-5k-202008?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1594932849000",
        "price": 1799
    },
    {
        "name": "Mac Mini (M1, 2020)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202011?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1604001244000",
        "price": 699
    },
    {
        "name": "Mac Pro (2019)",
        "ram": 32,
        "ssd": 512,
        "gpu": "AMD Radeon Pro 580X, 8 GB",
        "cpu": "Intel Xeon W 8-core",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-hero-201908?wid=1040&hei=940&fmt=jpeg&qlt=80&.v=1563823047451",
        "price": 5999
    },
    {
        "name": "iMac Pro (2017)",
        "ram": 32,
        "ssd": 1,
        "gpu": "Radeon Pro Vega 56, 8 GB",
        "cpu": "Intel Xeon W 8-core",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-pro-201706?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1497306000644",
        "price": 4999
    },
    {
        "name": "iMac 24-inch (M1, 2021) with 8-core GPU",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-blue-select-202104?wid=904&hei=840&fmt=jpeg&qlt=80&.v=1617492405000",
        "price": 1699
    },
    {
        "name": "Mac Mini (M2, 2023)",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202301?wid=532&hei=582&fmt=jpeg&qlt=95&.v=1671129824956",
        "price": 999
    },
    {
        "name": "iMac 27-inch (5K, 2020) with upgraded GPU",
        "ram": 16,
        "ssd": 1,
        "gpu": "AMD Radeon Pro 5700 XT, 16 GB",
        "cpu": "Intel Core i7-10700K",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-27-retina-5k-202008?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1594932849000",
        "price": 2499
    },
    {
        "name": "Mac Pro (2019) with Dual GPU",
        "ram": 64,
        "ssd": 1,
        "gpu": "AMD Radeon Pro Vega II Duo, 2x32 GB",
        "cpu": "Intel Xeon W 12-core",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-hero-201908?wid=1040&hei=940&fmt=jpeg&qlt=80&.v=1563823047451",
        "price": 12999
    },
    {
        "name": "iMac 24-inch (M1, 2021) with Touch ID Keyboard",
        "ram": 8,
        "ssd": 512,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-green-select-202104?wid=904&hei=840&fmt=jpeg&qlt=80&.v=1617492405000",
        "price": 1499
    },
    {
        "name": "Mac Mini (Intel, 2020)",
        "ram": 16,
        "ssd": 512,
        "gpu": "Intel UHD Graphics 630",
        "cpu": "Intel Core i5-8500",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-201810?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1539361472735",
        "price": 1099
    },
    {
        "name": "iMac 27-inch (5K, 2020) with Nano-texture Glass",
        "ram": 16,
        "ssd": 512,
        "gpu": "AMD Radeon Pro 5500 XT, 8 GB",
        "cpu": "Intel Core i7-10700K",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-27-retina-5k-202008?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1594932849000",
        "price": 2299
    },
    {
        "name": "Mac Pro (2019) with Afterburner",
        "ram": 48,
        "ssd": 2,
        "gpu": "AMD Radeon Pro Vega II, 32 GB",
        "cpu": "Intel Xeon W 16-core",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-hero-201908?wid=1040&hei=940&fmt=jpeg&qlt=80&.v=1563823047451",
        "price": 17999
    },
    {
        "name": "iMac 21.5-inch (4K, 2019)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Radeon Pro 555X, 2 GB",
        "cpu": "Intel Core i5-8500",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-21-retina-4k-201903?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1550795409260",
        "price": 1299
    },
    {
        "name": "iMac 24-inch (M1, 2021) with 16GB RAM",
        "ram": 16,
        "ssd": 1,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-yellow-select-202104?wid=904&hei=840&fmt=jpeg&qlt=80&.v=1617492405000",
        "price": 1999
    },
    {
        "name": "Mac Mini (M1, 2020) with 16GB RAM",
        "ram": 16,
        "ssd": 1,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202011?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1604001244000",
        "price": 1099
    },
    {
        "name": "iMac 27-inch (5K, 2020) with i9",
        "ram": 32,
        "ssd": 2,
        "gpu": "AMD Radeon Pro 5700 XT, 16 GB",
        "cpu": "Intel Core i9-10910",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-27-retina-5k-202008?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1594932849000",
        "price": 3299
    },
    {
        "name": "Mac Pro (2019) with 28-core Xeon",
        "ram": 128,
        "ssd": 4,
        "gpu": "AMD Radeon Pro W6900X, 32 GB",
        "cpu": "Intel Xeon W 28-core",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-pro-hero-201908?wid=1040&hei=940&fmt=jpeg&qlt=80&.v=1563823047451",
        "price": 54999
    },
    {
        "name": "iMac 24-inch (M1, 2021) with 2TB SSD",
        "ram": 16,
        "ssd": 2,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-24-orange-select-202104?wid=904&hei=840&fmt=jpeg&qlt=80&.v=1617492405000",
        "price": 2299
    },
    {
        "name": "Mac Mini (M2 Pro, 2023)",
        "ram": 32,
        "ssd": 1,
        "gpu": "Apple M2 Pro, 16-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-mini-select-202301?wid=532&hei=582&fmt=jpeg&qlt=95&.v=1671129824956",
        "price": 1999
    },
    {
        "name": "iMac 27-inch (5K, 2020) with 10-core i9",
        "ram": 64,
        "ssd": 2,
        "gpu": "AMD Radeon Pro 5700 XT, 16 GB",
        "cpu": "Intel Core i9-10910",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/imac-27-retina-5k-202008?wid=572&hei=572&fmt=jpeg&qlt=95&.v=1594932849000",
        "price": 3499
    }
]



@app_views.route('/products/apple/desktop', methods=['GET'], strict_slashes=False)
def get_apple_dt():
    """get all the accessories"""
    f_id = 0
    for dt in apple_desktops:
        dt['apple-dt-id'] = f_id
        f_id += 1

    return make_response(jsonify(apple_desktops), 200)
