from decimal import Decimal, getcontext

DevicesChoice =(
        ('android','Android'),
        ('windows','Windows'),
        ('linux','Linux'),
        ('mac','Mac'),
    )

getcontext().prec = 2

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
