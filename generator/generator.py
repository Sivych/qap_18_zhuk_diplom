from faker import Faker
from generator.data import NewUser
import allure


faker_en = Faker('En')
fake = Faker()
Faker.seed()


@allure.step("Generated new user")
def generated_new_user():
    yield NewUser(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
    )