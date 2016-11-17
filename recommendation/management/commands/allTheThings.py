from django.core.management import BaseCommand

#The class must be named Command, and subclass BaseCommand

class Command(BaseCommand):
    help = 'Add serviceable pincodes to the stores.'

    def add_arguments(self, parser):
        parser.add_argument('store_id', type=str, nargs='+',
                            help = "Store uid(for multiple comma (,) separated without white space)/all (for all Stores)")

    def handle(self, *args, **options):
        if "store_id" in options:
            store_option = options["store_id"][0]
        else:
            raise CommandError("Please enter a valid store uid(s) or 'all' to update all stores' serviceable pincode.")