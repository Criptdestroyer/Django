from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Ahmad Emir Alfatah' # TODO Implement this
mhs_major = 'Teknik Informatika Universitas Sriwijaya'
birth_year = 'Palembang, 12 Januari 2000'
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(2000,1,12) #TODO Implement this, format (Year, Month, Date)
motivation = 'Motivasi saya mengikuti kelas ini adalah saya ingin menguasai Django yang merupakan salah satu tools pemrograman web yang populer dan banyak digunakan di perusahaan besar, Django juga merupakan framework dari python dan mempunyai library yang lengkap untuk data science sehingga saya dapat belajar membuat website yang mempunyai kemampuan data science seperti Machine Learning, AI dan lain-lain.'
motivation2 = 'Ilmu yang saya dapatkan nanti jika saya bisa mengikuti kelas ini akan saya terapkan dalam membuat web sistem di kampus saya, mengajari anggota saya tentang pemrograman web Django dan lain-lain sehingga web sistem buatan kami bisa lebih powerful dan berguna bagi Civitas Akademika Universitas Sriwijaya.'


# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year), 'mhs_major':mhs_major, 'birth_year':birth_year, 'motivation':motivation, 'motivation2':motivation2}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
