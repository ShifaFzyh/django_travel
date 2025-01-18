from django.shortcuts import render

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

    context = {
        'ps_bandara' : ps_bandara,
    }
    return render(request, 'plane.html', context)

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