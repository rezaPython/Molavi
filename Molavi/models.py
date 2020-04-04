from django.db import models


class categories(models.Model):
    categories_name = models.CharField(max_length=300)

    def __str__(self):
        return self.categories_name


class raftar_mosbat(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class raftar_manfi(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class jameh(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class elm_o_andisheh(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class jahl(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class ghodrat(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class nezame_tabieye_donya(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)



class masnavi_manavi(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)


class zamimeh(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title + ' categoy: {} '.format(self.category)