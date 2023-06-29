from django.db import models

class PersonalDetails(models.Model):
    class Meta:
        verbose_name_plural = 'PersonalDetails'

    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=12)
    gst_number = models.CharField(max_length=15)
    bank_account_number = models.CharField(max_length=16)
    bank_name = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=11)
    bank_address = models.CharField(max_length=50)
    letter_head = models.FileField(upload_to='letter_head')
    invoice_number = models.PositiveSmallIntegerField(default=1)
    object = models.manager

    def __str__(self):
        return self.name


class CholaMandalam(models.Model):
    class Meta:
        verbose_name_plural = 'CholaMandalam'

    company_name = models.CharField(max_length=100, default='CholaMandalam Investments & Finance Co. Ltd.')
    date = models.DateField(auto_now_add=True)
    aps_id = models.CharField(max_length=25)
    customer_name = models.CharField(max_length=100)
    property_address = models.CharField(max_length=250)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices)
    search_number = models.CharField(max_length=16)
    rm_name = models.CharField(max_length=50)
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.property_address


class Poonawalla(models.Model):
    class Meta:
        verbose_name_plural = 'Poonawalla'

    company_name = models.CharField(max_length=100, default='Poonawalla Housing Finance Limited')
    date = models.DateField(auto_now_add=True)
    loan_application_number = models.CharField(max_length=20)
    name_of_borrower = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15, default='24AACCG2265N1ZI')
    place_of_supply = models.CharField(max_length=50)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    product_types = (
        ('H', 'Home Loan'),
        ('L', 'Loan Against Property'),
        ('APF', 'APF'),
    )
    product_type = models.CharField(max_length=3, choices=product_types, default='H')
    price = models.IntegerField(default=1000)
    subject_to_reverse_charge = models.BooleanField(default=False)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.name_of_borrower + ' - ' + self.place_of_supply


class AU(models.Model):
    class Meta:
        verbose_name_plural = 'AU'

    company_name = models.CharField(max_length=100, default='AU')
    date = models.DateField(auto_now_add=True)
    rlos_number = models.CharField(max_length=10)
    lead_number = models.CharField(max_length=20)
    lan_number = models.CharField(max_length=10)
    reject_hold = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    department_types = (
        ('H', 'Home Loan'),
        ('L', 'Loan Against Property'),
        ('APF', 'APF'),
    )
    department_type = models.CharField(max_length=3, choices=department_types, default='H')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    branch = models.CharField(max_length=12, default='Himmatnagar')
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.location


class Wonder(models.Model):
    class Meta:
        verbose_name_plural = 'Wonder'

    company_name = models.CharField(max_length=100, default='Wonder')
    customer_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    deal_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    address_of_property = models.CharField(max_length=100)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.address_of_property


class Aadhar(models.Model):
    class Meta:
        verbose_name_plural = 'Aadhar'

    company_name = models.CharField(max_length=100, default='Aadhar')
    date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    party_address = models.CharField(max_length=250, default='')
    gst_number_party = models.CharField(max_length=15, default='24AABCV5640B1ZS')
    delivery_address = models.CharField(max_length=250, default='')
    gst_number_delivery = models.CharField(max_length=15, default='27AABCV5640B2ZL')
    application_number = models.CharField(max_length=9)
    branch = models.CharField(max_length=20, default='Mehsana')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.party_address


