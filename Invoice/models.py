from django.db import models
from django.contrib.auth.models import User


class PersonalDetails(models.Model):
    class Meta:
        verbose_name_plural = 'PersonalDetails'

    name = models.CharField(max_length=100, blank=True)
    address_line_1 = models.CharField(max_length=150, blank=True)
    address_line_2 = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)
    pan_number = models.CharField(max_length=10, blank=True)
    aadhar_number = models.CharField(max_length=12, blank=True)
    gst_number = models.CharField(max_length=15, blank=True)
    bank_account_number = models.CharField(max_length=16, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    bank_ifsc_code = models.CharField(max_length=11, blank=True)
    bank_address = models.CharField(max_length=50, blank=True)
    letter_head = models.FileField(upload_to='letter_head', blank=True)
    invoice_number = models.PositiveSmallIntegerField(default=1, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.name


class CholaMandalam(models.Model):
    class Meta:
        verbose_name_plural = 'CholaMandalam'

    company_name = models.CharField(max_length=100, default='CholaMandalam Investments & Finance Co. Ltd.', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    aps_id = models.CharField(max_length=25, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    property_address = models.CharField(max_length=250, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, blank=True)
    search_number = models.CharField(max_length=16, blank=True)
    rm_name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.property_address


class Poonawalla(models.Model):
    class Meta:
        verbose_name_plural = 'Poonawalla'

    company_name = models.CharField(max_length=100, default='Poonawalla Housing Finance Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    loan_application_number = models.CharField(max_length=20, blank=True)
    name_of_borrower = models.CharField(max_length=100, blank=True)
    gst_number = models.CharField(max_length=15, default='24AACCG2265N1ZI', blank=True)
    place_of_supply = models.CharField(max_length=50, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    product_types = (
        ('H', 'Home Loan'),
        ('L', 'Loan Against Property'),
        ('APF', 'APF'),
    )
    product_type = models.CharField(max_length=3, choices=product_types, default='H', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    subject_to_reverse_charge = models.BooleanField(default=False, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False, blank=True)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.name_of_borrower + ' - ' + self.place_of_supply


class AU(models.Model):
    class Meta:
        verbose_name_plural = 'AU'

    company_name = models.CharField(max_length=100, default='AU', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    rlos_number = models.CharField(max_length=10, blank=True)
    lead_number = models.CharField(max_length=20, blank=True)
    lan_number = models.CharField(max_length=10, blank=True)
    reject_hold = models.BooleanField(default=False, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    property_address = models.CharField(max_length=50, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    department_types = (
        ('H', 'Home Loan'),
        ('L', 'Loan Against Property'),
        ('APF', 'APF'),
    )
    department_type = models.CharField(max_length=3, choices=department_types, default='H', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    branch = models.CharField(max_length=12, default='Himmatnagar', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.property_address


class Wonder(models.Model):
    class Meta:
        verbose_name_plural = 'Wonder'

    company_name = models.CharField(max_length=100, default='Wonder', blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    deal_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, blank=True)
    property_address = models.CharField(max_length=100, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.property_address


class Aadhar(models.Model):
    class Meta:
        verbose_name_plural = 'Aadhar'

    company_name = models.CharField(max_length=100, default='Aadhar', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    party_address = models.CharField(max_length=250, default='', blank=True)
    gst_number_party = models.CharField(max_length=15, default='24AABCV5640B1ZS', blank=True)
    delivery_address = models.CharField(max_length=250, default='', blank=True)
    gst_number_delivery = models.CharField(max_length=15, default='27AABCV5640B2ZL', blank=True)
    application_number = models.CharField(max_length=9, blank=True)
    branch = models.CharField(max_length=20, default='Mehsana', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.customer_name + ' - ' + self.party_address


class Axis(models.Model):
    class Meta:
        verbose_name_plural = 'Axis'

    company_name = models.CharField(max_length=100, default='Axis Finance Ltd.', blank=True)
    company_address = models.CharField(max_length=250, default='', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    gst_number = models.CharField(max_length=15, default='27AAACK3010F1Z6', blank=True)
    branch = models.CharField(max_length=20, default='Mehsana', blank=True)
    customer_name = models.CharField(max_length=100, blank=True)
    property_address = models.CharField(max_length=250, default='', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class Profectus(models.Model):
    class Meta:
        verbose_name_plural = 'Profectus'

    company_name = models.CharField(max_length=100, default='Profectus Capital Private Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    address_line_1 = models.CharField(max_length=100, default='', blank=True)
    address_line_2 = models.CharField(max_length=100, default='', blank=True)
    address_line_3 = models.CharField(max_length=100, default='', blank=True)
    subject = models.CharField(max_length=30, default='Bill fees & Expenses', blank=True)
    name_of_applicant = models.CharField(max_length=100, default='', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.address_line_1


class RBL(models.Model):
    class Meta:
        verbose_name_plural = 'RBL'

    company_name = models.CharField(max_length=100, default='RBL Bank Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    address_line_1 = models.CharField(max_length=100, default='', blank=True)
    address_line_2 = models.CharField(max_length=100, default='', blank=True)
    customer_name = models.CharField(max_length=100, default='', blank=True)
    aps_number = models.CharField(max_length=8, default='', blank=True)
    village = models.CharField(max_length=255, default='', blank=True)
    survey_number = models.CharField(max_length=100, default='', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.address_line_1


class HFFC(models.Model):
    class Meta:
        verbose_name_plural = 'HFFC'

    company_name = models.CharField(max_length=100, default='Home First Finance India Company Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    branch = models.CharField(max_length=20, default='Mehsana', blank=True)
    name_of_applicant = models.CharField(max_length=100, default='', blank=True)
    property_address = models.CharField(max_length=150, default='', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.property_address


class AYE(models.Model):
    class Meta:
        verbose_name_plural = 'AYE'

    company_name = models.CharField(max_length=100, default='AYE Finance (P) Ltd.', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_address = models.CharField(max_length=20, default='Ahmedabad', blank=True)
    name_of_applicant = models.CharField(max_length=100, default='', blank=True)
    aps = models.CharField(max_length=12, default='', blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class Mahindra(models.Model):
    class Meta:
        verbose_name_plural = 'Mahindra'

    company_name = models.CharField(max_length=100, default='Mahindra Rural Housing Finance Ltd', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    aps_number = models.CharField(max_length=7, default='', blank=True)
    location = models.CharField(max_length=20, default='', blank=True)
    customer_name = models.CharField(max_length=100, default='', blank=True)
    distance = models.PositiveSmallIntegerField(default=0, blank=True)
    request_received_date = models.DateField(auto_now_add=True, blank=True)
    repost_submitted_date = models.DateField(auto_now_add=True, blank=True)
    sro_1 = models.PositiveSmallIntegerField(default=245, blank=True)
    sro_2 = models.PositiveSmallIntegerField(default=0, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.aps_number


class YesBankAgri(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankAgri'

    company_name = models.CharField(max_length=100, default='Yes Bank Agri Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_address = models.CharField(max_length=20, default='', blank=True)
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM', blank=True)
    product_types = (
        ('KCC', 'KCC'),
        ('MEF', 'MEF'),
        ('FMA', 'FMA'),
    )
    product_type = models.CharField(max_length=20, choices=product_types, default='KCC', blank=True)
    product_price = models.IntegerField(default=1000, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    r_m_fpr_name = models.CharField(max_length=100, default='', blank=True)
    invoice_status = models.CharField(max_length=20, default='Pending', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class YesBankSagment(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankSagment'

    company_name = models.CharField(max_length=100, default='Yes Bank Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_address = models.CharField(max_length=20, default='', blank=True)
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM', blank=True)
    product_types = (
        ('BBS', 'BB Sagment'),
        ('MEF', 'MEF'),
        ('FMA', 'FMA'),
    )
    product_type = models.CharField(max_length=20, choices=product_types, default='BBS', blank=True)
    initiator_name = models.CharField(max_length=100, default='', blank=True)
    initiation_date = models.DateField(auto_now_add=True, blank=True)
    location = models.CharField(max_length=20, default='Mehsana', blank=True)
    type_of_services = (
        ('S', 'Stock'),
        ('IA', 'Invoice Audit'),
        ('V', 'Valuation'),
        ('TSR', 'TSR'),
        ('ROC', 'ROC'),
        ('IS', 'Interim Search'),
    )
    type_of_service = models.CharField(max_length=20, choices=type_of_services, default='S', blank=True)
    service_price = models.IntegerField(default=1000, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    property_address = models.CharField(max_length=100, default='', blank=True)
    client_name = models.CharField(max_length=100, default='', blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class YesBankAHFL(models.Model):
    class Meta:
        verbose_name_plural = 'YesBankAHFL'

    company_name = models.CharField(max_length=100, default='Yes Bank Limited', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_address = models.CharField(max_length=150, default='', blank=True)
    company_gst_number = models.CharField(max_length=15, default='24AAACY2068D1ZM', blank=True)
    initiator_name = models.CharField(max_length=100, default='', blank=True)
    initiation_date = models.DateField(auto_now_add=True, blank=True)
    location = models.CharField(max_length=20, default='Mehsana', blank=True)
    type_of_services = (
        ('TSR', 'TSR'),
        ('V', 'Vetting'),
        ('S', 'Stock'),
        ('IA', 'Invoice Audit'),
        ('ROC', 'ROC'),
    )
    type_of_service = models.CharField(max_length=20, choices=type_of_services, default='TSR', blank=True)
    service_price = models.IntegerField(default=1000, blank=True)
    type_choices = (
        ('L', 'legal'),
        ('V', 'vetting'),
        ('A', 'apf'),
        ('C', 'certified Copy'),
        ('S', 'Search'),
        ('B', 'BTCheque'),
        ('T', 'AHFL TSR'),
    )
    type = models.CharField(max_length=1, choices=type_choices, default='L', blank=True)
    price = models.IntegerField(default=1000, blank=True)
    property_address = models.CharField(max_length=100, default='', blank=True)
    client_name = models.CharField(max_length=100, default='', blank=True)
    pocket_expense = models.PositiveSmallIntegerField(default=0, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class IndiaBulls(models.Model):
    class Meta:
        verbose_name_plural = 'IndiaBulls'

    company_name = models.CharField(max_length=100, default='Indiabulls', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_zone = models.CharField(max_length=6, default='West-2', blank=True)
    company_location = models.CharField(max_length=20, default='Mehsana', blank=True)
    company_branch = models.CharField(max_length=20, default='Mehsana', blank=True)
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
    verification_type = models.CharField(max_length=20, choices=verification_types, default='R', blank=True)
    co_names = (
        ('IHFL', 'IHFL'),
        ('IVLFL', 'IVLFL'),
        ('ICCL', 'ICCL'),
    )
    co_name = models.CharField(max_length=20, choices=co_names, default='IHFL', blank=True)
    verification_rate = models.PositiveSmallIntegerField(default=1500, blank=True)
    number_of_verification = models.PositiveSmallIntegerField(default=1, blank=True)
    aps_id = models.CharField(max_length=8, default='', blank=True)
    customer_name = models.CharField(max_length=100, default='', blank=True)
    property_address = models.CharField(max_length=150, default='', blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_zone + ' - ' + self.company_location


class NewIndia(models.Model):
    class Meta:
        verbose_name_plural = 'NewIndia'

    company_name = models.CharField(max_length=100, default='The New India Assurance Co.Ltd.', blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    company_address = models.CharField(max_length=150, default='', blank=True)
    case_number = models.CharField(max_length=50, default='', blank=True)
    name_of_party = models.CharField(max_length=100, default='', blank=True)
    court_stamp_fee = models.PositiveSmallIntegerField(default=500, blank=True)
    advocate_fee = models.PositiveSmallIntegerField(default=500, blank=True)
    clerk_fee = models.PositiveSmallIntegerField(default=500, blank=True)
    expenses = models.PositiveSmallIntegerField(default=500, blank=True)
    travelling_expenses = models.PositiveSmallIntegerField(default=500, blank=True)
    other_expenses = models.PositiveSmallIntegerField(default=500, blank=True)
    remarks = models.CharField(max_length=250, default='', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.company_address


class AgriBank(models.Model):
    class Meta:
        verbose_name_plural = 'AgriBank'

    company_name = models.CharField(max_length=100, default='Agri Bank', blank=True)
    customer_name = models.CharField(max_length=100, default='', blank=True)
    village = models.CharField(max_length=255, default='', blank=True)
    price = models.PositiveSmallIntegerField(default=1000, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    checked = models.BooleanField(default=False, blank=True)
    paid_amount = models.PositiveIntegerField(default=0, blank=True)
    object = models.manager

    def __str__(self):
        return self.company_name + ' - ' + self.customer_name
