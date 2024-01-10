from django.db import models

# Create your models here.
class currency (models.Model):
    currency=models.CharField(max_length=5)
    rate=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.0)
    def __str__(self):
        return self.currency
class brand (models.Model):
    brand=models.CharField(max_length=5)
    def __str__(self):
        return self.brand
class unit (models.Model):
    unitProduct=models.CharField(max_length=5)
    def __str__(self):
        return self.unitProduct
    
class mainCategory (models.Model):
    mainCategory=models.CharField(max_length=5)
    def __str__(self):
        return self.mainCategory

class category (models.Model):
    category=models.CharField(max_length=5)
    def __str__(self):
        return self.category
    
class provider (models.Model):
    providerCode=models.CharField(max_length=5)
    provider=models.CharField(max_length=5)
    def __str__(self):
        return self.providerCode
    
class developer (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="developer_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="developer_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="developer_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="developer_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="developer_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="developer_provider")

    def __str__(self):
        return self.code
class powder (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="powder_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="powder_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="powder_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="powder_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="powder_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="powder_provider")

    def __str__(self):
        return self.code
class waste (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="waste_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="waste_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="waste_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="waste_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="waste_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="waste_provider")

    def __str__(self):
        return self.code
class box (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="box_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="box_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="box_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="box_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="box_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="box_provider")

    def __str__(self):
        return self.code
class head (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="head_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="head_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="head_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="head_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="head_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="head_provider")

    def __str__(self):
        return self.code
class empty (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="empty_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="empty_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="empty_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="empty_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="empty_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="empty_provider")

    def __str__(self):
        return self.code
class chip (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="chip_units")
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="chip_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="chip_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="chip_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="chip_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    providerCode=models.ForeignKey(provider, on_delete=models.CASCADE, related_name="chip_provider")

    def __str__(self):
        return self.code
class toner (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="toner_units")
    chip=models.ForeignKey(chip, on_delete=models.CASCADE, related_name="toner_chips")
    empty=models.ForeignKey(empty, on_delete=models.CASCADE, related_name="toner_empties")
    head=models.ForeignKey(head, on_delete=models.CASCADE, related_name="toner_heads")
    box=models.ForeignKey(box, on_delete=models.CASCADE, related_name="toner_boxes")
    waste=models.ForeignKey(waste, on_delete=models.CASCADE, related_name="toner_wastes")
    powder=models.ForeignKey(powder, on_delete=models.CASCADE, related_name="toner_powders")
    powderWeight=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    developer=models.ForeignKey(developer, on_delete=models.CASCADE, related_name="toner_developers")
    developerWeight=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    status=models.BooleanField(default=True)
    brand=models.ForeignKey(brand, on_delete=models.CASCADE, related_name="toner_brands")
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.ForeignKey(mainCategory, on_delete=models.CASCADE, related_name="toner_mainCategories")
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name="toner_categories")
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.ForeignKey(currency, on_delete=models.CASCADE, related_name="toner_currency")
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)

    def __str__(self):
        return self.code









