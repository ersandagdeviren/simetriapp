from django.db import models

# Create your models here.
class unit (models.Model):
    unitProduct=models.CharField(max_length=5)
    def __str__(self):
        return self.unitProduct
class developer (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class powder (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class waste (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class box (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class head (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class empty (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class chip (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.CharField(max_length=5)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)
    provider=models.CharField(max_length=50)
    providerCode=models.CharField(max_length=50)

    def __str__(self):
        return self.code
class toner (models.Model):
    code= models.CharField(max_length=50)
    codeUyum=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    unit=models.ForeignKey(unit, on_delete=models.CASCADE, related_name="copier_units")
    chip=models.ForeignKey(chip, on_delete=models.CASCADE, related_name="copier_chips")
    empty=models.ForeignKey(empty, on_delete=models.CASCADE, related_name="copier_empties")
    head=models.ForeignKey(head, on_delete=models.CASCADE, related_name="copier_heads")
    box=models.ForeignKey(box, on_delete=models.CASCADE, related_name="copier_boxes")
    waste=models.ForeignKey(waste, on_delete=models.CASCADE, related_name="copier_wastes")
    powder=models.ForeignKey(powder, on_delete=models.CASCADE, related_name="copier_powders")
    powderWeight=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    developer=models.ForeignKey(developer, on_delete=models.CASCADE, related_name="copier_developers")
    developerWeight=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    status=models.BooleanField(default=True)
    brand=models.CharField(max_length=50,blank=True)
    barcode=models.CharField(max_length=50,blank=True)
    mainCategory=models.CharField(max_length=50,blank=True)
    category=models.CharField(max_length=50,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    tax=models.PositiveIntegerField(blank=True)
    currency=models.CharField(max_length=5,blank=True)
    stockAmount=models.PositiveIntegerField(default=0)
    photoPath=models.CharField(max_length=5,blank=True)

    def __str__(self):
        return self.code









