import random
from faker import Faker
from typing import Any, Optional


from django.core.management.base import BaseCommand, CommandError, CommandParser

from placeholder.models import UserInfo 


class GenerateUserInfo(object):
    __email_domain = [
        "@gmail.com",
        "@microsoft.com",
        "@reddit.com",
        "@twitter.com"
    ]

    def __init__(self) -> None:
        self.fake = Faker()

    def __last_primary_key(self) -> int:
        qs: UserInfo = UserInfo.objects.last()
        if not qs:
            return 0
        else:
            return qs.id

    def generate_id(self) -> int:
        return self.__last_primary_key() + 1

    def generate_name(self):
        return self.fake.name()
    
    def __number(self) -> str:
        return str(random.randint(1000, 9999))
    
    def generate_email(self):
        name: list[str] = self.generate_name().split()
        name.append(self.__number())
        return "".join(name) + random.choice(self.__email_domain)

    def generate_address(self):
        return self.fake.address()

class Command(BaseCommand):
    help = "Populate the data with fake data."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--populate",
            action="store_true",
            help="Populate placeholder database",
        )
        parser.add_argument(
            "--row",
            type=int,
            help="Write specified number of rows"
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=1000,
            help="Populate placeholder database",
        )
        
    def handle(self, *args: Any, **options: Any) -> str | None:
        userinfo = GenerateUserInfo()

        # get limit and row
        limit = options["limit"]
        row = options['row']

        # print(limit, row)

        # if row is provide, then popluate that many `row`
        # else populate with the default `limit`
        if row:
            for i in range(row):
                UserInfo.objects.create(
                    id = userinfo.generate_id(),
                    user = userinfo.generate_name(),
                    email = userinfo.generate_email(),
                    address = userinfo.generate_address()
                )
                self.stdout.write("Generate row {}\r".format(i), ending="")
        else:
            for i in range(limit):
                UserInfo.objects.create(
                    id = userinfo.generate_id(),
                    user = userinfo.generate_name(),
                    email = userinfo.generate_email(),
                    address = userinfo.generate_address()
                )
                self.stdout.write("Generate row {}\r".format(i), ending="")
                
        self.stdout.write("Success generate database.")