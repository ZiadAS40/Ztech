#!/usr/bin/python3
"""make the accessories section"""

from api.v1.views import app_views
from flask import jsonify, make_response
import uuid

apple_laptops = [
    {
        "name": "MacBook Air (M1, 2020)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M1, 7-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-silver-m1?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1604668805000",
        "price": 999
    },
    {
        "name": "MacBook Pro 13-inch (M1, 2020)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-spacegray-m1?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1604668805000",
        "price": 1299
    },
    {
        "name": "MacBook Pro 16-inch (2019)",
        "ram": 16,
        "ssd": 512,
        "gpu": "AMD Radeon Pro 5300M, 4 GB",
        "cpu": "Intel Core i7-9750H",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-201911?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1573440669000",
        "price": 2399
    },
    {
        "name": "MacBook Air (M2, 2022)",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M2, 8-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022-silver?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1199
    },
    {
        "name": "MacBook Pro 14-inch (M1 Pro, 2021)",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M1 Pro, 16-core GPU",
        "cpu": "Apple M1 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-14-spacegray-m1pro?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 1999
    },
    {
        "name": "MacBook Pro 16-inch (M1 Pro, 2021)",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M1 Pro, 16-core GPU",
        "cpu": "Apple M1 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-spacegray-m1pro?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 2499
    },
    {
        "name": "MacBook Air (M1, 2020) with 16GB RAM",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M1, 7-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-silver-m1?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1604668805000",
        "price": 1399
    },
    {
        "name": "MacBook Pro 13-inch (M2, 2022)",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1599
    },
    {
        "name": "MacBook Air (M2, 2022) with 1TB SSD",
        "ram": 16,
        "ssd": 1024,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1499
    },
    {
        "name": "MacBook Pro 16-inch (M2 Pro, 2023)",
        "ram": 32,
        "ssd": 1,
        "gpu": "Apple M2 Pro, 19-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-m2pro-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 2999
    },
    {
        "name": "MacBook Air (M2, 2022) with Touch ID",
        "ram": 8,
        "ssd": 512,
        "gpu": "Apple M2, 8-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1299
    },
    {
        "name": "MacBook Pro 13-inch (M2 Pro, 2023)",
        "ram": 16,
        "ssd": 1,
        "gpu": "Apple M2 Pro, 16-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-m2pro-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 1799
    },
    {
        "name": "MacBook Pro 14-inch (M1 Max, 2021)",
        "ram": 32,
        "ssd": 1,
        "gpu": "Apple M1 Max, 32-core GPU",
        "cpu": "Apple M1 Max",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-14-m1max?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 2499
    },
    {
        "name": "MacBook Air (M1, 2020) with 512GB SSD",
        "ram": 8,
        "ssd": 512,
        "gpu": "Apple M1, 7-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-silver-m1?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1604668805000",
        "price": 1249
    },
    {
        "name": "MacBook Pro 16-inch (M1 Max, 2021) with 64GB RAM",
        "ram": 64,
        "ssd": 1,
        "gpu": "Apple M1 Max, 32-core GPU",
        "cpu": "Apple M1 Max",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-m1max?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 3499
    },
    {
        "name": "MacBook Air (M2, 2022) with 256GB SSD",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M2, 8-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1099
    },
    {
        "name": "MacBook Pro 13-inch (M2 Pro, 2023) with 32GB RAM",
        "ram": 32,
        "ssd": 1,
        "gpu": "Apple M2 Pro, 16-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-m2pro-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 1899
    },
    {
        "name": "MacBook Air (M2, 2022) with 512GB SSD and 16GB RAM",
        "ram": 16,
        "ssd": 512,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1499
    },
    {
        "name": "MacBook Pro 14-inch (M1 Max, 2021) with 64GB RAM",
        "ram": 64,
        "ssd": 1,
        "gpu": "Apple M1 Max, 32-core GPU",
        "cpu": "Apple M1 Max",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-14-m1max?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 2999
    },
    {
        "name": "MacBook Pro 16-inch (M2 Pro, 2023) with 2TB SSD",
        "ram": 32,
        "ssd": 2048,
        "gpu": "Apple M2 Pro, 19-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-m2pro-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 3399
    },
    {
        "name": "MacBook Air (M2, 2022) with 1TB SSD and 16GB RAM",
        "ram": 16,
        "ssd": 1024,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1799
    },
    {
        "name": "MacBook Pro 13-inch (M1, 2020) with 1TB SSD",
        "ram": 8,
        "ssd": 1024,
        "gpu": "Apple M1, 8-core GPU",
        "cpu": "Apple M1",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-spacegray-m1?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1604668805000",
        "price": 1499
    },
    {
        "name": "MacBook Pro 16-inch (M1 Max, 2021) with 32GB RAM",
        "ram": 32,
        "ssd": 512,
        "gpu": "Apple M1 Max, 32-core GPU",
        "cpu": "Apple M1 Max",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-m1max?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1635355793000",
        "price": 2999
    },
    {
        "name": "MacBook Air (M2, 2022) with 512GB SSD and Touch ID",
        "ram": 8,
        "ssd": 512,
        "gpu": "Apple M2, 8-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1399
    },
    {
        "name": "MacBook Pro 14-inch (M2 Pro, 2023) with 2TB SSD",
        "ram": 32,
        "ssd": 2048,
        "gpu": "Apple M2 Pro, 16-core GPU",
        "cpu": "Apple M2 Pro",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-14-m2pro-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 2199
    },
    {
        "name": "MacBook Air (M2, 2022) with 1TB SSD",
        "ram": 8,
        "ssd": 1024,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1699
    },
    {
        "name": "MacBook Pro 13-inch (M2, 2022) with 1TB SSD",
        "ram": 16,
        "ssd": 1024,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1699
    },
    {
        "name": "MacBook Air (M2, 2022) with 8GB RAM and 256GB SSD",
        "ram": 8,
        "ssd": 256,
        "gpu": "Apple M2, 8-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1099
    },
    {
        "name": "MacBook Pro 16-inch (M2 Max, 2023) with 64GB RAM",
        "ram": 64,
        "ssd": 1,
        "gpu": "Apple M2 Max, 38-core GPU",
        "cpu": "Apple M2 Max",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-pro-16-m2max-2023?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1674829276000",
        "price": 3599
    },
    {
        "name": "MacBook Air (M2, 2022) with 16GB RAM and 256GB SSD",
        "ram": 16,
        "ssd": 256,
        "gpu": "Apple M2, 10-core GPU",
        "cpu": "Apple M2",
        "img": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-13-2022?wid=832&hei=872&fmt=jpeg&qlt=80&.v=1657805671000",
        "price": 1299
    }
]


for lt in apple_laptops:
    lt['id'] = str(uuid.uuid4())
    lt['cat'] = "lt"


@app_views.route('/products/apple/laptop', methods=['GET'], strict_slashes=False)
def get_apple_lt():
    """get all the accessories"""


    return make_response(jsonify(apple_laptops), 200)

@app_views.route('/products/apple/laptop/<lt_id>', methods=['GET'], strict_slashes=False)
def apple_laptops_getter_with_id(lt_id):
    """getting all the apple_laptopss"""
    for lt in apple_laptops:
        if lt_id == lt['id']:
            return make_response(jsonify(lt), 200)
    return make_response(jsonify({}), 404)
