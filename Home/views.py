from multiprocessing import context
from pstats import Stats
from telnetlib import STATUS
from django.shortcuts import render
from django.views import View
from product.models import productCategory

class index(View):
    
    def get(self,request):
        navigationProductCategories=productCategory.objects.filter(status=True)
        homeProductCategories = productCategory.objects.filter(status=True).order_by('name')[0:3]
        # for productCategory in homeProductCategories:
        #     print(productCategory.ProductCategory.filter(status=True))
        context={
            'navigationProductCategories':navigationProductCategories,
            'homeProductCategories':homeProductCategories
            
        }
        
        return render(request,'index.html',context)
        


