from decimal import Decimal, getcontext

# set limit to digit on right of decimal
getcontext().prec = 2

# In pagination count of item in each is result
count_item_in_each_page= 16


# it is  device choice dropdown for all possible devices avaliable
DevicesChoice =(
        ('android','Android'),
        ('windows','Windows'),
        ('linux','Linux'),
        ('mac','Mac'),
    )




# Compress a number into  nearest k,million or billion 
def compress_number(number):
    if number < 100:
        return str(number)
    elif number < 1000000:
        # Format the number with K suffix and explicitly handle rounding
        return f"{Decimal(number/1000).quantize(Decimal('1.00'))}K"
    elif number < 1000000000:
        # Format the number with M suffix and explicitly handle rounding
        return f"{Decimal(number/1000000).quantize(Decimal('1.00'))}M"
    else:
        # Format the number with B suffix and explicitly handle rounding
        return f"{Decimal(number/1000000000).quantize(Decimal('1.00'))}B"


# function for compressing download in a queryset
def compress_download(queryset):
    for queryobj in queryset:
        queryobj.total_downloads = compress_number(queryobj.total_downloads)


#function to retrivew name attribute value from get request
def get_name(request,name):
    search_keyword = ""
    if request.GET.get(name):
        search_keyword = request.GET.get("search_keyword")
    return search_keyword    