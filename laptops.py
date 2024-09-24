#!/usr/bin/python3
import json
import re

def get_budget(laps, budget):
    final_laps = []
    
    for lap in laps:
        price_str = lap.get('price', '')
        price_match = re.findall(r'\d+', price_str)
        
        if price_match:
            lap_price = int(''.join(price_match))
            
            if lap_price <= budget:
                final_laps.append(lap)
    
    return final_laps


laptops = [
    {
        "name": "Dell XPS 15",
        "price": "$1,799",
        "CPU": {
            "nameOfCpu": "Intel Core i7-11800H",
            "cores": 8,
            "threads": 16,
            "baseClock": "2.3 GHz",
            "maxClock": "4.6 GHz",
            "cache": "24 MB"
        },
        "GPU": {
            "nameOfGpu": "NVIDIA GeForce RTX 3050 Ti",
            "vram": "4 GB GDDR6",
            "cudaCores": 2560,
            "clockSpeed": "1.5 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "1 TB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "86 Wh",
            "batteryLife": "Up to 8 hours"
        },
        "Ports": [
            "2x Thunderbolt 4",
            "1x USB 3.2 Type-C",
            "1x SD card reader",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.8 kg",
        "OS": "Windows 11"
    },
    {
        "name": "Lenovo ThinkPad X1 Carbon Gen 9",
        "price": "$1,399",
        "CPU": {
            "nameOfCpu": "Intel Core i5-1135G7",
            "cores": 4,
            "threads": 8,
            "baseClock": "2.4 GHz",
            "maxClock": "4.2 GHz",
            "cache": "8 MB"
        },
        "GPU": {
            "nameOfGpu": "Intel Iris Xe",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "1.3 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "LPDDR4x",
            "speed": "4266 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "14 inches",
            "resolution": "1920 x 1200",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "57 Wh",
            "batteryLife": "Up to 15 hours"
        },
        "Ports": [
            "2x Thunderbolt 4",
            "2x USB 3.2",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.13 kg",
        "OS": "Windows 11"
    },
    {
        "name": "ASUS ROG Zephyrus G14",
        "price": "$1,499",
        "CPU": {
            "nameOfCpu": "AMD Ryzen 9 5900HS",
            "cores": 8,
            "threads": 16,
            "baseClock": "3.3 GHz",
            "maxClock": "4.6 GHz",
            "cache": "16 MB"
        },
        "GPU": {
            "nameOfGpu": "NVIDIA GeForce RTX 3060",
            "vram": "6 GB GDDR6",
            "cudaCores": 3840,
            "clockSpeed": "1.7 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "1 TB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "14 inches",
            "resolution": "2560 x 1440",
            "refreshRate": "120 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "76 Wh",
            "batteryLife": "Up to 10 hours"
        },
        "Ports": [
            "2x USB 3.2 Type-C",
            "2x USB 3.2 Type-A",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.6 kg",
        "OS": "Windows 11"
    },
    {
        "name": "HP Spectre x360 14",
        "price": "$1,249",
        "CPU": {
            "nameOfCpu": "Intel Core i7-1165G7",
            "cores": 4,
            "threads": 8,
            "baseClock": "2.8 GHz",
            "maxClock": "4.7 GHz",
            "cache": "12 MB"
        },
        "GPU": {
            "nameOfGpu": "Intel Iris Xe",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "1.35 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "LPDDR4x",
            "speed": "4266 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "13.5 inches",
            "resolution": "1920 x 1280",
            "refreshRate": "60 Hz",
            "panelType": "OLED"
        },
        "Battery": {
            "capacity": "66 Wh",
            "batteryLife": "Up to 12 hours"
        },
        "Ports": [
            "2x Thunderbolt 4",
            "1x USB 3.2 Type-A",
            "1x microSD card reader",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.34 kg",
        "OS": "Windows 11"
    },
    {
        "name": "Acer Predator Helios 300",
        "price": "$1,299",
        "CPU": {
            "nameOfCpu": "Intel Core i7-10750H",
            "cores": 6,
            "threads": 12,
            "baseClock": "2.6 GHz",
            "maxClock": "5.0 GHz",
            "cache": "12 MB"
        },
        "GPU": {
            "nameOfGpu": "NVIDIA GeForce RTX 3060",
            "vram": "6 GB GDDR6",
            "cudaCores": 3840,
            "clockSpeed": "1.7 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "DDR4",
            "speed": "2933 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "144 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "59 Wh",
            "batteryLife": "Up to 6 hours"
        },
        "Ports": [
            "3x USB 3.2",
            "1x USB Type-C",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo",
            "1x Ethernet"
        ],
        "Weight": "2.5 kg",
        "OS": "Windows 10"
    },
    {
        "name": "Razer Blade 15",
        "price": "$2,399",
        "CPU": {
            "nameOfCpu": "Intel Core i7-11800H",
            "cores": 8,
            "threads": 16,
            "baseClock": "2.3 GHz",
            "maxClock": "4.6 GHz",
            "cache": "24 MB"
        },
        "GPU": {
            "nameOfGpu": "NVIDIA GeForce RTX 3070",
            "vram": "8 GB GDDR6",
            "cudaCores": 5120,
            "clockSpeed": "1.73 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "1 TB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "2560 x 1440",
            "refreshRate": "165 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity":None
        }
    }
]

laptops.extend([
    {
        "name": "Lenovo Legion 5",
        "price": "$1,199",
        "CPU": {
            "nameOfCpu": "AMD Ryzen 5 5600H",
            "cores": 6,
            "threads": 12,
            "baseClock": "3.3 GHz",
            "maxClock": "4.2 GHz",
            "cache": "16 MB"
        },
        "GPU": {
            "nameOfGpu": "NVIDIA GeForce GTX 1660 Ti",
            "vram": "6 GB GDDR6",
            "cudaCores": 1536,
            "clockSpeed": "1.5 GHz"
        },
        "RAM": {
            "size": "16 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "120 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "80 Wh",
            "batteryLife": "Up to 7 hours"
        },
        "Ports": [
            "1x USB Type-C",
            "4x USB 3.2",
            "1x HDMI",
            "1x Ethernet",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "2.3 kg",
        "OS": "Windows 10"
    },
    {
        "name": "Acer Swift 3",
        "price": "$899",
        "CPU": {
            "nameOfCpu": "AMD Ryzen 7 5700U",
            "cores": 8,
            "threads": 16,
            "baseClock": "1.8 GHz",
            "maxClock": "4.3 GHz",
            "cache": "8 MB"
        },
        "GPU": {
            "nameOfGpu": "AMD Radeon Graphics",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "2.0 GHz"
        },
        "RAM": {
            "size": "8 GB",
            "type": "LPDDR4x",
            "speed": "4266 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "14 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "48 Wh",
            "batteryLife": "Up to 12 hours"
        },
        "Ports": [
            "1x USB Type-C",
            "2x USB 3.2",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.2 kg",
        "OS": "Windows 10"
    },
    {
        "name": "ASUS VivoBook 15",
        "price": "$699",
        "CPU": {
            "nameOfCpu": "Intel Core i5-1135G7",
            "cores": 4,
            "threads": 8,
            "baseClock": "2.4 GHz",
            "maxClock": "4.2 GHz",
            "cache": "8 MB"
        },
        "GPU": {
            "nameOfGpu": "Intel Iris Xe",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "1.3 GHz"
        },
        "RAM": {
            "size": "8 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "256 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "42 Wh",
            "batteryLife": "Up to 8 hours"
        },
        "Ports": [
            "1x USB Type-C",
            "2x USB 3.2",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.8 kg",
        "OS": "Windows 10"
    },
    {
        "name": "Dell Inspiron 15 5000",
        "price": "$749",
        "CPU": {
            "nameOfCpu": "Intel Core i5-1135G7",
            "cores": 4,
            "threads": 8,
            "baseClock": "2.4 GHz",
            "maxClock": "4.2 GHz",
            "cache": "8 MB"
        },
        "GPU": {
            "nameOfGpu": "Intel Iris Xe",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "1.3 GHz"
        },
        "RAM": {
            "size": "8 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "512 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "15.6 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "42 Wh",
            "batteryLife": "Up to 6 hours"
        },
        "Ports": [
            "1x USB Type-C",
            "2x USB 3.2",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.8 kg",
        "OS": "Windows 10"
    },
    {
        "name": "HP Pavilion x360",
        "price": "$649",
        "CPU": {
            "nameOfCpu": "Intel Core i3-1125G4",
            "cores": 4,
            "threads": 8,
            "baseClock": "3.0 GHz",
            "maxClock": "3.7 GHz",
            "cache": "8 MB"
        },
        "GPU": {
            "nameOfGpu": "Intel Iris Xe",
            "vram": "Shared",
            "cudaCores": None,
            "clockSpeed": "1.3 GHz"
        },
        "RAM": {
            "size": "8 GB",
            "type": "DDR4",
            "speed": "3200 MHz"
        },
        "Storage": {
            "type": "SSD",
            "capacity": "256 GB",
            "interface": "NVMe"
        },
        "Display": {
            "size": "14 inches",
            "resolution": "1920 x 1080",
            "refreshRate": "60 Hz",
            "panelType": "IPS"
        },
        "Battery": {
            "capacity": "43 Wh",
            "batteryLife": "Up to 8 hours"
        },
        "Ports": [
            "1x USB Type-C",
            "2x USB 3.2",
            "1x HDMI",
            "1x 3.5mm headphone/microphone combo"
        ],
        "Weight": "1.6 kg",
        "OS": "Windows 10"
    }
])

def convert_to_gb(storage_str):
    conversion_factors = {
        'KB': 1 / (1024 * 1024),  
        'MB': 1 / 1024,           
        'GB': 1,                  
        'TB': 1000,               
        'PB': 1000000             
    }

    storage_str = storage_str.strip().upper() 
    value, unit = float(storage_str.split()[0]), storage_str.split()[1]

    
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unknown storage unit: {unit}")

def rate_cpu(min_clock_speed, max_clock_speed, cores, threads, cache_memory):
    # Define the rating criteria
    # Assume realistic min/max for each parameter
    min_clock_speed_min = 1.0  # GHz
    max_clock_speed_max = 5.0  # GHz
    cores_min = 1
    cores_max = 16  # Example maximum for consumer CPUs
    threads_min = 1
    threads_max = 32  # Example maximum
    cache_memory_min = 1  # MB
    cache_memory_max = 32  # MB

    # Normalize scores to a 10-point scale
    min_clock_speed_score = max(0, min(min_clock_speed / min_clock_speed_min, 1)) * 10
    max_clock_speed_score = max(0, min(max_clock_speed / max_clock_speed_max, 1)) * 10
    cores_score = max(0, min(cores / cores_max, cores_min)) * 10
    threads_score = max(0, min(threads / threads_max, 1)) * 10
    cache_memory_score = max(0, min(cache_memory / cache_memory_max, 1)) * 10

    # Calculate the overall score with weights
    overall_score = (
        (min_clock_speed_score * 0.2) +
        (max_clock_speed_score * 0.3) +
        (cores_score * 0.3) +
        (threads_score * 0.1) +
        (cache_memory_score * 0.1)
    )

    return overall_score

def rate_gpu(cuda_cores, vram, clock_speed):
    if cuda_cores == None:
        cuda_cores = 0

    min_cuda_cores = 64  
    max_cuda_cores = 8192  
    min_vram = 1  
    max_vram = 32  
    min_clock_speed = 1.0  
    max_clock_speed = 2.5  

    
    cuda_cores_score = max(0, min(cuda_cores / max_cuda_cores, 1)) * 10
    vram_score = max(0, min(vram / max_vram, 1)) * 10
    clock_speed_score = max(0, min(clock_speed / max_clock_speed, 1)) * 10

    
    overall_score = (
        (cuda_cores_score * 0.33) +  
        (vram_score * 0.33) +        
        (clock_speed_score * 0.34)   
    )

    return overall_score

def rate_ram(size, ram_type, speed):
    # Define min/max ranges for each parameter
    min_size = 4  # GB (minimum acceptable size)
    max_size = 64  # GB (high-end maximum for RAM for power users)
    min_speed = 1600  # MHz (minimum acceptable speed)
    max_speed = 5000  # MHz (high-end maximum for RAM speed)

    # Define type scores (assigning higher score for newer types)
    type_scores = {
        'DDR3': 6,  # Older RAM type
        'DDR4': 8,  # Current standard for many systems
        'DDR5': 10  # Newer, higher-performing RAM type
    }

    # Normalize size score (scale to 10, now with 32 GB as 10)
    size_score = max(0, min(size / max_size, 1)) * 10
    
    # Get RAM type score (default to 6 if type not found)
    type_score = type_scores.get(ram_type, 6)
    
    # Normalize speed score (scale to 10)
    speed_score = max(0, min(speed / max_speed, 1)) * 10

    # Calculate overall score with custom weights
    overall_score = (
        (size_score * 0.4) +  # Size is still important (40% weight)
        (type_score * 0.3) +  # Type is also important (30% weight)
        (speed_score * 0.3)   # Speed is also important (30% weight)
    )

    return overall_score

def rate_storage(storage_type, capacity, interface):
    # Define min/max ranges for capacity
    min_capacity = 128  # GB (minimum acceptable size for SSD)
    max_capacity = 4000  # GB (max capacity considered for high-end storage)

    # Define type scores
    type_scores = {
        'SSD': 9,   # SSDs score higher in general
        'HDD': 6    # HDDs score lower
    }
    
    # Define interface scores
    interface_scores = {
        'NVMe': 10,  # NVMe is the fastest
        'SATA': 7    # SATA is slower
    }

    # Normalize capacity score (scale to 10)
    capacity_score = max(0, min(capacity / max_capacity, 1)) * 10
    
    # Get storage type score (default to 6 if type not found)
    type_score = type_scores.get(storage_type, 6)
    
    # Get interface score (default to 7 if interface not found)
    interface_score = interface_scores.get(interface, 7)

    # Calculate overall score with custom weights
    overall_score = (
        (capacity_score * 0.4) +    # Capacity is important (40% weight)
        (type_score * 0.3) +        # Type is important (30% weight)
        (interface_score * 0.3)     # Interface is important (30% weight)
    )

    return overall_score

def rate_laps(laps):
    final_laps = []
    for lap in laps:
        cpu_rate = rate_cpu(float(re.findall(r'(\d+\.?\d*)\s*GHz', lap['CPU']['baseClock'])[0]),
                            float(re.findall(r'(\d+\.?\d*)\s*GHz', lap['CPU']['maxClock'])[0]),
                            lap['CPU']['cores'],
                            lap['CPU']['cores'],
                            int(re.findall(r'(\d+\.?\d*)\s*MB', lap['CPU']['cache'])[0]))
        vram = re.findall(r'(\d+\.?\d*)\s*GB', lap['GPU']['vram'])
        if vram:
            v_amount = int (vram[0])
        else:
            v_amount = 0
        gpu_rate = rate_gpu(lap['GPU']['cudaCores'],
                            v_amount,
                            float(re.findall(r'(\d+\.?\d*)\s*GHz', lap['CPU']['baseClock'])[0])
                            )
        ram_rate = rate_ram(int(re.findall(r'(\d+\.?\d*)\s*GB', lap['RAM']['size'])[0]),
                            lap["RAM"]["type"],
                            int(re.findall(r'(\d+\.?\d*)\s*MHz', lap['RAM']['speed'])[0]))
        storage_rate = rate_storage(lap["Storage"]["type"],
                                    convert_to_gb(lap['Storage']['capacity']),
                                    lap["Storage"]['interface'])
        
        final_rate = (cpu_rate * 0.4) + (gpu_rate * 0.1) * (ram_rate * 0.3) * (storage_rate * 0.2)

        lap['rate'] = round(final_rate, 2)
        final_laps.append(lap)
    return final_laps


with open('laptops.json', 'w') as f:
    json.dump(laptops, f)