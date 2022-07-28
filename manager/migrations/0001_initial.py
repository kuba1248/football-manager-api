# Generated by Django 4.0.5 on 2022-07-01 20:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=255, null=True)),
                ("team_name", models.CharField(max_length=100, unique=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("profile_image", models.URLField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("US", "United States"),
                            ("AF", "Afghanistan"),
                            ("AL", "Albania"),
                            ("DZ", "Algeria"),
                            ("AS", "American Samoa"),
                            ("AD", "Andorra"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AQ", "Antarctica"),
                            ("AG", "Antigua And Barbuda"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AW", "Aruba"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BS", "Bahamas"),
                            ("BH", "Bahrain"),
                            ("BD", "Bangladesh"),
                            ("BB", "Barbados"),
                            ("BY", "Belarus"),
                            ("BE", "Belgium"),
                            ("BZ", "Belize"),
                            ("BJ", "Benin"),
                            ("BM", "Bermuda"),
                            ("BT", "Bhutan"),
                            ("BO", "Bolivia"),
                            ("BA", "Bosnia And Herzegowina"),
                            ("BW", "Botswana"),
                            ("BV", "Bouvet Island"),
                            ("BR", "Brazil"),
                            ("BN", "Brunei Darussalam"),
                            ("BG", "Bulgaria"),
                            ("BF", "Burkina Faso"),
                            ("BI", "Burundi"),
                            ("KH", "Cambodia"),
                            ("CM", "Cameroon"),
                            ("CA", "Canada"),
                            ("CV", "Cape Verde"),
                            ("KY", "Cayman Islands"),
                            ("CF", "Central African Rep"),
                            ("TD", "Chad"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CX", "Christmas Island"),
                            ("CC", "Cocos Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CG", "Congo"),
                            ("CK", "Cook Islands"),
                            ("CR", "Costa Rica"),
                            ("CI", "Cote D`ivoire"),
                            ("HR", "Croatia"),
                            ("CU", "Cuba"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czech Republic"),
                            ("DK", "Denmark"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("TP", "East Timor"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("SV", "El Salvador"),
                            ("GQ", "Equatorial Guinea"),
                            ("ER", "Eritrea"),
                            ("EE", "Estonia"),
                            ("ET", "Ethiopia"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FO", "Faroe Islands"),
                            ("FJ", "Fiji"),
                            ("FI", "Finland"),
                            ("FR", "France"),
                            ("GF", "French Guiana"),
                            ("PF", "French Polynesia"),
                            ("TF", "French S. Territories"),
                            ("GA", "Gabon"),
                            ("GM", "Gambia"),
                            ("GE", "Georgia"),
                            ("DE", "Germany"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GR", "Greece"),
                            ("GL", "Greenland"),
                            ("GD", "Grenada"),
                            ("GP", "Guadeloupe"),
                            ("GU", "Guam"),
                            ("GT", "Guatemala"),
                            ("GN", "Guinea"),
                            ("GW", "Guinea-bissau"),
                            ("GY", "Guyana"),
                            ("HT", "Haiti"),
                            ("HN", "Honduras"),
                            ("HK", "Hong Kong"),
                            ("HU", "Hungary"),
                            ("IS", "Iceland"),
                            ("IN", "India"),
                            ("ID", "Indonesia"),
                            ("IR", "Iran"),
                            ("IQ", "Iraq"),
                            ("IE", "Ireland"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JP", "Japan"),
                            ("JO", "Jordan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KI", "Kiribati"),
                            ("KP", "Korea (North)"),
                            ("KR", "Korea (South)"),
                            ("KW", "Kuwait"),
                            ("KG", "Kyrgyzstan"),
                            ("LA", "Laos"),
                            ("LV", "Latvia"),
                            ("LB", "Lebanon"),
                            ("LS", "Lesotho"),
                            ("LR", "Liberia"),
                            ("LY", "Libya"),
                            ("LI", "Liechtenstein"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("MO", "Macau"),
                            ("MK", "Macedonia"),
                            ("MG", "Madagascar"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("MV", "Maldives"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MH", "Marshall Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MU", "Mauritius"),
                            ("YT", "Mayotte"),
                            ("MX", "Mexico"),
                            ("FM", "Micronesia"),
                            ("MD", "Moldova"),
                            ("MC", "Monaco"),
                            ("MN", "Mongolia"),
                            ("MS", "Montserrat"),
                            ("MA", "Morocco"),
                            ("MZ", "Mozambique"),
                            ("MM", "Myanmar"),
                            ("NA", "Namibia"),
                            ("NR", "Nauru"),
                            ("NP", "Nepal"),
                            ("NL", "Netherlands"),
                            ("AN", "Netherlands Antilles"),
                            ("NC", "New Caledonia"),
                            ("NZ", "New Zealand"),
                            ("NI", "Nicaragua"),
                            ("NE", "Niger"),
                            ("NG", "Nigeria"),
                            ("NU", "Niue"),
                            ("NF", "Norfolk Island"),
                            ("MP", "Northern Mariana Islands"),
                            ("NO", "Norway"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PW", "Palau"),
                            ("PA", "Panama"),
                            ("PG", "Papua New Guinea"),
                            ("PY", "Paraguay"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PN", "Pitcairn"),
                            ("PL", "Poland"),
                            ("PT", "Portugal"),
                            ("PR", "Puerto Rico"),
                            ("QA", "Qatar"),
                            ("RE", "Reunion"),
                            ("RO", "Romania"),
                            ("RU", "Russian Federation"),
                            ("RW", "Rwanda"),
                            ("KN", "Saint Kitts And Nevis"),
                            ("LC", "Saint Lucia"),
                            ("VC", "St Vincent/Grenadines"),
                            ("WS", "Samoa"),
                            ("SM", "San Marino"),
                            ("ST", "Sao Tome"),
                            ("SA", "Saudi Arabia"),
                            ("SN", "Senegal"),
                            ("SC", "Seychelles"),
                            ("SL", "Sierra Leone"),
                            ("SG", "Singapore"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SB", "Solomon Islands"),
                            ("SO", "Somalia"),
                            ("ZA", "South Africa"),
                            ("ES", "Spain"),
                            ("LK", "Sri Lanka"),
                            ("SH", "St. Helena"),
                            ("PM", "St.Pierre"),
                            ("SD", "Sudan"),
                            ("SR", "Suriname"),
                            ("SZ", "Swaziland"),
                            ("SE", "Sweden"),
                            ("CH", "Switzerland"),
                            ("SY", "Syrian Arab Republic"),
                            ("TW", "Taiwan"),
                            ("TJ", "Tajikistan"),
                            ("TZ", "Tanzania"),
                            ("TH", "Thailand"),
                            ("TG", "Togo"),
                            ("TK", "Tokelau"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad And Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Turkey"),
                            ("TM", "Turkmenistan"),
                            ("TV", "Tuvalu"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("AE", "United Arab Emirates"),
                            ("UK", "United Kingdom"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VU", "Vanuatu"),
                            ("VA", "Vatican City State"),
                            ("VE", "Venezuela"),
                            ("VN", "Viet Nam"),
                            ("VG", "Virgin Islands (British)"),
                            ("VI", "Virgin Islands (U.S.)"),
                            ("YE", "Yemen"),
                            ("YU", "Yugoslavia"),
                            ("ZR", "Zaire"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        max_length=255,
                    ),
                ),
                ("value", models.FloatField(default=20000000)),
                ("team_budget", models.FloatField(default=5000000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("age", models.IntegerField(default=26)),
                (
                    "market_value",
                    models.FloatField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("GK", "Goal_Keeper"),
                            ("DF", "Defender"),
                            ("MF", "Midfielder"),
                            ("A", "Attacker"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "shirt_number",
                    models.IntegerField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                ("country", models.CharField(max_length=255)),
                (
                    "player_value",
                    models.FloatField(
                        default=1000000,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
                (
                    "transfer_status",
                    models.CharField(
                        choices=[("UA", "Unavaliable"), ("A", "Avaliable")],
                        default="UA",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="manager.team"
                    ),
                ),
            ],
        ),
    ]
