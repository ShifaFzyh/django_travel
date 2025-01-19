from django.shortcuts import render
import math

def haversine(lat1, lon1, lat2, lon2):
    # Konversi derajat ke radian
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Rumus Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Jarak dalam kilometer (radius bumi = 6371 km)
    r = 6371
    distance = r * c
    return distance

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def help(request):
    return render(request, 'help.html')

def login(request):
    return render(request, 'login.html')

def process_form(request): 
    if request.method == "POST": 
    # Data form 
        email = request.POST.get("floating_email") 
        nama1 = request.POST.get("floating_first_name") 
        nama2 = request.POST.get("floating_last_name") 
        phone = request.POST.get("floating_phone") 
    
    bio = { 
            "email": email, 
            "nama1": nama1, 
            "nama2": nama2, 
            "phone": phone, 
    }

    return render(request, "bio.html", {"bio": bio})

def bio_motor(request):
    return render(request, 'bio_motor.html')

def plane(request):
    ps_bandara = ['International Suvarnabhumi(Bangkok)',
                'Changi (Singapura)',
                'Internasional Kuala Lumpur (Malaysia)',
                'Internasional Don Mueang (Bangkok)',
                'Internasional Phuket (Thailand)',
                'Internasional I Gusti Ngurah Rai (Bali)',
                'Internasional Noi Bai Hanoi (Vietnam)',
                'Internasional Phu Quoc (Vietnam)',
                'Internasional Ninoy Aquino (Manila)',
                'Internasional Soekarno-Hatta (Jakarta)']
        
            # Tambahkan jarak ke konteks
    context = {
        'ps_bandara': ps_bandara,
    }

    return render(request, 'plane.html', context)
    
def process_plane(request):
    if request.method == "POST":
        asal = request.POST.get('bandaraasal')  # Menggunakan POST untuk mendapatkan data
        tujuan = request.POST.get('bandaratujuan')

        bandara_data = {
            'International Suvarnabhumi(Bangkok)': (13.7563, 100.5671),
            'Changi (Singapura)': (1.3644, 103.9915),
            'Internasional Kuala Lumpur (Malaysia)': (2.7456, 101.7072),
            'Internasional Don Mueang (Bangkok)': (13.9125, 100.6072),
            'Internasional Phuket (Thailand)': (7.8804, 98.3923),
            'Internasional I Gusti Ngurah Rai (Bali)': (-8.7482, 115.1672),
            'Internasional Noi Bai Hanoi (Vietnam)': (21.2181, 105.8003),
            'Internasional Phu Quoc (Vietnam)': (10.2899, 103.9840),
            'Internasional Ninoy Aquino (Manila)': (14.5086, 121.0190),
            'Internasional Soekarno-Hatta (Jakarta)': (-6.1256, 106.6552),
        }

        # Memastikan bandara asal dan tujuan valid
        if asal in bandara_data and tujuan in bandara_data:
            # Ambil koordinat untuk bandara asal dan tujuan
            lat1, lon1 = bandara_data[asal]
            lat2, lon2 = bandara_data[tujuan]

            # Hitung jarak menggunakan fungsi haversine
            jarak = haversine(lat1, lon1, lat2, lon2)

            # Menghitung total harga (misalnya, Rp 2300 per km)
            harga_per_km = 2300  # Misalnya Rp 2300 per kilometer

            # Menghitung total harga
            total = jarak * harga_per_km

            def format_rupiah(value):
                return f"Rp {value:,.0f}".replace(',', '.')

            harga_pswt = {
                "bandara1": asal, 
                "bandara2": tujuan, 
                "Harga per kilometer": format_rupiah(harga_per_km),
                "Harga": format_rupiah(total)
            }

            return render(request, "harga_pswt.html", {"harga_pswt": harga_pswt})
        else:
            # Jika bandara tidak valid
            return render(request, "plane.html", {"error": "Bandara asal atau tujuan tidak valid."})

    return render(request, "plane.html")


def train(request):
    krt_stasiun = {'Jakarta',
                 'Tangerang',
                 'Bandung',
                 'Surabaya',
                 'Semarang',
                 'Yogyakarta',
                 'Solo',
                 'Malang',
                 'Cirebon',
                 'Tegal'}
    context = {
        'krt_stasiun' : krt_stasiun,
    }
    return render(request, 'train.html', context)

def process_krt(request): 
    if request.method == "POST": 
        # Data form 
        stasiun1 = request.POST.get("stasiun1") 
        stasiun2 = request.POST.get("stasiun2")

        def get_harga_stasiun(stasiun): 
            harga_stasiun = {
                'Jakarta': 5000,
                'Tangerang': 10000,
                'Bandung': 15000,
                'Surabaya': 20000,
                'Semarang': 25000,
                'Yogyakarta': 30000,
                'Solo': 35000,
                'Malang': 40000,
                'Cirebon': 45000,
                'Tegal': 50000
            }
            return harga_stasiun.get(stasiun, 0)  # Mengembalikan 0 jika stasiun tidak valid

        harga1 = get_harga_stasiun(stasiun1)
        harga2 = get_harga_stasiun(stasiun2)

        selisih = abs(harga2 - harga1)
        total = selisih * 10 + 100000 # Menghitung total harga

        def format_rupiah(value):
            return f"Rp {value:,.0f}".replace(',', '.')

        harga_krt = { 
            "st1": stasiun1, 
            "st2": stasiun2, 
            "Harga": format_rupiah(total)
        }

        return render(request, "harga_krt.html", {"harga_krt": harga_krt})
    
    return render(request, "train.html")

def bus(request):
    bus_terminal = {'Jakarta',
                 'Tangerang',
                 'Bandung',
                 'Surabaya',
                 'Semarang',
                 'Yogyakarta',
                 'Solo',
                 'Malang',
                 'Cirebon',
                 'Tegal'}
    context = {
        'bus_terminal' : bus_terminal,
    }
    return render(request, 'bus.html', context)

def process_bus(request): 
    if request.method == "POST": 
        # Data form 
        trm1 = request.POST.get("terminal1") 
        trm2 = request.POST.get("terminal2")

        def get_harga_terminal(terminal): 
            harga_terminal = {
                'Jakarta': 5000,
                'Tangerang': 10000,
                'Bandung': 15000,
                'Surabaya': 20000,
                'Semarang': 25000,
                'Yogyakarta': 30000,
                'Solo': 35000,
                'Malang': 40000,
                'Cirebon': 45000,
                'Tegal': 50000
            }
            return harga_terminal.get(terminal, 0)  # Mengembalikan 0 jika stasiun tidak valid

        harga1 = get_harga_terminal(trm1)
        harga2 = get_harga_terminal(trm2)

        selisih = abs(harga2 - harga1)
        total = selisih * 5 + 100000 # Menghitung total harga

        def format_rupiah(value):
            return f"Rp {value:,.0f}".replace(',', '.')

        harga_bus = { 
            "trm1": trm1, 
            "trm2": trm2, 
            "Harga": format_rupiah(total)
        }

        return render(request, "harga_bus.html", {"harga_bus": harga_bus})
    
    return render(request, "bus.html")

def car(request):
    return render(request, 'car.html')

def motor(request):
    return render(request, 'motor.html')

def app(request):
    
    
    return render(request, 'app.html')