
from django.shortcuts import render, redirect
from .blockchain import Blockchain
from .models import Block

def ledger_home(request):
    bc = Blockchain()
    blocks = Block.objects.all().order_by('index')
    return render(request, 'ledger.html', {'blocks': blocks})

def add_demo_block(request):
    bc = Blockchain()
    bc.add_block({"demo": "sample transaction"})
    return redirect('ledger_home')