class Axis(models.Model):
    class Meta:
        verbose_name_plural = 'Axis'

    company_name = models.CharField(max_length=100, default='Axis Finance Ltd.')
    company_address = models.CharField(max_length=250, default='')
    date = models.DateField(auto_now_add=True)
    gst_number = models.CharField(max_length=15, default='27AAACK3010F1Z6')
    branch = models.CharField(max_length=20, default='Mehsana')
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, default='')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class Profectus(models.Model):
    class Meta:
        verbose_name_plural = 'Profectus'

    company_name = models.CharField(max_length=100, default='Profectus Capital Private Limited')
    date = models.DateField(auto_now_add=True)
    address_line_1 = models.CharField(max_length=100, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    address_line_3 = models.CharField(max_length=100, default='')
    subject = models.CharField(max_length=30, default='Bill fees & Expenses')
    name_of_applicant = models.CharField(max_length=100, default='')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.address_line_1


class RBL(models.Model):
    class Meta:
        verbose_name_plural = 'RBL'

    company_name = models.CharField(max_length=100, default='RBL Bank Limited')
    date = models.DateField(auto_now_add=True)
    address_line_1 = models.CharField(max_length=100, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    customer_name = models.CharField(max_length=100, default='')
    aps_number = models.CharField(max_length=8, default='')
    village = models.CharField(max_length=20, default='')
    survey_number = models.CharField(max_length=100, default='')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.address_line_1


class HFFC(models.Model):
    class Meta:
        verbose_name_plural = 'HFFC'

    company_name = models.CharField(max_length=100, default='Home First Finance India Company Limited')
    date = models.DateField(auto_now_add=True)
    branch = models.CharField(max_length=20, default='Mehsana')
    name_of_applicant = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=150, default='')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.address


class AYE(models.Model):
    class Meta:
        verbose_name_plural = 'AYE'

    company_name = models.CharField(max_length=100, default='AYE Finance (P) Ltd.')
    date = models.DateField(auto_now_add=True)
    company_address = models.CharField(max_length=20, default='Ahmedabad')
    name_of_applicant = models.CharField(max_length=100, default='')
    aps = models.CharField(max_length=12, default='')
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class Mahindra(models.Model):
    class Meta:
        verbose_name_plural = 'Mahindra'

    company_name = models.CharField(max_length=100, default='Mahindra Rural Housing Finance Ltd')
    date = models.DateField(auto_now_add=True)
    aps_number = models.CharField(max_length=7, default='')
    location = models.CharField(max_length=20, default='')
    customer_name = models.CharField(max_length=100, default='')
    distance = models.PositiveSmallIntegerField(default=0)
    request_received_date = models.DateField(auto_now_add=True)
    repost_submitted_date = models.DateField(auto_now_add=True)
    sro_1 = models.PositiveSmallIntegerField(default=245)
    sro_2 = models.PositiveSmallIntegerField(default=0)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.aps_number


class YesBankAgri(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankAgri'

    company_name = models.CharField(max_length=100, default='Yes Bank Agri Limited')
    date = models.DateField(auto_now_add=True)
    company_address = models.CharField(max_length=20, default='')
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM')
    product_types = (
        ('KCC', 'KCC'),
        ('MEF', 'MEF'),
        ('FMA', 'FMA'),
    )
    product_type = models.CharField(max_length=20, choices=product_types, default='KCC')
    product_price = models.IntegerField(default=1000)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    r_m_fpr_name = models.CharField(max_length=100, default='')
    invoice_status = models.CharField(max_length=20, default='Pending')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class YesBankSagment(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankSagment'

    company_name = models.CharField(max_length=100, default='Yes Bank Limited')
    date = models.DateField(auto_now_add=True)
    company_address = models.CharField(max_length=20, default='')
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM')
    product_types = (
        ('BBS', 'BB Sagment'),
        ('MEF', 'MEF'),
        ('FMA', 'FMA'),
    )
    product_type = models.CharField(max_length=20, choices=product_types, default='BBS')
    initiator_name = models.CharField(max_length=100, default='')
    initiation_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=20, default='Mehsana')
    type_of_services = (
        ('S', 'Stock'),
        ('IA', 'Invoice Audit'),
        ('V', 'Valuation'),
        ('TSR', 'TSR'),
        ('ROC', 'ROC'),
        ('IS', 'Interim Search'),
    )
    type_of_service = models.CharField(max_length=20, choices=type_of_services, default='S')
    service_price = models.IntegerField(default=1000)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    property_address = models.CharField(max_length=100, default='')
    client_name = models.CharField(max_length=100, default='')
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class YesBankAHFL(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankAHFL'

    company_name = models.CharField(max_length=100, default='Yes Bank Limited')
    date = models.DateField(auto_now_add=True)
    company_address = models.CharField(max_length=150, default='')
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM')
    initiator_name = models.CharField(max_length=100, default='')
    initiation_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=20, default='Mehsana')
    type_of_services = (
        ('TSR', 'TSR'),
        ('V', 'Vetting'),
        ('S', 'Stock'),
        ('IA', 'Invoice Audit'),
        ('ROC', 'ROC'),
    )
    type_of_service = models.CharField(max_length=20, choices=type_of_services, default='TSR')
    service_price = models.IntegerField(default=1000)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
        ('T', 'AHFL TSR'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L')
    price = models.IntegerField(default=1000)
    property_address = models.CharField(max_length=100, default='')
    client_name = models.CharField(max_length=100, default='')
    pocket_expense = models.PositiveSmallIntegerField(default=0)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class IndiaBulls(models.Model):
    class Meta:
        verbose_name_plural = 'IndiaBulls'

    company_name = models.CharField(max_length=100, default='Indiabulls')
    date = models.DateField(auto_now_add=True)
    company_zone = models.CharField(max_length=6, default='West-2')
    company_location = models.CharField(max_length=20, default='Mehsana')
    company_branch = models.CharField(max_length=20, default='Mehsana')
    verification_types = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
        ('V', 'Vetting'),
        ('R', 'Report'),
    )
    verification_type = models.CharField(max_length=20, choices=verification_types, default='R')
    co_names = (
        ('IHFL', 'IHFL'),
        ('IVLFL', 'IVLFL'),
        ('ICCL', 'ICCL'),
    )
    co_name = models.CharField(max_length=20, choices=co_names, default='IHFL')
    verification_rate = models.PositiveSmallIntegerField(default=1500)
    number_of_verification = models.PositiveSmallIntegerField(default=1)
    aps_id = models.CharField(max_length=8, default='')
    customer_name = models.CharField(max_length=100, default='')
    property_address = models.CharField(max_length=150, default='')
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_zone + ' - ' + self.company_location


class NewIndia(models.Model):
    class Meta:
        verbose_name_plural = 'NewIndia'

    company_name = models.CharField(max_length=100, default='The New India Assurance Co.Ltd.')
    date = models.DateField(auto_now_add=True)
    company_address = models.CharField(max_length=150, default='')
    case_number = models.CharField(max_length=50, default='')
    name_of_party = models.CharField(max_length=100, default='')
    court_stamp_fee = models.PositiveSmallIntegerField(default=500)
    advocate_fee = models.PositiveSmallIntegerField(default=500)
    clerk_fee = models.PositiveSmallIntegerField(default=500)
    expenses = models.PositiveSmallIntegerField(default=500)
    travelling_expenses = models.PositiveSmallIntegerField(default=500)
    other_expenses = models.PositiveSmallIntegerField(default=500)
    remarks = models.CharField(max_length=250, default='')
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class AgriBank(models.Model):
    class Meta:
        verbose_name_plural = 'AgriBank'

    company_name = models.CharField(max_length=100, default='Agri Bank')
    customer_name = models.CharField(max_length=100, default='')
    village = models.CharField(max_length=100, default='')
    price = models.PositiveSmallIntegerField(default=1000)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.customer_name
