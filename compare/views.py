from django.shortcuts import render
from .utils import Search, compute
# Create your views here.
def index(request):
    vendorlist = ["Cisco Anyconnect","Juniper VPN", "OpenVPN VPN"]
    vendors = ["vendor1", "vendor2", "Attack Window"]
    if request.method == "POST":
        vendor1 = request.POST.get("layer1")
        vendor2 = request.POST.get("layer2")
        c = 0
        vendors = [vendor1, vendor2]
        results = []
        for item in vendors:
            vendor, product = item.split(" ")
            results.append(Search().run("-d", vendor, product, 50))

        data, severities = compute(results)
        vendors.append("Attack Window")
        final_severities= {}
        for ven in severities:
            final_severities[vendors[c]] = ven
            c += 1
        return render(request, 'severity.html', {"vendorlist": vendorlist, "data":data, "vendors": vendors, "severities":final_severities})
    else:
        return render(request, 'index.html',{"vendorlist":vendorlist, "vendors": vendors})
