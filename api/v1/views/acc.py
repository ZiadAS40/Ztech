#!/usr/bin/python3
"""make the accessories section"""

from api.v1.views import app_views
from flask import jsonify, make_response

accessories = [
    {
        "kind": "Keyboard",
        "model": "Logitech MX Keys",
        "price": 99.99
    },
    {
        "kind": "Mouse",
        "model": "Razer DeathAdder V2",
        "price": 69.99
    },
    {
        "kind": "Headphone",
        "model": "Sony WH-1000XM4",
        "price": 349.99
    },
    {
        "kind": "Monitor",
        "model": "Dell UltraSharp U2720Q",
        "price": 549.99
    },
    {
        "kind": "Webcam",
        "model": "Logitech C920",
        "price": 79.99
    },
    {
        "kind": "External SSD",
        "model": "Samsung T7 1TB",
        "price": 169.99
    },
    {
        "kind": "Docking Station",
        "model": "CalDigit TS3 Plus",
        "price": 249.99
    },
    {
        "kind": "Mouse Pad",
        "model": "SteelSeries QcK",
        "price": 14.99
    },
    {
        "kind": "Speakers",
        "model": "Audioengine A5+ Wireless",
        "price": 499.99
    },
    {
        "kind": "USB Hub",
        "model": "Anker 7-Port USB 3.0",
        "price": 39.99
    },
    {
        "kind": "Gaming Chair",
        "model": "Secretlab Titan Evo 2022",
        "price": 449.99
    },
    {
        "kind": "Mechanical Keyboard",
        "model": "Corsair K95 RGB Platinum",
        "price": 199.99
    },
    {
        "kind": "Gaming Mouse",
        "model": "Logitech G502 Hero",
        "price": 79.99
    },
    {
        "kind": "Headset",
        "model": "HyperX Cloud II",
        "price": 99.99
    },
    {
        "kind": "Microphone",
        "model": "Blue Yeti USB Microphone",
        "price": 129.99
    },
    {
        "kind": "Mouse Bungee",
        "model": "BenQ Zowie Camade II",
        "price": 24.99
    },
    {
        "kind": "Cooling Pad",
        "model": "Cooler Master Notepal X3",
        "price": 49.99
    },
    {
        "kind": "External Hard Drive",
        "model": "WD My Passport 4TB",
        "price": 109.99
    },
    {
        "kind": "Surge Protector",
        "model": "APC P11VT3 11-Outlet Surge Protector",
        "price": 29.99
    },
    {
        "kind": "VR Headset",
        "model": "Oculus Quest 2",
        "price": 299.99
    }
]


@app_views.route('/products/accessories', methods=['GET'], strict_slashes=False)
def get_acc():
    """get all the accessories"""
    f_id = 0
    for accessory in accessories:
        accessory['acc-id'] = f_id
        f_id =+ 1

    return make_response(jsonify(accessories), 200)
